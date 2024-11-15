#!/bin/bash

if [ -z "$1" ]; then
  echo "Пожалуйста, введите число."
  exit 1
fi

number=$1

if ! [[ "$number" =~ ^-?[0-9]+$ ]]; then
  echo "Введите действительное целое число."
  exit 1
fi

if [ "$number" -ge 0 ]; then
  for (( i=$number; i>=0; i-- )); do
    echo "$i"
    sleep 1
  done
else
  for (( i=$number; i<=0; i++ )); do
    echo "$i"
    sleep 1
  done
fi
