import time

import json
import requests

from tools import encrypt

'''
http://www.miaodiyun.com/doc/https_sms.html
'''

# 请求地址
api_url='https://api.miaodiyun.com/20150822/industrySMS/sendSMS'


# 开发者信息 - 由登录秒嘀获取
ACCOUNT_SID = 'c1686ba3f4544f6bb048cd23eee27273'
AUTH_TOKEN = 'cbcb3575480d4b1b814b2095feea3f55'
REST_URL = r'https://api.miaodiyun.com'

def send_sms_captcha(phone,code,valid_time_text):
    # POST 请求体参数
    accountSid = ACCOUNT_SID
    smsContent = AUTH_TOKEN
    templateid = '1352966489'
    param = str(code) + str(valid_time_text)
    to = str(phone)
    timestamp = str(time.time())
    real_sig = accountSid + smsContent + timestamp
    sig = str(encrypt.encrypt_md5(real_sig))
    respDataType = 'JSON'

    # 请求体
    data = {
        'accountSid': accountSid,
        'smsContent': smsContent,
        'templateid': templateid,
        'param': param,
        'to': to,
        'timestamp': timestamp,
        'sig': sig,
        'respDataType': respDataType,
    }

    # 请求体转换为 JSON 数据并编码
    data = json.dumps(data).encode(encoding='utf-8')

    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        # "Content-Type": "application/json"
        "Content-type": "application/x-www-form-urlencoded",
    }

    post_url = '{}/?accountSid={}&smsContent=【深圳市龙华区美由纪贸易商行】尊敬的用户，您好，您的验证码为{}，请于{}分钟内正确输入，如非本人操作，请忽略此短信。&to={}&timestamp={}&sig={}&respDataType={}'. \
        format(api_url, accountSid, code, valid_time_text, to, timestamp, sig, respDataType)
    # print(post_url)

    res = requests.post(post_url, data=data, headers=headers)
    # print(res.text)

    return res


# send_sms_captcha(18870279895,777777,1)












