from scrapy.cmdline import execute


# 1. 爬取分类名称
# execute('scrapy crawl classification'.split())

# 2. 爬取每个分类下所有的花卉名称和地址，用于后期给花卉添加标签
# scrapy runspider classification_all.py 

# 3. 爬取所有的类别名称
# execute('scrapy crawl category'.split())

# 4. 爬取所有花卉的名称的地址，用于获取详细
# scrapy runspider flowers_list.py

# 5. 爬取所有花卉的详细信息，不包括图片
# scrapy runspider flowers_detail.py