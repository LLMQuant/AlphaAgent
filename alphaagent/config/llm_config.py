from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# make sure that env variable is loaded while calling
load_dotenv(verbose=True, override=True)


class LLMConfig(BaseSettings):
    """LLM basic configuration."""

    openai_api_key: str = ""
    chat_openai_api_key: str = ""
    chat_api_base: str = ""
    chat_api_version: str = ""
    chat_model: str = ""
    chat_max_tokens: int = 3000
    chat_temperature: float = 0.5
    chat_stream: bool = True
    chat_seed: int | None = None
    chat_frequency_penalty: float = 0.0
    chat_presence_penalty: float = 0.0
    chat_token_limit: int = 100000  # 100000 is the maximum limit of gpt4, which might increase in the future version of gpt
    default_system_prompt: str = "You are an Finace AI assistant who helps to answer user's questions in finance domain."
    max_past_message_include: int = 5
