#!/usr/bin/python
import csv
import StringIO
import sys
import re
import urllib
import urllib2
import json
import base64

YHAT_USERNAME = ""
YHAT_APIKEY = ""

def post(data):
    url = "http://cloud.yhathq.com/%s/models/ProductClassifier/?hadoop=true" % YHAT_USERNAME
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    auth = '%s:%s' % (YHAT_USERNAME, YHAT_APIKEY)
    base64string = base64.encodestring(auth).replace('\n', '')
    req.add_header("Authorization", "Basic %s" % base64string)
    try:
        data = json.dumps(data)
    except Exception, e:
        return
    response = urllib2.urlopen(req, data)
    rsp = response.read()
    try:
        return json.loads(rsp)
    except:
        return

def make_prediction(data):
    data = {"texts": data}
    prediction = post(data)
    if "error" in prediction:
        sys.stderr.write("Could not process row: %s: \n" % (str(prediction['error']), str(data)))
    for result in prediction['result']:
        if result is None:
            sys.stderr.write("Could not process row.\n")
            continue
        safe_text = urllib.quote(result['text'])
        print json.dumps(result)
 
def main(argv):
    payload = []
    for line in sys.stdin:
        f = StringIO.StringIO(line)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data = { "text": row[0] }
            payload.append(data)

            if len(payload) >= 10000:
                make_prediction(payload)
                payload = []
    if len(payload) > 0:
        make_prediction(payload)


if __name__ == "__main__":
    main(sys.argv)
