from connexion.exceptions import OAuthProblem  # Exception used for authentication failures

# A valid API key for demo purposes (in production, you'd check a database or external service)
VALID_TOKEN = "valid-token-123"

def verify_token(apikey, required_scopes=None):
    """
    Connexion automatically calls this function when an endpoint requires JwtTokenAuth security.

    :param apikey: The API key provided by the client (from 'x-access-token' header)
    :param required_scopes: A list of scopes required by the endpoint (unused for API keys)
    :return: A dictionary representing the authenticated user (if valid)
    """
    print(f"API key received: {apikey}")
    
    # Check if the provided API key matches the valid token
    if apikey != VALID_TOKEN:
        # Raise OAuthProblem (Connexion returns a 401 Unauthorized response)
        raise OAuthProblem("Invalid or missing API key")
    
    # Return a "user info" dictionary to indicate successful authentication
    return {"sub": "user123"}