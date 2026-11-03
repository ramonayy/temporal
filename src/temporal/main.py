
import asyncio

from temporalio.client import Client

from workflows import FeedTheCat


async def main():
    client = await Client.connect("localhost:7233")

    result = await client.execute_workflow(
        FeedTheCat.run,
        "Mimi",
        id="feed-mimi-001",
        task_queue="cat-food-queue",
    )

    print(f"Ergebnis: {result}")


if __name__ == "__main__":
    asyncio.run(main())
