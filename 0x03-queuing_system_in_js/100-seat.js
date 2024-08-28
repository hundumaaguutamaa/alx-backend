const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

const app = express();
const port = 1245;

const client = redis.createClient();
client.on('error', (err) => {
    console.error('Redis client not connected to the server:', err);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const getAsync = promisify(client.get).bind(client);

function reserveSeat(number) {
    client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
    const seats = await getAsync('available_seats');
    return seats;
}

let reservationEnabled = true;
reserveSeat(50);

const queue = kue.createQueue();

app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save((err) => {
        if (err) {
            return res.json({ status: 'Reservation failed' });
        }
        res.json({ status: 'Reservation in process' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (err) => {
        console.log(`Seat reservation job ${job.id} failed: ${err}`);
    });
});

app.get('/process', (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        const seats = await getCurrentAvailableSeats();
        const availableSeats = parseInt(seats);

        if (availableSeats <= 0) {
            reservationEnabled = false;
            return done(new Error('Not enough seats available'));
        }

        reserveSeat(availableSeats - 1);
        if (availableSeats - 1 === 0) {
            reservationEnabled = false;
        }
        done();
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

