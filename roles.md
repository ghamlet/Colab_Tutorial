1. Матвей: оставляем width = 416  height = 416 и count_images = 452  (yes)
базовый датасет 0.26 на платформе    


2. Саня: width = 416  height = 416  count_images = 5_000


3. Егор: width = 608  height = 608  count_images = 452
базовый датасет 0.66 на платформе





Чтобы сделать обнаруженные ограниченные рамки более точными, можно добавить 3 параметра ignore_thresh = .9 iou_normalizer=0.5 iou_loss=giou к каждому [yolo]слою и обучить его. Это увеличит mAP@0,9, но уменьшит mAP@0,5.

Только если вы эксперт в нейронных сетях обнаружения - пересчитайте якоря для вашего набора данных для widthи height из cfg-файла: darknet.exe detector calc_anchors data/obj.data -num_of_clusters 9 -width 416 -height 416 затем установите те же 9 anchorsв каждом из 3 [yolo]-слоев в вашем cfg-файле. Но вы должны изменить индексы якорей masks=для каждого [yolo]-слоя, так что для YOLOv4 1-й-[yolo]-слой имеет якоря меньше 30x30, 2-й - меньше 60x60, 3-й - оставшиеся, и наоборот для YOLOv3. Также вы должны изменить filters=(classes + 5)*<number of mask>перед каждым [yolo]-слоем. Если многие из рассчитанных якорей не помещаются под соответствующие слои - тогда просто попробуйте использовать все якоря по умолчанию



https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny-3l.cfg



1. использовать кфг -файл с 3 [yolo]-слоями (я)

1. обучить на большом количестве фотографий с 416 на 416 или 608 на 608
2. строчку change_in_file(config_file, "random=0", "random=1") закоментить или оставить
3.  3 параметра ignore_thresh = .9 iou_normalizer=0.5   iou_loss=giou к ка%cd ..
from google.colab import drive

import os
drive.mount('/content/gdrive')
!ln -s /content/gdrive/MyDrive/ /mydrive # это команда создать ссылку, так что длинный путь /content/gdrive/MyDrive/ будет равнозначен короткому и удобному /mydrive

%cd /mydrive


! git clone https://github.com/ghamlet/Colab_Tutorial.gitждому [yolo]слою и обучить его.
4.   max_batches = 9000  всем




### Обучаю 

второй акк

DATASET_FOLDER = "valid"       # название архива и одноименной папки в нём где хранятся наши фотографии и аннотации к ним

count_images = 2_000           #  количество фотографий которое мы хотим добавить (если в датасете меньше фотографий, то используется то количество которое имеется)

classes = ["drone"]            # список классов

width = 608                 # ширина и высота изображения (darknet автоматически преобразует фотографии в нужный размер)
height = 608

num_of_clusters = 9    # defolt 6
max_batches = 9000    # or None
improve_find_bounding_boxes = True
random = False






-------------

DIR_NAME = "Find_drones"        # имя папки как она называется на диске
DATASET_FOLDER = "train"       # название архива и одноименной папки в нём где хранятся наши фотографии и аннотации к ним

count_images = 10_000           #  количество фотографий которое мы хотим добавить (если в датасете меньше фотографий, то используется то количество которое имеется)

classes = ["drone"]            # список классов

width = 608                # ширина и высота изображения (darknet автоматически преобразует фотографии в нужный размер)
height = 608


num_of_clusters = 9    # defolt 6
max_batches = 9000    # or None
improve_find_bounding_boxes = True
random = False
