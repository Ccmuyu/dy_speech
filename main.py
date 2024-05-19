# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
import websockets
import time
import speech


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


async def echo(websocket, path):
    async for message in websocket:
        print(f'[{time.ctime()}]: ')
        print(message)
        speech.speak(message)
        # message = "服务端获取到消息: {}".format(message)
        # await websocket.send(message)


def init():
    print('WebSocket服务启动成功，可通过 ws://localhost:8765 进行访问')
    asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()


'''
# 创建一个WebSocket服务端
# 用于接收解析到的弹幕数据
# 测试弹幕转发功能
'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('')
    init()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
