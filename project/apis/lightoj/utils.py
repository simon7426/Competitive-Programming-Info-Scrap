import requests
from bs4 import BeautifulSoup

base_url = "https://lightoj.com/user/"


def get_solve(user_id):
    try:
        url = base_url + user_id
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        solved = soup.find("div", {"class": "like-count"})
        follow = soup.find("div", {"class": "follow-count"})
        print(solved.span.text)
        print(follow.span.text)
        return (solved.span.text, follow.span.text)
    except Exception as e:
        print(e)
        return "fail"
