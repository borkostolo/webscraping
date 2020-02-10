
from scrapy import Spider, Request
from food.items import FoodItem
import re

class FoodSpider(Spider):
    name = 'food_spider'
    allowed_urls = ['https://www.foodnetwork.com']
    start_urls   = ['https://www.foodnetwork.com/recipes/food-network-kitchen']

    def parse (self, response):

        a_to_z_list = response.xpath('//div[@class="aToZ section"]/section/ul/li/a/@href').getall()
        a_to_z_list1 = [re.sub(r'//',r'https://',url) for url in a_to_z_list]

        for i , url in enumerate (a_to_z_list1):
            print('='*50)
            print(f'Sending {i+1} page {url} to next level')
            print('='*50)
            yield Request(url=url, callback=self.parse_page_by_letter)

    def parse_page_by_letter (self, response):
        food_by_letterx = response.xpath('//div[@class="o-Capsule__m-Body"]/div/ul/li/a/@href').getall()

        food_by_letterx1 = [re.sub(r'//',r'https://',url) for url in food_by_letterx]
        print(food_by_letterx1,'Sending ...')

        for i , url in enumerate(food_by_letterx1):
            yield Request(url=url, callback=self.parse_food_page)

    def parse_food_page (self, response):
        print('Hello Afrika!!!!!',response.url)
        # Food Name
        name = response.xpath('//div[@class="assetTitle"]/section//h1/span/text()').get()
        # Level of expertise
        level = response.xpath('//div[@class="recipeInfo"]/div/ul[1]/li[1]/span[2]/text()').get()
        # Number of servings 
        serve = response.xpath('//div[@class="recipeInfo"]/div/ul[3]/li[1]/span[2]/text()').get()
        serve = int(re.findall('\d+',serve)[0])
        # Cooking time
        cooktime = response.xpath('//div[@class="recipeInfo"]/div/ul[1]/li[2]/span[2]/text()').get()
        # hour, minute  = re.findall('(\d).*\s(\d+)',ct)[0]
        # cooktime = int(hour)*60 + int(minute)

        # ingredients list format 
        ingredients = response.xpath('//div[@class="recipe-body"]/div/section/section/div/p/text()').getall() 

        item = FoodItem()
        item['name'] = name
        item['level'] = level
        item['servings'] = serve
        item['total'] = cooktime
        item['ingredients'] = ingredients
        item['steps'] = 'WIP'
        item['review'] = 'WIP'
        item['rating'] = 'WIP'
        yield item










         