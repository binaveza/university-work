#!/bin/bash

if [[ -z $1 ]]; then
  echo "Ошибка: Необходимо указать путь к файлу."
  exit 1
fi

if [[ ! -f $1 ]]; then
  echo "Ошибка: Файл '$1' не существует."
  exit 1
fi

while IFS= read -r line; do
  echo "$line"
done < "$1"