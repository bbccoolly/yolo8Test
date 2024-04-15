from PIL import Image
from ultralytics import YOLO

# Load a model
model = YOLO('best.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of images
results = model(['t1.jpg'])  # return a list of Results objects
# results = model.predict('t1.jpg', save=True, imgsz=320, conf=0.5)

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    result.save(filename='result.jpg')  # save to disk


# Visualize the results
# for i, r in enumerate(results):
#     # Plot results image
#     im_bgr = r.plot()  # BGR-order numpy array
#     im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image
#
#     # Show results to screen (in supported environments)
#     r.show()
#
#     # Save results to disk
#     r.save(filename=f'results{i}.jpg')