#Location-Based Service LBS
from flask import jsonify,request,url_for,abort,Response
from flask_login import current_user, login_user,logout_user,login_required
import time,datetime
from app.api import bp
from app.api.errors import bad_request,error_response

from urllib.request  import urlopen
from json import load
import sys
import chardet
import re


def get_client_ip():
    clientip=request.remote_addr
    if clientip=='127.0.0.1' or clientip.find('::')>0:
        try:
            clientip = load(urlopen('http://httpbin.org/ip'))['origin']
        except Exception as e:
            print(e)
            clientip=u'未知'
    return clientip

def get_client_location_by_ip(clientip):
    clientip =get_client_ip()
    location=u'未知'
    try:
        content = urlopen('http://ip.ws.126.net/ipquery?ip=%s'%(clientip)).read().decode('gb2312')
        obj=re.search(r'lo="(.*)".*lc="(.*)";',content,re.M|re.I)
        if obj:
            location = obj.group(1)+obj.group(2)
    except Exception as e:
        print(e)
    return location 
@bp.route('/get_ip',methods=['GET'])
def get_ip():
    return jsonify({'ip':get_client_ip()})

@bp.route('/get_location',methods=['GET'])
def get_location():
    clientip = get_client_ip()
    localtion = get_client_location_by_ip(clientip)
    return jsonify({'location':localtion,'ip':clientip})
