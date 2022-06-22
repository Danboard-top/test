import scrapy
import asyncio
from gerapy_pyppeteer import PyppeteerRequest
from lxml import etree

async def hello(page):
    await page.click('.btn-next')

class App1Spider(scrapy.Spider):
    name = 'app1'
    # allowed_domains = ['df']
    # start_urls = ['http://df/']
    page = 10

    def start_requests(self):
        urls = 'https://spa6.scrape.center/page/1'

        yield PyppeteerRequest(urls, callback=self.show, wait_for='.m-b-sm')
        # for i in range(1,4):
        #     urls = 'https://spa6.scrape.center/page/{}'.format(i)
        #     yield PyppeteerRequest(urls, callback=self.show, wait_for='.m-b-sm')

    def show(self, response):
        print(response.url)
        source = response.text
        demo = etree.HTML(source).xpath('//div[@class="el-card__body"]')
        for i in demo:
            title = i.xpath('div[1]/div[2]/a/h2/text()')[0]
            types = i.xpath('div[1]/div[2]/div[1]//text()')
            print(title,'|'.join(map(str.strip,types)))
        App1Spider.page = App1Spider.page-1
        if App1Spider.page>0:
            yield PyppeteerRequest(response.url, callback=self.show, wait_for='.m-b-sm', actions=hello,dont_filter=True)
