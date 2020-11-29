# -*- coding: utf-8 -*-#
# filename: receive.py
import xml.etree.ElementTree as ET


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)
    elif msg_type == 'voice':
        return VoiceMsg(xmlData)
    elif msg_type == 'video':
        return VideoMsg(xmlData)
    elif msg_type == 'shortvideo':
        return ShortVideoMsg(xmlData)
    elif msg_type == 'location':
        return LocationMsg(xmlData)
    elif msg_type == 'link':
        return LinkMsg(xmlData)
    else:
        return Msg(xmlData)




class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        if xmlData.find('MsgId') is not None: 
            self.MsgId = xmlData.find('MsgId').text


class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text.encode("utf-8")



class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text
        self.PicUrl = xmlData.find('PicUrl').text

class VoiceMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MediaId = xmlData.find('MediaId').text
        self.Format = xmlData.find('Format').text

class VideoMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MediaId = xmlData.find('MediaId').text
        self.ThumbMediaId = xmlData.find('ThumbMediaId').text

class ShortVideoMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MediaId = xmlData.find('MediaId').text
        self.ThumbMediaId = xmlData.find('ThumbMediaId').text
class LocationMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Location_X = xmlData.find('Location_X').text
        self.Location_Y = xmlData.find('Location_Y').text
        self.Scale = xmlData.find('Scale').text
        self.Label = xmlData.find('Label').text 

class LinkMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Title = xmlData.find('Title').text
        self.Description = xmlData.find('Description').text
        self.Url = xmlData.find('Url').text
        self.Label = xmlData.find('Label').text 


