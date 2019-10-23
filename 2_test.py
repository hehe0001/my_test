#!/user/bin/env python
#  _*_ coding:utf-8 _*_
import requests


class TestList():
    def test_list(self):
        res = requests.get(url='https://t-user.120yibao.com/api/user/patient/list?_t=1571653641',
                           params={'token':'ac4c7997-42d9-41c8-8d33-8d33dbc12000'})

        print(res.json())
        assert res.status_code == 200