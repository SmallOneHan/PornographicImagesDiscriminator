import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
import items

class PictureSpider(scrapy.Spider):
	name = "PictureSpider"
	start_urls = ['http://image.baidu.com/']

	def __init__(self, name=None, **kwargs):
		scrapy.Spider.__init__(self, name=None, **kwargs)
		self.driver = webdriver.Chrome()

	def parse(self,response):
		for box in response.xpath('//a[@class="img_link_layer"]') :
			shortUrl = box.xpath('@href').extract()[0]
			url = response.urljoin(shortUrl)
			self.driver.get(url)
			elements = self.driver.find_elements(By.XPATH,'//li[@class="imgitem"]')
			for i,element in enumerate(elements):
				if i>40:
					break
				image_urls = element.get_attribute('data-objurl')
				item = items.BaiduPictureItem()
				item['image_urls'] = [image_urls]
				yield item

		




			