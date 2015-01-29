# Job
These are the scripts that you actually need to run in order to run your giant 
Hadoop job (or step for EMR).


- `generate.py`: Generates the json config file for the aws cli
- `yhat-batch.py`: Mapper code that executes on EMR
- `run.sh`: Invokes AWS CLI to create job


```
$ ./run.sh <cluster-id>
$ ./run.sh j-1BDGS72EJF
```
