UA = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50', 
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 
'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 
'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11', 
'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11', 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11', 
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
]

# 模块 (模块名称，是否开启爬取)
# MODULES = [('classification', False), ('classification_all', True)]

# redis key
CLASSIFICATION_KEY = 'huhua:classification'
CLASSIFICATION_START_URL = 'classification:start_urls'
CLASSIFICATION_ALL_KEY = 'huhua:classification_all'

CATEGORY_KEY = 'huhua:category'
FLOWERS_LIST_START_URL = 'flowers_list:start_urls'

FLOWERS_DETAIL_START_URL = 'flowers_detail:start_urls'
FLOWERS_IMAGE_START_URL = 'flowers_image:start_urls'

FLOWERS_DETAIL_KEY = 'huhua:flowers'

FLOWERS_AVATAR_KEY = 'huhua:avatar'

# mongodb
MONGO_HOST = '192.168.1.101'
MONGO_PORT = 27017

MONGO_DB_PROXY = 'ip_proxy'
MONGO_COLLECTION_PROXY = 'proxies'
MONGO_CONNSTR_PROXY = 'mongodb://ip_proxy:123@192.168.10.107:27017/ip_proxy'

# redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
# mysql
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DB = 'huahui'
MYSQL_PORT = 3306
