# -*- coding: utf-8 -*-

# Scrapy settings for newyorker project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'newyorker'

SPIDER_MODULES = ['newyorker.spiders']
NEWSPIDER_MODULE = 'newyorker.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newyorker (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.9',
   'Cookie':'CN_xid=c9daee6c-8ae9-4afe-ae7f-f1010861db9f; ev_abValue=7; ev_sid=5af188fbe4b0c5edfb52560c; ev_did=5af188fbe4b0c5edfb52560b; ev_abGroup=4MeterMax; sID=32128e65-903d-4df4-9fde-7a3e980f3204; _sdsat_landing_page=https://www.newyorker.com/|1525778683143; _sdsat_session_count=1; _sdsat_traffic_source=http://www.qkankan.com/north-america/america/medium/200904/1726.html; optimizelyEndUserId=oeu1525778683917r0.08081796238026051; optimizelySegments=%7B%222711860772%22%3A%22referral%22%2C%222722510763%22%3A%22none%22%2C%222724481038%22%3A%22false%22%2C%222740140473%22%3A%22gc%22%7D; optimizelyBuckets=%7B%7D; AMCVS_F7093025512D2B690A490D44%40AdobeOrg=1; _ga=GA1.2.584364082.1525778683; _gid=GA1.2.1986351377.1525778684; CN_sp=6f1c54da-9487-46cc-99f0-bbdd8f73ce3e; CN_su=18ceff58-16a6-4180-8dcc-fcee31cea36d; __srret=1; AMCV_F7093025512D2B690A490D44%40AdobeOrg=102365995%7CMCIDTS%7C17660%7CMCMID%7C28210273886482298512077648467173537490%7CMCAAMLH-1526383484%7C11%7CMCAAMB-1526383484%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1525785884s%7CNONE%7CMCSYNCSOP%7C411-17667%7CMCAID%7CNONE%7CvVersion%7C2.2.0; s_vnum_m=1527782400604%26vn%3D1; sinvisit_m=true; _dr=http%3A%2F%2Fwww.qkankan.com%2Fnorth-america%2Famerica%2Fmedium%2F200904%2F1726.html; v30=qkankan.com; v39=qkankan.com; s_cc=true; CN_atmosphere_test=91cd4ff4-3c5a-4e70-8b0b-e10dfc3bbd0b; CN_atmo_list_test=false,0,1; __srui=6bd55cee-52b2-11e8-a9e4-22000b75814b; aamconde=conde%3Dsv%3BCN%3D750744; aam_optimizely=aam%3D226821; aam_uuid=28405979351844308502060629886533745163; _sdsat_AAM_UUID=28405979351844308502060629886533745163; s_ppn=no%20value; s_pct=null; _sdsat_lt_pages_viewed=4; _sdsat_pages_viewed=4; s_depth=4; timeSpent=1525778717760; s_sq=%5B%5BB%5D%5D; pID=9b684063-a1c4-4969-9f96-6520a1f28a4d; s_nr=1525778905566-New',
    'Referer':'https://www.newyorker.com/latest/news',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'newyorker.middlewares.NewyorkerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'newyorker.middlewares.NewyorkerDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'newyorker.pipelines.NewyorkerPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
