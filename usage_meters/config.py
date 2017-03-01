"""
Module for parsing configuration files.
Configuration files should be yaml.
"""
import yaml


_CONF = {}


def load(filename):
    """Load a dictionary from a yaml file.
    Expects the file at filename to be a yaml file.
    Returns the parsed configuration as a dictionary.
    :param filename: Name of the file
    :type filename: String
    :return: Loaded configuration
    :rtype: Dict
    """
    if not filename in _CONF:
        with open(filename, 'r') as f:
            _CONF[filename] = yaml.safe_load(f)
    return _CONF[filename]
