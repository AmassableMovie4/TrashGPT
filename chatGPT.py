import openai

openai.api_key = "YOUR_API_KEY"

model_engine = "text-davinci-003"
prompt = "Hello, how are you today?"

completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.5,
        max_tokens=4000,
        n=1,
        stop=None,
    )
response = completion.choices[0].text
print(response)