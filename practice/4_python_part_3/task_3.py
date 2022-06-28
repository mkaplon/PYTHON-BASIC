"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
from operator import is_
import re


def is_http_domain(domain: str) -> bool:
    match = r"^(http)s?://([a-zA-Z0-9]+\.)+[a-zA-Z0-9]+/?$"
    return bool(re.search(match, domain))


"""
write tests for is_http_domain function
"""

def test_domain_http():
    assert is_http_domain('https://wikipedia.org/') == True

def test_domain_https():
    assert is_http_domain('http://wikipedia.org') == True

def test_domain_without_http():
    assert is_http_domain('griddynamics.com') == False