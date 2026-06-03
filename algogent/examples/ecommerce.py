"""
ALGOgent Runtime SDK
E-Commerce Example
"""

import asyncio

from algogent.core.runtime import Runtime


async def create_order():

    await asyncio.sleep(1)

    return {
        "order_id": "ORD-1001",
        "status": "created",
    }


async def main():

    runtime = Runtime()

    result = await runtime.run(
        create_order
    )

    print(result.to_dict())


if __name__ == "__main__":
    asyncio.run(main())