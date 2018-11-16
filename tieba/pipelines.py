# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os
import uuid
from .test_os import mkdir

class Images_Pipeline(ImagesPipeline):
        # 获取settings文件里设置的变量值
        IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

        def get_media_requests(self, item, info):
            image_url = item["image_url"]
            yield scrapy.Request(image_url)

        def item_completed(self, result, item, info):
            image_path = [x["path"] for ok, x in result if ok]
            # 创建路径
            # mkpath = self.IMAGES_STORE + item['image_url'][33:41] + '/'
            # 创建文件夹
            # mkdir(mkpath)
            # 将图片放置在文件夹中
            os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + str(uuid.uuid4())[-5:] + ".jpg")

            return item
