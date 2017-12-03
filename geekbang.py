】import requests
import json
import send_email

url = 'https://search.geekbang.org/searchmore'
headers = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

def deal_sented_content(url):
    #form data
    data = {
        'q':'',
        't':'0',
        's':'AI',
        'size':'20',
        'p':'1',
        'o':'-1'
    }
    response = requests.post(url, headers=headers, data=data)
    data = json.loads(response.text)
    data_lst = data.get("result").get("content")
    content_lst = []
    #处理发送邮件内容
    if data_lst:
        for index, item in enumerate(data_lst, 1):
            title = item.get('title').split('：')[-1].strip()
            url = item.get('url')
            content = '({index}) {title} \n {url} '.format(index=index,
                                                            title=title,
                                                            url=url
                                                            )
            content_lst.append(centent) 
         content = '\n'.join(content_lst)
     return content

def main(url):
    content = deal_sented_content(url)
    send_email.sendEmail('极客搜索', content)

if __name__ == '__main__':
    main(url)
