import os
from PIL import Image

# Paths
root_dir = 'GTSDB'  # Change this to your dataset root path
images_dir = os.path.join(root_dir, 'images')
labels_dir = os.path.join(root_dir, 'labels')
os.makedirs(labels_dir, exist_ok=True)

# Read gt.txt
gt_file = os.path.join(root_dir, 'gt.txt')
with open(gt_file, 'r') as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split(';')
    filename, left, top, right, bottom, class_id = parts
    left, top, right, bottom = map(int, [left, top, right, bottom])
    class_id = int(class_id)
    class_path = str(class_id) if class_id >= 10 else '0' + str(class_id)

    # Image path
    img_path = os.path.join(root_dir, filename)
    try:
        img = Image.open(img_path)
    except:
        print(f"Error opening image {img_path}. Skipping.")
        continue
    W, H = img.size

    # Convert to YOLO format
    x_center = ((left + right) / 2) / W
    y_center = ((top + bottom) / 2) / H
    bbox_width = (right - left) / W
    bbox_height = (bottom - top) / H

    yolo_label = f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}"

    # Save label file
    txt_name = os.path.splitext(os.path.basename(filename))[0] + ".txt"
    label_path = os.path.join(labels_dir, txt_name)

    with open(label_path, 'a') as label_file:
        label_file.write(yolo_label + '\n')

    # Optional: convert .ppm to .jpg
    jpg_path = os.path.join(images_dir, os.path.splitext(os.path.basename(filename))[0] + ".jpg")
    img.convert('RGB').save(jpg_path)
