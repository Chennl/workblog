# -*- coding: utf-8 -*-#
# filename: reply.py
import time

class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"

class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{Content}]]></Content>
            </xml>
            """
        return XmlForm.format(**self.__dict)

class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <Image>
                <MediaId><![CDATA[{MediaId}]]></MediaId>
                </Image>
            </xml>
            """
        return XmlForm.format(**self.__dict)

class VoiceMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[voice]]></MsgType>
                <Voice>
                <MediaId><![CDATA[{MediaId}]]></MediaId>
                </Voice>
            </xml>
            """
        return XmlForm.format(**self.__dict)
class VideoMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId,title,description):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId
        self.__dict['Title'] = title
        self.__dict['Description'] = description
    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[video]]></MsgType>
                <Video>
                    <MediaId><![CDATA[{mediaId}]]></MediaId>
                    <Title><![CDATA[{title}]]></Title>
                    <Description><![CDATA[{description}]]></Description>
                </Video>
            </xml>
            """
        return XmlForm.format(**self.__dict)

class MusicMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId,title,description,musicUrl,hqMusicUrl):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId
        self.__dict['Title'] = title
        self.__dict['Description'] = description
        self.__dict['MusicUrl'] = musicUrl
        self.__dict['HQMusicUrl'] = hqMusicUrl
    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[music]]></MsgType>
                <Music>
                    <Title><![CDATA[{title}]]></Title>
                    <Description><![CDATA[{description}]]></Description>
                    <MusicUrl><![CDATA[{MusicUrl}]]></MusicUrl>
                    <HQMusicUrl><![CDATA[{HQMusicUrl}]]></HQMusicUrl>
                    <ThumbMediaId><![CDATA[media_id]]></ThumbMediaId>
                </Music>
            </xml>
            """
        return XmlForm.format(**self.__dict) 


class NewsMsg(Msg):
    def __init__(self, toUserName, fromUserName, articleCount,title,description,picUrl,url):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['ArticleCount'] = articleCount
        self.__dict['Title'] = title
        self.__dict['Description'] = description
        self.__dict['PicUrl'] = picUrl
        self.__dict['Url'] = url
    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>{ArticleCount}</ArticleCount>
                <Articles>
                    <item>
                    <Title><![CDATA[{Title}]]></Title>
                    <Description><![CDATA[{Description}]]></Description>
                    <PicUrl><![CDATA[{PicUrl}]]></PicUrl>
                    <Url><![CDATA[{Url}]]></Url>
                    </item>
                </Articles>
            </xml>
            """
        return XmlForm.format(**self.__dict) 


 