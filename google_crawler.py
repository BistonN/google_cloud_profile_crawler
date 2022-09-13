import pandas as pd
import requests
from bs4 import BeautifulSoup

start_urls = pd.read_csv('data.csv').values.tolist()
students = []

def format_string(string):
    return string.replace('\n', '')

for url_proflie in start_urls:
    r = requests.get(url_proflie[0])
    soup = BeautifulSoup(r.text, 'html.parser')
    badges = []
    for on_badge in soup.select('div.profile-badge'):
        name = format_string(soup.select_one('h1.ql-headline-1').text)
        url_badge = format_string(on_badge.select_one('a').get('href'))
        name_badge = format_string(on_badge.select('span')[0].text)
        date_badge = format_string(on_badge.select('span')[1].text)

        format_badges = {
            'name_badge': name_badge,
            'date_badge': date_badge,
            'url_badge': url_badge
        }
        badges.append(format_badges)

    student = {
        'name': name,
        'badges': badges
    }
    students.append(student)
print(students)