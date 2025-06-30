def load_prompt_template(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
