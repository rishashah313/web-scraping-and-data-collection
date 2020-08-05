from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import scrapy


class UrlsSpider_xpath(scrapy.Spider):
    name = 'ByXpath_argument'
    
    start_urls = []
    url_file = open("file_with_urls.txt", "r")
    for url in url_file:
        url = url.strip("\n")
        start_urls += [url]
                
        
    def parse(self, response):
        driver = webdriver.Chrome(executable_path=r"C:\Users\risha\Downloads\chromedriver_win32\chromedriver.exe")
        print("URL: " + response.request.url)
        driver.get(response.request.url)
        name=input("Enter the name of the file")
        filename = name + ".txt"
        file = open(filename, "a")
            
        """
        Manually find the xpath of the content you want to scrape by inspecting that element
        The xpath will look like the following samples:
        //div[@class = 'field-items']
        //div[@class = 'wpb_wrapper']
        //div[@class='column colOne']
        """
        xpath_argu = input("Enter the xpath")
        for content in response.xpath(xpath_argu):
            
            html_text = content.extract()
            """
            The statement will look as follows:
            text = content.xpath("//div[@class='col-lg-12']/p").extract()
            """
            html_text = str(html_text)
            soup = BeautifulSoup(html_text, 'html.parser')
            text = soup.get_text()
            text_encoded = text.encode("utf-8")
            text_encoded = str(text_encoded)
            file.write(text_encoded)
            file.write("\n")
            print(text)
            print("\n")
