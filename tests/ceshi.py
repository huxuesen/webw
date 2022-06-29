import ast
from collections import OrderedDict

import requests
from task.utils.selector.selector import SelectorABC as FatherSelector


url ='https://www.conference-board.org/publications/DDE-Update-on-US-and-EU-China-Relations-March-2022'
'''
json = '{"query":"","filters":{"all":[{"kpmg_tab_type":["Insights"]},{"kpmg_article_type":["Article-General"]},{"kpmg_template_type":["article-details-template","insights-flexible-template","editable-flex-template","editable-campaign-template"]}]},"result_fields":{"kpmg_image":{"raw":{}},"kpmg_description":{"raw":{}},"kpmg_banner_flag":{"raw":{}},"kpmg_primary_tag":{"raw":{}},"kpmg_article_date":{"raw":{}},"kpmg_contact_job_ttl":{"raw":{}},"kpmg_article_readtime":{"raw":{}},"kpmg_title":{"raw":{}},"kpmg_contact_fn":{"raw":{}},"kpmg_contact_ln":{"raw":{}},"kpmg_event_type":{"raw":{}},"kpmg_contact_city":{"raw":{}},"kpmg_event_start_time":{"raw":{}},"kpmg_article_date_time":{"raw":{}},"kpmg_contact_country":{"raw":{}},"kpmg_tab_type":{"raw":{}},"kpmg_short_desc":{"raw":{}},"kpmg_article_primary_format":{"raw":{}},"kpmg_article_type":{"raw":{}},"kpmg_event_startdate":{"raw":{}},"kpmg_url":{"raw":{}},"kpmg_template_type":{"raw":{}}},"page":{"size":10,"current":1},"sort":{"kpmg_filter_date":"desc"}}'

headers = """{"User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}"""
if json == '':
    r = requests.get(url, headers, timeout=10)
r = requests.post(url, json, headers, timeout=10)
'''
r = requests.get(url, headers, timeout=10)
r.encoding = r.apparent_encoding
html = r.text
print(html)


