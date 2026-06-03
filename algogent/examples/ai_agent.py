"""
ALGOgent Runtime SDK
AI Agent Example
"""

import asyncio

from algogent.core.runtime import Runtime


async def search():

    await asyncio.sleep(1)

    return "search complete"


async def analyze():

    await asyncio.sleep(1)

    return "analysis complete"


async def write_report():

    await asyncio.sleep(1)

    return "report generated"


async def main():

    runtime = Runtime()

    result1 = await runtime.run(
        search
    )

    result2 = await runtime.run(
        analyze
    )

    result3 = await runtime.run(
        write_report
    )

    print(result1.data)
    print(result2.data)
    print(result3.data)


if __name__ == "__main__":
    asyncio.run(main())