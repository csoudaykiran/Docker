from connexion.exceptions import OAuthProblem  # Used to raise 401 Unauthorized errors
import jwt  # PyJWT for decoding/encoding JWT tokens

# Secret key for signing JWT tokens (use environment variables in real apps)
SECRET_KEY = "mysecret"

def decode_token(token):
    """
    Connexion will call this function for every endpoint that requires JwtTokenAuth.
    It receives the Bearer token (without the "Bearer " prefix).
    
    :param token: The JWT token provided in the Authorization header
    :return: A dictionary with user info (if valid)
    """
    try:
        # Decode the token using HS256 algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print(f"Decoded token payload: {payload}")
        
        # Ensure the token has scopes (required for scope validation)
        if "scope" not in payload:
            raise OAuthProblem("Token missing scopes")
        return payload  # Connexion expects a dictionary of claims
    except jwt.ExpiredSignatureError:
        raise OAuthProblem("Token has expired")
    except jwt.InvalidTokenError:
        raise OAuthProblem("Invalid token")
