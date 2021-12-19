from flask_restx import Resource, fields
from flask_restx.namespace import Namespace

from project.apis.atcoder.utils import get_solve

atcoder_namespace = Namespace("atcoder")

basic_response = atcoder_namespace.model(
    "response",
    {
        "message": fields.String,
        "rating": fields.Integer,
        "max_rating": fields.Integer,
        "participated": fields.Integer,
    },
)


class Atcoder(Resource):
    @atcoder_namespace.marshal_with(basic_response)
    @atcoder_namespace.response(200, "Successfully Retrived Results.")
    @atcoder_namespace.response(400, "Unable to get information.")
    def get(self, username):
        resp = get_solve(user_id=username)
        if resp == "fail":
            atcoder_namespace.abort(400, "Unable to get information.")
        response_object = {
            "message": "Successfully Retrived Results.",
            "rating": int(resp[0]),
            "max_rating": int(resp[1]),
            "participated": int(resp[2]),
        }
        return response_object, 200


atcoder_namespace.add_resource(Atcoder, "/<username>", endpoint="atcoder")
