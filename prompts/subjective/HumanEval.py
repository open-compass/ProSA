HumanEval_prompts = dict(
    prompt_1="Create a Python script for this problem:\n{prompt}\nResponse:\n",
    prompt_2="Provide a Python script that solves the following problem:\n{prompt}\n",
    prompt_3="Complete the following Python code:\n{prompt}",

    prompt_4="Please provide a self-contained Python script that solves the following problem in a markdown code block:\n```\n{prompt}\n```",
    prompt_5="Could you provide a response to complete the following Python code:\n{prompt}\nResponse:", 
    prompt_6="Please help me to create a Python script for this problem:\n{prompt}\nResponse:\n",

    prompt_7="You are a very helpful AI assistant. Could you provide a response to complete the following Python code:\n{prompt}\nYour response:",
    prompt_8="As an outstanding AI assistant, please provide a self-contained Python script that solves the following problem in a markdown code block:\n```\n{prompt}\n```\n",
    prompt_9="As an AI expert in coding. Please help me to create a Python script for this problem:\n{prompt}\nYour response should only contain the code for the function.",

    prompt_10="Could you provide a response to complete the following Python code:\n{prompt}\nYou need to put the script in the following format:\n```python\n# Your response\n```",
    prompt_11="Please provide a self-contained Python script that solves the following problem in a markdown code block:\n```\n{prompt}\n```\nYou have to follow the following format:```python\n# Your script\n```",
    prompt_12="Please help me to create a Python script for this problem:\n{prompt}\nYour response should only contain the code for the function.",
)