**First Run**
Model used yolov8n.pt *n stands for nano*
parameters: `yolo train model=yolov8n.pt data=dataset/data.yaml epochs=10 imgsz=640`
results: ![[Pasted image 20251230223004.png]]
![[Pasted image 20251230223019.png]]
**Second run**
After doing research I realized I should be using the latest model YOLOv11

parameters: `yolo train model=yolov11n.pt data=dataset/data.yaml epochs=50 imgsz=640 patience=5 batch=-1 cache=True device=0`

patience parameter stopped training at 22 epochs
![[Pasted image 20260102075401.png]]
![[Pasted image 20260102075343.png]]

**third run** 
I'm now going to try the standard epochs of 300, I've also read in github forums that the patience is default to 50, meaning my 5 patience was way too strict. New patience of 50(15%-20%) of total epochs. I'm also decreasing the image size to increase the batch size within my 3gb GPU.
parameter: `yolo train model=runs/detect/train6/weights/last.pt data=dataset/data.yaml epochs=300 imgsz=540 patience=50 batch=-1 cache=True device=0`
![[Pasted image 20260102221410.png]]
![[Pasted image 20260102221421.png]]
This run was a flop! it only improved after one epoch :(. And the confusion matrix has gotten worse since run 3
**Fourth run**
I've been using images that resemble my chess set off of roboflow, but I now added 21 of my own annotated images of my actual chess set and uploaded the data. I'm going back to my run 2 model to train and I'm going to also lower the image size to fit more. 
parameters: `yolo train model=runs/detect/train6/weights/best.pt data=dataset/data.yaml epochs=300 imgsz=416 patience=50 batch=-1 cache=True device=0`

----------------------------------------------
Jump: 2026/07/06

**Fifth run**
