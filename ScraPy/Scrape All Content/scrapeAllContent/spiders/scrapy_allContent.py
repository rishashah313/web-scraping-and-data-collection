import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from bs4 import BeautifulSoup
import requests

class UrlsSpider(scrapy.Spider):
    name = 'urlsspider'
    allowed_domains = ['bedsider.org']
    start_urls = ['https://www.bedsider.org/']
    global_arr = []
    global_var = 0

    rules = (Rule(LxmlLinkExtractor(allow=(), unique=True), callback='parse', follow=True))
    
    def parse(self, response):
        for link in LxmlLinkExtractor(allow_domains=self.allowed_domains, unique=True).extract_links(response):
            print("self.start_urls")
            print(self.start_urls)
            print("self.allowed_domains")
            print(self.allowed_domains)
            print(self.global_arr)
            if link.url not in self.global_arr:
                self.global_arr.append(link.url)
                print(self.global_var)
                print(link.url)
                
                page = requests.get(link.url)        #to extract page from website
                html_code = page.content        #to extract html code from page

                try:
                    soup = BeautifulSoup(html_code, 'html.parser')  #Parse html code
                    for script in soup(["script", "style"]):
                                    script.extract()    # extract

                    text = soup.get_text()# get text
                    # break into lines and remove leading and trailing space 
                    lines = (line.strip() for line in text.splitlines())
                    # break multi-headlines into a line 
                    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                    # drop blank lines
                    text = '\n'.join(chunk for chunk in chunks if chunk)
                    text_extracted = text.encode("utf-8") 
                    text_decoded = text_extracted.decode('utf8', 'ignore')
                    file = open("bedsider.txt", "a")
                    file.write(link.url)
                    file.write(text_decoded)
                    file.write("***")
                    self.global_var = self.global_var + 1
                    
                except Exception as e:
                    print(e)
                
                
                yield scrapy.Request(link.url, callback=self.parse)
