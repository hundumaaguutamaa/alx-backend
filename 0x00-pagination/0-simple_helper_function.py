#!/usr/bin/env python3
"""index_range that takes two integer arguments page and page_size """


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    two integers with their type:
    return type expectation: tuple
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
