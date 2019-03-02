import scrapy


def create_category_paths(categories: list) -> list:
    """Construct flat category list into 2D array, remove 全部分類.
    
    Arguments:
        categories {list} -- [description]
    
    Returns:
        list -- [description]
    """
    paths = []
    path = []
    for category in categories:
        if category == '全部分類':
            if path:
                paths.append(path)
            path = []
        else:
            path.append(category)
    if path:
        paths.append(path)
    return paths


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
        for url in urls:
            yield response.follow(url, callback=self.parse_receipes)

        next_page = response.xpath(('//a[@rel="next"]/@href')).extract_first()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_category)

    def parse_receipes(self, response):
        title = response.css('title::text').re(r'(.*) by')
        author = response.xpath(
            '//div[@class="author-name"]/a[@class="author-name-link"]/text()').get()
        images = response.css('img.main-pic::attr(src)').extract()
        categories = response.xpath(
            '//div[@class="findmore inner-block"]/div[@class="category-tags"]/ul/li/a/text()').getall()
        category_paths = create_category_paths(categories)
        description = ''.join(response.xpath(
            '//div[@class="header-row description"]/p/text()').getall())
        ingredients = list(
            set(response.css('div.ingredient-name::text').getall()))
        steps = '\n'.join(response.xpath(
            '//li[@class="step"]/div/div/text()').getall())

        yield {
            'url': response.url,
            'Tilte': title,
            'Author': author,
            'images-url': images,
            'Category paths': category_paths,
            'Description': description,
            'Ingredients': ingredients,
            'Steps': steps,
        }
