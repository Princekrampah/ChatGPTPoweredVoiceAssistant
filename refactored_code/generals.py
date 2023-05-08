def general_questions(openai, text) -> str:
    openai_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": text},
        ]
    )

    response_text = openai_response.get("choices")[0].get("message").get("content")

    return response_text