import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Тесты для функции capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


class TestStringUtils:
    @pytest.fixture
    def utils(self):
        return StringUtils()

# Тесты для функции trim
    def test_trim_positive(self, utils):
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("skypro") == "skypro"
        assert utils.trim(" ") == ""

# Тесты для функции contains
    def test_contains_positive(self, utils):
        assert utils.contains("SkyPro", "S") is True
        assert utils.contains("Hello World", " ") is True
        assert utils.contains("Hello World", "World") is True
        assert utils.contains("SkyPro", "U") is False
        assert utils.contains("SkyPro", "s") is False

# Тесты для функции delete_symbol
    def test_delete_symbol_positive(self, utils):
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("test123test", "test") == "123"
        assert utils.delete_symbol("SkyPro", "x") == "SkyPro"
        assert utils.delete_symbol("", "") == ""

    # Негативные тесты
    def test_contains_empty_string(self, utils):
        assert utils.contains("", "a") is False
        assert utils.contains("", " ") is False

    def test_delete_symbol_empty_target(self, utils):
        assert utils.delete_symbol("", "a") == ""
        assert utils.delete_symbol("", "test") == ""

    def test_trim_empty_string(self, utils):
        assert utils.trim("") == ""

    def test_capitalize_empty_string(self, utils):
        assert utils.capitalize("") == ""
