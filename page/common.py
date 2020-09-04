import json
from poium import Page, NewPageElement
from selenium import webdriver


class Base(Page):
    # 下拉框（select组件）
    def set_value(self, css_selector, value):
        js = '''
                   (function(selector, value) {
                           var elem = document.querySelector(selector)
                           if(!elem) return;
                           var event = document.createEvent('HTMLEvents');
                           event._mucValue = JSON.parse(value);
                           event.initEvent('mucChange', true, true);
                           elem.dispatchEvent(event);
                   })('%s','%s')
                   '''
        # print(js % (css_selector, value))
        self.driver.execute_script(js % (css_selector, json.dumps(value)))

    # 表示将元素滚动到屏幕中间
    def swipe_into(self, xpath_url):
        # 1、找到我要滚动到可见区域的元素
        loc = xpath_url
        target = self.driver.find_element_by_xpath(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    #   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
    def isElementExist(self, xpath_url):
        try:
            self.driver.find_element_by_xpath(xpath_url)
            return True
        except:
            return False
