import requests

URL = "http://127.0.0.1:5000/add_to_cart"
 
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Host':'localhost:5000',
    'Origin':'http://localhost:5000',
    'Referer':'http://localhost:5000/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    "Content-Type": "application/x-www-form-urlencoded",
    'Cookie':'session=eyJjYXJ0Ijp7ImFwcGxlIjoiMyIsIm1pbGsiOiI0NTMifX0.ZXhZUg.nChOw6ciYI5-WjncDK_qZdc8r8w'
    }

data = {'item':'car','quantity':'1'}

r = requests.post(url=URL, headers=headers,data=data)
print(r.status_code)