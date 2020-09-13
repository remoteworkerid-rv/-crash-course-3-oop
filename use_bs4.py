import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success ! Response = {response.status_code}')
        # print(f'content {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil Pemanggilan {url}')
        print(f'Title {soup.title.string}')

    else:
        print(f'OOPP !!! ada kesalahan requests {response.status_code}')
except Exception as e:
    print(f'There is an error {e}')

print('Program ended')