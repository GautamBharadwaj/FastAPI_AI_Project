from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
import base64

# Load a pre-trained TensorFlow model (e.g., MobileNetV2)
model = tf.keras.applications.MobileNetV2(weights='imagenet')

app = FastAPI()

class ImageData(BaseModel):
    image_base64: str

@app.post("/predict/")
async def predict(image_data: ImageData):
    # Decode image from base64 string
    img_data = base64.b64decode(image_data.image_base64)
    img = Image.open(BytesIO(img_data))

    # Preprocess the image for prediction
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict the class
    predictions = model.predict(img_array)
    predicted_class = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0][0][1]
    return {"predicted_class": predicted_class}
