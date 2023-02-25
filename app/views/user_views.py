from flask import Blueprint, request, jsonify
from db.user_db import fetch_user_by_email, insert_user, fetch_users_favorite_products, append_favorite_products_to_user
from utils.utils import stringify_id
from schemas.user_schema import UserSchema, UserFavoriteProductSchema

user_view_blueprint = Blueprint('user_view_blueprint', __name__)

@user_view_blueprint.route('/', methods=['POST'])
def create_user():
    request_data = request.get_json()

    try:
        exists = fetch_user_by_email(request_data['email'])
    except Exception as error:
        return {'message': 'Not able to check if user exists', 'error': str(error), 'status': 500}
    
    
    if exists:
        return jsonify({'error': 'User already exists'})
    

    new_user_data = {**request_data, 'favorite_products': []}


    try:
        user = UserSchema(**new_user_data)
    except ValueError as error:
        return {'message': 'validation error', 'error': str(error), 'status': 400}


    try:
        insert_user(user.dict())
    except Exception as error:
        return {'message': 'Not able to add user to database', 'error': str(error), 'status': 500}

    
    return {'message': 'User successfully added', 'status': 201}


@user_view_blueprint.route('/<user_email>/favorite/', methods=['POST', 'GET'])
def user_favorite_products(user_email):


    if request.method == 'GET':
        user = fetch_user_by_email(user_email)
        favorite_product_array = user['favorite_products']
        if not favorite_product_array:
            return {'message': 'User has no favorite products'}
        
        try:
            favorite_products = fetch_users_favorite_products(favorite_product_array)
        except Exception as error:
            return {'message': 'Not able to fetch favorite products', 'error': str(error), 'status': 500}

        for favorite_product in favorite_products:
            stringify_id(favorite_product)


        return favorite_products
    else:
        request_data = request.get_json()
        products_list = request_data['favorite_products']


        for product in products_list:
            try:
                product = UserFavoriteProductSchema(**product)
            except ValueError as error:
                return {'message': 'validation error', 'error': str(error), 'status': 400}
            

        append_favorite_products_to_user(user_email, products_list)
        return {'message': 'success'}
