#!/bin/bash
###
### This script manages data between your local directory and the S3 bucket used
### for your EMR job. It's important to note that all of your Python scripts 
### must be on S3 prior to running a job (so if you make changes, they'll need 
### to be pushed before running ./job.run.sh <cluster_id>).
### 

if [[ "$1" == "up" ]]; then
    # we're not going to use `s3cmd sync` to avoid some pitfalls
    # also, we're making out scripts public so they can be used in demos, 
    # `--acl-public` isn't neccessary so you can remove it if you'd like your 
    # scripts/data to remain private
    s3cmd put --acl-public bootstrap/* s3://yhat-hadoop-example/bootstrap/
    s3cmd put --acl-public input/* s3://yhat-hadoop-example/input/
    s3cmd put --acl-public job/* s3://yhat-hadoop-example/job/
    s3cmd put logs/* s3://yhat-hadoop-example/logs/
elif [[ "$1" == "download" ]]; then
    if [[ "$2" == "logs" ]]; then
        s3cmd sync s3://yhat-hadoop-demo/logs/ ./logs
    elif [[ "$2" == "output" ]]; then
        s3cmd sync s3://yhat-hadoop-demo/output/ ./output
    elif [[ "$2" == "all" ]]; then
        s3cmd sync s3://yhat-hadoop-demo/ .
    else
        echo "not a valid second argument"
    fi
else
  echo "sync.sh"
  echo "        up"
  echo "        download logs|output|all"
  echo ""
  grep "^### " "$0" | cut -c 5-
fi
