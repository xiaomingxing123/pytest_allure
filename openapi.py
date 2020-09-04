import unittest, requests, json, time
from ddt import ddt, data, idata, file_data


@ddt
class DamoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.transactionId = int(time.time())     # 获取当前时间戳作为流水号
        cls.token = cls.get_refreshToken()
        # #totalPrice1, mainPrice1, exRiskPrices1
        # cls.mainfee = cls.test_calcPrice()
        # cls.totalfee = cls.calcPrice()
        # cls.exRiskfee = cls.calcPrice()
        cls.product = {
            # "productCode": "4FE",     # 信泰超级玛丽2号max-主险code
            "productCode": "C011",       # 204087duanxian
            "openUid": 10          # uid
        }

        # 投保方案
        cls.plan = {
            "curTime": "20200828",  # 购买日期
            "coverage": 10000000000,  # 容易出错    10万：保额后面追加4个0
            "insuredTime": "Y1",  # 保障时间    C：终身    A70：至70岁   A80：至80岁
            "chargeYears": "Y1",  # 缴费年限    Y1：一次交清   Y10：10年交...
            "begTime": "20200829"  # 生效日期
        }

        # 投保人
        cls.applicant = {
            "cname": "撤啊销",
            "sex": "M",               # M：男性  F：女性
            "birth": "19710126",
            "taxPayType": 1,          # 税收居民身份证
            "socialins": 1,          # 有无社保  0：无社保  1：有社保
            #"annualIncome": 500,     # 年收入
            "id": "110101197101269754",
            "mobile": "18588086703",
            "email": "dale@muchenglin.com",
            "careerCode": [
                "一般行业",
                "机关团体公司行号",
                "A01001"
            ]
        }

        # 被保人
        cls.insured = {
            "relationToApply": 1,
            "cname": "撤啊销",
            "sex": "M",               # M：男性  F：女性
            "birth": "19710126",
            "taxPayType": 1,          # 税收居民身份证
            #"socialins": 0,          # 有无社保  0：无社保  1：有社保
            #"annualIncome": 500,     # 年收入
            "id": "110101197101269754",
            "mobile": "18588086703",
            "email": "dale@muchenglin.com",
            "careerCode": [
                "一般行业",
                "机关团体公司行号",
                "A01001"
            ],
            "socialins": 1
        }

    @classmethod
    def tearDownClass(cls):
        pass

    @staticmethod
    def get_refreshToken():
        url = 'https://openapi-test.baodan360.com/euler/refreshToken'
        data = {'appId': '1000', 'appSecret': 'ankerxiong'}      # appid配置
        print('request' + json.dumps(data))
        ret = requests.post(url, json.dumps(data))
        return ret.json()['access_token']

    # 试算
    def calcPrice(self, transactionId):
        url = 'https://openapi-test.baodan360.com/euler/calcPrice'
        data = {
            "accessToken": self.token,
            "version": "2.0.0",
            "bizContent": {
                "transactionId": self.transactionId,
                "clientType": 1,
                "productCode": self.product['productCode'],
                "returnUrl": "https://www.baidu.com/",
                "timeoutUrl": "https://www.jd.com/",
                "common": {
                    "openUid": self.product['openUid']
                },
                "applicant": {
                    "cname": self.applicant['cname'],
                    "sex": self.applicant['sex'],
                    "birth": self.applicant['birth'],
                    "taxPayType": self.applicant['taxPayType'],
                    "mobile": self.applicant['mobile'],
                    "email": self.applicant['email'],
                    "socialins": self.applicant['socialins'],
                    "certificate": {
                        "idType": "0",
                        "id": self.applicant['id'],
                        # "idValidType": "1",
                        # "idValidEndTime": "20301206"
                    },
                },
                "insureds": [
                    {
                        "insured": {
                            "curTime": self.plan['curTime'],
                            # "relationToApply": self.insured['relationToApply'],
                            "relationToApply": 1,
                            "cname": self.insured['cname'],
                            "sex": self.insured['sex'],
                            "birth": self.insured['birth'],
                            "taxPayType": self.insured['taxPayType'],
                            "mobile": self.insured['mobile'],
                            "socialins": self.insured['socialins'],
                            "certificate": {
                                #"idType": "0",  #身份证
                                "idType": "1",  # 出生证
                                "id": self.insured['id'],
                                # "idValidType": "1",
                                # "idValidEndTime": "20241206"
                            },
                        },
                        "plan": {
                            "coverage": self.plan['coverage'],
                            "insuredTime": self.plan['insuredTime'],
                            "chargeYears": self.plan['chargeYears'],
                            "begTime": self.plan['begTime'],
                            "payType": "Y"
                        },
                    }
                ]
            }
        }
        ret = requests.post(url, json.dumps(data))
        # totalPrice1 = ret.json()['data']['insuredPrice'][0]['totalPrice']
        # mainPrice1 = ret.json()['data']['insuredPrice'][0]['mainPrice']
        # exRiskPrices1 = ret.json()['data']['insuredPrice'][0]['exRiskPrices']
        # return totalPrice1, mainPrice1, exRiskPrices1

        print(data)
        return ret.json()

        # return ret.json()['insuredPrice']

    # 核保
    def checkPolicy(self, totalPrice):
        # def test_checkPolicy(self):
        url = 'https://openapi-test.baodan360.com/euler/checkPolicy'
        data = {
            "accessToken": self.token,
            "version": "2.0.0",
            "bizContent": {
                "transactionId": self.transactionId,
                "clientType": 1,
                "productCode": self.product['productCode'],
                "returnUrl": "https://www.baidu.com/",
                "timeoutUrl": "https://www.jd.com/",
                "totalFee": totalPrice,
                "common": {
                    "openUid": self.product['openUid']
                },
                "applicant": {
                    "cname": self.applicant['cname'],
                    "sex": self.applicant['sex'],
                    "birth": self.applicant['birth'],
                    "taxPayType": self.applicant['taxPayType'],
                    "mobile": self.applicant['mobile'],
                    "email": self.applicant['email'],
                    "socialins": self.applicant['socialins'],
                    "certificate": {
                        "idType": "0",
                        "id": self.applicant['id'],
                        # "idValidType": "1",
                        # "idValidEndTime": "20201206"
                    },
                },
                "insureds": [
                    {
                        "insured": {
                            "curTime": self.plan['curTime'],
                            # "relationToApply": self.insured['relationToApply'],
                            "relationToApply": 1,
                            "cname": self.insured['cname'],
                            "sex": self.insured['sex'],
                            "birth": self.insured['birth'],
                            "taxPayType": self.insured['taxPayType'],
                            "socialins": self.insured['socialins'],
                            "mobile": self.insured['mobile'],
                            "certificate": {
                                "idType": "0",
                                "id": self.insured['id'],
                                # "idValidType": "1",
                                # "idValidEndTime": "20230702"
                            },
                        },
                        "plan": {
                            "coverage": self.plan['coverage'],
                            "insuredTime": self.plan['insuredTime'],
                            "chargeYears": self.plan['chargeYears'],
                            "begTime": self.plan['begTime'],
                            "payType": "Y"
                        },

                        "priceInfo": {
                            "totalPrice": totalPrice,
                            "mainPrice": totalPrice,
                            "exRiskPrices": [

                            ]
                        }
                    }
                ]
            }
        }
        print(self.token, self.transactionId)
        ret = requests.post(url, json.dumps(data))
        # print(ret.json())
        print(data)
        return ret.json()

    # 下单
    def submitOrder(self, checkId, totalPrice):
        url = 'https://openapi-test.baodan360.com/euler/submitOrder'
        data = {
            "accessToken": self.token,
            "version": "2.0.0",
            "bizContent": {
                "transactionId": self.transactionId,
                "clientType": 1,
                "productCode": self.product['productCode'],
                "returnUrl": "https://www.baidu.com/",
                "timeoutUrl": "https://www.jd.com/",
                "totalFee": totalPrice,
                "checkId": checkId,
                "insuredNotify": "http://dev.xinhulu.com/daleTest/insuredNotify",
                "epolicyNotify": "http://dev.xinhulu.com/daleTest/epolicyNotify",
                "common": {
                    "openUid": self.product['openUid']
                },
                "applicant": {
                    "cname": self.applicant['cname'],
                    "sex": self.applicant['sex'],
                    "birth": self.applicant['birth'],
                    "taxPayType": self.applicant['taxPayType'],
                    "mobile": self.applicant['mobile'],
                    "socialins": self.applicant['socialins'],
                    "email": self.applicant['email'],
                    "certificate": {
                        "idType": "0",
                        "id": self.applicant['id'],
                        # "idValidType": "1",
                        # "idValidEndTime": "20201206"
                    },
                },
                "insureds": [
                    {
                        "insured": {
                            "curTime": self.plan['curTime'],
                            # "relationToApply": self.insured['relationToApply'],
                            "relationToApply": 1,
                            "cname": self.insured['cname'],
                            "sex": self.insured['sex'],
                            "birth": self.insured['birth'],
                            "taxPayType": self.insured['taxPayType'],
                            "socialins": self.insured['socialins'],
                            "mobile": self.insured['mobile'],
                            "certificate": {
                                "idType": "0",
                                "id": self.insured['id'],
                                # "idValidType": "1",
                                # "idValidEndTime": "20230702"
                            },
                        },
                        "plan": {
                            "coverage": self.plan['coverage'],
                            "insuredTime": self.plan['insuredTime'],
                            "chargeYears": self.plan['chargeYears'],
                            "begTime": self.plan['begTime'],
                            "payType": "Y"
                        },

                        "priceInfo": {
                            "totalPrice": totalPrice,
                            "mainPrice": totalPrice,
                            "exRiskPrices": [

                            ]
                        }
                    }
                ]
            }
        }
        ret = requests.post(url, json.dumps(data))
        print(data)
        return ret.json()

    # 修改订单金额
    def changePay(self, bdealId):
        url = "https://beta.xinhulu.com/anker/editMoney?bdealId=" + bdealId
        ret = requests.post(url)

    # 创建支付
    def createPay(self, bdealId):
        url = 'https://openapi-test.baodan360.com/euler/createPay'
        data = {
            "accessToken": self.token,
            "version": "2.0.0",
            "bizContent": {
                "transactionId": self.transactionId,
                "clientType": 2,
                "payType": 1,
                "productCode": self.product['productCode'],
                "bdealId": bdealId,
                "paySuccessUrl": "https://www.baidu.com/",
                "payFailUrl": "https://www.jd.com/",
                "payCancelUrl": "https://www.suning.com/",
                "payNotifyUrl": "https://dev.xinhulu.com/daleTest/payNotifyUrl"
            }
        }
        ret = requests.post(url, json.dumps(data))
        print(ret.json())

    # 支付
    def mock_pay(self, bdealId):
        url = 'http://beta.xinhulu.com/Dale/mockOpenBDealPaid?bdealId=' + bdealId
        ret = requests.post(url)

    def test_calcPrice(self):
        # 试算
        ret = self.calcPrice(self.transactionId)
        print(ret)

        print('====' * 30)

        # 核保
        totalPrice = ret['data']['totalPrice']
        ret = self.checkPolicy(totalPrice)
        print(ret)
        print('====' * 30)

        # 出单
        checkId = ret['data']['checkId']
        ret = self.submitOrder(checkId, totalPrice)
        print(ret)
        print('====' * 30)

        # 修改订单金额
        bdealId = ret['data']['bdealId']
        print(bdealId)
        self.changePay(bdealId)
        print('====' * 30)

        # 创建支付
        self.createPay(bdealId)
        print('====' * 50)

        # # 支付
        # time.sleep(0.5)
        # self.mock_pay(bdealId)

        # 犹豫期退保
        # refuse = self.refuse()
        # print(refuse)


if __name__ == '__main__':
    unittest.main()
