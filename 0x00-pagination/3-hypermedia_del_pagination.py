#!/usr/bin/env python3
"""Simple pagination sample.
"""
import csv
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    
    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: The start and end indices for the pagination.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        
        Returns:
            List[List]: The dataset loaded from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of the dataset.
        
        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.
        
        Returns:
            List[List]: The page of the dataset.
        """
        assert isinstance(page, int) and page > 0, "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be an integer greater than 0"
        
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        
        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Retrieves a hypermedia page of the dataset.
        
        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.
        
        Returns:
            Dict[str, Any]: A dictionary containing the pagination data.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        
        hypermedia_data = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
        
        return hypermedia_data

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Retrieves a hypermedia page of the dataset based on a start index.
        
        Args:
            index (int, optional): The start index. Defaults to None.
            page_size (int, optional): The number of items per page. Defaults to 10.
        
        Returns:
            Dict[str, Any]: A dictionary containing the pagination data.
        """
        dataset = self.dataset()
        total_items = len(dataset)

        if index is None:
            index = 0

        assert isinstance(index, int) and 0 <= index < total_items, "index must be a valid range"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be an integer greater than 0"

        next_index = index + page_size
        if next_index >= total_items:
            next_index = None

        data = dataset[index:index + page_size]

        hyper_index_data = {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }

        return hyper_index_data


# Example usage:
if __name__ == "__main__":
    server = Server()
    print(server.get_hyper(1, 10))  # Example output: Hypermedia pagination for the first 10 rows
    print(server.get_hyper(2, 5))   # Example output: Hypermedia pagination for the second page with 5 rows per page
    print(server.get_hyper_index(0, 10))  # Example output: Hypermedia pagination starting at index 0 with 10 rows
    print(server.get_hyper_index(15, 5))  # Example output: Hypermedia pagination starting at index 15 with 5 rows

