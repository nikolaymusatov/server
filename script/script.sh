#!/bin/bash
code=$(curl -s localhost:2000 -o /dev/null -w '%{response_code}')
while [ 1 = 1 ]
do
code=$(curl -s localhost:2000 -o /dev/null -w '%{response_code}')
if [ $code = 200 ]; then
    curl --data "test" localhost:2000
    echo
    sleep 10
else
    break
fi
done