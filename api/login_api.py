# 封装登录api
import requests


class Login_api :
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"

    def login(self,mobile,password):
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(self.login_url,json=jsonData)
    # 传入json数据
    def my_login(self,jsonData):
        return requests.post(self.login_url,json=jsonData)
