#!/bin/bash

echo "Начало работы скрипта..."

echo "Создаю новую директорию 'new_directory'."
mkdir new_directory

sleep 2

echo "Перейду в созданную директорию."
cd new_directory

sleep 2

echo "Создаю три файла: file1.txt, file2.txt, file3.txt."
touch file1.txt
touch file2.txt
touch file3.txt

sleep 2

echo "Удаляю созданные файлы."
rm file1.txt file2.txt file3.txt

sleep 2

echo "Возвращаюсь в исходный каталог."
cd ..

echo "Удаляю директорию 'new_directory'."
rmdir new_directory
