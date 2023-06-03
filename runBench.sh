# args: $1: port $2: endpoint $3: fout 
nohup python3 bench.py $1 $3 &
K6_CALLEE_PORT=$1 K6_CALLEE_ENDPOINT=$2 k6 run script.js 