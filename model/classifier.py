from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd
import numpy as np
import pprint as pp
import sys


df = pd.read_csv("./products.csv")
idx = np.random.rand(len(df)) > 0.75
train = df[idx==False]
test = df[idx==True]


categories = ['Pet Care', 'Frozen Foods', 'Hair Shampoo', 'Soda']
to_number = lambda x: categories.index(x)
to_label = lambda x: categories[x]

vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')

X_train = vectorizer.fit_transform(train.product_name)
y_train = train.category.apply(lambda x: categories.index(x))

X_test = vectorizer.transform(test.product_name)
y_test = test.category.apply(lambda x: categories.index(x))


clf = KNeighborsClassifier(n_neighbors=13)
clf.fit(X_train, y_train)

preds = clf.predict(X_test)


def make_prediction(texts):
    if len(texts)==0:
        return {}
    if len(texts)==1:
        texts = [texts]
    raw_texts = [row['text'] for row in texts]
    matrix = vectorizer.transform(raw_texts)
    output = clf.predict_proba(matrix)
    results = []

    for text, out in zip(raw_texts, output):
        result = {
            "text": text,
            "guesses": dict(zip(categories, out.tolist()))
        }
        results.append(result)
    return results

### Actually deploying our model to Yhat
from yhat import Yhat, YhatModel

class ProductClassifier(YhatModel):
    def execute(self, data):
        if "texts" not in data:
            return {}
        texts = data["texts"]
        return make_prediction(texts)

# example handling a single record
example = {
    "texts": {
        "text": "Alpo dog food"
    }
}
pp.pprint(ProductClassifier().execute(example))

# example handling multiple records
example = {
    "texts": [
        {"text": "Alpo dog food" },
        {"text": "Diet Coke"}
    ]
}
pp.pprint(ProductClassifier().execute(example))

YHAT_USERNAME = ""
YHAT_APIKEY = ""

try:
    yh = Yhat(YHAT_USERNAME, YHAT_APIKEY, "http://cloud.yhathq.com/")
except:
    print "Please add in your YHAT_USERNAME and YHAT_APIKEY"
    sys.exit(1)

print yh.deploy("ProductClassifier", ProductClassifier, globals())
