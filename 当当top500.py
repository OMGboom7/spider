import json
import re

import requests
"""
https://github.com/wistbean/learn_python3_spider
"""

def main(page):
    print('start')
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    items = parse_result(html)

    for item in items:
        write_item_to_file(item)
        print(item)

    print('end')

def request_dandan(url):
    # try:
        response = requests.get(url)
        print(response)
        # if requests.status_codes == 200:
        # print(response.text)
        return response.text
    # except requests.RequestException:
    #     return None


def parse_result(html):
    pattern = re.compile(
        '<li>.*?list_num.*?(d+).</div>.*?<img src="(.*?)".*?class="name".*?title="('
        '.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">('
        '.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><spansclass="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, str(html))
    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }
        # print(item)


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + 'n')
        f.close()


if __name__ == "__main__":
    main(1)
