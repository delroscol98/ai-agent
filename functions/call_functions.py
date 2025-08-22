from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file_content import schema_write_file_content, write_file_content
from functions.run_python_file import schema_run_python_file, run_python_file

from config.config import WORKING_DIRECTORY

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file_content
    ]
)


def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    function_args = function_call_part.args

    if not verbose:
        print(f" - Calling function: {function_name}")

    print(f"Calling function: {function_name}({function_args})")

    functions_map = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "write_file_content": write_file_content,
        "run_python_file": run_python_file
    }

    if function_name not in functions_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    args = dict(function_args)
    args["working_directory"] = WORKING_DIRECTORY
    function_result = functions_map[function_name](**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
