from flask import Flask
from views.user_views import user_view_blueprint
from views.product_views import product_view_blueprint

app = Flask(__name__)

app.register_blueprint(user_view_blueprint, url_prefix='/user')
app.register_blueprint(product_view_blueprint, url_prefix='/product')

if __name__ == '__main__':
    app.run('0.0.0.0', '5000')