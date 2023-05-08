# import generate file function
from generate_file_name import generate_random_file_name


def write_program(openai, text: str):
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= text,
        temperature=0,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    if 'choices' in response:
        x = response['choices']

        if len(x) > 0:
            response_text = x[0]['text']

        else:
            response_text = ""
    
        if "python" in text.lower():
            file_name = generate_random_file_name()
            file_name = file_name + ".py"

        if "javascript" in text.lower():
            file_name = generate_random_file_name()
            print(file_name)
            file_name = file_name + ".js"

        if "java" in text.lower():
            file_name = generate_random_file_name()
            print(file_name)
            file_name = file_name + ".java"

        if "c plus plus" in text.lower():
            file_name = generate_random_file_name()
            file_name = file_name + ".cpp"

        if "golang" in text.lower() or "in go" in text.lower():
            file_name = generate_random_file_name()
            file_name = file_name + ".go"

    return response_text