from flask_restx import Namespace, Resource, fields

from project.apis.codeforces.utils import get_info

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
        try:
            resp = get_info(username)
            response_object = {"message": "Successfull", **resp}
            return response_object, 200
        except Exception as e:
            print(e)
            codeforces_namespace.abort(400, "Operation error")


codeforces_namespace.add_resource(
    CodeforcesInfo, "/<username>", endpoint="CodeforcesUser"
)
