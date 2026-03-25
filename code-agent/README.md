## Code Agent

A coding agent that use reflection design pattern to generate and test python code

### Installation

- Make sure you have a `GROQ_API_KEY` in the environment variables
- Install `pip3 install groq os dotenv`

### Reflection Design Pattern

- User sends a request to generate the code to `qwen3-32b` model
- The returned code is to tested using another model to check for errors and to make the improvements
- The updated code is returned to the user

### Evals

- Uses LLM as judge to see how reflection improved the performace
