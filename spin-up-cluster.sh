#!/bin/bash

# this will create a cluster with 3 worker nodes and 1 master
aws emr create-cluster --name "YhatDemoCluster" --ami-version 3.3 \
  --use-default-roles --ec2-attributes KeyName="yhat-dev" \
  --applications Name=Hue Name=Hive Name=Pig \
  --instance-count 4 --instance-type m3.xlarge \
  --log-uri s3://yhat-hadoop-example/logs/ \
  --bootstrap-action Path=s3://yhat-hadoop-example/bootstrap/bootstrap.sh
