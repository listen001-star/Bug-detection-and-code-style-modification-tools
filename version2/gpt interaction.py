import openai
import report


def get_chat_messages(prompt_text):
    openai.api_key = 'API'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=prompt_text,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message.content

output = report.run_pylint('test.py')

prompt_text = [{"role": "system", "content": "You are an expert in Python."},
                {"role": "user", "content": "I used Pylint to test my code, below is the result. Could you give me some advice on my code"},
                {"role":"user","content":output}
                 ]



# prompt_text = [{"role": "system", "content": "You are an expert in Python."},
#                 {"role": "user", "content": "This is my Pylint output, can you help me analyze how to solve these problems?"},
#                 {"role": "system", "content": "I would like to know: 1. How to solve these problems?2. If some issues are insignificant, how can I configure them to be ignored?"},
#                 {"role":"user","content":output}
#                  ]

response_content = get_chat_messages(prompt_text)


print("Suggestions：", response_content)


