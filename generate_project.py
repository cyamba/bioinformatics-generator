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
    project = prompt("Enter your project name", "bioinformatics")
    author = prompt("Enter your email address", "you@example.com")
    sub_folder = prompt("Enter the internal module folder name", "modules")
    return project, project, author, sub_folder


def define_directories(project, sub_folder):
    return [
        f"{project}/{project}/utils",
        f"{project}/{project}/{sub_folder}",
        f"{project}/tests",
        f"{project}/data",
        f"{project}/notebooks",
        f"{project}/scripts",
    ]


def define_files(project, author, email, sub_folder):
    return {
        f"{project}/README.md": (
            f"# {project.capitalize()} Bioinformatics Project\n\n"
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

        f"{project}/requirements.txt": "pytest\n",

        f"{project}/.gitignore": (
            "__pycache__/"
            "*.pyc\n"
            ".env\n"
            ".venv/\n"
            ".idea/\n"
            "*.iml\n"
        ),

        f"{project}/pyproject.toml": f"""\
[tool.poetry]
name = \"{project}\"
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

        f"{project}/{project}/__init__.py": "",
        f"{project}/{project}/utils/__init__.py": "",
        f"{project}/{project}/{sub_folder}/__init__.py": "",
        f"{project}/tests/__init__.py": "",
    }


def write_structure(dirs, files):
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"{FOLDER} Created directory: {directory}")

    for filepath, content in files.items():
        with open(filepath, "w") as f:
            f.write(content)
        print(f"{PAGE} Created file: {filepath}")


def create_project_structure(project, author, email, sub_folder):
    dirs = define_directories(project, sub_folder)
    files = define_files(project, author, email, sub_folder)
    write_structure(dirs, files)
    print(f"\n{CHECK} Project '{project}' scaffold created successfully by {author}.")


if __name__ == "__main__":
    project_name, author_name, author_email, subpackage = prompt_user_input()
    create_project_structure(project_name, author_name, author_email, subpackage)
