import requests
import pandas as pd

r = requests.get('http://jsonplaceholder.typicode.com/posts')
r = r.json()
r0= pd.DataFrame(r)

r = requests.get('http://jsonplaceholder.typicode.com/comments')
r = r.json()
r01= pd.DataFrame(r)

print(r01['postId'].value_counts())

