import pytest

from hooks.pre_gen_project import validate_line_length


def test_validate_line_length():
    try:
        validate_line_length(88)
    except ValueError as exc:
        assert False, f"'validate_line_length' raised an exception {exc}"

    with pytest.raises(ValueError):
        validate_line_length(1_000)

    with pytest.raises(ValueError):
        validate_line_length(-10)
