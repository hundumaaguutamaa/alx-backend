#!/usr/bin/env python3
"""Pagintion function
"""

from typing import Tuple


def index_range(page, page_size):
    """Retrives index range from given page and size. """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index

