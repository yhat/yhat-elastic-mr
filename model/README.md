# Product Classification Model
Please note that this model isn't very good, it's just for demo purposes ;)

### Getting more data (optional)
```
# https://www.factual.com/keys
$ export FACTUAL_KEY="" # your key
$ export FACTUAL_SECRET="" # your secret
$ python get_data.py
```

### Building and deploying the model

```
$ pip install scikit-learn==0.14.1
$ pip install pandas==0.14.1
$ pip install -U yhat
$ python classifier.py
```
