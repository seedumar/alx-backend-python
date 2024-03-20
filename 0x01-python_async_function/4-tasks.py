#!/usr/bin/env python3
"""
Contains an asynchronous function that runs returned asynchronous codes
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    executes tasks created from task_wait_random
    """
    delays = []
    for task in asyncio.as_completed([task_wait_random(max_delay)
                                      for _ in range(n)]):
        result = await task
        delays.append(result)
    return delays
