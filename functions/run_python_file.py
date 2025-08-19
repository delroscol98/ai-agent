import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    # Get the absolute file_path
    abs_working_dir_path = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_working_dir_path, file_path)

    # check if the file_path is inside the working_directory
    if os.path.dirname(abs_file_path) != abs_working_dir_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # check if the file_path exists
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    # check if the file_path leads to a Python file
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        # from this file run a subprocess of the file_path with any valid args
        full_command = ["python", abs_file_path] + args
        result = subprocess.run(full_command, timeout=30000, capture_output=True, cwd=working_directory)

        if result == None:
            return "No output produced"
        elif result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        else:
            return f"STDOUT: {result.stdout}; STDERR: {result.stderr}"

    except Exception:
        return "Error: executing Python file: {e}"
