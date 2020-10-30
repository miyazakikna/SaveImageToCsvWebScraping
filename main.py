# coding: utf-8

from bs4 import BeautifulSoup
import json
import urllib.request
import csv
import re

# 「いらすとや」の画像URLを取得
url = "https://www.irasutoya.com/search/label/%E3%83%93%E3%82%B8%E3%83%8D%E3%82%B9"
# 画像ページのURLを格納するリストを用意
link_list = []
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, "html.parser")
# 画像リンクのタグをすべて取得
image_list = soup.select('div.boxmeta.clearfix > h2 > a')
# 画像リンクを1つずつ取り出す
for image_link in image_list:
    link_url = image_link.attrs['href']
    link_list.append(link_url)

for page_url in link_list:
    page_html = urllib.request.urlopen(page_url)
    page_soup = BeautifulSoup(page_html, "html.parser")
    # 画像ファイルのタグをすべて取得
    img_list = page_soup.select('div.separator > a > img')
    # imgタグを1つずつ取り出す
    for img in img_list:
        img_name = (img.attrs['alt'])
        # 画像ファイルのURLを抽出
        img_url = (img.attrs['src'])
        list = [img_name, img_url]
        # csv形式で保存する
        with open('hoge.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(list)
