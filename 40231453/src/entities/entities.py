"""
Entity classes corresponding to the ER Diagram designed in the theoretical
section (User, Profile, Subscription, Plan, Payment, Content, Episode,
Genre, CastMember, WatchHistory, Review, Device).

These are plain data classes; persistence is out of scope for the exam.
"""

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List, Optional


@dataclass
class User:
    user_id: int
    full_name: str
    email: str
    password_hash: str
    phone: str
    join_date: date


@dataclass
class Profile:
    profile_id: int
    user_id: int
    profile_name: str
    avatar_url: str
    kids_mode: bool = False


@dataclass
class Device:
    device_id: int
    user_id: int
    device_type: str  # mobile | laptop | smart_tv
    device_token: str
    last_login: Optional[datetime] = None


@dataclass
class Plan:
    plan_id: int
    plan_name: str
    price: float
    max_devices: int
    max_quality: str


@dataclass
class Subscription:
    sub_id: int
    user_id: int
    plan_id: int
    start_date: date
    end_date: date
    status: str = "active"


@dataclass
class Payment:
    payment_id: int
    sub_id: int
    amount: float
    paid_date: date
    method: str
    status: str = "paid"


@dataclass
class Content:
    content_id: int
    title: str
    type: str  # movie | series
    release_year: int
    description: str = ""
    poster_url: str = ""
    genre_ids: List[int] = field(default_factory=list)
    cast_ids: List[int] = field(default_factory=list)


@dataclass
class Episode:
    episode_id: int
    content_id: int
    season_num: int
    episode_num: int
    duration_sec: int
    video_url: str


@dataclass
class Genre:
    genre_id: int
    genre_name: str


@dataclass
class CastMember:
    cast_id: int
    name: str
    bio: str = ""


@dataclass
class WatchHistory:
    history_id: int
    profile_id: int
    content_id: int
    last_position_sec: int = 0
    last_watched: Optional[datetime] = None


@dataclass
class Review:
    review_id: int
    profile_id: int
    content_id: int
    rating: int
    comment: str = ""
    review_date: Optional[date] = None
