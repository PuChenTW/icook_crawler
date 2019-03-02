# icook crawler
This is a Scrapy project to scrape recipes from [icook](https://icook.tw/).

## Extracted data

This project extracts recipes, combined with the respective url, title, author, images-url, category paths, description, ingredients and steps.
The extracted data looks like this sample:

    {
        "url": "https://icook.tw/recipes/102998", 
        "Tilte": ["木瓜牛奶凍 [超簡易15分鐘食譜]"], 
        "Author": "Mrs P's Kitchen", 
        "images-url": ["https://tokyo-kitchen.icook.network/uploads/recipe/cover/102998/large_59087c73f032e695.jpg"], 
        "Category paths": [["烘焙點心", "果凍、茶凍"]], 
        "Description": "這個外形非常可愛的甜點，美味又營養豐富！經常飲木瓜鮮奶，可試試這個甜點，木瓜含豐富的維生素，再加上牛奶，成養顏美肌的甜點。做法超簡單，15分鐘做好，新手不敗，快試試！請也支持我的Facebook 專頁唷*^O^* \n", 
        "Ingredients": ["糖", "吉利丁粉", "新鮮牛奶", "木瓜"], 
        "Steps": "先將木瓜去皮，切開一半，用匙羹刮去木瓜籽，去囊。如想多放點奶涷，可刮去一上木瓜肉\n用小鍋煮熱牛奶，下糖，煮至糖溶化，再加入吉利丁粉，不停攪拌至完全溶化即可\n將牛奶倒入木瓜內，待涼後放入冰箱冷藏一小時以上至奶凍完全凝固\n切件享用！"
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