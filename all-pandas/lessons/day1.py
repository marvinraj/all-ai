import pandas as pd

data = {
    'apples': [1,2,3,4,5],
    'oranges': [6,7,8,9,10]
}

purchases = pd.DataFrame(data)
print(purchases)