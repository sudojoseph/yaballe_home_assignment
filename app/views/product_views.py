import requests
from flask import Blueprint, request
from db.product_db import fetch_product_from_db, insert_new_product
from db.db_utils import stringify_id
import os


YABALLE_SERVER_KEY = os.getenv('YABALLE_SERVER_KEY')


product_view_blueprint = Blueprint('product_view_blueprint', __name__)


@product_view_blueprint.route('/', methods=['POST'])
def fetch_product():
    request_data = request.get_json()
    source = request_data['source']
    source_id = str(request_data['source_id'])


    product = fetch_product_from_db(source, source_id)


    if not product:
        response = requests.get(f'https://ebazon-prod.herokuapp.com/ybl_assignment/{source}/{source_id}/{YABALLE_SERVER_KEY}').json()
        response_object = response['data']
        new_product = {}
        new_product['product_id'] = str(response_object['source_id'])
        new_product['title'] = response_object['title']
        new_product['price'] = response_object['price']
        new_product['source'] = response_object['source']
        product = new_product
        insert_new_product(product)


    stringify_id(product)


    return product
    