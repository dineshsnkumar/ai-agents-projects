## Code Agent

A coding agent that use reflection design pattern to generate and test python code

### Installation

- Make sure you have a `GROQ_API_KEY` in the environment variables
- Install `pip3 install groq os dotenv`

### Reflection Design Pattern

- User sends a request to generate the code to `qwen3-32b` model
- The returned code is to tested using `openai/gpt-oss-120b` model to check for errors and to make the improvements
- The updated code is returned to the user

### Example

- `user_question = "Write Python code for Product of a array except self"`
- `qwen3-32b` model returns the following code

```python
def productExceptSelf(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    result = [prefix[i] * suffix[i] for i in range(n)]
    return result

# Example usage:
# nums = [1, 2, 3, 4]
# print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]

```

- Passing the code to `openai/gpt-oss-120b`model returns the following feeedback

`The original implementation correctly computes the product of array elements except self using separate prefix and suffix arrays. It works for the provided example and runs in O(n) time, but it uses O(n) extra space for the two auxiliary arrays. This can be optimized to O(1) additional space (excluding the output list) by computing the prefix products directly into the result array and then merging the suffix products in a second pass. Additionally, adding type hints, a docstring, and handling edge cases (empty input) makes the function more robust and user‑friendly.`

- Code returned to the user after reflection step

```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result

```
