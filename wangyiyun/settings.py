# -*- coding: utf-8 -*-

# Scrapy settings for wangyiyun project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wangyiyun'

SPIDER_MODULES = ['wangyiyun.spiders']
NEWSPIDER_MODULE = 'wangyiyun.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wangyiyun (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie':'_ntes_nuid=5e2135ea19041c08d61bddbb9009de63; _ntes_nnid=a387121ca9ed891dca82492f6c088c57,1483420952257; __utma=187553192.690483437.1489583101.1489583101.1489583101.1; __utmz=187553192.1489583101.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __oc_uuid=ff821060-097f-11e7-8c2a-73421a9a1bc4; mail_psc_fingerprint=032ad52396a72877e07f21386dee35a2; NTES_CMT_USER_INFO=106964635%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B06o2qr%7Chttps%3A%2F%2Fsimg.ws.126.net%2Fe%2Fimg5.cache.netease.com%2Ftie%2Fimages%2Fyun%2Fphoto_default_62.png.39x39.100.jpg%7Cfalse%7CbTE1MTUyMzQ3Mjc3QDE2My5jb20%3D; usertrack=c+5+hlkgTIMgjwa+EDUGAg==; _ga=GA1.2.690483437.1489583101; Province=025; City=05278; NTES_PASSPORT=aXWcpL4bYTLQnXY4eO888VlwXt.v922HPG1pBkj.vkeDwsISwc4gjpib7gtylUsoCy.yIGuJPZg7Uq2lTWqIo3A5ddE7eIf5DP_mjdHrg7ky2KFIZHP60ge8g; P_INFO=m15152347277@163.com|1500267468|1|blog|11&10|jis&1499527300&mail163#jis&320800#10#0#0|151277&1|study&blog&photo|15152347277@163.com; UM_distinctid=15d4ee58fc9483-032aae6568b355-333f5902-100200-15d4ee58fca912; NTES_SESS=35juNvuVAClEtPfwjy5rP5GVXVpRFMmwg2ItfudhfLmyGTk4G2l_fIFHi_xsOJTWQrUJvW3JwsMFyepEs0SR6z1_QnKjbQFaesBY9ABy0TVFP_KIiXNgb89wCGe.3_hmKR90f2ybdvNPWqPX8_YesVlIQrWdw5Nfg6KF0EcoVXO3DgV09cJHAeiE_; S_INFO=1500623480|1|0&80##|m15152347277; ANTICSRF=dd45f2a4489d303de869d820a0dadf05; playerid=64643457; JSESSIONID-WYYY=oR0Q0Ce%2Bhldid%2FFtfsiobsg%5Cecyra1qnHBuFFPNBUW%2BbZ3%5C2uq5%2Fqz4VrhRll0%5CaVCfY%2Fg0%2BC47vS%5Cv6rsyuD76tlqWN%2BUryVxph9fZeCmVIDtu5so7vdcdp%2B92hI3A0R5Zm%2Besa5l3ND%5Cz59WOYTY%2FCUjG%2B8gFSGVyzTpMquPQIxyIM%3A1500647790286; _iuqxldmzr_=32; MUSIC_U=f5333454d16d0f0ca5e59b3a82afaabcb107f5e73a4504bae87278f38158d65dbef309e3badc0bfac257abd5a88c5d62dc7e2cf554b1b3fc233a987fb3c42671e386323209b86ec1bf122d59fa1ed6a2; __remember_me=true; __csrf=5cd5b19efc6ea479e298487216162acf; __utma=94650624.776578804.1489210725.1500604214.1500644866.50; __utmb=94650624.28.10.1500644866; __utmc=94650624; __utmz=94650624.1499960824.48.42.utmcsr=yukunweb.com|utmccn=(referral)|utmcmd=referral|utmcct=/412.html',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wangyiyun.middlewares.WangyiyunSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'wangyiyun.middlewares.WangyiyunDownloaderMiddleware': 543,
    'wangyiyun.middlewares.RandomUserAgent': 400,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'wangyiyun.pipelines.WangyiyunPipeline': 300,
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
USER_AGENTS = [
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",

]

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = 'wangyiyunyinyue'
