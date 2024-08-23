"""All llm related utils classes which to call llm api."""

from openai import OpenAI

from alphaagent.config.llm_config import LLMConfig


class LLMReferenceAgent:
    def __init__(self):
        self.llm_config = LLMConfig()
        self.api_key = self.llm_config.openai_api_key
        self.chat_api_base = self.llm_config.chat_api_base
        self.model = self.llm_config.chat_model
        self.temperature = self.llm_config.chat_temperature
        self.former_messages = []

    def build_messages(
        self,
        system_prompt: str | None = None,
        user_prompt: str | None = None,
        former_messages: list[dict] | None = None,
    ) -> list[dict[str, str]]:
        if former_messages is None:
            former_messages = []
        system_prompt = (
            self.llm_config.default_system_prompt
            if system_prompt is None
            else system_prompt
        )
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(
            former_messages[-1 * self.llm_config.max_past_message_include :]
        )
        messages.append({"role": "user", "content": user_prompt})
        return messages

    def complete_message(self, *, system_prompt: str, user_prompt: str | None = None) -> (str | None):
        """Complete the message."""
        messages = self.build_messages(system_prompt, user_prompt, self.former_messages)

        client = OpenAI(api_key=self.api_key, base_url=self.chat_api_base)
        chat_completion = client.chat.completions.create(
            messages=messages, model=self.model
        )
        return chat_completion.choices[0].message.content
