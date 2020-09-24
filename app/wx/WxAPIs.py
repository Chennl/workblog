
import urllib.request
import urllib.parse
import json
from app.wx import menu_info,WxConstants

APPID='wxfa9191e55c89875b'
APPSECRET='7df989af9e549cfbad94dc08bbf84534'

def WxGet(url):
        try:
            response = urllib.request.urlopen(url)
            print('WxGet: [url]:',url,' [info]:',response.info(),'[HTTP status code]:',response.getcode())
            response_data =response.read().decode('utf-8')
            return json.loads(response_data)
        except Exception as e:
            print('Internet Error',e)


def WxPost(url,data):
        #json.dumps() 字符编码转换 https://www.cnblogs.com/stubborn412/p/3818423.html
        post_data = json.dumps(data,ensure_ascii=False)
        post_data = bytes(post_data,'utf-8')
        #print(post_data)
        try:
            request = urllib.request.Request(url, data=post_data,method='POST')
            response = urllib.request.urlopen(request)
            print('WxPost: [url]:',url,' [info]:',response.info(),' [HTTP status code]:',response.getcode())

            response_data =response.read().decode('utf-8')
            print(response_data)
            return json.loads(response_data)
        except Exception as e:
            print(e)

def get_access_token():
    targetUrl='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(APPID,APPSECRET)
    return WxGet(targetUrl)

def get_menu(access_token):
    targetUrl='https://api.weixin.qq.com/cgi-bin/menu/get?access_token={}'.format(access_token)
    return WxGet(targetUrl)

def create_menu(access_token,menu_data):
    targetUrl=' https://api.weixin.qq.com/cgi-bin/menu/create?access_token={}'.format(access_token)
    return WxPost(targetUrl,menu_data)
 
def delete_menu(access_token):
    targetUrl='https://api.weixin.qq.com/cgi-bin/menu/delete?access_token={}'.format(access_token)
    return WxGet(targetUrl)
    


#用户管理
#获取关注用户
#返回结果
#{
#     "total": 2, 
#     "count": 2, 
#     "data": {
#         "openid": [
#             "oMcHK6h_cRu_mVXlftDqA87KRkbs", 
#             "oMcHK6rFMfGeJx4w35_XbXVvMAsA"
#         ]
#     }, 
#     "next_openid": "oMcHK6rFMfGeJx4w35_XbXVvMAsA"
# }
#
def get_user(access_token):
    targetUrl='https://api.weixin.qq.com/cgi-bin/user/get?access_token={}'.format(access_token)
    return WxGet(targetUrl)

    # 获取用户基本信息
    # 返回结果
    # {
    #     "subscribe": 1, 
    #     "openid": "oMcHK6h_cRu_mVXlftDqA87KRkbs", 
    #     "nickname": "ChenNianlai", 
    #     "sex": 1, 
    #     "language": "zh_CN", 
    #     "city": "杭州", 
    #     "province": "浙江", 
    #     "country": "中国", 
    #     "headimgurl": "http://thirdwx.qlogo.cn/mmopen/jJSbu4Te5ib9tvmPlTn4GddttBVjtCdx2DicWmibIF9v881icqDorrhqUB6r5uqDa6FsZoxJ3ibHK9J0dyibgct5qgod6zQQc4fOko/132", 
    #     "subscribe_time": 1600823444, 
    #     "remark": "", 
    #     "groupid": 0, 
    #     "tagid_list": [ ], 
    #     "subscribe_scene": "ADD_SCENE_QR_CODE", 
    #     "qr_scene": 0, 
    #     "qr_scene_str": ""
    # }
def get_user_info(access_token,open_id):
    targetUrl='https://api.weixin.qq.com/cgi-bin/user/info?access_token={}&openid={}'.format(access_token,open_id)
    return WxGet(targetUrl)
 
if __name__=='__main__':
    data={'access_token': '37_UvmV6W_zJ5FBr7Et5nZGVj3I6l--oFCMxpnZaezyc7d9xxoVAaM5Trv1-Jbg1UojmMquA6KMEv9uFSZKXO73C5iuoCIKqpKRvtbfqF7GdeuSqWxd6OUyHmESzIFUfReA0Hq9NQ1t6lLiXbRKWSGdABAPLZ', 'expires_in': 7200}
    #data = get_access_token()
    access_token= data['access_token']
  
    return_json= get_menu(access_token)
    if 'errcode' in return_json:
        errcode = return_json['errcode']
        errmessage = WxConstants.WxResponseCode[errcode]
        if errcode == 46003:
            print('errcode:',errcode ,'errmessage:', errmessage)
            print('不存在的菜单数据，正在为你创建自定义菜单...')
            return_json = create_menu(access_token,menu_info.menu_data)
            errcode = return_json['errcode']
            
            errmessage = WxConstants.WxResponseCode[errcode]
            print('errcode:',errcode ,'errmessage:', errmessage)
        else:
            print('errcode:',errcode ,'errmessage:', errmessage) 
    else:   
        print(return_json)
        #print('正在删除自定义菜单...')
        #return_json = delete_menu(access_token)
        #errcode = return_json['errcode']
        #errmessage = WxConstants.WxResponseCode[errcode]
        #print('errcode:',errcode ,'errmessage:', errmessage)
    #return_json = delete_menu(access_token)
    #print(return_json)
    #return_json = create_menu(access_token,menu_info.menu_data)
    #print(return_json)
