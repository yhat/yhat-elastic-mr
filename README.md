# Yhat EMR Demo
Using Yhat with Hadoop streaming

This example hooks up Yhat with the Hadoop streaming API. We're going to feed 
CPG product names into our pipeline and score/tag records using a Product 
Classification model on Yhat (our mapper). We don't have a reducer step, so data
is just output straight from the `yhat-batch.py` job to our S3 bucket as 
line-delimited JSON that looks like this:

```
{"text": "Aranciata Orange", "guesses": {"Frozen Foods": 0.30769230769230771, "Hair Shampoo": 0, "Pet Care": 0, "Soda": 0.69230769230769229}}
```

Results can be downloaded using the `sync.sh` script.

### Requirements

- `awscli`: `pip install awscli`
- `scikit-learn` (to build the model)
- `pandas` (to build the model)
- `factual-python-client` (to source data)

### Getting Started

```
# make sure all of your data is uploaded onto S3
# if you're setting things up on your own S3 account, you'll need to
# do a find/replace on "yhat-hadoop-example" with the name of your own
# bucket
$ ./sync.sh up
$ ./spin-up-server.sh
{
      "ClusterId": "j-3UH0PR3KEO157"
}
$ ./job/run.sh j-3UH0PR3KEO157
```
