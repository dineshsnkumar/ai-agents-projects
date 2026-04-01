import os
import re
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"),)


def generate_code(question:str, model:str) -> str | None:
    """
    Generate python code based on user_query
    """
    system_prompt = f"""
        You are a Python assistant. Given the user query write a Python code. If you cannot write a code for the user query return "Cannot write code" 

        User Query:
        {question}

        Return a strict code wrapped in <execute_python> </execute_python> tags
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
    
    respone = chat_completion.choices[0].message.content
    return respone


def reflect_code(question:str, code_original:str, model:str) -> str | None:
    """
    Evaluate the Python code and if necessary improve the code.
    """
    system_prompt = f"""
    You are a Python code reviewer and refiner.

    User Question 
    {question}

    Orignial code
    {code_original}

    Step 1: Evaluate the Orignial code to the User Question
    Step 2: If the Orignial code could be improved, give the updated code.
    If the Orignial code is already correct, return it unchanged

    Return feedback in a paragraph form

    """

    chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": question,
          },
          {
              "role": "user",
              "content": code_original,
          },
          {
            "role": "system",
            "content": system_prompt,
        }
      ],
      model=model,
    )
    content = chat_completion.choices[0].message.content
    return content


def updated_code(question:str, code_original:str, feedback:str,  model:str) -> str | None:
    """
    Evaluate the Python code and if necessary improve the code.
    """
    system_prompt = f"""
    You are a Python code reviewer and refiner. Given user question, Original code and reflection, retrun the 
    updated code 

    User Question 
    {question}

    Orignial code
    {code_original}

    Feedback 
    {feedback}

    Return the updated code 
    """
    chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": question,
          },
          {
              "role": "user",
              "content": code_original,
          },
          {
              "role": "user",
              "content": feedback,
          },
          {
            "role": "system",
            "content": system_prompt,
        }
      ],
      model=model,
    )
    content = chat_completion.choices[0].message.content
    return content




def code_workflow():
    user_question = input("Hi, How can I help you with today? ")
    code_version_one = generate_code(user_question, model= "qwen/qwen3-32b") 
    print(code_version_one)

    if code_version_one:
        match = re.search(r"<execute_python>([\s\S]*?)</execute_python", code_version_one)
        if match:
            code = match.group(1).strip()
            feedback = reflect_code(question=user_question, code_original=code, model="openai/gpt-oss-120b")
            if feedback and code:
                refined_code = updated_code(user_question, code, feedback, model="openai/gpt-oss-120b")
                return refined_code


  
code_workflow()
