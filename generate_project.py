import os

ROCKET = "\U0001F680"
FOLDER = "\U0001F4C1"
PAGE = "\U0001F4DD"
CHECK = "✅"


def prompt(message, default=""):
    value = input(f"{message} [{default}]: ")
    return value.strip() or default


def prompt_user_input():
    print(f"{ROCKET} Bioinformatics Project Generator\n")
    proj_name = prompt("Enter your project name", "bioinformatics")
    author = prompt("Enter your email address", "you@example.com")
    sub_folder = prompt("Enter the internal module folder name", "modules")
    return proj_name, proj_name, author, sub_folder


def define_directories(proj_name, sub_folder):
    return [
        f"{proj_name}/{proj_name}/utils",
        f"{proj_name}/{proj_name}/{sub_folder}",
        f"{proj_name}/tests",
        f"{proj_name}/data",
        f"{proj_name}/notebooks",
        f"{proj_name}/scripts",
    ]


def define_files(proj_name, author, email, sub_folder):
    return {
        f"{proj_name}/README.md": (
            f"# {proj_name.capitalize()} Bioinformatics Project\n\n"
            f"This project scaffolds a Python-based bioinformatics environment,\n"
            f"supporting project types like Rosalind problem-solving, pipelines,\n"
            f"dashboards, and more.\n\n"
            f"## Features\n"
            f"- Modular architecture\n"
            f"- Customizable internal structure (e.g., problems, modules)\n"
            f"- Poetry for dependency management\n\n"
            f"## Usage\n"
            f"```\n"
            f"python generate_project.py\n"
            f"```\n"
        ),

        f"{proj_name}/requirements.txt": "pytest\n",

        f"{proj_name}/.gitignore": (
            "__pycache__/"
            "*.pyc\n"
            ".env\n"
            ".venv/\n"
            ".idea/\n"
            "*.iml\n"
        ),

        f"{proj_name}/pyproject.toml": f"""\
[tool.poetry]
name = \"{proj_name}\"
version = \"0.1.0\"
description = \"Bioinformatics project scaffold\"
authors = [\"{author} <{email}>\"]

[tool.poetry.dependencies]
python = \"^3.10\"

[tool.poetry.dev-dependencies]
pytest = \"*\"

[build-system]
requires = [\"poetry-core\"]
build-backend = \"poetry.core.masonry.api\"
""",

        f"{proj_name}/{proj_name}/__init__.py": "",
        f"{proj_name}/{proj_name}/utils/__init__.py": "",
        f"{proj_name}/{proj_name}/{sub_folder}/__init__.py": "",
        f"{proj_name}/tests/__init__.py": "",
    }


def write_structure(dirs, files):
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"{FOLDER} Created directory: {directory}")

    for filepath, content in files.items():
        with open(filepath, "w") as f:
            f.write(content)
        print(f"{PAGE} Created file: {filepath}")


def create_project_structure(proj_name, author, email, sub_folder):
    dirs = define_directories(proj_name, sub_folder)
    files = define_files(proj_name, author, email, sub_folder)
    write_structure(dirs, files)
    print(f"\n{CHECK} Project '{proj_name}' scaffold created successfully by {author}.")


if __name__ == "__main__":
    project_name, author_name, author_email, subpackage = prompt_user_input()
    create_project_structure(project_name, author_name, author_email, subpackage)
