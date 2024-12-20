import uuid
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Features:
    age: int
    experience_level: str
    hackathons_done: int
    programming_skills: Dict[str, int]
    preferred_team_size: int
    preferred_languages: List[str]
    preferred_role: str
    disponiblity_days: Dict[str, bool]
    university: str
    friend_registration: List[str]

