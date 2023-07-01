from time import sleep
from rsshub.utils import DEFAULT_HEADERS, fetch


def parse_html(post):
    item = {}
    item['title'] = post.xpath('text()').extract_first()
    item['link'] = post.xpath('@href').extract_first()
    html = fetch(item['link'], headers=DEFAULT_HEADERS)
    item['description'] = (
        html
        .xpath('//div[@id="detail"]')
        .get()
    )
    sleep(1)
    return item