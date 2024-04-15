import os

# 设置你的图片和标签的目录路径
labels_dir = 'D:/workplace-python/yolo8Lcz/yolo8Lcz/ultralytics/dataset/train/labels'

# 列出所有图片文件
image_files = [f for f in os.listdir(labels_dir) if os.path.isfile(os.path.join(labels_dir, f))]

# 开始遍历图片并重新命名图片及其对应的标注文件
for i, image_file in enumerate(image_files, 1):
    # 文件的扩展名
    ext = os.path.splitext(image_file)[1]
    # 不包含扩展名的文件名部分
    old_base_name = os.path.splitext(image_file)[0]

    # 构造新的文件名（按需调整格式）
    new_file_name = f"DJI_{i:04d}{ext}"

    # 路径拼接
    old_image_path = os.path.join(labels_dir, image_file)
    new_image_path = os.path.join(labels_dir, new_file_name)

    # # 对于标签文件
    # old_label_basename = old_base_name + '.txt'
    # old_label_path = os.path.join(labels_dir, old_label_basename)
    # new_label_name = f"DJI_{i:04d}.txt"
    # new_label_path = os.path.join(labels_dir, new_label_name)

    # 对图片文件重命名
    os.rename(old_image_path, new_image_path)
    print(f'Renamed image: {old_image_path} to {new_image_path}')

    # # 检查标签文件存在，如果是则重命名
    # if os.path.exists(old_label_path):
    #     os.rename(old_label_path, new_label_path)
    #     print(f'Renamed label: {old_label_path} to {new_label_path}')
    # else:
    #     print(f'Label file {old_label_path} not found.')

print('Renaming completed.')
