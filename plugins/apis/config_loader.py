import yaml


def loader(file_path):
    return yaml.load(open(file_path))
