#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """index helper function"""
    return (((page - 1) * page_size), (page * page_size))
