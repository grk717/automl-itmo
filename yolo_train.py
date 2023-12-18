from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO('yolov8n-cls.pt')
    results = model.train(data=r'./data/icebergs/yolo_dataset/', epochs=50, imgsz=64, project='icebergs_yolo', workers=1)