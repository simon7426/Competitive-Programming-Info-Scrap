import requests
from bs4 import BeautifulSoup
from flask import current_app as app

base_url = "https://lightoj.com/user/"


def get_solve(user_id):
    try:
        url = base_url + user_id
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        solved = soup.find("div", {"class": "like-count"})
        follow = soup.find("div", {"class": "follow-count"})
        # print(solved.span.text)
        # print(follow.span.text)
        return (solved.span.text, follow.span.text)
    except Exception as e:
        app.logger.info(e)
        return "fail"
