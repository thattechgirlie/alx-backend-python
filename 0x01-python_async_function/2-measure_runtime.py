#!/usr/bin/env python3
"""Measure total execution time of a func"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures and returns the total execution time of a function
    that launches n coroutines, each waiting up to max_delay seconds.
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n