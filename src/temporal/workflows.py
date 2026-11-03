
from datetime import timedelta

from temporalio import workflow


@workflow.defn
class FeedTheCat:
    @workflow.run
    async def run(self, cat_name: str) -> str:
        result = await workflow.execute_activity(
            "feed_the_cat",
            cat_name,
            start_to_close_timeout=timedelta(seconds=10),
        )

        return result
