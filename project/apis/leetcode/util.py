import requests

base_url = f"https://leetcode.com/graphql"


def get_info(username):
    query = """{ matchedUser(username: "%s") {
username
submitStats: submitStatsGlobal {
acSubmissionNum {
difficulty
count
submissions
}
}
}
}
    """ % (
        username
    )
    resp = requests.get(base_url, json={"query": query})
    resp_data = resp.json().get("data")
    submissions = resp_data["matchedUser"]["submitStats"]["acSubmissionNum"]
    # print(resp_data['matchedUser']['username'])
    ret = {}
    for submission in submissions:
        ret[submission["difficulty"]] = {
            "count": submission["count"],
            "submissions": submission["submissions"],
        }
        # print(submission['difficulty'],submission['count'],submission['submissions'])
    return ret
