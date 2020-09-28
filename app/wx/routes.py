from datetime import datetime
from flask import render_template,  redirect, url_for, request,jsonify,current_app
from app.wx import bp
import hashlib
import xml.etree.ElementTree as ET
from app.wx  import receive,reply,WxAPIs
from flask import request
import requests
import urllib.parse

def checkSignature():
    signature  = request.args.get('signature','')
    timestamp =  request.args.get('timestamp','')
    nonce =  request.args.get('nonce','')
    token = "7242609C8AEF41F88622A80AFCBE4E83"
 
    # 2、 进行字典排序
    data = [token, timestamp, nonce]
    data.sort()

    # 3、三个参数拼接成一个字符串并进行sha1加密
    temp = ''.join(data)
    sha1 = hashlib.sha1(temp.encode('utf-8'))
    hashcode = sha1.hexdigest()
    print("handle/GET func: hashcode:{}, signature:{} ".format(hashcode, signature))

    return  hashcode == signature

@bp.route('/',methods=['GET'])
@bp.route('/index',methods=['GET'])
def index():
    return render_template('wx/index.html')

@bp.route('/get_sign',methods=['GET'])
def get_sign(): 
    redirect_url=request.args.get('url')
    print(redirect_url)
    sign =WxAPIs.get_jsapi_sign(redirect_url)
    print(WxAPIs.get_jsapi_sign(redirect_url))
    return jsonify({'jsapi_sign':sign})


@bp.route('/jssdkindex',methods=['GET'])
def jssdk_index():
    code = request.args.get('code','no-code')
    state =request.args.get('state','no-state')
    url=request.url
    return render_template('wx/code.html',code=code,state=state,url=url)
    #return render_template('wx/jindex.html',yourname=yourname,jsapi_sign=jsapi_sign)
    #https://open.weixin.qq.com/connect/oauth2/authorize?appid=APPID&redirect_uri=REDIRECT_URI&response_type=code&scope=SCOPE&state=STATE#wechat_redirect
    #https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxfa9191e55c89875b&redirect_uri=http%3A//localhost%3A5000/wx/jssdkindex&response_type=code&scope=snsapi_userinfo&state=7df989af9e549cf#wechat_redirect
    #if code == '':
    # redirect_uri=urllib.parse.quote('http://www.zjswdl.cn/wx/code')
    # url='https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri={}&response_type=code&scope=snsapi_userinfo&state={}#wechat_redirect'.format(WxAPIs.APPID,redirect_uri,WxAPIs.STATE)
    # print(url)
    # return redirect(url)
    # else:
    #     print(url)
    #     #获取code后，请求以下链接获取access_token：
    #     url='https://api.weixin.qq.com/sns/oauth2/access_token?appid=wxfa9191e55c89875b&secret=7df989af9e549cfbad94dc08bbf84534&code={}&grant_type=authorization_code'.format(code)
    #     res = requests.get(url)
    #     token_info = res.json()
    #     access_token =token_info['access_token']
    #     openid = token_info['openid']
    #     current_app.logger.info('Code:',code)
    #     current_app.logger.info('Access token:',access_token)
    #     current_app.logger.info('Open Id:',openid)
    #     url='https://api.weixin.qq.com/sns/userinfo?access_token={}&openid={}&lang=zh_CN'.format(access_token,openid)
    #     r = requests.get(url)
    #     user_info = r.json()
    #     url='https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={}&type=jsapi'.format(access_token)
    #     r = requests.get(url)
    #     ticket_info =r.json()
    #     jsapi_ticket = ticket_info['ticket']
    #     sign = sign.Sign(jsapi_ticket,'http://www.zjswdl.cn')

    #     return redirect(url_for('index'),token_info=token_info,user_info=user_info,ticket_info=ticket_info,sign=sign)

@bp.route('/MP_verify_BYFISTG63Qu18us1.txt',methods=['GET'])
def get_mp_verify():
    return render_template('wx/MP_verify_BYFISTG63Qu18us1.txt')

@bp.route('/code_a',methods=['GET'])
def get_code_a():
    return render_template('wx/code_a.html')

@bp.route('/code_b',methods=['GET'])
def get_code_b():
    code = request.args.get('code','no code')
    state = request.args.get('state','no state')
    url = request.url
    return render_template('wx/code_b.html',code=code,state=state,url=url)


@bp.route('/next',methods=['GET'])
def next():
    return render_template('wx/next.html')

@bp.route('/wxsvr',methods=['GET','POST'])
def Handle(object=''):
    current_app.logger.info('request.method:'+request.method)
    current_app.logger.info('request.url:'+request.url)
    #current_app.logger.info('request.body:'+request.body.read())
#INFO:flask.app:request.url:http://localhost:8008/wx/wxsvr?
# signature=9cab268d4bf28b694eaa5d68a57cc08ff510bb73
# &timestamp=1601184099&nonce=1583543568
# &openid=oMcHK6h_cRu_mVXlftDqA87KRkbs
 
    if request.method == 'GET':
        try:
            # # 1、 获取携带的 signature、timestamp、nonce、echostr
            echostr =  request.args.get('echostr','')
            # signature  = request.args.get('signature','')
            # timestamp =  request.args.get('timestamp','')
            # nonce =  request.args.get('nonce','')
            # echostr =  request.args.get('echostr','')
            
            #print(signature, timestamp, nonce, echostr)

            # token = "7242609C8AEF41F88622A80AFCBE4E83"

            # # 2、 进行字典排序
            # data = [token, timestamp, nonce]
            # data.sort()

            # # 3、三个参数拼接成一个字符串并进行sha1加密
            # temp = ''.join(data)
            # sha1 = hashlib.sha1(temp.encode('utf-8'))
            # hashcode = sha1.hexdigest()

            # print("handle/GET func: hashcode, signature: ", hashcode, signature)

            # 4、对比获取到的signature与根据上面token生成的hashcode，如果一致，则返回echostr，对接成功
            if  checkSignature() :
                return echostr
            else:
                'error'
                
        except Exception as e:
            print(e)
    elif request.method=='POST':
        try:
            webData =  request.get_data()
            #后台打日志
            recMsg = receive.parse_xml(webData)
            #current_app.logger.info("request.get_data is ", webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = str(recMsg.Content, encoding = "utf-8")  
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif isinstance(recMsg,receive.ImageMsg) and recMsg.MsgType =='image':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                mediaId = recMsg.MediaId 
                replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
            else:
                # toUser = recMsg.FromUserName
                # fromUser = recMsg.ToUserName
                # content = u'你刚才发了消息类型是:'+recMsg.MsgType  
                # replyMsg = reply.TextMsg(toUser, fromUser, content)
                # return replyMsg.send()
                return 'success' 
        except Exception as e:
             current_app.logger.error(e)
             return 'success'
        
#WARNING:tornado.access:405 POST /wx/wxsvr?signature=0038d6efd1c0652643283085f2171f77f0f5c4a7&timestamp=1600851814&nonce=1080361974&openid=oMcHK6h_cRu_mVXlftDqA87KRkbs
