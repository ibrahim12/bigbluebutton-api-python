import pytest

from util import UrlBuilder


@pytest.mark.parametrize(
    "api_call,params,expected_url",
    [
        ('create', {'name': 'test'}, "https://www.bbb.com/bigbluebutton/api/create?name=test&checksum=94a6087025f335a03f585a0a87f6797aff04b2c2"),
        ('create', {'name': 'test name'}, "https://www.bbb.com/bigbluebutton/api/create?name=test+name&checksum=6b3b06295927cbae5e5ebe10abccc9ed3d066fc1")

    ]
)
def test_buildUrl(api_call, params, expected_url):
    bbbServerBaseUrl = "https://www.bbb.com/bigbluebutton/api"
    securitySalt = "abcd"

    builder = UrlBuilder(bbbServerBaseUrl, securitySalt)
    url = builder.buildUrl(api_call, params)

    assert url == expected_url
