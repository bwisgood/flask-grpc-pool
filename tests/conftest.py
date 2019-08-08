import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import pytest
from sample.sample import app as App


@pytest.fixture
def app():
    App.config["TESTING"] = True
    return App
