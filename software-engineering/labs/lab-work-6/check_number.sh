#!/bin/bash

echo "Введите число: " 
read number

if ! [[ "$number" =~ ^-?[0-9]+$ ]]; then
    echo "Ошибка: Это не число!"
    exit 1
fi

if [ "$number" -gt 0 ]; then
    echo "Это число положительное!"
elif [ "$number" -lt 0 ]; then
    echo "Это число отрицательное!"
else
    echo "Вы ввели ноль."
fi
