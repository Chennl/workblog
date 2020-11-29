import time
import random
import string
import hashlib

class Sign:
    def __init__(self, jsapi_ticket, url):
        self.ret = {
            'nonceStr': self.__create_nonce_str(),
            'jsapi_ticket': jsapi_ticket,
            'timestamp': self.__create_timestamp(),
            'url': url
        }

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())
    def sign(self):
        string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
        print(string)
        self.ret['signature'] = hashlib.sha1(string.encode('utf-8')).hexdigest()
        return self.ret
   
    


if __name__ == '__main__':
    # 注意 URL 一定要动态获取，不能 hardcode
    access_token = '37_X0nSn6iflzU1YGesfTLmCwRZVPa4pCa-CPOJxJ9vUcv2I9Zf8r4WrWWtWNfOYVuR68SLHnoeGs4SR2eqo1SDkPtPXOJ5YY27-Z_Vy30GYshtfsJGegLujwSNTmudCxlOptv8RqRsGJeORAJ0HJHaAAAUWU'
    # url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?type=jsapi&access_token={}".format(access_token)
    # r = requests.get(url)
    # data = r.json()
    # jsapi_ticket = data['ticket']
    jsapi_ticket = 'O3SMpm8bG7kJnF36aXbe88Q6dQDPs9NF5_obOiNFRwu0vcPrzZFVM-pUK8HUC9X9SBfxt2U9Vadde_6GMVrvcQ'
    sign = Sign(jsapi_ticket, 'http://www.zjswdl.cn')
    print(sign.sign())
    print(sign.ret['nonceStr'])
