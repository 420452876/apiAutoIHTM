import unittest,logging,requests
# 登录测试类
from api.login_api import Login_api
from parameterized import parameterized
from uitls import assert_common_utils, get_login_data

class TestLoginParams(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = Login_api()
    # 关闭
    def tearDown(self):
        pass

    # 登录成功
    @parameterized.expand(get_login_data())
    def test01_login(self,mobile, password, http_code, success, code, message):
        response = self.login_api.login(mobile,password)
        logging.info("登录成功结果：{}".format(response.json()))
        assert_common_utils(self,response,http_code,success,code,message)