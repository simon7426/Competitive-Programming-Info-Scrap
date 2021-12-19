from flask_restx import Resource, fields
from flask_restx.namespace import Namespace

from project.apis.spoj.utils import get_solve

spoj_namespace = Namespace("spoj")

basic_response = spoj_namespace.model(
    "response",
    {"message": fields.String, "solved": fields.Integer, "submission": fields.Integer},
)


class SPOJ(Resource):
    @spoj_namespace.marshal_with(basic_response)
    @spoj_namespace.response(200, "Successfully Retrived Results.")
    @spoj_namespace.response(400, "Unable to get information.")
    def get(self, username):
        resp = get_solve(user_id=username)
        if resp == "fail":
            spoj_namespace.abort(400, "Unable to get information.")
        response_object = {
            "message": "Successfully Retrived Results.",
            "solved": int(resp[0]),
            "submission": int(resp[1]),
        }
        return response_object, 200


spoj_namespace.add_resource(SPOJ, "/<username>", endpoint="spoj")
