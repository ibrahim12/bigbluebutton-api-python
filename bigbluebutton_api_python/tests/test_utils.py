import pytest

from util import UrlBuilder


@pytest.mark.parametrize(
    "api_call,params,expected_url",
    [
        ('create', {'name': 'test'}, "https://www.bbb.com/bigbluebutton/api/create?name=testchecksum=94a6087025f335a03f585a0a87f6797aff04b2c2"),
        ('create', {'name': 'test name'}, "https://www.bbb.com/bigbluebutton/api/create?name=test+namechecksum=54ec1fa5e4ef7ba5288d73a5f22acba57c8aa2d0")

    ]
)
def test_buildUrl(api_call, params, expected_url):
    bbbServerBaseUrl = "https://www.bbb.com/bigbluebutton/api"
    securitySalt = "abcd"

    builder = UrlBuilder(bbbServerBaseUrl, securitySalt)
    url = builder.buildUrl(api_call, params)

    assert url == expected_url
