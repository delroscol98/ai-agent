import os

from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)


def write_file(working_directory, file_path, content):
    # get the absolute paths for the working_directory and file_path
    abs_working_dir_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir_path, file_path))

    # check if the file_path goes to outside of working_directory
    if not abs_file_path.startswith(abs_working_dir_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # check if the file_path exists:
    # if no, make the path recursively
    if not os.path.exists(abs_file_path):
        try:
            os.makedirs(os.path.dirname(abs_file_path))
        except Exception as e:
            return f"Error: Creating directory: {e}"

    else:
        # check if the file_path does exist but leads to a directory
        if os.path.isdir(abs_file_path):
            return f"Error: {abs_file_path} is a directory not a file"

    # write/overwrite the file with content
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
