import os
from config.config import MAX_CHARS

from google.genai import types


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns up to {MAX_CHARS} from a file. Use this to read or get contents of a file, not to write or modify files.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(working_directory, file_path):
    # get absolute paths to file_path
    abs_working_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # check if the file_path is outside the working_directory
    if not abs_file_path.startswith(abs_working_path):
        return (
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        )

    # check if the path leads to a file
    if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        # read the file up to a MAX_CHARS length
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            file_size = os.path.getsize(abs_file_path)
            if file_size > MAX_CHARS:
                file_content_string += '{file_content_string} [...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
