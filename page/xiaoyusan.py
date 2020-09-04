from poium import Page, NewPageElement
import json
from page.info import info_deal


class XiaoyusanPage(Page):
    """
    商详页面封装操作到的元素
    """
    click_bug_sx = NewPageElement(xpath="//*[contains(text(),'立即投保')]", describe="立即投保")
    """
    试算页面封装操作到的元素
    """
    plan_id = NewPageElement(xpath="//*[text()= '" + info_deal.plan_info["coverage"] + "']", describe="标准版")
    plan_Guarantee_time = NewPageElement(xpath="//*[text()= '" + info_deal.plan_info["Guarantee_time"] + "']",
                                         describe="保障年限")
    plan_Pay_period = NewPageElement(xpath="//*[text()= '" + info_deal.plan_info["Pay_period"] + "']", describe="交费年限")
    plan_ext_risk_bbrhm = NewPageElement(xpath="//*[text()= '投保']", describe="投保")
    """
    登录页面封装操作到的元素
    """
    phone_input_dx = NewPageElement(xpath="//*[@placeholder='请输入手机号' and @class='form-sign-input']", describe="请输入手机号")
    phone_input_cx = NewPageElement(xpath="// *[ @ id = 'input_phone']", describe="请输入手机号")

    security_input_dx = NewPageElement(xpath="//*[@placeholder='请输入验证码' and @class='form-sign-input']",
                                       describe="请输入验证码")
    security_input_cx = NewPageElement(xpath="//*[@id='input_code']", describe="请输入验证码")
    login_click_cx = NewPageElement(xpath="// *[ @ id = 'query']", describe="确定")
    login_click_dx = NewPageElement(
        xpath="//*[contains(text(),'确定') and @style='background-color: rgb(140, 127, 238);'  ]", describe="确定")
    """
          键告页面封装操作到的元素
    """
    healthy_yes = NewPageElement(xpath="//*[contains(text(),'确认无以上问题')]", describe="确认无以上问题")

    """
      下单页面封装操作到的元素
    """

    click_bug = NewPageElement(xpath="//*[@id='app']/form/div[2]/section/div/a", describe="立即支付")
    hq_tbr_name = NewPageElement(xpath="//*[@id='app']/form/div[1]/div[1]/article/div/div/div[1]/div[1]/div/input",
                                 describe="获取投保人姓名")
    select_tbr_validity_type = NewPageElement(xpath="//*[text()= '" + info_deal.tbr_info["idValidType"] + "']",
                                              describe="证件有效期类型")

    select_tbr = NewPageElement(xpath="//*[@id='app']/form/div[1]/div[1]/article/div[1]/div[1]/div/div",
                                describe="进入选择投保人")
    select_tbr_first = NewPageElement(
        xpath="/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/i",
        describe="选择第一个投保人")
    select_bbr = NewPageElement(xpath="//*[@id='app']/form/div[1]/div[2]/div/article/div[2]/div/div[1]/div[1]/div/div",
                                describe="进入选择投保人")
    select_bbr_first = NewPageElement(
        xpath="/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/i",
        describe="选择第一个投保人")
    tbr_name_input = NewPageElement(xpath="//*[@placeholder='请填写投保人姓名']", describe="填写投保人姓名")
    tbr_id_input = NewPageElement(xpath="//*[@placeholder='请输入投保人证件号码']", describe="填写投保人证件号")
    tbr_phone_num_input = NewPageElement(xpath="//*[@placeholder='请填写投保人手机号']", describe="请填写投保人手机号")
    tbr_email_input = NewPageElement(xpath="//*[@placeholder='请填写投保人邮箱']", describe="请填写投保人邮箱")
    bbr_name_input = NewPageElement(xpath="//*[@placeholder='请填写被保人姓名']", describe="填写被保人姓名")
    bbr_id_input = NewPageElement(xpath="//*[@placeholder='请输入被保人证件号']", describe="填写被保人证件号")
    hq_tips = NewPageElement(class_name="gold-dialog-text", describe="弹窗")
    hq_abnormal = NewPageElement(class_name="element-error", describe="提示语")
    residentDetail = NewPageElement(xpath="//*[@placeholder='请填写投保人详细地址']", describe="详细地址")
    bbr_height = NewPageElement(xpath="//*[@placeholder='请输入被保人身高']", describe="被保人身高")
    bbr_weight = NewPageElement(xpath="//*[@placeholder='请输入被保人体重']", describe="被保人体重")
    bankNo = NewPageElement(xpath="//*[@placeholder='请填写投保人银行卡号']", describe="请填写投保人银行卡号")

    """
          订单确认页面封装操作到的元素
    """
    click_fxk = NewPageElement(class_name="act-gold-protocol-icon")
    click_bug_zf = NewPageElement(xpath="//*[contains(text(),'立即购买')]", describe="立即购买")
    """
           模拟支付页面封装操作到的元素
    """
    hq_zfxx = NewPageElement(xpath="/html/body", describe="获取模拟支付信息")

    """
          合规弹框封装操作到的元素
    """
    accept_button = NewPageElement(xpath="//*[@class= 'gold-dialog-item gold-dialog-confirm']", describe="同意并继续")
