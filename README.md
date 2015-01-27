# Yhat EMR Demo
Using Yhat with Hadoop streaming


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
