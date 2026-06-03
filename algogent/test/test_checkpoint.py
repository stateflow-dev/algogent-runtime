import asyncio

from algogent.state.checkpoint import CheckpointManager


async def main():

    cp = CheckpointManager()

    checkpoint_id = await cp.create(
        {
            "step": 3,
            "status": "running"
        }
    )

    print("Checkpoint:", checkpoint_id)

    state = await cp.restore(
        checkpoint_id
    )

    print(state)


asyncio.run(main())