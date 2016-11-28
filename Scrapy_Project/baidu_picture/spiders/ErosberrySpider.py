import scrapy
import items
from bs4 import BeautifulSoup 
import re

class ErosberrySpider(scrapy.Spider):
	name = "ErosberrySpider"
	start_urls = ['http://www.erosberry.com/top_rated']
	is_first_in = True
	max_pages = 10 #the number of pages to crawl

	def parse(self,response):
		for img in response.xpath('//img'):
			shortUrl = img.xpath('@src').extract()[0]
			url = response.urljoin(shortUrl)
			if url.split('.')[-1] == 'jpg': #ignore png icon in this page
				item = items.BaiduPictureItem()
				item['image_urls'] = [url]
				yield item
				

		if self.max_pages > 0: #go to next page
			
			text = response.text
			soup = BeautifulSoup(text)
			nav = soup.find_all('ul','nav')[0]
			tag_a = nav.find_all('a')
			for tag in tag_a:
				if len(re.compile('Next').findall(tag.contents[0])) > 0:
					relative_link = tag.attrs['href']
					next_page = self.start_urls[0] + relative_link
					print next_page
					yield scrapy.Request(next_page, callback=self.parse)
					self.max_pages -= 1
					break

		
			