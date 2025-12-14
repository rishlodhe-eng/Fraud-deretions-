import json
import urllib.request
import urllib.error

URL = 'http://127.0.0.1:8000/transactions/validate'

def post(data):
    req = urllib.request.Request(URL, data=json.dumps(data).encode(), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as r:
            print('STATUS', r.status)
            print(r.read().decode())
    except urllib.error.HTTPError as e:
        print('STATUS', e.code)
        body = e.read().decode()
        print(body)

print('--- Empty body ---')
post({})

print('\n--- Negative amount ---')
post({
    'transaction_id': 'txn_1',
    'user_id': 'user_1',
    'amount': -10,
    'currency': 'USD',
    'merchant': 'Shop'
})

print('\n--- Valid transaction ---')
post({
    'transaction_id': 'txn_2',
    'user_id': 'user_2',
    'amount': 100.5,
    'currency': 'USD',
    'merchant': 'Shop'
})
