# 封装api
import requests

class Employee_api :
    def __init__(self):
        pass

    # 封装登录api
    def login(self,mobile,password):
        login_url = "http://182.92.81.159/api/sys/login"
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(login_url,json=jsonData)

    # 封装添加员工接口
    def emp_add(self,username,mobile,headers):
        add_url = "http://182.92.81.159/api/sys/user"
        return requests.post(add_url, json={
                         "username": username,
                         "mobile": mobile,
                         "timeOfEntry": "2020-02-27",
                         "formOfEmployment": 1,
                         "departmentName": "酱油2部",
                         "departmentId": "120502600533443434",
                         "correctionTime": "2020-02-27T16:00:00.000Z"
                     },
                     headers=headers)

    # 封装查询员工接口
    def emp_select(self,emp_id,headers):
        select_url = "http://182.92.81.159/api/sys/user/" + emp_id
        return requests.get(select_url, headers=headers)

    # 封装修改员工接口
    def emp_update(self,emp_id,headers,username):
        update_url = "http://182.92.81.159/api/sys/user/" + emp_id
        return requests.put(update_url, json={"username": username}, headers=headers)

    # 封装删除员工接口
    def emp_del(self,emp_id,headers):
        del_url = "http://182.92.81.159/api/sys/user/" + emp_id
        return requests.delete(del_url, headers=headers)

