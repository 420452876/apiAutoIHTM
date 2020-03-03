# 导包
import unittest,logging,requests,app,pymysql
# 创建测试类
from api.emp_api import Employee_api
from parameterized import parameterized
from uitls import assert_common_utils, DBUtils, get_add_emp, get_select_emp, get_update_emp, get_del_emp


class TestEmployeeParams(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.emp_api = Employee_api()

    # 关闭
    def tearDown(self):
        pass

    # 登录
    def test01_emp_login(self):
        # 调用登录
        response = self.emp_api.login("13800000002", "123456")
        logging.info("登录响应体为：{}".format(response.json()))
        # 取出令牌，拼接为Bearer 开头的字符串
        token = "Bearer " + response.json().get("data")
        logging.info("令牌为：{}".format(token))

        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        logging.info("请求头为：{}".format(app.HEADERS))

    # 添加员工用例
    @parameterized.expand(get_add_emp())
    def test02_emp_add(self,username, message, mobile, http_code, success, code):
        # 调用添加员工
        response_emp_add = self.emp_api.emp_add(username, mobile, app.HEADERS)
        logging.info("添加员工结果为：{}".format(response_emp_add.json()))
        # 获取添加的员工id
        app.EMP_ID = response_emp_add.json().get("data").get("id")

        logging.info("添加的员工id为：{}".format(app.EMP_ID))
        # 调用工具类的断言接口
        assert_common_utils(self, response_emp_add, http_code, success, code, message)

    # 查询员工用例
    @parameterized.expand(get_select_emp())
    def test03_emp_select(self,message,http_code, success, code):
        # 调用查询员工
        response_emp_select = self.emp_api.emp_select(app.EMP_ID,app.HEADERS)
        logging.info("查询的结果为：{}".format(response_emp_select.json()))
        # 调用工具类的断言接口
        assert_common_utils(self,response_emp_select,http_code,success,code,message)

    # 修改员工用例
    @parameterized.expand(get_update_emp())
    def test04_emp_update(self,username,message, http_code, success, code):
        # 调用修改员工
        response_emp_update = self.emp_api.emp_update(app.EMP_ID, app.HEADERS, username)
        logging.info("修改的结果为：{}".format(response_emp_update.json()))
        # 调用工具类的断言接口
        with DBUtils() as db :

            sql = "select username from bs_user where id={}".format(app.EMP_ID)
            logging.info("查询的SQL语句为：{}".format(sql))
            # 执行sql语句
            db.execute(sql)
            # 获取结果行数
            result = db.fetchone()
            logging.info("修改后SQL结果为：{}".format(result))
            # 对返回的查询结果进行断言
            self.assertIn(username,result[0])


        # 断言结果
        assert_common_utils(self, response_emp_update, http_code, success, code, message)

    # 删除员工用例
    @parameterized.expand(get_del_emp())
    def test05_emp_del(self,message, http_code, success, code):
        # 调用删除员工
        response_emp_del = self.emp_api.emp_del(app.EMP_ID, app.HEADERS)
        logging.info("删除的结果为：{}".format(response_emp_del.json()))
        # 调用工具类的断言接口
        assert_common_utils(self, response_emp_del, http_code, success, code, message)
