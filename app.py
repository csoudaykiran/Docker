import connexion
from flask import redirect
from security import check_account_id

cnx_app = connexion.App(__name__, specification_dir="./")

cnx_app.add_api(
    "swagger.yaml",
    strict_validation=True,
    validate_responses=True,
    options={"swagger_ui": True},
    auth_all_paths=True,
    security_map={"AccountIdAuth": check_account_id},
)

app = cnx_app.app

@app.route("/")
def redirect_to_ui():
    return redirect("/ui")

if __name__ == "__main__":
    cnx_app.run(host="0.0.0.0", port=8000)
