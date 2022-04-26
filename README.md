# lung-segmentation
## Основное описание
Данный проект является вариантом решения задачи [Lung Nodule Segmentation on LUNA](https://paperswithcode.com/sota/lung-nodule-segmentation-on-luna).  
[Bi-Directional ConvLSTM U-Net](https://paperswithcode.com/paper/bi-directional-convlstm-u-net-with-densley) на сегодняшний момент является наиболее оптимальным.  
В качестве основы для проекта был взят [BCDU-Net](https://github.com/rezazad68/BCDU-Net).  

## Запуск программы  
1. Запустить 

Решение для работы использует уже обученую модель [NYU Depth V2](https://drive.google.com/file/d/19dfvGvDfCRYaqxVKypp1fRHwK7XtSjVu/view?usp=sharing).

## Требования

- Ubuntu (Вероятно, под WSL тоже заработает)
- python 3
- Docker без *sudo*

## Запуск

### Простой запуск примера:

```
python3 run.py
```

Запустится докер с обученной моделью. Построится коллаж из тестовых картинок после обработки. Результат будет записан в `test.png` в рабочей директории.

### Дополнительные возможности:

Модель поддерживает картинки в формате `png` разрешением 640х480 с тремя каналами 

Скрипт `run.py` имеет два аргумета `--tests` и `--out`. В них можно опционально передать директорию с тестовыми картинками и жиректорию для записи результата.

Запуск:

```
python3 run.py --tests <path-to-tests> --out <path-to-out>
```

## Сборка образа

Для сборки образа необходиа обученная модель [NYU Depth V2](https://drive.google.com/file/d/19dfvGvDfCRYaqxVKypp1fRHwK7XtSjVu/view?usp=sharing).

Её необходимо скачать и положить в директорию с `Dockerfile`, а затем запустить сборку образа:

```
docker build .
```




## Основные требования  
- 
- Python
- 
