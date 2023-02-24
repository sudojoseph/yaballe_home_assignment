from .db_init import products_collection


def fetch_product_from_db(source, source_id):
    return products_collection.find_one({'source': f'{source}.com', 'product_id': source_id})


def insert_new_product(product_object):
    return products_collection.insert_one(product_object)