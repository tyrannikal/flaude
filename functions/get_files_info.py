import os


def get_files_info(working_directory, directory=".") -> str:
    result_str = ""

    try:
        cwd_absolute = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(cwd_absolute, directory))
        valid_target_dir = (
            os.path.commonpath([cwd_absolute, target_dir]) == cwd_absolute
        )
        if not valid_target_dir:
            return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'    Error: "{directory}" is not a directory'

        for item in os.listdir(target_dir):
            item_path = os.path.normpath(os.path.join(target_dir, item))
            result_str += f"    - {item}: "
            result_str += f"file_size={os.path.getsize(item_path)} bytes, "
            result_str += f"is_dir={str(os.path.isdir(item_path))}\n"

    except os.error:
        print("    Error: something wrong. Better error messages later")

    return result_str
