# %%
import os
import openai
from django.conf import settings


openai.api_key = settings.OPENAI_API_KEY


def get_chatgpt_dream_assessment(dream):
    """
    Docs
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that gives interpretations of dreams and predictions for the future"},
            {"role": "user", "content": f"Can you give me a creative interpretation and predictions for the future based on the dream below? {dream}"},
        ]
    )

    return response.choices[0].message.content

# %%
