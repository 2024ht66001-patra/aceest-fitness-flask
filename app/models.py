import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict, Any

DATA_FILE = os.path.join(os.path.dirname(__file__), "workouts.json")
DEFAULT_STORE = {"Warm-up": [], "Workout": [], "Cool-down": []}


@dataclass
class Workout:
    exercise: str
    duration: int
    category: str = "Workout"
    timestamp: str = datetime.utcnow().isoformat() + "Z"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def _ensure_store():
    if not os.path.exists(DATA_FILE):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_STORE, f, indent=2)


def load_workouts() -> Dict[str, list]:
    _ensure_store()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_workouts(data: Dict[str, list]):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_workout(exercise: str, duration: int, category: str = "Workout") -> Dict[str, Any]:
    if not exercise or duration is None:
        raise ValueError("exercise and duration are required")
    try:
        duration = int(duration)
    except (TypeError, ValueError):
        raise ValueError("duration must be an integer")

    store = load_workouts()
    if category not in store:
        raise ValueError("invalid category")

    entry = Workout(exercise=exercise.strip(), duration=duration, category=category).to_dict()
    store[category].append(entry)
    save_workouts(store)
    return entry


def get_all_workouts() -> Dict[str, list]:
    return load_workouts()


def clear_workouts():
    save_workouts(DEFAULT_STORE.copy())