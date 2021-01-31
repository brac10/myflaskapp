import pytest
import os
from example2 import example2
""" Containss unit tests for example 2
"""
def test_get_current_director(monkeypatch):
    """
    Given
    WHEN
    THEN
    """
    def mock_getcwd():
        return '/home/pi/myDev/python/myflaskapp'
           
    monkeypatch.setattr(os, 'getcwd', mock_getcwd)
    assert example2() == '/home/pi/myDev/python/myflaskapp'