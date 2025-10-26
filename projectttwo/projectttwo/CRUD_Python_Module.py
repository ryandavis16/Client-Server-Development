# CRUD_Python_Module.py
# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 
from typing import Any, Dict, List, Optional
from pymongo.errors import PyMongoError


class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'rdavis' 
        PASS = 'Sixj8397' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        try:
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT), tz_aware=True) 
            self.database = self.client['%s' % (DB)] 
            self.collection = self.database['%s' % (COL)] 
        except PyMongoError as e:
            raise RuntimeError(f"Mongo connection failed: {e}") from e

    # Create a method to return the next available record number for use in the create method
    # (Optional/placeholder for your project’s numbering needs.)

    # Complete this create method to implement the C in CRUD. 
    def create(self, data: Optional[Dict[str, Any]]):
        """
        Insert one document into aac.animals.
        Returns True on success, False on failure.
        """
        if not isinstance(data, dict) or not data: 
            return False
        try:
            result = self.collection.insert_one(data)  # data should be dictionary
            return bool(result.acknowledged and result.inserted_id)
        except PyMongoError:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query: Optional[Dict[str, Any]]):
        """
        Query documents with find(). 
        Accepts a dict filter (or None for all docs).
        Returns a list of documents; empty list on error.
        """
        try:
            cursor = self.collection.find(query or {})
            return list(cursor)
        except PyMongoError:
            return []
