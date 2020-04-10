from app import app
from bson.objectid import ObjectId
import json
import data

def setup_function():
    data.DATABASE_NAME = "cardpad_test"

def teardown_function():
    with data.create_connection() as conn:
        conn.drop_database('cardpad_test')

def test_add_card():
    response = app.test_client().post('/add-card',json={
        'title':'Hello world',
        'content':'This is a good day to live',
        'tags':'a,b,c'
    })
    assert response.status_code == 200

    response_data = response.get_json()
    print(response_data)


    # test the db
    with data.create_connection() as conn:
        found = conn['cardpad_test']['cards'].find_one({
            '_id':ObjectId(response_data['new_card_id']['$oid'])
        })
        print(found)
        assert found != None
        assert found['title'] == 'Hello world'
        assert found['content'] == 'This is a good day to live'
        assert found['tags'] == 'a,b,c'
