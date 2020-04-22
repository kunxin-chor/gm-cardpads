import pymongo
import os

DB_URL = os.environ.get('DB_URL')
DATABASE_NAME = "cardpad"

def create_connection(db_url=""):
    if len(db_url) == 0:
        db_url = DB_URL
    return pymongo.MongoClient(db_url)

def add_card(user_id, title, content, tags):
    conn = create_connection()
    insert_result = conn[DATABASE_NAME]['cards'].insert_one({
        "user_id":user_id,
        "title":title,
        "content":content,
        "tags":tags
    })
    return insert_result.inserted_id

def find_card_by_tag(user_id, tag):
    conn = create_connection
    cards = conn[DATABASE_NAME]["cards"].find({
        "user_id":user_id,
        "tags":tag
    })
    return cards
