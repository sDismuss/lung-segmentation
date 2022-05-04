# lung-segmentation
## Основное описание
Данный проект является вариантом решения задачи [Lung Nodule Segmentation on LUNA](https://paperswithcode.com/sota/lung-nodule-segmentation-on-luna).  
[Bi-Directional ConvLSTM U-Net](https://paperswithcode.com/paper/bi-directional-convlstm-u-net-with-densley) на сегодняшний момент является наиболее оптимальным.  
В качестве основы для проекта был взят [BCDU-Net](https://github.com/rezazad68/BCDU-Net).
![Пример работы](sample_results.png "Пример работы")

## Предварительная подготовка
- Git Bash

## Основная установка
Скачать проект с GitHub
```
git clone https://github.com/sDismuss/lung-segmentation.git
```
*Примечание:* Рекомендуется воспользоваться консолью Git Bash  
  
Следующий шаг заключается в том, чтобы из консоли построить проект
```
docker build -t lung-seg .
docker run -it --name lung-container lung-seg
```
  
## Основные команды
1. Подготовка изображений  
Скачать изображения можно отсюда: [3d_images](https://www.kaggle.com/datasets/kmader/finding-lungs-in-ct-data?select=3d_images.zip) (3d изображений достаточно).  
Архив нужно распаковать в папку input рядом с example.  
  
Следующая команда подготовит изображения  
```
python Prepare_data.py
```
  
2. Тренировка модели  
Эту часть можно пропустить, скачав следующий файл: [weight](https://drive.google.com/open?id=1pHOntUOdqd0MSz4cHUOHi2Ssn3KBH-fU)  
Данный файл нужно поместить в папку processed_data (создайте, если он отсутствует
  
При желании можно запустить следующую команду, чтобы положить тот же результат  
```
python train_lung.py
```
  
3. Проверка модели
Для получения результатов тренировки модели запустите следующую команду
```
python evaluate_perfomance.py
```
  
## Некоторые примечания
Из 4 вариантов 3d_images можно также взять только одну из них. Этого достаточно, чтобы получить оптимальные результаты.  
В качестве проверки было сравнение между 15 и 154 изображениями. Разница в 0.001.

