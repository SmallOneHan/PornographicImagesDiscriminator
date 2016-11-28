# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import settings
import os

class BaiduPicturePipeline(object):

	# num = 0
	# root_dir = settings.IMAGES_STORE + '/full/'

	# def process_item(self, item, spider):
		
	# 	name = self.root_dir + item['images'][0]['path'].split('/')[-1]
	# 	if os.path.exists(name):
	# 		os.rename(name, self.root_dir+str(self.num)+'.jpg')
	# 		self.num += 1
		return item