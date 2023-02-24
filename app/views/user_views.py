from flask import Blueprint, request, jsonify
from db.user_db import fetch_user_by_email, insert_user, fetch_users_favorite_products, append_favorite_products_to_user
from db.db_utils import stringify_id

user_view_blueprint = Blueprint('user_view_blueprint', __name__)

@user_view_blueprint.route('/', methods=['POST'])
def create_user():
    request_data = request.get_json()

    exists = fetch_user_by_email(request_data['email'])
    if exists:
        return jsonify({'error': 'User already exists'})
    
    user_object = {**request_data, 'favorite_products': []}
    insert_user(user_object)
    return {'message': 'User successfully added'}


@user_view_blueprint.route('/<user_email>/favorite/', methods=['POST', 'GET'])
def user_favorite_products(user_email):


    if request.method == 'GET':
        user = fetch_user_by_email(user_email)
        favorite_product_array = user['favorite_products']
        if not favorite_product_array:
            return {'message': 'User has no favorite products'}
        

        favorite_products = fetch_users_favorite_products(favorite_product_array)


        for favorite_product in favorite_products:
            stringify_id(favorite_product)


        return favorite_products
    else:
        request_data = request.get_json()
        products_list = request_data['favorite_products']
        append_favorite_products_to_user(user_email, products_list)
        return {'message': 'success'}
