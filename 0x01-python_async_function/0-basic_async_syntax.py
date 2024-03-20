#!/usr/bin/env python3
"""
Module that utilises an async coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
   Takes in max_delay,waits for a random delay
    between 0 and max_delay and returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
