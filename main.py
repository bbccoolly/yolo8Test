from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO('yolov8n.yaml')

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')

# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.train(data='coco128.yaml', epochs=1)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
results = model('https://ultralytics.com/images/zidane.jpg')

# Export the model to ONNX format
success = model.export(format='onnx')  # 这里省略了path参数
# if success:
#     import shutil
#     shutil.move('path_to_your_onnx_file/bus_test.onnx', 'D:/workplace-python/yolo8Lcz/yolo8Lcz/modelLcz/bus_test.onnx')

