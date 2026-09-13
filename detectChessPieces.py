from ultralytics import YOLO
import cv2

model = YOLO("Modeldata/runs/detect/train8/weights/best.pt")
image = "Modeldata/train/images/IMG_0001_1_jpg.rf.d102cc9deab17f30e3d91de27b72b4f7.jpg"
results = model(image, conf=0.1, iou=0.1)
annotated = results[0].plot()
cv2.namedWindow("Detection", cv2.WINDOW_NORMAL)
cv2.imshow("Detection", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()