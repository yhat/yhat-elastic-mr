#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

CLUSTER_ID="$1"

if [ -z "${CLUSTER_ID}" ]; then
  echo "Please specify a CLUSTER_ID"
  exit 1
fi

${DIR}/generate.py > job.json
echo "Kicking off job on CLUSTER_ID: ${CLUSTER_ID}"
cat job.json

aws emr add-steps --cluster-id ${CLUSTER_ID} --steps file://./job.json
rm job.json
