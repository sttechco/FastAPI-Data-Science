import requests as rq

def test():
    result = rq.post('http://127.0.0.1:8000/users', data={"name": "Marco", "age": 30})
    print(f"==[ result: {result.json()}")

if __name__=="__main__":
    test()