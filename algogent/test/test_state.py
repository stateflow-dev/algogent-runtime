import asyncio

from algogent.state.state_manager import StateManager


async def main():

    state = StateManager()

    await state.save_state(
        {
            "runtime": "algogent",
            "version": "1.0"
        }
    )

    data = await state.load_state()

    print(data)


asyncio.run(main())