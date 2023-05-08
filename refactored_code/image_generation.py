def generate_image(openai, text) -> str:
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    return image_url

