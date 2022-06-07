import requests
from bs4 import BeautifulSoup
from flask import current_app as app

base_url = "https://atcoder.jp/users/"


def get_solve(user_id):
    try:
        url = base_url + user_id
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        solved = soup.find_all("table", {"class": "dl-table"})
        data = solved[1].find_all("td")
        current_rating = data[1].find("span").text
        highest_rating = data[2].find("span").text
        participated = data[3].text
        # print(current_rating, highest_rating, participated)
        return (current_rating, highest_rating, participated)
    except Exception as e:
        app.logger.info(e)
        return "fail"
