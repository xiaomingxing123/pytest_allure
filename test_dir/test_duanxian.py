import sys
import pytest
from os.path import dirname, abspath
from page.info import info_deal
from time import sleep
import allure

from page.xiaoyusan import XiaoyusanPage

sys.path.insert(0, dirname(dirname(abspath(__file__))))


class Testxaidan:
    """正常下单"""

    @allure.feature('正常下单')
    def test_xiaoyusan_xiadan_case(self, browser, base_url):
        page = XiaoyusanPage(browser)
        with allure.step("step1：打开要测试的商品链接"):
            page.get(base_url + '111905')
            sleep(2)
            assert browser.title == "小雨伞贴心5守护保"
        page.click_bug_sx.click()
        sleep(2)
        # 登录
        page.phone_input_dx.send_keys(info_deal.user_info["user_phone"])
        sleep(2)
        page.security_input_dx.send_keys(info_deal.user_info["user_user_security"])
        sleep(2)
        page.login_click_dx.click()
        sleep(2)
        # 健康告知页
        assert browser.title == "健康告知"
        page.healthy_yes.click()
        sleep(2)
        # 下单页
        assert browser.title == "填写投保信息"
        page.tbr_name_input.send_keys("李狗蛋")
        page.tbr_id_input.send_keys(440301199411102972)
        page.tbr_email_input.send_keys("albert@muchenglin.com")
        page.tbr_phone_num_input.send_keys(17665106373)
        page.bbr_name_input.send_keys("李狗蛋")
        page.bbr_id_input.send_keys(440301199411102972)
        sleep(2)
        page.click_bug_sx.click()
        # 进入订单确认页
        sleep(2)
        assert browser.title == "订单确认页"
        page.click_fxk.click()
        sleep(2)
        page.click_bug_zf.click()
        sleep(2)
        print(browser.title)
        assert browser.title == "选择支付方式"
        # 模拟支付
        a = page.driver.current_url
        c = str(int(a[-8:]) + 1)  # 获取dealid
        b = "http://beta.xinhulu.com/zaletest/mockDealPaid?uid=72102408&dealid="
        d = b + c
        print(d)
        page.get(d)
        sleep(2)
        text_mnzf = page.hq_zfxx.text
        print(text_mnzf)


class Testxaidan_abnormal:
    """异常校验
    """

    @allure.feature('重复下单')
    # test01重复下单
    def test_xiadan_abnormal01_case(self, browser, base_url):
        page = XiaoyusanPage(browser)
        page.get(base_url)
        sleep(2)
        assert browser.title == "小雨伞贴心守护保"
        page.click_bug_sx.click()
        sleep(2)
        # 健告页
        assert browser.title == "健康告知"
        page.healthy_yes.click()
        # 下单页
        sleep(2)
        # 输入投保人姓名
        page.tbr_name_input.clear()
        page.tbr_name_input.send_keys("李狗蛋")
        # 输入投保人身份证号
        sleep(1)
        page.tbr_id_input.clear()
        page.tbr_id_input.send_keys(440301199411102972)
        # 输入投保人邮箱
        sleep(1)
        page.tbr_email_input.clear()
        page.tbr_email_input.send_keys("albert@muchenglin.com")
        # 输入投保人手机号码
        sleep(1)
        page.tbr_phone_num_input.clear()
        page.tbr_phone_num_input.send_keys(17665106373)
        # 输入被保人姓名
        sleep(1)
        page.bbr_name_input.clear()
        page.bbr_name_input.send_keys("李狗蛋")
        # 输入被保人身份证号
        sleep(1)
        page.bbr_id_input.clear()
        page.bbr_id_input.send_keys(440301199411102972)
        sleep(1)
        page.click_bug_sx.click()
        sleep(1)
        assert page.hq_tips.text == "被保人李狗蛋已购买此产品，此产品不能重复投保，请选择其他被保人"

    @allure.feature('投保人异常校验')
    def test_xiadan_abnormal02_case(self, browser, base_url):
        """投保人异常校验
        """
        page = XiaoyusanPage(browser)
        page.get(base_url)
        sleep(2)
        assert browser.title == "小雨伞贴心守护保"
        page.click_bug_sx.click()
        sleep(2)
        # 健告页
        assert browser.title == "健康告知"
        page.healthy_yes.click()
        # 下单页
        sleep(2)
        # 输入投保人姓名
        # 1、含特殊字符
        page.tbr_name_input.clear()
        page.tbr_name_input.send_keys("李狗蛋%")
        sleep(2)
        page.click_bug_sx
        assert page.hq_abnormal.text == "请输入投保人姓名"
        sleep(2000)
        # 2、名字长度不够
        page.bbr_name_input.clear()
        page.bbr_name_input.send_keys("李狗蛋")
        sleep(2)
        page.tbr_name_input.clear()
        page.tbr_name_input.send_keys("李")
        sleep(2)
        assert page.hq_abnormal.text == "请输入投保人姓名"
        # 3、中英混搭
        sleep(2)
        page.bbr_name_input.clear()
        page.bbr_name_input.send_keys("李狗蛋")
        sleep(2)
        page.tbr_name_input.clear()
        page.tbr_name_input.send_keys("李单·D")
        sleep(2)
        assert page.hq_abnormal.text == "请输入投保人姓名"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_duanxian.py"])
