#!/bin/bash

working_dir="$PWD"

echo "Шаг 1: Создание директории для файлов..."
mkdir "$working_dir/temp_dir"

sleep 1

echo "Шаг 2: Создание файлов file1, file2, file3..."
touch "$working_dir/temp_dir/file1.txt" "$working_dir/temp_dir/file2.txt" "$working_dir/temp_dir/file3.txt"

sleep 1

echo "Шаг 3: Создание директории для копий файлов..."
mkdir "$working_dir/backup_dir"

sleep 1

echo "Шаг 4: Получение текущей даты..."
current_date=$(date +"%Y-%m-%d")

sleep 1

echo "Шаг 5: Создание файлов с датой в названии..."
for file in "$working_dir/temp_dir/"*; do
  filename=$(basename "$file")
  new_filename="${filename}_${current_date}"
  cp "$file" "$working_dir/backup_dir/${new_filename}"
done

sleep 1

echo "Завершено! Файлы скопированы в backup_dir с датами."