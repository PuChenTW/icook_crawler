# icook crawler
This is a Scrapy project to scrape recipes from [icook](https://icook.tw/).

## Extracted data

This project extracts recipes, combined with the respective title, author, images-url, category, description, ingredients and steps.
The extracted data looks like this sample:


    {
        "Tilte": ["台式蘿蔔糕"], 
        "Author": "[Ca Ca Cooking]", 
        "images-url": ["https://tokyo-kitchen.icook.network/uploads/recipe/cover/280175/large_c31ca00e545c0521.jpg"], 
        "Category": ["中式點心"], 
        "Description": "在家也可以做出簡單美味的台式蘿蔔糕哦~", 
        "Ingredients": ["在來米粉", "小蝦米", "白蘿蔔", "乾香菇", "油蔥酥", "沙拉油", "鹽", "胡椒粉"], 
        "Steps": "將白蘿蔔削皮後刨絲，乾香菇泡軟後切丁，小蝦米洗淨瀝乾備用。熱鍋加入1匙的油，將香菇加入香..."
    }

## Running the spiders
Install scrapy if you haven't:

    $ pip install scrapy
You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl icook
If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl icook -o recipes.json

These formats are supported out of the box:
* JSON
* JSON lines
* CSV
* XML