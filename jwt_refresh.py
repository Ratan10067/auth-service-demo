import secrets
import time
class RefreshTokenManager:
    """Manages secure refresh token rotation to prevent replay attacks."""
    def __init__(self, token_ttl_days: int = 7):
        self.token_ttl_seconds = token_ttl_days * 86400
        self.active_tokens = {}
    def issue_refresh_token(self, user_id: str) -> str:
        token = secrets.token_urlsafe(32)
        self.active_tokens[token] = {
            "user_id": user_id,
            "expires_at": time.time() + self.token_ttl_seconds,
            "revoked": False
        }
        return token
    def rotate_token(self, old_token: str) -> str:
        """Rotate token and invalidate previous token."""
        if old_token not in self.active_tokens:
            raise ValueError("Invalid refresh token")
        record = self.active_tokens[old_token]
        if record["revoked"] or time.time() > record["expires_at"]:
            raise ValueError("Token is expired or revoked")
        # Invalidate old token (one-time use)
        record["revoked"] = True
        # Issue new token
        return self.issue_refresh_token(record["user_id"])
