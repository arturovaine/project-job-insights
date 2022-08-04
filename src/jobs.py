from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(f"{path}") as file:
        jobs_list = []
        jobs_csv = csv.DictReader(file, delimiter=",", quotechar='"')
        for item in jobs_csv:
            jobs_list.append(item)
        return jobs_list


# print(read('src/jobs.csv'))
