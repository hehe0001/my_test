#!/user/bin/env python
#  _*_ coding:utf-8 _*_

import requests
import pytest

class TestV2exApiWithParams(object):
    domain = 'https://www.v2ex.com/'

    @pytest.fixture(params=['python', 'java', 'go', 'nodejs'])
    def lang(self, request):
        return request.param

    def test_node(self, lang):
        path = 'api/nodes/show.json?name=%s' %(lang)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == lang
        assert 0