from scrapy import Spider,Request,FormRequest
import re
import json
from lxml import etree
from ..settings import DEFAULT_REQUEST_HEADERS



from ..settings import DEFAULT_REQUEST_HEADERS
from wangyiyun.items import WangyiyunItem


class WangyiyunSpider(Spider):
    name = 'wangyiyun'
    base_url = 'https://music.163.com'

    def start_requests(self):

            #url = 'https://music.163.com/discover/artist/cat?id=1001&initial=65'
            url = 'https://music.163.com/discover/toplist?id=3778678'
            yield Request(url=url, callback=self.parse,) #用来获取页码#region = gulou,jianye 等
    def parse(self, response):
        #print(response.text)
        selector = etree.HTML(response.text)

        IDS = selector.xpath('//ul[@class="f-hide"]/li/a/@href')
        for ID in IDS:
            id= ID[9:]
            url='http://music.163.com/'+ID
        #url = 'https://music.163.com/song?id=516076896'
        #id = '516076896'
            yield Request(url=url,meta={'id': id},callback=self.parse_getinfo)
    def parse_getinfo(self,response):

        item = WangyiyunItem()
        music_id = response.meta['id']
        music = response.xpath('//div[@class="tit"]/em[@class="f-ff2"]/text()').extract_first()
        artist = response.xpath('//div[@class="cnt"]/p[1]/span/a/text()').extract_first()
        album = response.xpath('//div[@class="cnt"]/p[2]/a/text()').extract_first()


        data = {
            'csrf_token': '',
            'params': '6swhKKQl63AzjW0B/5kNFvDjyk7xi4mQQXSpLwVXoAylLi16EG7rNjC1bKCcwHsk259PZ+Ve9pxL2LWOORWf8tB7k/BQwaCLpMGRvetacfXelc23XkQVb8UAT62qv3edpCg3FZlabTZqqaZbjQS9ZoRFhNz4UNooPYjgMCttMCrASStlKFFqSnT+N1gychNkAU1rq1QlckVpWvmkX7xg3pU+DgNriAwZL8Rros8/klE=',
            'encSecKey': '871d301c5e39b6fff624db5e256276e401a06905b06008a5a58139217c59b74c0d8a0f615ccd180c14d39beff23f1465aace4115a934df3d7e954c4a16116b4d9b85129f590414c596027b7f417ed1c3e2986a2d4024518172e3e14fc1aa17bd3cb63ff4ac593b72b25512858f2cc577fcc3355a90e7b0717e19fc2e3b8f2c00'
        }
        DEFAULT_REQUEST_HEADERS['Referer'] = self.base_url + '/playlist?id=' + str(music_id)
        music_comment = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(music_id)

        yield FormRequest(music_comment, meta={'id':music_id,'music':music,'artist':artist,'album':album}, \
                          callback=self.parse_comment, formdata=data)




    def parse_comment(self, response):
        '''获取歌曲信息
        '''
        id = response.meta['id']
        music = response.meta['music']
        artist = response.meta['artist']
        album = response.meta['album']
        result = json.loads(response.text)
        comments = []
        comment_total = result.get('total')
        if 'hotComments' in result.keys():
            for comment in result.get('hotComments'):
                hotcomment_author = comment['user']['nickname']
                hotcomment = comment['content']
                hotcomment_like = comment['likedCount']#点赞
                hotcomment_avatar = comment['user']['avatarUrl']#头像

                data = {
                    'nickname': hotcomment_author,
                    'content': hotcomment,
                    'likedcount': hotcomment_like,
                    'avatarurl': hotcomment_avatar
                }
                comments.append(data)
        item = WangyiyunItem()
        item['id'] = id
        item['name']= music
        item['singer']= artist
        item['album']= album
        item['comment_total'] =comment_total
        item['comment']= comments
        yield item





















