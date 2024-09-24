import os
import plaid
from flask import Flask, request, jsonify
from plaid.model import ItemPublicTokenExchangeRequest
from plaid.api import plaid_api
from plaid.model import TransactionsGetRequest
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


PLAID_CLIENT_ID = os.getenv('PLAID_CLIENT_ID')
PLAID_SECRET = os.getenv('PLAID_SECRET')
PLAID_ENV = os.getenv('PLAID_ENV', 'sandbox')  

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox if PLAID_ENV == 'sandbox' else plaid.Environment.Production,
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET,
    }
)
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

@app.route('/get_access_token', methods=['POST'])
def get_access_token():
    
    public_token = request.json['public_token']
    exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
    response = client.item_public_token_exchange(exchange_request)
    access_token = response['access_token']
    return jsonify({"access_token": access_token})

@app.route('/transactions', methods=['POST'])
def get_transactions():
    
    access_token = request.json['access_token']
    request = TransactionsGetRequest(
        access_token=access_token,
        start_date='2022-01-01',
        end_date='2024-09-23'
    )
    response = client.transactions_get(request)
    transactions = response['transactions']
    return jsonify(transactions)

if __name__ == '__main__':
    app.run(debug=True)
