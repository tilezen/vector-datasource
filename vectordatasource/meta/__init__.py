import os.path


def find_yaml_path():
    import vectordatasource
    vec_src_path = os.path.dirname(vectordatasource.__file__)
    yaml_path = os.path.abspath(os.path.join(vec_src_path, '..', 'yaml'))
    return yaml_path
