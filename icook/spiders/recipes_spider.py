import scrapy


class RecipesSpider(scrapy.Spider):
    name = "icook"
    start_urls = [
        'https://icook.tw/categories/',
    ]

    def parse(self, response):
        urls = response.xpath('//a[@class="list-title"]/@href').extract()
        for url in urls:
            yield response.follow(url, callback=self.parse_category)

    def parse_category(self, response):
        urls = response.xpath((
            '//div[@class="browse-recipe-content"]'
            '/a[@class="browse-recipe-name"]/@href')
        ).extract()
        category_name = response.xpath('//h2[@class="category-name"]/text()').re(r'(\w+)')
        for url in urls:
            yield response.follow(url, callback=self.parse_receipes, meta={'category': category_name})

        next_page = response.xpath((
            '//a[@rel="next"]/@href')
        ).extract_first()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_category)

    def parse_receipes(self, response):
        category = response.meta.get('category')
        title = response.css('title::text').re(r'(.*) by')
        ingredients = list(
            set(response.css('div.ingredient-name::text').getall()))
        images = response.css('img.main-pic::attr(src)').extract()
        yield {
            'Tilte': title,
            'Category': category,
            'Ingredients': ingredients,
            'images-url': images
        }
