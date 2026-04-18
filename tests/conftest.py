import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(autouse=True)
def reset_activities():
    original_activities = copy.deepcopy(activities)
    try:
        yield
    finally:
        activities.clear()
        activities.update(original_activities)


@pytest.fixture
def client():
    return TestClient(app)
