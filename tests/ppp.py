from playwright.sync_api import Playwright, sync_playwright
from lxml import etree
import re
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    def cancel_request(route, request):
        route.abort()
        page.route(re.compile(r"(\.png)|(\.jpg)"), cancel_request)
    page = context.new_page()
    page.goto("https://www.kearney.com/")
    htm=page.content()

    context.close()
    browser.close()
    print(htm)
    html = etree.HTML(htm)
    print(html)
    a = '//*[@id="articleAdtDiv_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_MFHuqrEr0n7v"]/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/a/div'
    b=html.xpath(a)
    print(b)

with sync_playwright() as playwright:
    run(playwright)
