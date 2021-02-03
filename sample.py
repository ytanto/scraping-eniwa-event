# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import chromedriver_binary

options = Options()
# headlessモードを使用する
options.add_argument('--headless')
# headlessモードで暫定的に必要なフラグ(そのうち不要になる)
options.add_argument('--disable-gpu')
# すべての拡張機能を無効にする。ユーザースクリプトも無効にする
options.add_argument('--disable-extensions')
# Proxy経由ではなく直接接続する
options.add_argument('--proxy-server="direct://"')
# すべてのホスト名
options.add_argument('--proxy-bypass-list=*')
# 起動時にウィンドウを最大化す
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
try:
    # Googleの検索TOP画面を開く。
    driver.get("https://www.city.eniwa.hokkaido.jp/kurashi/calendar.html")
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "lxml")
    # print(soup.prettify())
    table = soup.find('table', {'id': 'calListTable'}).tbody
    rows = table.find_all('tr')
    print(rows[0])

    # # 検索語として「selenium」と入力し、Enterキーを押す。
    # search = driver.find_element_by_name('q')
    # search.send_keys("selenium automation")
    # search.send_keys(Keys.ENTER)
    # # タイトルに「Selenium - Web Browser Automation」と一致するリンクをクリックする。
    # #element = driver.find_element_by_partial_link_text("SeleniumHQ Browser Automation")
    # #element = driver.find_element_by_link_text("WebDriver")
    # element = driver.find_element_by_partial_link_text("Selenium")
    # element.click()

    # 5秒間待機してみる。
    sleep(1)
    # ブラウザを終了する。
    driver.close()
except:
    driver.close()
