from lxml import html
import requests
url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
values = {'log': 'admin',
          'pwd': '123456aA'}

session = requests.Session()
resp    = session.post(url,data=values)
tree = html.fromstring(resp.content)
print(tree.xpath('//span[@class="display-name"]/text()')[0])
