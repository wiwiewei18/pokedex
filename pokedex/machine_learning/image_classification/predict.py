from ultralytics import YOLO
import numpy as np

model = YOLO('./pokedex/machine_learning/image_classification/runs/classify/train/weights/best.pt')

def classifyImage(image):
    results = model(image)
    classificationNames = results[0].names
    probs = results[0].probs.data.tolist()

    return classificationNames[np.argmax(probs)]