from functions.get_files_content import get_files_content


def test():
    result = get_files_content("calculator", "main.py")
    print("Result for current main.py:")
    print(result)

    result = get_files_content("calculator", "pkg/calculator.py")
    print("Result for pkg/calculator.py:")
    print(result)

    result = get_files_content("calculator", "/bin/cat")
    print("Result for /bin/cat:")
    print(result)

    result = get_files_content("calculator", "pkg/does_not_exist.py")
    print("Result for pkg/does_not_exist.py:")
    print(result)

if __name__ == "__main__":
    test()
