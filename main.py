from subprocess import run


def check_poetry():
    try:
        run(["poetry", "--version"], capture_output=True, check=True)
        return True
    except FileNotFoundError:
        return False


def create_boilerplate():
    run(["python", "boilerplate_generator/project_creator.py"])


if __name__ == "__main__":
    if check_poetry():
        print("Poetry is available in this environment.")
        create_boilerplate()
    else:
        print("Poetry is not installed. Please install Poetry to proceed.")

