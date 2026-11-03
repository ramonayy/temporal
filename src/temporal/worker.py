
import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from workflows import FeedTheCat
from activities import feed_the_cat


async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="cat-food-queue",
        workflows=[FeedTheCat],
        activities=[feed_the_cat],
    )

    print("🐾 Cat Worker läuft!")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
