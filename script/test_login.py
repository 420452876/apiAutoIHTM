import unittest,logging,requests
# 登录测试类
from api.login_api import Login_api
from uitls import assert_common_utils


class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = Login_api()
    # 关闭
    def tearDown(self):
        pass

    # 登录成功
    def test01_login_success(self):
        response = self.login_api.login("13800000002","123456")
        logging.info("登录成功结果：{}".format(response.json()))
        assert_common_utils(self,response,200,True,10000,"操作成功")

    # 用户名不存在
    def test02_username_is_exist(self):
        response = self.login_api.login("13870000002", "123456")
        logging.info("用户名不存在的结果：{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码错误
    def test03_password_error(self):
        response = self.login_api.login("13800000002", "error")
        logging.info("密码错误的结果：{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 用户名为空
    def test04_username_is_null(self):
        response = self.login_api.login("", "123456")
        logging.info("用户名为空的结果：{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test05_password_is_null(self):
        response = self.login_api.login("13800000002", "")
        logging.info("密码为空的结果：{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 缺少参数mobile
    def test06_lack_mobile(self):
        response = self.login_api.my_login({"password":"123456"})
        logging.info("缺少参数mobile的结果：{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 缺少参数有password
    def test07_lack_password(self):
        response = self.login_api.my_login({"mobile":"13800000002"})
        logging.info("缺少参数mobile的结果：{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 错误参数mobile
    def test08_error_mobile(self):
        response = self.login_api.my_login({"mobil":"13800000002","password":"123456"})
        logging.info("错误参数mobile的结果：{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 错误参数password
    def test09_error_password(self):
        response = self.login_api.my_login({"mobile": "13800000002", "password1": "123456"})
        logging.info("错误参数password的结果：{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参数
    def test10_more_parameter(self):
        response = self.login_api.my_login({"mobile": "13800000002", "password": "123456","admin":"asas"})
        logging.info("多参数的结果：{}".format(response.json()))
        assert_common_utils(self, response, 200, True, 10000, "操作成功")

    # 无参数
    def test11_not_parameter(self):
        response = requests.post("http://182.92.81.159/api/sys/login")
        logging.info("无参数的结果：{}".format(response.json()))
        assert_common_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")