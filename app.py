import connexion
from flask import redirect

# Create a Connexion app instance (which internally wraps a Flask app)
# The OpenAPI specification is stored in the current directory (./)
cnx_app = connexion.App(__name__, specification_dir='./')

# Add the API defined in swagger.yaml
# options={"swagger_ui": True} enables the Swagger UI at /ui
cnx_app.add_api(
    'swagger.yaml',
    options={"swagger_ui": True}
)

# Flask app object (can be used for adding additional Flask routes)
app = cnx_app.app

@app.route('/')
def redirect_to_ui():
    """
    Redirect the root URL (/) to the Swagger UI page.
    """
    return redirect('/ui')

if __name__ == "__main__":
    # Start the Connexion app (which uses Uvicorn or Flask internally)
    cnx_app.run(host="0.0.0.0", port=8000)
