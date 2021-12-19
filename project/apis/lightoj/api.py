from flask_restx import Resource, fields
from flask_restx.namespace import Namespace

from project.apis.lightoj.utils import get_solve

lightoj_namespace = Namespace("lightoj")

basic_response = lightoj_namespace.model(
    "response",
    {"message": fields.String, "solved": fields.Integer, "submission": fields.Integer},
)


class LightOJ(Resource):
    @lightoj_namespace.marshal_with(basic_response)
    @lightoj_namespace.response(200, "Successfully Retrived Results.")
    @lightoj_namespace.response(400, "Unable to get information.")
    def get(self, username):
        resp = get_solve(user_id=username)
        if resp == "fail":
            lightoj_namespace.abort(400, "Unable to get information.")
        response_object = {
            "message": "Successfully Retrived Results.",
            "solved": int(resp[0]),
            "submission": int(resp[1]),
        }
        return response_object, 200


lightoj_namespace.add_resource(LightOJ, "/<username>", endpoint="lightoj")
