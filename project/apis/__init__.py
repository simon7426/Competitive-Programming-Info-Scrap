from flask_restx import Api

from project.apis.alive import alive_namespace
from project.apis.atcoder.api import atcoder_namespace
from project.apis.codeforces.api import codeforces_namespace
from project.apis.leetcode.api import leetcode_namespace
from project.apis.lightoj.api import lightoj_namespace
from project.apis.spoj.api import spoj_namespace
from project.apis.vjudge.api import vjudge_namespace

api = Api(version="1.0", title="S3 Connect API Docs", doc="/docs")

api.add_namespace(alive_namespace, path="/api/alive")
api.add_namespace(atcoder_namespace, path="/api/user/atcoder")
api.add_namespace(codeforces_namespace, path="/api/user/codeforces")
api.add_namespace(leetcode_namespace, path="/api/user/leetcode")
api.add_namespace(lightoj_namespace, path="/api/user/lightoj")
api.add_namespace(spoj_namespace, path="/api/user/spoj")
api.add_namespace(vjudge_namespace, path="/api/user/vjudge")
