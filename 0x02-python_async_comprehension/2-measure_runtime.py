#!/usr/bin/env python3
"""Measures execution time"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure runtime coroutine 4 times and returnstotal
    execution time required to complete all tasks
    """
    t_start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)