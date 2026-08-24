import time
from collections import defaultdict
class RateLimiter:
    """In-memory sliding window rate limiter to prevent brute-force attacks."""
    def __init__(self, max_requests: int = 5, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)
    def is_allowed(self, ip_address: str) -> bool:
        now = time.time()
        # Filter out timestamps older than the sliding window
        self.requests[ip_address] = [
            t for t in self.requests[ip_address] if now - t < self.window_seconds
        ]
        if len(self.requests[ip_address]) >= self.max_requests:
            return False
        self.requests[ip_address].append(now)
        return True
