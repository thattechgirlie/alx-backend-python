#!/usr/bin/env python3
"""method that spawns Tasks n times with
specified delay between each call."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns the max delay between each call returning a list of delays.
    Args:
        n: no of spawn wait random
        max_delay: btwn each call
    Returns: list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
