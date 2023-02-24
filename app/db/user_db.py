from .db_init import user_collection, products_collection


def fetch_user_by_email(user_email):
    return user_collection.find_one({'email': user_email})


def insert_user(user_object):
    return user_collection.insert_one(user_object)


def fetch_users_favorite_products(pruducts_array):
    query = {'$or': [{'product_id': p['product_id'], 'source': p['source']} for p in pruducts_array]}
    favorite_products = list(products_collection.find(query))
    return favorite_products


def append_favorite_products_to_user(email, products_list):
    return user_collection.update_one({'email': email}, {'$addToSet': {'favorite_products': {'$each': products_list}}})
