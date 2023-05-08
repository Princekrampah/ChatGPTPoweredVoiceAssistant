import datetime

# used to generate file names
def generate_random_file_name() -> str:
    basename = "gpt_code_file"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    file_name = "_".join([basename, suffix])
    return file_name