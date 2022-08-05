from src.brazilian_jobs import read_brazilian_file

path = "tests/mocks/brazilians_jobs.csv"

# dict_pt = {"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}
dict_en = {"title": "Maquinista", "salary": "2000", "type": "trainee"}


def test_brazilian_jobs():
    try:
        dict = read_brazilian_file(path)
        assert dict_en in dict
    except ValueError:
        raise
