# -*- coding: utf-8 -*-
import scrapy
import re
import datetime

from scrapy import Request
from scrapy.loader import ItemLoader
from urllib import parse

from ArticleSpider.items import JobBoleArticleItem, ArticleItemLoder
from ArticleSpider.utils.common import get_md5

class jobbolespider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://blog.jobbole.com/114690/']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1. 获取文章列表页中的文章的url并交给scrapy下载后进行解析
        2. 获取下一页的url并交给scrapy进行下载，下载后交给parse
        """

        # 解析列表页中的所有的文章的url并交给scrapy下载后进行解析
        # 说明：urljoin(response.url, post_url)  url拼接。有的href取出来没有域名，如href="/article/",
        #       而response.url是当前域名，拼接后就是http://xxx.com/article/
        #       如果本身就有域名如 http://xxx.com/article/，则不进行拼接
        post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={'front_img_url': image_url}, callback=self.parse_detail)

        # 获取下一页的数据
        # next_url = response.css('.next.page-numbers::attr(href)').extract_first()
        # if next_url:
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)


    def parse_detail(self, response):

        # ----------------------------------------
        # 通过Xpsth提取字段

        # re_selector = response.xpath("//*[@id='post-114690']/div[1]/h1/text()")
        # 获取标题
        # title = response.xpath("//div[@class='entry-header']/h1/text()").extract_first()

        # 获取发表时间
        # ftime = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract_first().strip().replace('·','').strip()

        # 获取点赞数
        # zan = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract_first()

        # 获取收藏人数
        # shoucang = re.match('.*(\d+).*', response.xpath("//span[contains(@class, 'bookmark-btn ')]/text()").extract_first())
        # if shoucang:
        #     shoucang_count = int(shoucang.group(1))
        # else:
        #     shoucang_count = 0

        # 获取评论人数
        # comment = re.match('.*(\d+).*', response.xpath("//span[contains(@class, 'hide-on-480')]/text()").extract_first())
        # if comment:
        #     comment_count = int(comment.group(1))
        # else:
        #     comment_count = 0

        # --------------------------------------------

        # 通过 css 选择器提取字段

        # 封面图
        # front_img_url = response.meta.get('front_img_url', '')
        #
        # # 标题
        # title_css = response.css(".entry-header h1::text").extract_first()
        #
        # # 时间
        # ftime_css = response.css("p.entry-meta-hide-on-mobile::text").extract_first().strip().replace('·', '').strip()
        #
        # # 电赞数
        # zan_css_count = response.css(".vote-post-up h10::text").extract_first()
        #
        # # 收藏数
        # shoucang_re = response.css(".bookmark-btn::text").extract_first()
        # shoucang_css = re.match('.*(\d+).*', shoucang_re)
        # if shoucang_css:
        #     shoucang_css_count = int(shoucang_css.group(1))
        # else:
        #     shoucang_css_count = 0
        #
        # # 评论数
        # comment_re = response.css('a[href="#article-comment"] span::text').extract_first()
        # comment_css = re.match('.*(\d+).*', comment_re)
        # if comment_css:
        #     comment_css_count = int(comment_css.group(1))
        # else:
        #     comment_css_count = 0
        #
        # tags_css_list = response.css('p.entry-meta-hide-on-mobile a::text').extract()
        # tags_css_list = [element for element in tags_css_list if not element.strip().endswith('评论')]
        # tags_css = ','.join(tags_css_list)
        # content_css = response.css("div.entry").extract_first()

        # article_item = JobBoleArticleItem()
        # article_item['title'] = title_css
        # article_item['url'] = response.url
        # article_item['url_object_id'] = get_md5(response.url)
        # try:
        #     ftime_css = datetime.datetime.strftime(ftime_css, "%Y/%m/%d").date()
        # except Exception as e:
        #     ftime_css = datetime.datetime.now().date()
        # article_item['ftime'] = ftime_css
        # article_item['front_img_url'] = [front_img_url]
        # article_item['zan_count'] = zan_css_count
        # article_item['shoucang_count'] = shoucang_css_count
        # article_item['comment_count'] = comment_css_count
        # article_item['tags'] = tags_css
        # article_item['content'] = content_css

        # -----------------------------------------------

        # 通过itemLoder提取字段

        # 封面图
        front_img_url = response.meta.get('front_img_url', '')
        # 通过itemloder加载item
        # ArticleItemLoder 自定义类，显示第一个，相当于上述中的extract()[0]
        item_loder = ArticleItemLoder(item=JobBoleArticleItem(), response=response)
        item_loder.add_css('title', '.entry-header h1::text')
        item_loder.add_value('url', response.url)  # 不是解析的用value
        item_loder.add_value('url_object_id', get_md5(response.url))
        item_loder.add_css('ftime', 'p.entry-meta-hide-on-mobile::text')
        item_loder.add_value('front_img_url', [front_img_url])
        # item_loder.add_css('front_img_path', )
        item_loder.add_css('zan_count', '.vote-post-up h10::text')
        item_loder.add_css('shoucang_count', '.bookmark-btn::text')
        item_loder.add_css('comment_count', 'a[href="#article-comment"] span::text')
        item_loder.add_css('tags', 'p.entry-meta-hide-on-mobile a::text')
        item_loder.add_css('content', 'div.entry')

        article_item = item_loder.load_item()

        yield article_item


