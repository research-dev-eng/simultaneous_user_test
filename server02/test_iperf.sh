#!/bin/bash

# Loop through client IDs and corresponding ports
for i in {21..108}; do
  port=$((5200 + i))
  vagrant ssh client$i -c "iperf3 -c 192.168.113.3 -p $port -t 3600 -R" &
  sleep 0.5
done

