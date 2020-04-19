import requests, json

from util.nzutil_url import join_url_fragements


SUPPLIER_TO_DELETE = '' # Supplier whose product will be deleted


AUTHORIZATION    = 'Basic N21jNGZyN2tqdzh6cnE3a2loYmZpYTV5cThkOHJxNjU6dDg5czk1amJqbm1lZmQyZHhzNDN1bmwxcjJwNnp1ZjA='

IV_TENANT_ID    = 'us-4474f893'

S4S_URL          = "https://s4s-supplement-service-dev.mybluemix.net/s4s"



OPERATION_URL_LIST   = 'suppliers/products'

OPERATION_URL_DELETE   = 'products'

headers = {
    'Authorization': AUTHORIZATION,
    'Content-Type': 'application/json'
  }

urlListProduct = join_url_fragements(S4S_URL, IV_TENANT_ID, OPERATION_URL_LIST)

supplier_list = json.loads("{\"supplier_ids\":[]}")

supplier_list["supplier_ids"].append(SUPPLIER_TO_DELETE)

response = requests.request("POST", urlListProduct, headers=headers, data=json.dumps(supplier_list))

print ("response: ", response.text)

itemlist = json.loads(response.text)

for item in itemlist:
  item_id = item["item_id"]

  print ("*** Deleteing ", item_id, " ************************")
  url = join_url_fragements(S4S_URL, IV_TENANT_ID, OPERATION_URL_DELETE, item_id)

  payload = {}

  response = requests.request("DELETE", url, headers=headers, data = payload)

  print(response.text.encode('utf8'))


# for item in items_to_delete:
