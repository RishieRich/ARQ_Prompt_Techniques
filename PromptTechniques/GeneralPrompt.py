# Guidelines for Prompting
# In this lesson, you'll practice two prompting principles and their related tactics in order to write effective prompts for large language models.


from langchain_community.chat_models import ChatOllama

DEFAULT_MODEL = "llama3"

chat_llm = ChatOllama(
    model=DEFAULT_MODEL,
    temperature=0.0,
)

def get_completion(prompt:str) -> str:
    """Get a completion from the chat model given a prompt."""
    response = chat_llm.invoke(prompt)

# ---- Tactic 1: Summary with delimiters ----

text = """
You should express what you want a model to do by 
providing instructions that are as clear and 
specific as you can possibly make them. 
This will guide the model towards the desired output, 
and reduce the chances of receiving irrelevant 
or incorrect responses. Don't confuse writing a 
clear prompt with writing a short prompt. 
In many cases, longer prompts provide more clarity 
and context for the model, which can lead to 
more detailed and relevant outputs.
"""

prompt = f"""
Summarize the text delimited by triple backticks 
into a single sentence.
```{text}
"""

response = get_completion(prompt)
print("=== Tactic 1 ===")
print(response)
print()