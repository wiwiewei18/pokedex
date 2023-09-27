from flask import Blueprint, request
from werkzeug.utils import secure_filename
import os
import uuid

from pokedex.machine_learning.image_classification import predict

bp = Blueprint('image_classification', __name__)

@bp.route('/classify-pokemon-image', methods=('POST',))
def classify_pokemon_image():
    image = request.files['image']
    uniqueId = uuid.uuid4()
    savedImageDir = f"./pokedex/temp/{secure_filename(str(uniqueId) + image.filename)}"
    
    image.save(savedImageDir)

    prediction = predict.classifyImage(savedImageDir)

    os.remove(savedImageDir)
    
    return prediction