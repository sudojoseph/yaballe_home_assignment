# Yaballe

## Installation

To get started with this project, you will need to perform the following steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment: python3 -m venv env
4. Activate the virtual environment: source env/bin/activate
5. Install the required dependencies: pip install -r requirements.txt
6. Navigate to the /app directory:
7. Run: python3 app.py

## Usage

To use this project, you will need to set two environment variables:

```bash
export YABALLE_SERVER_KEY=<YABBALE_SERVER_KEY>
export MONGO_DB_PASSWORD_YABALLE=<MONGO_DB_PASSWORD_YABALLE>
```

### Add a Product

To add a product, create a **POST** request with the following endpoint:

```bash
http://127.0.0.1:5000/products/

```

Use this JSON object:

```javascript

{
    "source_id": "B07PXGQC1Q",
    "source": "amazon"
}

```

### Create a User

To create a user, make a **POST** request to:

```bash
http://127.0.0.1:5000/user

```

with the following JSON object:

```javascript

{
	"first_name": "Fred",
	"last_name": "Flinstone",
	"email": "fred@flinstone.com"
}

```

### Update a User's Favorite Products

To update a user's favorite products, you need to make a **PUT** request with the following URL:

```bash
http://127.0.0.1:5000/user/<users_email>/favorite

```
Use the following JSON object:

```javascript

{
	"favorite_products": [
		{
			"product_id": "B07J34ZVRT",
			"source": "amazon"
		},
		{
			"product_id": "485666578",
			"source": "walmart"
		}
	]
}

```

### Get a User's Favorite Products

To get all the user's favorite products, make a **GET** request with the following URL:

```bash
http://127.0.0.1:5000/user/<users_email>/favorite

```

***Just a small note: if a user adds a product to their favorites but the product is not currently saved in MongoDB, it won't show up in the GET request.*** 