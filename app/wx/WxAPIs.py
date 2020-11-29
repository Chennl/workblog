
import urllib.request
import urllib.parse
import json
import os
import time
from app.wx import WxConstants,sign
import requests
 

APPID='wxfa9191e55c89875b'
#APPID='wxe5c0f537d7c604c6'
APPSECRET='7df989af9e549cfbad94dc08bbf84534'
REDIRECT_URL='www.zjswdl.cn'
STATE='7df989af9e549cf'

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


def get_access_token_from_file():
    json_data = {}
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'data')
    if not os.path.exists(file_path):
        os.mkdir(file_path)
        return ''

    access_token_file = os.path.join(file_path,'access_token.json')
    if os.path.isfile(access_token_file):
        with open(access_token_file,'r') as fp:
            json_str = fp.read()
            if(len(json_str)<10):
                return ''
            json_data = json.loads(json_str)

        expires_by = json_data['expires_by']
        if expires_by < int(time.time()):
            return ''
        else:
            return json_data['access_token']
    else:
        return ''
def get_access_token_by_code_from_file():
    json_data = {}
    file_path = get_data_file_path()
    access_token_file = os.path.join(file_path,'access_token_by_code.json')
    if os.path.isfile(access_token_file):
        with open(access_token_file,'r') as fp:
            try:
                json_data = json.load(fp)
            except ValueError:
                json_data={"errcode":40014,"errmsg":"JSON syntax error"}
        
        if json_data['expires_by'] < int(time.time()):
            json_data={"errcode":40014,"errmsg":"access token time out"}
        else:
            return json_data
    else:
        json_data={"errcode":40014,"errmsg":"no access token found"}
    return json_data

def get_data_file_path():
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'data')
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path

def get_jsapi_ticket_from_file():
    json_data = {}
    jsapi_ticket_file = os.path.join(get_data_file_path(),'jsapi_ticket.json')
    if os.path.isfile(jsapi_ticket_file):
        with open(jsapi_ticket_file,'r',encoding='utf-8') as fp:
            json_str = fp.read()
            if(len(json_str)<10):
                return ''
            json_data = json.loads(json_str)
            
        expires_by = json_data['expires_by']
        if expires_by < int(time.time()):
            return ''
        else:
            return json_data['ticket']
    else:
        return ''


def get_access_token():

    access_token =get_access_token_from_file()
    
    if access_token == '':
        url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(APPID,APPSECRET)
        r = requests.get(url)
        data = r.json()
        create_time =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        data['expires_by'] = int(time.time()) + 7000
        data['create_time'] = create_time
        access_token = data['access_token']
        print("Access Token:",access_token)
        access_token_file = os.path.join(get_data_file_path(),'access_token.json')
        with open(access_token_file,'w+',encoding='utf-8') as fp:
            json.dump(data,fp,ensure_ascii=False)
    return access_token

def get_access_token_by_code(code=''):

    if code == '':
        data =get_access_token_by_code_from_file()

    else:  
        url='https://api.weixin.qq.com/sns/oauth2/access_token?appid={}&secret={}&code={}&grant_type=authorization_code'.format(APPID,APPSECRET,code)
        data = WxGet(url)
        if 'errcode' not in data:
            create_time =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            data['expires_by'] = int(time.time()) + 7000
            data['create_time'] = create_time
            access_token_file = os.path.join(get_data_file_path(),'access_token_by_code.json')
            with open(access_token_file,'w+',encoding='utf-8') as fp:
                json.dump(data,fp,ensure_ascii=False)
    return data

def get_jsapi_ticket():
    jsapi_ticket = get_jsapi_ticket_from_file()
    if jsapi_ticket == '':
        access_token = get_access_token()
        url='https://api.weixin.qq.com/cgi-bin/ticket/getticket?type=jsapi&access_token={}'.format(access_token)

        r = requests.get(url)
        ticket_info =r.json()
        print('ticket json:',ticket_info)
        if ticket_info['errcode']== 0:
            ticket_info['expires_by'] = int(time.time()) + 7000
            ticket_info['create_time'] =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            jsapi_ticket = ticket_info['ticket']
            jsapi_ticket_file = os.path.join(get_data_file_path(),'jsapi_ticket.json')
            with open(jsapi_ticket_file,'w+',encoding='utf-8') as fp:
                json.dump(ticket_info,fp,ensure_ascii=False)
    return jsapi_ticket


def get_jsapi_sign(redirect_url=REDIRECT_URL):
    jsapi_ticket = get_jsapi_ticket()
    #redirect_url='http://www.zjswdl.cn'+request.full_path
    print(redirect_url)
    if jsapi_ticket !='':
        jsapi_sign = sign.Sign(jsapi_ticket, redirect_url)
        return jsapi_sign.sign()
    else:
        return {}

def get_menu(access_token):
    targetUrl='https://api.weixin.qq.com/cgi-bin/menu/get?access_token={}'.format(access_token)
    return WxGet(targetUrl)

def get_menu_from_file():
    file_path= os.path.join(get_data_file_path(),'menu.json')
    with open(file_path,'r',encoding='utf-8') as fp:
        return json.load(fp)
    return {}
    
def create_menu(access_token):
    menu_data = get_menu_from_file()
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
               #https://api.weixin.qq.com/sns/userinfo?access_token=ACCESS_TOKEN&openid=OPENID&lang=zh_CN
    return WxGet(targetUrl)


def upload_media(access_token,media_type,files):
    targetUrl='https://api.weixin.qq.com/cgi-bin/media/upload?access_token={}&type={}'.format(access_token,media_type)
    return requests.post(url=targetUrl,  files=files)


def upload_image(access_token):
    files = {'file':open('C:\\workspace\\pythonWorkspace\\workblog\\app\\wx\\medias\\tea.jpg','rb')}
    return upload_media(access_token,'image',files)
    #{'type': 'image', 'media_id': 'lpQgSKQSGMe0P0hX2lQjyJdW7Ix8nW1kh9DmUQ39cTYJu1SDjPbpTPwgbwAqVxKd', 'created_at': 1601004616, 'item': []}

def update_menu():
     access_token = get_access_token()
     delete_menu(access_token)
     create_menu(access_token)

if __name__=='__main__':
    code='031C1QFa16WUHz0F2uFa1uFbZS1C1QFA'
    data = get_access_token_by_code(code)
    print(data)
    #print(get_menu_from_file())
    #update_menu()
    #jsapi_sign = get_jsapi_sign()

    #print(jsapi_sign)

    #data = get_jsapi_ticket(access_token)
    #print(data)
    #get_jsapi_ticket
    #response = upload_image(access_token)
    #print(response.json())
  #Media API

  # Menu API
    # return_json= get_menu(access_token)
    # if 'errcode' in return_json:
    #     errcode = return_json['errcode']
    #     errmessage = WxConstants.WxResponseCode[errcode]
    #     if errcode == 46003:
    #         print('errcode:',errcode ,'errmessage:', errmessage)
    #         print('不存在的菜单数据，正在为你创建自定义菜单...')
    #         return_json = create_menu(access_token,menu_info.menu_data)
    #         errcode = return_json['errcode']
            
    #         errmessage = WxConstants.WxResponseCode[errcode]
    #         print('errcode:',errcode ,'errmessage:', errmessage)
    #     else:
    #         print('errcode:',errcode ,'errmessage:', errmessage) 
    # else:   
    #     print(return_json)
    #     print('正在删除自定义菜单...')
    #     return_json = delete_menu(access_token)
    #     errcode = return_json['errcode']
    #     errmessage = WxConstants.WxResponseCode[errcode]
    #     print('errcode:',errcode ,'errmessage:', errmessage)
  
