import os
from config import max_chars


def get_file_content(working_directory, file_path) -> str:
    content = ""

    try:
        cwd_absolute = os.path.abspath(working_directory)
        file_path_absolute = os.path.normpath(os.path.join(cwd_absolute, file_path))
        valid_target_dir = (
            os.path.commonpath([cwd_absolute, file_path_absolute]) == cwd_absolute
        )
        if not valid_target_dir:
            return f'    Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_path_absolute):
            return f'    Error: File not found or is not a regular file: "{file_path}"'

        with open(file_path_absolute, "r") as f:
            content = f.read(max_chars)
            if f.read(1):
                content += f'[...File "{file_path_absolute}" truncated at {max_chars} characters]'
    except os.error:
        print("    Call to 'os' function failed.")

    return content
