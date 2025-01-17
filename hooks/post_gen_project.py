"""This module is called after project is created."""
from typing import List

import textwrap
from pathlib import Path
from shutil import move, rmtree

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_MODULE = "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}"
CREATE_EXAMPLE_TEMPLATE = "{{ cookiecutter.create_example_template }}"

# Values to generate correct license
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.organization }}"

# Values to generate github repository
GITHUB_USER = "{{ cookiecutter.github_username }}"

licenses_dict = {
    "MIT": "mit",
    "BSD-3": "bsd3",
    "GNU GPL v3.0": "gpl3",
    "Apache Software License 2.0": "apache",
    "Proprietary": "proprietary",
}


def generate_license(directory: Path, license_shortname: str) -> None:
    """Generate license file for the project.

    Args:
        directory: path to the project directory
        license_shortname: chosen license
    """
    move(str(directory / "_licenses" / f"{license_shortname}.txt"), str(directory / "LICENSE"))
    rmtree(str(directory / "_licenses"))


def remove_unused_files(directory: Path, module_name: str, need_to_remove_cli: bool) -> None:
    """Remove unused files.

    Args:
        directory: path to the project directory
        module_name: project module name
        need_to_remove_cli: flag for removing CLI related files
    """
    files_to_delete: List[Path] = []

    def _cli_specific_files() -> List[Path]:
        return [directory / "src" / module_name / "__main__.py"]

    if need_to_remove_cli:
        files_to_delete.extend(_cli_specific_files())

    for path in files_to_delete:
        path.unlink()


def print_further_instructions(project_name: str, directory: Path, github: str) -> None:
    """Show user what to do next after project creation.

    Args:
        project_name: current project name
        directory: Path to the project directory
        github: GitHub username
    """
    message = f"""
    Your project {project_name} is created.

    1) Now you can start working on it:

        $ cd {directory} && git init -b main

    2) If your system Python version is not {{ cookiecutter.minimum_python_version }} or higher:

        $ pyenv local $(pyenv versions --bare | grep '{{ cookiecutter.minimum_python_version }}')

    3) If you don't already have Poetry installed:

        $ make poetry-download

    4) Initialize Poetry and install pre-commit hooks:

        $ make install
        $ make pre-commit-install

    5) Activate virtual environment shell:

        $ source "$(poetry env list --full-path | grep Activated | cut -d' ' -f1)/bin/activate"

    6) Upload initial code to GitHub:

        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git remote add origin https://github.com/{github}/{project_name}.git
        $ gh repo create --private {github}/{project_name}
        $ git push -u origin main

    7) For running all checks and making badges:

        $ make test && make lint && make check-codestyle && make mypy && make check-safety && make extrabadges
    """
    print(textwrap.dedent(message))


def main() -> None:
    """Main function."""
    generate_license(directory=PROJECT_DIRECTORY, license_shortname=licenses_dict[LICENSE])
    remove_unused_files(
        directory=PROJECT_DIRECTORY,
        module_name=PROJECT_MODULE,
        need_to_remove_cli=CREATE_EXAMPLE_TEMPLATE != "cli",
    )
    print_further_instructions(
        project_name=PROJECT_NAME, directory=PROJECT_DIRECTORY, github=GITHUB_USER
    )


if __name__ == "__main__":
    main()
