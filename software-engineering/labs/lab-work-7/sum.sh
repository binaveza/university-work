!/bin/bash

if [[ $# -ne 2 ]]; then
  echo "Ошибка"
  exit 1
fi

num1=$1
num2=$2

result=$(( num1 + num2 ))

echo "$num1 + $num2 = $result"