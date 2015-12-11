# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
import urllib2
import cookielib
import urllib
# 单位净值      asset-value     0.9360
# 净值增长率    asset-amt       1.08%
# 累计净值      asset-all       0.9360
# 净值更新日期  date            2013/2/5
# 最近估值      price
# 涨跌幅        amt
# 涨跌额        amt-value
# 最新规模      scale           13.68亿元
# 风险等级      risk            高风险
# 申购状态      subscribe-status 可申购
# 赎回状态      redeem-status   可赎回

value_list = ["asset-value", "asset-amt", "asset-all", "date", "price", "amt", "amt-vaue", "scale", "risk", "subscribe-status","redeem-status"]

class FundDataParser(HTMLParser):
    def __init__(self, value_list = value_list):
        HTMLParser.__init__(self) # old-style class could not use super
        self._process = False
        self.value_list =  value_list
        self.attr = ""
        self.data = {}
        self.result = {}

    def get(self, code):
        url = "http://www.jisilu.cn/data/sfnew/#tlink_3"
        f = urllib2.urlopen(url)
        html = f.read()
        print html
        self.feed(html)
        self.close()
        self.result = self.data
        self.data = {}
        return(self.result)

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            for attr in attrs:
                if (attr[0] == "class"):
                    # case <span class="asset-amt red">
                    for attr_name in attr[1].split():
                        if attr_name in self.value_list:
                            self._process = True
                            self.attr = attr_name

    def handle_data(self, data):
        if self._process:
            self.data[self.attr] = data
            self._process = False

def main():
    """docstring for main"""
    parser = FundDataParser()
    #print parser.get("040020")
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    h = urllib2.urlopen('http://www.jisilu.cn/')
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
           'Referer' : '******'}
    postData = {'op' : 'dmlogin',
            'f' : 'st',
            'user' : '15068846837',
            'pass' : '584520',
            'rmbr' : 'true',
            'tmp' : '0.040590047836304'

            }
    postData = urllib.urlencode(postData)
    request = urllib2.Request('http://www.jisilu.cn/login/', postData, headers)

    print request
    response = urllib2.urlopen(request)
    text = response.read()
    print text
    print "******************************************************************"
    parser.get("217004")

if __name__ == '__main__':
    main()