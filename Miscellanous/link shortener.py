from pyshorteners import Shortener

url = input('Enter your url : ')

short_url = Shortener().tinyurl.short(url)

print(f'Your shortened url is {short_url}')
