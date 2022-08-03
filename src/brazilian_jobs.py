from functools import lru_cache
from . import jobs


@lru_cache
def read_brazilian_file(path):
    """Reads a portuguese file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    dict_jobs = jobs.read(path)
    for job in dict_jobs:
        job["title"] = job.pop("titulo")
        job["salary"] = job.pop("salario")
        job["type"] = job.pop("tipo")

    return dict_jobs
