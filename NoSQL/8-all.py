#!/usr/bin/env python3
"""returns all values in a collection"""


def list_all(mongo_collection):
    """returns all values in a collection"""
    return mongo_collection.find()
