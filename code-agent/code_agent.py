import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"),)


def generate_code(question:str, model:str) -> str|None:
    """Generate python code based on user_query"""
    system_prompt = f"""
        You are a Python assistant. Given the user query write a Python code. If you cannot write a code for the user query return "Cannot write code" 

        User Query:
        {question}

        Return ONLY the code wrapped in <python> tags
    """
    chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": question,
          },
          {
            "role": "system",
            "content": system_prompt,
        }
      ],
      model=model,
  )
    
    return chat_completion.choices[0].message.content

  

print(generate_code(question="Write a Python code for two sum problem", model= "qwen/qwen3-32b"))

