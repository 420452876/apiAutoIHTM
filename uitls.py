# 定义工具栏

# 封装通用断言函数
import os,json

import pymysql

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def assert_common_utils(self, response, http_code, success, code, message):
    # 断言请求响应
    self.assertEqual(http_code, response.status_code)
    # 断言响应体
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

class DBUtils :
    # 初始化
    def __init__(self,host='182.92.81.159',user='readuser',password='iHRM_user_2019',database='ihrm'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 使用with语法时，进入函数时会先运行enter的代码
    def __enter__(self):
        # 与数据库进行连接
        self.conn = pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        # 获取游标
        self.cursor = self.conn.cursor()
        return self.cursor

    # 代表退出with语句块时，会运行exit的代码
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor :
            self.cursor.close()
        if self.conn :
            self.conn.close()

# 获取登录json文件
def get_login_data():
    filename = BASE_DIR + "/data/login_data.json"
    with open(filename,'r',encoding='utf-8') as f :
        jasnData = json.load(f)
        case_list = []
        for case in jasnData :
            mobile = case.get("mobile")
            password = case.get("password")
            http_code = case.get("http_code")
            success = case.get("success")
            code = case.get("code")
            message = case.get("message")
            case_list.append((mobile, password, http_code, success, code, message))
    # print(case_list)
    return case_list

# 获取添加员工json参数
def get_add_emp():
    filename = BASE_DIR + "/data/emp_data.json"
    with open(filename,'r', encoding='utf-8') as f :
       jsonData =  json.load(f)
       data = jsonData.get("add_emp")
       case_list = []

       username = data.get("username")
       mobile = data.get("mobile")
       http_code = data.get("http_code")
       success = data.get("success")
       code = data.get("code")
       message = data.get("message")
       case_list.append((username, message, mobile, http_code, success, code))
    return case_list

# 获取查询员工json参数
def get_select_emp():
    filename = BASE_DIR + "/data/emp_data.json"
    with open(filename, 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
        data = jsonData.get("select_emp")
        case_list = []
        http_code = data.get("http_code")
        success = data.get("success")
        code = data.get("code")
        message = data.get("message")
        case_list.append((message,http_code, success, code))
    return case_list

# 获取修改员工json参数
def get_update_emp() :
    filename = BASE_DIR + "/data/emp_data.json"
    with open(filename, 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
        data = jsonData.get("update_emp")
        case_list = []
        username = data.get("username")
        http_code = data.get("http_code")
        success = data.get("success")
        code = data.get("code")
        message = data.get("message")
        case_list.append((username,message, http_code, success, code))
    return case_list

# 获取删除员工json参数
def get_del_emp():
    filename = BASE_DIR + "/data/emp_data.json"
    with open(filename, 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
        data = jsonData.get("del_emp")
        case_list = []
        http_code = data.get("http_code")
        success = data.get("success")
        code = data.get("code")
        message = data.get("message")
        case_list.append((message, http_code, success, code))
    return case_list
