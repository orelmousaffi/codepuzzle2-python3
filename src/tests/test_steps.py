import pytest

from src.calculator import add


@pytest.mark.parametrize(
    ("input", "expected"),
    [pytest.param("", 0, id="input of empty string to 0")],
)
def test_checks_for_base_case_(input, expected):
    """given an empty string should return. add(\"\") = 0"""
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
    """given a string with a single value should return the same value"""
    actual = add(input)
    assert actual == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        pytest.param("1,1", 2, id='input string of "1,1" should return 2'),
        pytest.param("20,22", 42, id='input string of "20,22" should return 42'),
    ],
)
def test_check_sum_of_two_comma_separated_values_(input, expected):
    """given a string with two comma separated values should return the sum of them"""
    actual = add(input)
    assert actual == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        pytest.param("1,2,3", 6, id='input string of "1,2,3" should return 6'),
        pytest.param(
            "1,2,3,4,5", 15, id='input string of "1,2,3,4,5" should return 15'
        ),
        pytest.param(
            "4,6,3,7,12,1,9", 42, id='input string of "4,6,3,7,12,1,9" should return 42'
        ),
        pytest.param(
            "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1",
            100,
            id='input string of 100 individual "1"s should return 42',
        ),
    ],
)
def test_check_sum_of_N_comma_separated_values_(input, expected):
    """given a string with N comma separated values should return the sum of all of them"""
    actual = add(input)
    assert actual == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        pytest.param("1\n2,3", 6, id='input string of "1\n2,3" should return 6'),
        pytest.param("4\n2\n7", 13, id='input string of "4\n2\n7" should return 13'),
        pytest.param(
            "1,2\n3\n4,5", 15, id='input string of "1,2\n3\n4,5" should return 15'
        ),
        pytest.param(
            "4\n6\n3,7,1,1\n1,1\n8,1\n9",
            42,
            id='input string of "4\n6\n3,7,1,1\n1,1\n8,1\n9" should return 42',
        ),
    ],
)
def test_accept_either_comma_or_newline_as_separator_(input, expected):
    """should accept either commas and/or new lines ('\\n') as value separators."""
    actual = add(input)
    assert actual == expected


@pytest.mark.parametrize(
    ("input", "error_trigger"),
    [
        pytest.param(
            "1,-2",
            -2,
            id='input string of "1,-2" should throw exception: "negative numbers not allowed: -2"',
        ),
        pytest.param(
            "-1\n-2,3,-4",
            -1,
            id='input string of "-1\n-2,3,-4" should throw exception: "negative numbers not allowed: -1"',
        ),
        pytest.param(
            "///\n-4/6/3/-7/1/-1/1/-1/8/1/9",
            -4,
            id='input string of "///\n-4/6/3/-7/1/-1/1/-1/8/1/9" should throw exception: "negative numbers not allowed: -4"',
        ),
        pytest.param(
            "//*\n-1*-2-1*-10",
            -1,
            id='input string of "//*\n-1*-2-1*-10" should throw exception: "negative numbers not allowed: -1"',
        ),
    ],
)
def test_should_not_accept_negative_numbers_(input, error_trigger):
    """should not accept negative numbers, throwing an error specifying the problematic numbers."""
    errorStr = "negative numbers not allowed: {negative_number}".format(
        negative_number=error_trigger
    )
    with pytest.raises(Exception, match=errorStr):
        add(input)


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        pytest.param("1001,2", 2, id='input string of "1001,2" should return 2'),
        pytest.param("1000,2", 1002, id='input string of "1000,2" should return 1002'),
        pytest.param(
            "///\n2000/6/1/1/1234/5/3000/8/1/9",
            31,
            id='input string of "///\n2000/6/1/1/1234/5/3000/8/1/9" should return 31',
        ),
        pytest.param(
            "1\n2000,1\n10", 12, id='input string of "1\n2000,1\n10" should return 12'
        ),
    ],
)
def test_ignore_numbers_greater_than_1000_(input, expected):
    """should ignore (not add) numbers greater than 1000."""
    actual = add(input)
    assert actual == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        pytest.param(
            "//[;;;]\n1;;;2;;;3",
            6,
            id='input string of "//[;;;]\n1;;;2;;;3" should return 6',
        ),
        pytest.param(
            "//[-_-]\n1-_-2-_-3-_-4-_-5",
            15,
            id='input string of "//[-_-]\n1-_-2-_-3-_-4-_-5" should return 15',
        ),
        pytest.param(
            "//[//]\n4//6//3//7//1//1//1//1//8//1//9",
            42,
            id='input string of "//[//]\n4//6//3//7//1//1//1//1//8//1//9" should return 42',
        ),
        pytest.param(
            "//[&.?!]\n1&.?!1&.?!1&.?!1&.?!1&.?!1",
            6,
            id='input string of "//[&.?!]\n1&.?!1&.?!1&.?!1&.?!1&.?!1" should return 6',
        ),
    ],
)
def test_accept_multi_character_cusomt_delimiters_(input, expected):
    """should accept multi-character custom delimiter using this format: '//[delimiter]\\n(numbers…)'."""
    actual = add(input)
    assert actual == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        pytest.param(
            "//[;][*]\n1;2*3", 6, id='input string of "//[;][*]\n1;2*3" should return 6'
        ),
        pytest.param(
            "//[/][*]\n1/2/3**4/5",
            15,
            id='input string of "//[/][*]\n1/2/3**4/5" should return 15',
        ),
        pytest.param(
            "//[:][_][^][-]\n4:6-3-7_1-1^1:1_8^1^9",
            42,
            id='input string of "//[:][_][^][-]\n4:6-3-7_1-1^1:1_8^1^9" should return 42',
        ),
        pytest.param(
            "//[+][*][^]\n1^1+1^1*1*1",
            6,
            id='input string of "//[+][*][^]\n1^1+1^1*1*1" should return 6',
        ),
    ],
)
def test_accept_mutiple_single_letter_custom_delimeters_(input, expected):
    """should allow multiple single character delimiters using this format: '//[delim1][delim2]...\\n(numbers…)'."""
    actual = add(input)
    assert actual == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        pytest.param(
            "//[**][;]\n1;2**3",
            6,
            id='input of string "//[**][;]\n1;2**3" should return 6',
        ),
        pytest.param(
            "//[//][***]\n1//2//3***4//5",
            15,
            id='input of string "//[//][***]\n1//2//3***4//5" should return 15',
        ),
        pytest.param(
            "//[:)][:(]\n4:)6:(3:(7:)1:)1:)1:(1:)8:)1:)9",
            42,
            id='input of string "//[:)][:(]\n4:)6:(3:(7:)1:)1:)1:(1:)8:)1:)9" should return 42',
        ),
    ],
)
def test_accept_multiple_multi_character_custom_delimeters_(input, expected):
    """should allow multiple multi-characters delimiters using this format: '//[delim1][delim2]...\\n(numbers…)'."""
    actual = add(input)
    assert actual == expected
