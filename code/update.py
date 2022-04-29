import requests
import os
import time

from selenium import webdriver
from bs4 import BeautifulSoup


def update():

      url = "https://www.atptour.com/en/players/jiri-vesely/v708/overview"
      home_url = "https://www.atptour.com/en/players"
      header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                "referer":home_url}

      #ファイルのある場所に移動
      os.chdir(os.path.dirname(__file__))
 
      #ドライバーの設定 
      options = webdriver.ChromeOptions()
      options.add_experimental_option('excludeSwitches', ['enable-logging'])
      #options.add_argument('--headless')
      driver = webdriver.Chrome('..\\chromedriver',options=options) 
      
      try:
           #URL読み込み
           driver.get(url)
           time.sleep(1)
         
           #htmlの情報を取得
           html = driver.page_source.encode('utf-8')
           soup = BeautifulSoup(html, "html.parser")
      finally:
           driver.close()


      s = requests.Session()
      res = s.get(url=url, headers=header)
      cookies = dict(res.cookies)

      print(cookies)

      #res = requests.get(url=url, headers=header)

      print(res)

      print(soup)
      with open("test.html", mode="w", encoding="UTF-8") as f:
           f.write(str(soup))


if __name__=="__main__":

      update()