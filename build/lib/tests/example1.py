import requests

BASEURL = 'http://localhost'


def example1():

    r = requests.get(BASEURL + 'get')
    if r.status_code == 200:
        response_data = r.json()
        return r.status_code, response_data["url"]
    else:
        return r.status_code, ''

if __name__ == '__main__':
    status_code, url = example1()
    print(f'HTTP Response... Status Code: {status_code}, URL: {url}')