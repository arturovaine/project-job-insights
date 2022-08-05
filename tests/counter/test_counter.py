from src.counter import count_ocurrences
# from src.jobs import read
# import pytest

mock_py = [{}]
mock_js = [{}]

path = "src/jobs.csv"

word_py = "python"
word_js = "javascript"

# python -> 1639
# javascript -> 122


def test_counter():
    try:
        python_count = count_ocurrences(path, word_py)
        assert python_count == 1639
    except ValueError as err:
        print(err)
        raise

    try:
        javascript_count = count_ocurrences(path, word_js)
        assert javascript_count == 122
    except ValueError as err:
        print(err)
        raise
