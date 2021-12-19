from flask_restx import Resource, fields
from flask_restx.namespace import Namespace

from project.apis.vjudge.utils import get_solve

vjudge_namespace = Namespace("vjudge")

basic_response = vjudge_namespace.model(
    "response",
    {"message": fields.String, "solved": fields.Integer, "submission": fields.Integer},
)


class VJudge(Resource):
    @vjudge_namespace.marshal_with(basic_response)
    @vjudge_namespace.response(200, "Successfully Retrived Results.")
    @vjudge_namespace.response(400, "Unable to get information.")
    def get(self, username):
        resp = get_solve(user_id=username)
        if resp == "fail":
            vjudge_namespace.abort(400, "Unable to get information.")
        response_object = {
            "message": "Successfully Retrived Results.",
            "solved": int(resp[0]),
            "submission": int(resp[1]),
        }
        return response_object, 200


vjudge_namespace.add_resource(VJudge, "/<username>", endpoint="vjudge")
