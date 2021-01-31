import pytest
import requests
from example1 import example1

def test_get_response_succes(monkeypatch):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = 'http://httpbin.org/get'
            self.headers = {'blah': '1234'}
        
        def json(self):
            return {'account' : '5678',
                    'url': 'http://www.testurl.com'}
    
    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    assert example1() == (200, 'http://www.testurl.com') 

def test_get_response_failure(monkeypatch):
    class MockResponse(object):
        def __init__(self):
            self.status_code = 404
            self.url = 'http://httpbin.org/get'
            self.headers = {'blah':'1234'}
        
        def json(self):
            return {'error': 'bad'}
    
    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    assert example1() == (404, '')