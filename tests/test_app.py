import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'ACEest Fitness & Gym Tracker' in response.data

def test_add_workout(client):
    response = client.post('/add', data={
        'exercise': 'Running',
        'duration': '30',
        'category': 'Workout'
    })
    assert response.status_code == 302  # Redirect after successful post
    assert b'Running added to Workout category successfully!' in response.data

def test_view_summary(client):
    response = client.get('/summary')
    assert response.status_code == 200
    assert b'Session Summary' in response.data

def test_invalid_duration(client):
    response = client.post('/add', data={
        'exercise': 'Cycling',
        'duration': 'invalid',
        'category': 'Workout'
    })
    assert response.status_code == 200
    assert b'Duration must be a number.' in response.data

def test_empty_workout(client):
    response = client.post('/add', data={
        'exercise': '',
        'duration': '',
        'category': 'Workout'
    })
    assert response.status_code == 200
    assert b'Please enter both exercise and duration.' in response.data