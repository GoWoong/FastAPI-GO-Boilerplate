import os

def create_project_structure(project_name):
    # Define your project structure here
    project_structure = [
        f'{project_name}/',
        f'{project_name}/app/',
        f'{project_name}/app/__init__.py',
        # Add more directories and files as needed
    ]

    # Create directories and files
    for item in project_structure:
        os.makedirs(item, exist_ok=True)

def main():
    project_name = input("Enter project name: ")
    create_project_structure(project_name)
    print(f"Project '{project_name}' created successfully!")

if __name__ == "__main__":
    main()