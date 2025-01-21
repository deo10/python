import  requests

my_request = requests.get('https://www.python.org')

print(my_request)
# <Response [200]>

print(my_request.text)
# html code of the page
print(my_request.status_code)
# 200

