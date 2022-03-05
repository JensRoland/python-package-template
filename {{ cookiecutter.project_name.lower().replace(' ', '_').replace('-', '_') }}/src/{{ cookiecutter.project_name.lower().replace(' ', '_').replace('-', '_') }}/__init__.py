"""{{ cookiecutter.project_description }}."""

{% if cookiecutter.minimal_python_version == '3.7' -%}import importlib_metadata{%- else -%}from importlib import metadata as importlib_metadata{%- endif %}


def get_version() -> str:
    """Get the version of the package."""
    try:
        return str(importlib_metadata.version(__name__))
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
