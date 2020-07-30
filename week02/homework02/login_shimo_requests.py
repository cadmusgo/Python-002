import requests

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Referer' : 'https://shimo.im/login?from=home'
}

s = requests.Session()

# 登陸前讀取cookie
pre_login = 'https://shimo.im/login?from=home'
pre_resp = s.get(pre_login, headers=headers)

# login
form_data = {
    'email': 'cadmus.go@gmail.com',
    'mobile': '+86undefined',
    'password': 'XPV3FKlkFUyPMDRnBFQR'
}
login_url = 'https://shimo.im/lizard-api/auth/password/login'

respone = s.post(login_url,headers=headers,cookies = s.cookies)
print(respone.text)






#
# user_name = 'cadmus.go@gmail.com'
# user_passowrd = 'XPV3FKlkFUyPMDRnBFQR'
#
# r = requests.get("https://shimo.im/login?from=home",headers={'user-agent' : user_agent})
# print(r.content)