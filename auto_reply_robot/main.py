import itchat
import requests

def get_response(_info):
    print(_info)
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '0fa7f77a072948bdbfd703d0c9284214',
        'info':_info,
        'userid': 'sweetymousewh',
    }
    r = requests.post(api_url, data=data).json()
    print(r.get('text'))
    return r

@itchat.msg_register(itchat.content.TEXT)
def  text_reply(msg):
    return "你的小可爱回复:" + get_response(msg["Text"])["text"]



if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()