import json
import os

FILE_NAME = "analytics.json"


def load_analytics():

    if not os.path.exists(FILE_NAME):

        data = {
            "tutor": 0,
            "quiz": 0,
            "roadmap": 0,
            "skill_gap": 0,
            "interview": 0
        }

        with open(FILE_NAME, "w") as f:
            json.dump(data, f)

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def increment_counter(feature):

    data = load_analytics()

    data[feature] += 1

    with open(FILE_NAME, "w") as f:
        json.dump(data, f)


def get_analytics():

    return load_analytics()