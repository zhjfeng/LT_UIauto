'''
@Time  : 2020/5/15 16:39
@Author: fengzhj
@doc   : 教师管理页面相关用例
'''

from conftest import browser
import pytest
from page.login import Loginpage
from page.admin_manger import Adminpage
import allure
import time

@allure.feature('乐桃学院-老师管理')

class TestTM():

    def test_TM_page(self,browser):
        """是否进入老师管理页面"""
        tm_page = Loginpage(browser).admin_login('18888888888', 'test1234').tc_manger()
        assert '老师管理' == tm_page.get_tcmangertitle()

    def test_TM_phone(self,browser):
        """查找号码"""
        phone = '17777777777'
        tm_page = Loginpage(browser).admin_login('18888888888', 'test1234').tc_manger()
        tm_page.find_teacher_phone(phone)
        assert phone == tm_page.get_phone()

    def test_TM_name(self,browser):
        """查找姓名"""
        name = '自动化测试'
        tm_page = Loginpage(browser).admin_login('18888888888', 'test1234').tc_manger()
        tm_page.find_teacher_name(name)
        assert name == tm_page.get_name()

    def test_edit_name(self,browser):
        """编辑老师"""
        name = '自动化测试'  # 老师姓名
        edit_name = '编辑测试'  # 编辑老师姓名
        tm_page = Loginpage(browser).admin_login('18888888888', 'test1234').tc_manger()
        tm_page.find_teacher_name(name)
        tm_page.edit_TC(edit_name)
        assert edit_name == tm_page.get_name()

    def test_del_name(self,browser):
        """移除老师"""
        name = '编辑测试'
        tm_page = Loginpage(browser).admin_login('18888888888', 'test1234').tc_manger()
        tm_page.del_TC(name)
        tm_page.find_teacher_name(name)
        assert '暂无数据' == tm_page.find_date()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_teacher_manger.py"])