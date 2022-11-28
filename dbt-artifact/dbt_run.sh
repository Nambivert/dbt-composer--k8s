#!/bin/bash
mode=$1
dbt_target=$2
dbt_models=$3
dbt_vars=$4
full_refresh=$5

cd /app/

if [ $mode = "run" ]; then
    echo "dbt Mode is run"
    if [ $full_refresh = "True" ]; then
        echo "Doing a full refresh"
        dbt run --target="$dbt_target" --models="$dbt_models" --vars="$dbt_vars" --profiles-dir=/app/profiles_dir --full-refresh
    else
        echo "Not doing a full refresh"
        dbt run --target="$dbt_target" --models="$dbt_models" --vars="$dbt_vars" --profiles-dir=/app/profiles_dir
    fi
elif [ $mode = "debug" ]; then
    echo "dbt Mode is debug"
    dbt debug --profiles-dir=/app/profiles_dir --target="$dbt_target"
else   
    echo "Incorrect dbt Mode. Nothing to do"
fi

# capture the exit code from the dbt run command
# so that the final exit code form removing virtualenv cmd doesn't get used by KubernetesPodOperator 
exit_code=$?

# rethrowing the exit code to KubernetesPodOperator
exit $exit_code