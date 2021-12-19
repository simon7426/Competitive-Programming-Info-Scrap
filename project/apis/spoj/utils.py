import requests
from bs4 import BeautifulSoup

base_url = "https://spoj.com/users/"


def get_solve(user_id):
    try:
        url = base_url + user_id
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        solved = soup.find("dl", {"class": "profile-info-data"}).find_all("dd")
        print(solved[0].text)
        print(solved[1].text)
        return (solved[0].text, solved[1].text)
    except Exception as e:
        print(e)
        return "fail"
