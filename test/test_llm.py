from alphaagent.utils.llm_utils import LLMReferenceAgent

llm_reference = LLMReferenceAgent()

print(
    llm_reference.complete_message(
        system_prompt="You are a helpful assistant.",
        user_prompt="What is the capital of France?",
    )
)
