import uuid
from connexion.exceptions import Unauthorized

def check_account_id(api_key=None, required_scopes=None):
    print(f"Security check called with api_key: {api_key}")

    if not api_key:
        raise Unauthorized("No authorization token provided")

    try:
        uuid.UUID(api_key)
    except ValueError:
        raise Unauthorized("Invalid Account-ID format")

    VALID_ACCOUNT_ID = "550e8400-e29b-41d4-a716-446655440000"
    if api_key == VALID_ACCOUNT_ID:
        return {"sub": "authorized_user"}

    raise Unauthorized("Unauthorized Account-ID")
