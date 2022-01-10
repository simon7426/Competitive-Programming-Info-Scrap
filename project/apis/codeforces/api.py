from flask_restx import Namespace, Resource, fields

from project.apis.codeforces.utils import get_info

codeforces_namespace = Namespace("Codeforces")

# leetcode_unit_response = codeforces_namespace.model(
#     "unit", {"count": fields.Integer, "submissions": fields.Integer}
# )

# leetcode_response = leetcode_namespace.model(
#     "response",
#     {
#         "message": fields.String,
#         "All": fields.Nested(leetcode_unit_response),
#         "Easy": fields.Nested(leetcode_unit_response),
#         "Medium": fields.Nested(leetcode_unit_response),
#         "Hard": fields.Nested(leetcode_unit_response),
#     },
# )


class CodeforcesInfo(Resource):
    # @leetcode_namespace.marshal_with(leetcode_response)
    # @leetcode_namespace.response(200, "Successfull")
    def get(self, username):
        resp = get_info(username)
        # print(resp)
        response_object = {"message": "Successfull", **resp}
        return response_object, 200


codeforces_namespace.add_resource(
    CodeforcesInfo, "/<username>", endpoint="CodeforcesUser"
)
