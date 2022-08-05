from src.sorting import sort_by


mock = [
    {
        "min_salary": 3000,
        "max_salary": 7000,
    },
    {
        "min_salary": 2000,
        "max_salary": 8000,
    },
    {
        "min_salary": 1000,
        "max_salary": 9000,
    },
]

sorted = [mock[2], mock[1], mock[0]]


def test_sort_by_criteria():
    try:
        sort_by(mock, "min_salary")
        assert mock == sorted
    except ValueError as err:
        print(err)
        raise

    try:
        sort_by(mock, "max_salary")
        assert mock == sorted
    except ValueError as err:
        print(err)
        raise
