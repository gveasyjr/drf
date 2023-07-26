import requests




endpoint = 'https://www.httpbin.org/status/200/'
endpoint = 'https://www.httpbin.org/anything'
endpoint = 'https://www.httpbin.org/'
endpoint = 'https://www.httpbin.org/anything'

get_response = requests.get(endpoint)
print(get_response.text) 