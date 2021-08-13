import os
import re

from covid_data import db as db  # noqa: F401
from covid_data import types as types  # noqa: F401
from covid_data.utils import places as places_utils  # noqa: F401
from db import queries as queries  # noqa: F401

with open(os.path.join(os.path.dirname(__file__), "../", "pyproject.toml"), "r") as f:
    project_info = f.read()

    regex = r"version = \"(.*)\""

    __version__ = re.findall(regex, project_info)[0]
