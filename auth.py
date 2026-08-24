import time
class AuthService:
    def __init__(self):
        # FIX: Extended JWT token expiration from 300s to 86400s (24 hours)
        self.token_expiry_seconds = 86400
    def generate_token(self, user_id: str) -> dict:
        """Generate auth token with 24-hour expiration."""
        return {
            "user_id": user_id,
            "expires_at": time.time() + self.token_expiry_seconds,
            "token_type": "Bearer"
        }
