from langchain_community.llms import OpenAI


llm = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)


def ask_agent(question):

    prompt = f"""
You are an ERP inventory assistant.

Answer the following question about inventory management:

{question}
"""

    response = llm.invoke(prompt)

    print("\nAI Agent Response:\n")
    print(response)