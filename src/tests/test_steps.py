import pytest

from src.calculator import add


@pytest.mark.parametrize(
    ("input", "expected"),
    [pytest.param("", 0, id="input of empty string to 0")],
)
def test_checks_for_base_case_(input, expected):
    actual = add(input)
    assert actual == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        pytest.param("0", 0, id='input string of "0" should return 0'),
        pytest.param("5", 5, id='input string of "5" should return 5'),
        pytest.param("42", 42, id='input string of "42" should return 42'),
    ],
)
def test_checks_for_single_value_string_(input, expected):
    print(f'\n > string "{input}" = {expected}')
    actual = add(input)
    assert actual == expected
