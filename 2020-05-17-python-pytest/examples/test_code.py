import pytest
from .code import *

class TestPub:

    def test_serve_beer_legal(self):
        adult = 25
        assert serve_beer(adult) == "Have beer"

    def test_serve_beer_illegal(self):
        child = 10
        assert serve_beer(child) == "No beer"
        
    def test_serve_beer_no_age(self):
        with pytest.raises(ValueError, match="Tell me your age"):
            age = None
            serve_beer(age)
