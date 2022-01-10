import requests

def get_color(rank):
    color = {
        "legendary grandmaster" : "black red",
        "international grandmaster": "red",
        "grandmaster" : "red",
        "international master": "orange",
        "master": "orange",
        "candidate master": "violet",
        "expert": "blue",
        "specialist": "cyan",
        "pupil": "green",
        "newbie": "gray",
    }
    if rank in color:
        return color[rank]
    else:
        return "gray"


def get_info(username):
    info_url = f"https://codeforces.com/api/user.info?handles={username}"
    status_url = f"https://codeforces.com/api/user.status?handle={username}"

    try:
        resp_info = requests.get(info_url)
        # print(resp_info.json())
        result = resp_info.json()["result"][0]
        rating = result.get('rating')
        rank = result.get('rank')
        max_rating = result.get('maxRating')
        max_rank = result.get('maxRank')
        contribution = result.get('contribution')
        # print(rating, rank, max_rating, max_rank)
        status_info = requests.get(status_url)
        problems = status_info.json()["result"]
        solvedCnt = len(list(filter(lambda x: x["verdict"]=="OK", problems)))
        # print(solvedCnt)
        return {
            "rating": rating,
            "max_rating": max_rating,
            "rank": rank,
            "rank_color": get_color(rank),
            "max_rank": max_rank,
            "max_rank_color": get_color(max_rank),
            "contribution": contribution,
            "solved": solvedCnt,
        }
    except Exception as e:
        print(e)
        raise Exception