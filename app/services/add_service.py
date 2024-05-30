import multiprocessing
from typing import List
import logging

logger = logging.getLogger(__name__)

# def add_lists(lists: List[List[int]]) -> List[int]:
#     return [sum(sublist) for sublist in lists]


def process_addition(lists: List[List[int]]) -> List[int]:
    with multiprocessing.Pool() as pool:
        results = pool.map(sum, lists)
    return results
