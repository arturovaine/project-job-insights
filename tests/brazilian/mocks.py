from src import jobs


def read_pt_file(path):
    dict_jobs = jobs.read(path)
    return dict_jobs
