from flask_restx import Namespace, Resource, fields

from project.apis.codeforces.utils import get_info
from project.apis.redis import get_redis_object, set_redis_object

codeforces_namespace = Namespace("Codeforces")

codeforces_response = codeforces_namespace.model(
    "response",
    {
        "message": fields.String,
        "rating": fields.Integer,
        "max_rating": fields.Integer,
        "rank": fields.String,
        "rank_color": fields.String,
        "max_rank": fields.String,
        "max_rank_color": fields.String,
        "contribution": fields.Integer,
        "solved": fields.Integer,
    },
)


class CodeforcesInfo(Resource):
    @codeforces_namespace.marshal_with(codeforces_response)
    @codeforces_namespace.response(200, "Successfull")
    @codeforces_namespace.response(400, "Operation error")
    def get(self, username):
        redis_key = f"codeforces_{username}"
        try:
            resp = get_info(username)
            response_object = {"message": "Successfull", **resp}
            set_redis_object(redis_key, response_object)
            return response_object, 200
        except Exception as e:
            print(e)
            ret_obj = get_redis_object(redis_key)
            if ret_obj is not None:
                print("***********Transfering From Cache*****************************")
                return ret_obj, 200
            else:
                codeforces_namespace.abort(400, "Operation error")


codeforces_namespace.add_resource(
    CodeforcesInfo, "/<username>", endpoint="CodeforcesUser"
)
