from datetime import datetime
from flask import render_template,  redirect, url_for, request,jsonify,current_app
from app.wx import bp
import hashlib
import xml.etree.ElementTree as ET
from app.wx  import receive,reply

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
@bp.route('/index/<yourname>')
def index(yourname=''):
    return render_template('wx/index.html',yourname=yourname)


@bp.route('/next',methods=['GET'])
def next():
    return render_template('wx/next.html')

@bp.route('/wxsvr',methods=['GET'])
def Handle(object=''):
    current_app.logger.info('request.method:'+request.method)
    current_app.logger.info('request.url:'+request.url)
    #current_app.logger.info('request.body:'+request.body.read())
   
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
            
            current_app.logger.info("request.get_data is ", webData)
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "test"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print("暂且不处理")
                return "success"
        except Exception as e:
            print(e)
#WARNING:tornado.access:405 POST /wx/wxsvr?signature=0038d6efd1c0652643283085f2171f77f0f5c4a7&timestamp=1600851814&nonce=1080361974&openid=oMcHK6h_cRu_mVXlftDqA87KRkbs
