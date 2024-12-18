import cv2
import os

current_directory = os.path.dirname(os.path.abspath(__file__))


def load_models():
    print("LOAD models")

    ### Напоминание, что в архив для ответа на платформе нало скидывать файлы, а не папку


    
    cfg_file = [f for f in os.listdir(current_directory) if f.endswith(".cfg")][0]
    weights_file = [f for f in os.listdir(current_directory) if f.endswith(".weights")][0]


    config_path = f"{current_directory}/{cfg_file}"  
    weights_path = f"{current_directory}/{weights_file}"





    net = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    yolo_model = cv2.dnn.DetectionModel(net)
    yolo_model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

    models = [yolo_model]
    return models


def detect_drone(image, models):
    model = models[0]
    drones = []

    class_ids, scores, boxes = model.detect(image, 0.4, 0.1)

    if boxes is not None and len(boxes) > 0:
        for i, box in enumerate(boxes):
            (x, y, w, h) = box
            
            cx = int(x + (w / 2))
            cy = int(y + (h / 2))

            drones.append([i, w * h, [cx, cy, w, h]])
        
        drones = sorted(drones, key=lambda x: x[1], reverse=True)

        need_drone = drones[0][2]
        
        xc_r, yc_r, w_r, h_r = need_drone
        # cv2.rectangle(image, (int(xc_r - w_r//2), int(yc_r - h_r//2)), (int(xc_r +w_r//2), int(yc_r + h_r//2)), (55, 0, 255), 2)
        # cv2.imshow("image", image)
        # cv2.waitKey(0)

        return need_drone
    else:
        # Возвращаем значение по умолчанию, если дрон не обнаружен
        return (100, 100, 100, 100)
