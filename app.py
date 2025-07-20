import connexion  # Connexion is used to bind Flask with OpenAPI
from flask import redirect

# Create the Connexion application
# specification_dir specifies where the OpenAPI (swagger.yaml) file is located
cnx_app = connexion.App(__name__, specification_dir='./')

# Add the API defined in swagger.yaml
# options={"swagger_ui": True} enables Swagger UI at /ui
# strict_validation=True ensures strict adherence to OpenAPI validation
cnx_app.add_api(
    'swagger.yaml',
    options={"swagger_ui": True},
    strict_validation=True
)

# Get the underlying Flask app (in case we want extra routes)
app = cnx_app.app

@app.route('/')
def redirect_to_ui():
    """
    Redirect the root URL (/) to the Swagger UI page.
    """
    return redirect('/ui')

if __name__ == "__main__":
    # Run the Connexion/Flask app on host 0.0.0.0 and port 8000
    cnx_app.run(host="0.0.0.0", port=8000)
