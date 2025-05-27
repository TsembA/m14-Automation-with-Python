import requests

response = requests.get('http://172-236-229-65.ip.linodeusercontent.com:8080/')
if response.status_code == 200:
    print('App running successfully!')
else:
    print('App down. Check logs!')