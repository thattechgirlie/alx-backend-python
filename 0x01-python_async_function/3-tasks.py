#!/usr/bin/env python3
"""Methos returns task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio task that waits for a
    random number of seconds up to the specified max_delay.
    Args:
        max_delay: wait time for a task
    Returns: an asyncio
    """
    return asyncio.create_task(wait_random(max_delay))