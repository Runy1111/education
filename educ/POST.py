import requests

data = {'custname': 'Сергей Корешков',
        'custtel': '89651779883',
        'custemail': 'serezha.koreshkov@gmail.com',
        'size': 'small',
        'topping': 'mushroom',
        'delivery': '18:45',
        'comments': ''}

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Priority": "u=1, i",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-68541f04-3cdfe3710f2ebed55010bba3"
  }

variable = requests.Session()

ara = variable.get('https://httpbin.org/form/post')
response = variable.post('https://httpbin.org/post', headers=headers, data=data, allow_redirects=True)

print(response.text)
