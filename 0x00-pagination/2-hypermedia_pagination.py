#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """index helper function"""
    return (((page - 1) * page_size), (page * page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page method"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        if start >= len(self.dataset()):
            return []
        else:
            return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get hyper method"""
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        size = len(data)
        total = len(dataset) // page_size + (len(dataset) % page_size > 0)
        next_page = None
        prev_page = None
        if page < total:
            next_page = page + 1
        if page > 1 and page < total:
            prev_page = page - 1
        return {"page_size": size,"page": page,"data": data
                ,"next_page": next_page,"prev_page": prev_page,"total_pages": total}
