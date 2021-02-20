#!/bin/bash -x

base_name=$1


conf_dir="conf"
conf_file="conf_$1.yml"

db_dir="data"
db_file="conf_$1.sqlite"

trades_dir="data"
trades_file="trades_conf_$1.csv"

logs_dir="logs"
logs_file="logs_conf_$1.log"

date_dir="snapshots/$base_name/$(date +"%Y-%m-%d_%H:%M:%S")"

mkdir -p $date_dir

cp $conf_dir/$conf_file $date_dir
cp $db_dir/$db_file $date_dir
cp $trades_dir/$trades_file $date_dir
cp $logs_dir/$logs_file $date_dir

