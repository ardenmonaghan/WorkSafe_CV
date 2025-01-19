import os
from ultralytics import YOLO


# class YOLOModel:
#     def __init__(self, model_path):
#         self.model_path = model_path
#         self.model = torch.hub.load(
#             "ultralytics/yolov5", 'custom', path=self.model_path, source="github")


if __name__ == "__main__":
    # print(os.getcwd())
    # model = YOLOModel("../testing_yolo/runs/detect/train4/weights/best.pt")
    # result = model("../images/image1.jpg")
    # result[0].show()
    model = YOLO('../testing_yolo/runs/detect/train4/weights/best.pt')
    print(model)
    result = model("../testing_yolo/images/image1.jpg")
    result[0].show()
