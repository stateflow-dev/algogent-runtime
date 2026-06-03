"""
ALGOgent Runtime SDK
Automation Example
"""

import asyncio

from algogent.core.runtime import Runtime


async def fetch_sheet():

    await asyncio.sleep(1)

    return {
        "rows": 50
    }


async def generate_content():

    await asyncio.sleep(1)

    return {
        "articles": 50
    }


async def send_email():

    await asyncio.sleep(1)

    return {
        "emails_sent": 50
    }


async def main():

    runtime = Runtime()

    sheet = await runtime.run(
        fetch_sheet
    )

    content = await runtime.run(
        generate_content
    )

    emails = await runtime.run(
        send_email
    )

    print(sheet.data)
    print(content.data)
    print(emails.data)


if __name__ == "__main__":
    asyncio.run(main())