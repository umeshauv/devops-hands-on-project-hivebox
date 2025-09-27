import pytest
from version import get_version

def test_version():
    assert  get_version() == 'v0.0.1'