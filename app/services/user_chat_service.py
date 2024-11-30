from app.utils.external_apis import answer_user_message
from IPython.display import Markdown


async def respond_to_user_message(user_message: str, top_passages: list):
    response = answer_user_message(user_message, top_passages)
    response = Markdown(response)
    return response
