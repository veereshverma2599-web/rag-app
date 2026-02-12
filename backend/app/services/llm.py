   
from transformers import pipeline
import asyncio

generator = pipeline(
    "text-generation",
    model="microsoft/phi-2",
    device_map="auto"
)

async def generate(question, context):

    prompt = f"""
Answer only from context.
If not found, say I don't know.

Context:
{context}

Question: {question}
"""

    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(
        None,
        lambda: generator(prompt, max_new_tokens=150)[0]["generated_text"]
    )

    return result

