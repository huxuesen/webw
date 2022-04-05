import ast
from collections import OrderedDict

import requests
from task.utils.selector.selector import SelectorABC as FatherSelector

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RequestsSelector(FatherSelector):
    def __init__(self, debug=False):
        self.debug = debug

    def get_html(self, url, headers):
        if headers:
            header_dict = ast.literal_eval(headers)
            if type(header_dict) != dict:
                raise Exception('必须是字典格式')

            r = requests.get(url, headers=header_dict, verify=False)    #关闭ssl验证。
        else:
            r = requests.get(url, timeout=10, verify=False)    #关闭ssl验证。
        r.encoding = r.apparent_encoding
        html = r.text
        return html

    def get_by_xpath(self, url, selector_dict, headers=None):
        html = self.get_html(url, headers)

        result = OrderedDict()
        for key, xpath_ext in selector_dict.items():
            result[key] = self.xpath_parse(html, xpath_ext)

        return result

    def get_by_css(self, url, selector_dict, headers=None):
        html = self.get_html(url, headers)

        result = OrderedDict()
        for key, css_ext in selector_dict.items():
            result[key] = self.css_parse(html, css_ext)

        return result

    def get_by_json(self, url, selector_dict, headers=None):
        html = self.get_html(url, headers)

        result = OrderedDict()
        for key, json_ext in selector_dict.items():
            result[key] = self.json_parse(html, json_ext)
            #去掉result中的所有["和"]符号
            result[key] = result[key].replace('[', '').replace(']', '').replace('"', '')

        return result
