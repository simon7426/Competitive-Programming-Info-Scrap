import requests
from bs4 import BeautifulSoup

base_url = "https://vjudge.net/user/"


def get_solve(user_id):
    try:
        url = base_url + user_id
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        solved = soup.find("a", {"title": "Overall solved"})
        attempt = soup.find("a", {"title": "Overall attempted"})
        print(solved.text)
        print(attempt.text)
        return (solved.text, attempt.text)
    except Exception as e:
        print(e)
        return "fail"
