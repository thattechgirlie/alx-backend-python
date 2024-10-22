#!/usr/bin/env python3
"""concurrent coroutines task"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns the wait_random function n times with a specified
    maximum delay between each call, returning a list of delays.
    Args:
        n: no of times spawn wait_random
        max_delay: between each call
    Returns:
        list of delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
