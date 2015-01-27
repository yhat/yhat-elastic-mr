#!/usr/bin/env python
###
### Simple python script to generate the required .json file for running "steps"
### or jobs, on EMR.
###

import uuid


# we're going to generate a UUID for each job. that way every job
# will have it's own output directory on S3
print """[
  {
    "Name": "Yhat Product Classifier CSV Streaming Step",
    "Args": [
        "-files", "s3://yhat-hadoop-example/job/yhat-batch.py",
        "-mapper","yhat-batch.py",
        "-reducer","NONE",
        "-input","s3://yhat-hadoop-example/input/",
        "-output","s3://yhat-hadoop-example/output/%s/"
    ],
    "ActionOnFailure": "CONTINUE",
    "Type": "STREAMING"
  }
]""" % str(uuid.uuid4())
