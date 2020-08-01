import urllib
from hashlib import sha1
from re import match

class UrlBuilder:
    def __init__(self, bbbServerBaseUrl, securitySalt):
        if not match('/[http|https]:\/\/[a-zA-Z1-9.]*\/bigbluebutton\/api\//', bbbServerBaseUrl):
            if not bbbServerBaseUrl.startswith("http://") and not bbbServerBaseUrl.startswith("https://"):
                bbbServerBaseUrl = "http://" + bbbServerBaseUrl
            if not bbbServerBaseUrl.endswith("/bigbluebutton/api/"):
                bbbServerBaseUrl = bbbServerBaseUrl[:(bbbServerBaseUrl.find("/", 8)
                    if bbbServerBaseUrl.find("/", 8) != -1 else len(bbbServerBaseUrl))] + "/bigbluebutton/api/"

        self.securitySalt         = securitySalt
        self.bbbServerBaseUrl     = bbbServerBaseUrl
    def prepare_params(self, params={}):
        for key, value in params.items():
            if isinstance(value, bool):
                params[key] = "true" if value else "false"
            else:
                params[key] = str(value)
        return params

    def buildUrl(self, api_call, params={}):
        url = self.bbbServerBaseUrl
        url += api_call + "?"

        params = self.prepare_params(params)
        params['checksum'] = self.__get_checksum(api_call, params)
        return url + urllib.parse.urlencode(params)

    def __get_checksum(self, api_call, params={}):
        secret_str = api_call
        params = self.prepare_params(params)
        secret_str += urllib.parse.urlencode(params)
        secret_str += self.securitySalt
        return sha1(secret_str.encode('utf-8')).hexdigest()
