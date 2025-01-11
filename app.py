from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import StreamingResponse
from ultralytics import YOLO
from io import BytesIO
from PIL import Image

# Load model at startup
model = YOLO("yolov8n.pt")  # Change yolov8n.pt to your model path

app = FastAPI()


@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
    output_image_name: str = Query(default="output_image.png", description="Name of the output image to save")
):
    # Read the uploaded image as bytes
    image_bytes = await file.read()

    # Convert the bytes to a PIL image
    image = Image.open(BytesIO(image_bytes))

    # Perform inference using the YOLO model
    results = model(image)
    output_array = results[0].plot()  # This gives a NumPy array
    output_image = Image.fromarray(output_array)

    # Convert the PIL Image to a byte stream
    img_byte_arr = BytesIO()
    output_image.save(img_byte_arr, format="PNG")
    output_image.save(output_image_name)
    img_byte_arr.seek(0)
    return StreamingResponse(img_byte_arr, media_type="image/png")
