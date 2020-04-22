from dotenv import load_dotenv
from app import app
from bson.objectid import ObjectId
import json
import data

data.DB_URL="mongodb://localhost:27017"


def setup_function():
    data.DATABASE_NAME = "cardpad_test"
    with data.create_connection() as conn:
        conn[data.DATABASE_NAME]['cards'].delete_many({})


def test_add_card():
    response = app.test_client().post('/add-card',json={
        'title':'Hello world',
        'content':'This is a good day to live',
        'tags':'a,b,c'
    })
    assert response.status_code == 200

    response_data = response.get_json()
    

    # test the db
    with data.create_connection() as conn:
        found = conn['cardpad_test']['cards'].find_one({
            '_id':ObjectId(response_data['new_card_id']['$oid'])
        })
        assert found != None
        assert found['title'] == 'Hello world'
        assert found['content'] == 'This is a good day to live'
        assert found['tags'] == 'a,b,c'

def test_find_card():
    fake_user_id = ObjectId()
    data.add_card(fake_user_id, "Mary has a little lamb", "ASD", ['a','b'])
    data.add_card(fake_user_id, "Mary has a little lamb", "ASD", ['a'])

    cards = data.find_card_by_tag(fake_user_id, 'a')
    assert len(list(cards)) == 2

    cards = data.find_card_by_tag(fake_user_id, 'b')
    assert len(list(cards)) == 1