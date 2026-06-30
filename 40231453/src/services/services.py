"""
Microservices corresponding to the Logical View of the architecture:
authentication, registration, content catalog, payment, streaming, search.

Function bodies contain minimal working logic so that unit/acceptance
tests can run, per the exam's testing requirement.
"""

from typing import Dict, List, Optional

from src.entities import User, Subscription, Content


class AuthenticationService:
    def __init__(self) -> None:
        self._sessions: Dict[int, bool] = {}

    def authenticate(self, user_id: int, password: str, stored_hash: str) -> bool:
        ok = password == stored_hash  # placeholder check, real hashing out of scope
        self._sessions[user_id] = ok
        return ok

    def is_authenticated(self, user_id: int) -> bool:
        return self._sessions.get(user_id, False)


class RegistrationService:
    def __init__(self) -> None:
        self._users: Dict[int, User] = {}

    def register(self, user: User) -> User:
        self._users[user.user_id] = user
        return user

    def get_user(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)


class SubscriptionService:
    def __init__(self) -> None:
        self._subs: Dict[int, Subscription] = {}

    def add_subscription(self, sub: Subscription) -> None:
        self._subs[sub.user_id] = sub

    def check_subscription(self, user_id: int) -> bool:
        sub = self._subs.get(user_id)
        return sub is not None and sub.status == "active"


class MovieCatalogService:
    def __init__(self) -> None:
        self._catalog: Dict[int, Content] = {}

    def add_content(self, content: Content) -> None:
        self._catalog[content.content_id] = content

    def get_movie(self, content_id: int) -> Optional[Content]:
        return self._catalog.get(content_id)

    def search(self, keyword: str) -> List[Content]:
        keyword = keyword.lower()
        return [c for c in self._catalog.values() if keyword in c.title.lower()]


class PaymentService:
    def process_payment(self, amount: float, method: str) -> bool:
        return amount > 0 and method in {"card", "wallet", "gateway"}


class StreamingService:
    def start_stream(self, content: Content):
        from src.patterns.decorator import BasicVideoStream

        return BasicVideoStream(content.title)
