from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_love():
    text = "I love machine learning!"
    emotion = 'love'

    response = client.post("/emotions/", json={"text": text})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['emotions'][0]['label'] == emotion


def test_predict_anger():
    text = "I hate machine learning!"
    emotion = 'anger'

    response = client.post("/emotions/", json={"text": text})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['emotions'][0]['label'] == emotion


def test_predict_disapproval():
    text = "I don't really care about machine learning. It's okay, but not my kind of thing."
    emotion = 'disapproval'

    response = client.post("/emotions/", json={"text": text})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['emotions'][0]['label'] == emotion


def test_predict_surprise():
    text = "Machine learning always makes leaves me awestruck at how unpredictable it is."
    emotion = 'surprise'

    response = client.post("/emotions/", json={"text": text})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['emotions'][0]['label'] == emotion


def test_predict_fear():
    text = "Every night I think about machine learning, and I am horrified."
    emotion = 'fear'

    response = client.post("/emotions/", json={"text": text})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['emotions'][0]['label'] == emotion


def test_predict_desire():
    text = "I wish machine learning could do my homework for me."
    emotion = 'desire'

    response = client.post("/emotions/", json={"text": text})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['emotions'][0]['label'] == emotion


def test_predict_sadness():
    text = "I cried all night just thinking about machine learning."
    emotion = 'sadness'

    response = client.post("/emotions/", json={"text": text})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['emotions'][0]['label'] == emotion


def test_predict_optimism():
    text = "I am hopeful that machine learning brings about a better world."
    emotion = 'optimism'

    response = client.post("/emotions/", json={"text": text})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['emotions'][0]['label'] == emotion
