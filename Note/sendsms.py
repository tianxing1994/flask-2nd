import time

from urllib import parse,request
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

# 短信模板所需要的两个参数： 验证码, 有效分钟数
code = 123456
valid_time_text = 1

# POST 请求体参数
accountSid = ACCOUNT_SID
smsContent = AUTH_TOKEN
templateid = '1352966489'
param = str(code)+str(valid_time_text)
to = '18870279895'
timestamp = str(time.time())
real_sig = accountSid + smsContent + timestamp
sig = str(encrypt.encrypt_md5(real_sig))
respDataType = 'JSON'

# 请求体
data = {
    'accountSid':accountSid,
    'smsContent':smsContent,
    'templateid':templateid,
    'param':param,
    'to':to,
    'timestamp':timestamp,
    'sig':sig,
    'respDataType':respDataType,
}
# 请求体转换为 JSON 数据并编码
data = json.dumps(data).encode(encoding='utf-8')

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    # "Content-Type": "application/json"
    "Content-type": "application/x-www-form-urlencoded",
}

# Python 发送 POST 请求并打印返回信息
# POST 请求，方法一：
# 将请求数据拼接成以下格式。 post 请求该地址
post_url = '{}/?accountSid={}&smsContent=【深圳市龙华区美由纪贸易商行】尊敬的用户，您好，您的验证码为{}，请于{}分钟内正确输入，如非本人操作，请忽略此短信。&to={}&timestamp={}&sig={}&respDataType={}'.\
    format(api_url,accountSid,code,valid_time_text,to,timestamp,sig,respDataType)
print(post_url)
# POST 请求:
res = requests.post(post_url,data=data,headers=headers)
print(res.text)

# # POST 请求，方法二：
# # 如方法一，需要将链接拼接成固定格式，但此方法还需要先对链接中的中文部分进行 utf-8 编码
# cn_word_1 = parse.quote('【深圳市龙华区美由纪贸易商行】尊敬的用户，您好，您的验证码为',encoding='utf-8')
# cn_word_2 = parse.quote('，请于',encoding='utf-8')
# cn_word_3 = parse.quote('分钟内正确输入，如非本人操作，请忽略此短信。',encoding='utf-8')
# # 拼接请求地址
# post_url = '{}/?accountSid={}&smsContent={}{}{}{}{}&to={}&timestamp={}&sig={}&respDataType={}'.\
#     format(api_url,accountSid,cn_word_1,code,cn_word_2,valid_time_text,cn_word_3,to,timestamp,sig,respDataType)
#
# print(post_url)
#
# req = request.Request(url=post_url,data=data,headers=headers)
# res = request.urlopen(req)
# res = res.read()
# print(res.decode(encoding='utf-8'))










