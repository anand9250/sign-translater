import cv2
import os
import time
import uuid

# Directory to store images
IMAGE_PATH = 'tensorflow/workspace/image/collectedimage'

# Labels to collect
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

# Create directories for each label
for label in labels:
    label_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(label_path, exist_ok=True)

    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)

    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            continue

        imagename = os.path.join(label_path, label + '.' + str(uuid.uuid1()) + '.jpg')
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
