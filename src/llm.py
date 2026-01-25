from src.config import openai, MODEL

def call_llm (system_prompt, user_prompt):
    response =openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role":"system", "content":system_prompt},
            {"role":"user", "content":user_prompt}
            ],
           
    )
    return response.choices[0].message.content


def call_llm_stream (system_prompt, user_prompt, stream=True):
    response =openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role":"system", "content":system_prompt},
            {"role":"user", "content":user_prompt}
            ],
            stream=stream
    )
    
    result=""
    for chunk in response:
        result+= chunk.choices[0].delta.content or ""
        yield result