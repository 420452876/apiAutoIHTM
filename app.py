# 存放全局变量，公有的配置函数或者类
import logging
import os
from logging import handlers
# 获取项目绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 定义响应头全局变量
HEADERS = None
# 定义添加的员工Id全局变量
EMP_ID = None

# 1 定义一个初始化日志配置的函数
def init_logging() :
    # 2 创建日志器
    logger = logging.getLogger()
    # 3 设置日志等级
    logger.setLevel(logging.INFO)
    # 4 创建处理器，通过处理控制日志的打印
    # 创建控制台处理器
    sh = logging.StreamHandler()
    #创建文件处理器
    fh = logging.handlers.TimedRotatingFileHandler(BASE_DIR + "/log/ihrm.log",
                                                   when='S',
                                                   interval=10,
                                                   backupCount=3,
                                                   encoding="utf-8")
    # 5 设置日志的格式，所需要创建格式和格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 6 将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 7 讲处理器添加到日志当中
    logger.addHandler(sh)
    logger.addHandler(fh)

if __name__ == '__main__':
    init_logging()
    logging.info("测试日志是否生效")
