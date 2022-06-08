#!/usr/bin/env python3
"""file with wait random function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Function to wait a random seconds and print them 

    Args:
        max_delay (int, optional): Defaults to 10.

    Returns:
        float: random number
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
