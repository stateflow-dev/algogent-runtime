import asyncio

from algogent.events.event_bus import EventBus

bus = EventBus()


@bus.subscribe("hello")
async def handler(event):

    print(event)


async def main():

    await bus.emit(
        "hello",
        {
            "message": "ALGOgent"
        }
    )


asyncio.run(main())