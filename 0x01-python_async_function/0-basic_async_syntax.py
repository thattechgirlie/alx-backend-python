#!/usr/bin/env python3
"""
coroutine that delays
certain amount of time and returns it
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns a random float between 0 and max_delay,
    Args:
        max_delay: upper limit.
    Returns:
        random float
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
