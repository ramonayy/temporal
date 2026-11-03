
from temporalio import activity


'''
Activities handle everything that interacts with the outside world, like:

    API calls
    Database queries
    LLM invocations
    File I/O
'''


@activity.defn(name="feed_the_cat")
async def feed_the_cat(cat_name: str) -> str:
    print(f"🐱 Ich füttere {cat_name} mit leckerem Katzenfutter!")

    return f"{cat_name} wurde erfolgreich gefüttert."
