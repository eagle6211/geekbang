import requests
import json
import send_email

url = 'https://search.geekbang.org/searchmore'
headers = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

def get_data_from(url):

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
    content = ''
    if data_lst:
        for index, item in enumerate(data_lst):
            title = item.get('title')
            if title.find('：') >=0 :
                title = str(index+1) +")" + title.split('：')[1].strip()
            else:
                title = str(index+1) +")" + title
            content += title +"\n"+ item.get('url')+"\n"
        send_email.sendEmail('极客搜索', content)

if __name__ == '__main__':
    get_data_from(url)
