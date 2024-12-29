#!/bin/bash

if [[ $# -ne 3 ]]; then
  echo "Ошибка: Недостаточно аргументов."
  echo "Использование: $0 <исходный_файл> <старое_слово> <новое_слово>"
  exit 1
fi

input_file="$1"
old_word="$2"
new_word="$3"
output_file="${input_file%.*}_output.${input_file##*.}"

if [[ ! -f "$input_file" ]]; then
  echo "Ошибка: Исходный файл '$input_file' не найден."
  exit 1
fi

rm -f "$output_file"

cp "$input_file" "$output_file"

sed -i "s/$old_word/$new_word/g" "$output_file"

echo "Файл '$output_file' с заменённым текстом был успешно создан."