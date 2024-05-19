import json

import pyttsx3

engine = pyttsx3.init()


# s = '{"id":7370634509789777000,"type":"member","nickname":"渝***","content":"来了","memberCount":12,"likeCount":0,"followCount":0,"totalUserCount":0,"rank":[],"gift":{"name":"","count":0,"url":"","desc":""}}'
# obj = json.loads(s)
# print(obj['content'])

def speak(message):
    obj = json.loads(message)
    text = gen_content(obj)
    if text != '':
        engine.say(text)
        engine.runAndWait()


def gen_content(message):
    message_type_ = message['type']
    # if message_type_ == 'member':  # 进入房间欢迎语
    #     return message['nickname'] + message['content']
    if message_type_ == 'chat':  # 聊天
        return message['content']
    # if message_type_ == 'like':  # 点赞
    #     return
    if message_type_ == 'gift':  # 礼物
        return '感谢' + message['nickname'] + message['content']
