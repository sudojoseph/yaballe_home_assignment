import requests
from flask import Blueprint, request
from db.product_db import fetch_product_from_db, insert_new_product
from utils.utils import stringify_id
from schemas.product_schema import ProductSchema
import os


YABALLE_SERVER_KEY = os.getenv('YABALLE_SERVER_KEY')


product_view_blueprint = Blueprint('product_view_blueprint', __name__)


@product_view_blueprint.route('/', methods=['POST'])
def fetch_product():
    request_data = request.get_json()
    source = request_data['source']
    source_id = str(request_data['source_id'])


    try:
        product = fetch_product_from_db(source, source_id)
    except Exception as error:
        return {'message': 'error fetching product', 'error': str(error), 'status': 500}


    if not product:
        try:
            response = requests.get(f'https://ebazon-prod.herokuapp.com/ybl_assignment/{source}/{source_id}/{YABALLE_SERVER_KEY}').json()
        except Exception as error:
            return {'message': 'error fetching product from yaballe', 'error': str(error), 'status': 500}


        response_object = response['data']
        new_product = {}
        new_product['product_id'] = str(response_object['source_id'])
        new_product['title'] = response_object['title']
        new_product['price'] = response_object['price']
        new_product['source'] = response_object['source'][:-4] if response_object['source'].endswith('.com') else response_object['source']
        product = new_product


        try:
            product = ProductSchema(**product)
        except ValueError as error:
            return {'message': 'validation error', 'error': str(error), 'status': 400}
        

        product = product.dict()


        try:
            insert_new_product(product)
        except Exception as error:
            return {'message': 'error inserting product', 'error': str(error), 'status': 500}


    stringify_id(product)


    return product
    