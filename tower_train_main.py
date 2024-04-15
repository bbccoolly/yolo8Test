from ultralytics import YOLO

# Create a new YOLO model using your custom configuration
# model = YOLO('D:\\workplace-python\\yolo8Lcz\\yolo8Lcz\\ultralytics\\dataset\\data.yaml', task='detect')  # 如果您有自定义模型的配置

# Load a pretrained YOLO model (recommended for training with a custom dataset)
model = YOLO('yolov8n.pt')  # 您可以使用官方预训练模型作为起点

# Train the model using your 'data.yaml'
results = model.train(data='D:\\workplace-python\\yolo8Lcz\\yolo8Lcz\\ultralytics\\dataset\\data.yaml', epochs=10,
                      imgsz=640)  # 使用您的data.yaml文件

# Evaluate the model's performance on the validation set
results = model.val(data='D:\\workplace-python\\yolo8Lcz\\yolo8Lcz\\ultralytics\\dataset\\data.yaml')

# Perform object detection on an image using the trained model
results = model('D:\\workplace-python\\yolo8Lcz\\yolo8Lcz\\ultralytics\\dataset\\test\\test1.JPG')  # 使用您的图片路径

# Export the trained model to ONNX format
success = model.export(format='onnx')

# 注意：请将'your_custom_model.yaml', 'data.yaml', 'path_to_your_image.jpg', 和
# 'path_where_to_save/exported_model.onnx' 替换为实际的文件或路径名。
