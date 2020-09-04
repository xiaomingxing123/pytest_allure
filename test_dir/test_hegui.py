import sys
import pytest
from os.path import dirname, abspath
from page.info import info_deal
from time import sleep
from page.common import Base

from page.xiaoyusan import XiaoyusanPage
from page import info

sys.path.insert(0, dirname(dirname(abspath(__file__))))


class Testxaidan:
    """正常下单"""

    def test_hegui_case(self, browser, base_url):
        page = XiaoyusanPage(browser)
        page.get(base_url + '138013')
        sleep(2)
        assert browser.title == "小雨伞超级玛丽重疾险（旗舰版Plus）"
        page.click_bug_sx.click()

        # 进入试算页
        sleep(2)
        assert browser.title == "保费试算"
        # 输入被保人生日
        page_set = Base(browser)
        page_set.set_value('[data-key="insureds.birth"]', info_deal.bbr_info["birthday"])
        # [110000, 110100, 110101] 地址代码
        page_set.set_value('[data-key="insureds.residentAddr"]', info_deal.bbr_info["address"])
        # 选择投保方案
        page.plan_id.click()  # 选择保额
        page_set.swipe_into("//*[text()='30年']")
        page.plan_Guarantee_time.click()  # 选择保障时间
        page.plan_Pay_period.click()  # 选择交费年限
        # 选择附加险
        if page_set.isElementExist("//*[text()='附加被保险人豁免保险费']"):
            page.plan_ext_risk_bbrhm.click()
        else:
            print("未找到此附加险")
        page.click_bug_sx.click()
        sleep(2)

        # 登录
        assert browser.title == "手机登录"
        page.phone_input_cx.send_keys(info_deal.user_info["user_phone"])
        page.security_input_cx.send_keys(info_deal.user_info["user_security"])
        page.login_click_cx.click()

        # 进入健告页
        sleep(2)
        assert browser.title == "投保告知"
        sleep(2000)
        page.healthy_yes.click()

        # 进入下单页
        sleep(5)
        # 输入投保人名字
        if page_set.isElementExist("//*[@placeholder='请填写投保人姓名']"):
            page.accept_button.click()
        else:
            print("没在合规流程")
        # 输入投保人证件号
        if page_set.isElementExist("//*[@placeholder='请输入投保人证件号码']"):
            page.tbr_id_input.send_keys(info_deal.tbr_info["ID_number"])
        else:
            print("已有投保人证件号码信息")
        # 输入投保人手机号
        if page_set.isElementExist("//*[@placeholder='请填写投保人手机号']"):
            page.tbr_phone_num_input.send_keys(info_deal.tbr_info["mobile"])
        else:
            print("已有投保人手机号码信息")
        # 输入投保人邮箱
        if page_set.isElementExist("//*[@placeholder='请填写投保人邮箱']"):
            page.tbr_email_input.send_keys(info_deal.tbr_info["email"])
        else:
            print("已有投保人邮箱信息")
        # 选择投保人证件有效期
        if page_set.isElementExist("//*[text()='证件有效期']"):
            page.select_tbr_validity_type.click()
            sleep(2)
            page_set.set_value('[data-key="applicant.idValidEndTime"]', info_deal.tbr_info["Effective_time"])
        else:
            print("不需要选择证件有效止期")
        # 选择投保人职业
        sleep(1)
        page_set.set_value('[data-key="applicant.careerCode"]', info_deal.tbr_info["careerCode"])
        # 输入投保人手机号码
        sleep(1)
        # 输入投保人长期居住地址
        page_set.swipe_into("//*[text()='长期居住地']")
        page.residentDetail.clear()
        page.residentDetail.send_keys(info_deal.tbr_info["residentDetail"])
        # 输入被保人身高体重信息
        if page_set.isElementExist("//*[text()='身高(cm)']"):
            page.bbr_height.send_keys(info_deal.bbr_info_buy["height"])
            page.bbr_weight.send_keys(info_deal.bbr_info_buy["weight"])
        else:
            print("没有被保人升高体重元素")
        # 输入续期银行卡信息
        if page_set.isElementExist("//*[text()='续费银行账户']"):
            page_set.swipe_into("//*[text()='开户行支行']")
            page_set.set_value('[data-key="renewalBank.bank"]', info_deal.bank_info["bank"])
            page.bankNo.clear()
            page.bankNo.send_keys(info_deal.bank_info["bankNo"])
        else:
            print("没有续期银行卡")
        page.click_bug.click()
        # 进入订单确认页
        sleep(10)
        assert browser.title == "健康告知"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_hegui.py"])
