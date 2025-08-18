import os


def print_directory_contents(path):
    directory_contents = os.listdir(path)

    def get_file_size_and_is_dir(el):
        file_size = os.path.getsize(path + '/' + el)
        is_dir = os.path.isdir(path + '/' + el)
        return f"- {el}: file_size={file_size} bytes, is_dir={is_dir}"

    return "\n".join(map(get_file_size_and_is_dir, directory_contents))


def get_files_info(working_directory, directory="."):
    try:
        # Join the working directory with the requested directory
        full_path = os.path.join(working_directory, directory)

        # Convert both paths to absolute paths to handle relative references like "../"
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)

        # Check if the absolute path starts with the working directory path
        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # check if the directory argument is an actual directory
        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'

        # print contents of the directory
        return print_directory_contents(abs_full_path)

    except Exception as e:
        return f"Error: {e}"
