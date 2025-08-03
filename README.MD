# Object Detection API with FastAPI and OpenCV DNN

This project allows you to perform object detection using a pre-trained MobileNet model wrapped in a FastAPI backend. It returns annotated images with bounding boxes drawn over detected objects.

## 🚀 Features
- FastAPI server for REST API access
- Uses OpenCV's DNN module and MobileNet SSD model
- Dockerized for easy deployment

## 🧾 Project Structure
```
Lab-1/
├── app/
│   ├── main.py
│   └── requirements.txt
├── images/  # Input test images
├── images_with_boxes/
├── images_predicted/
├── images_uploaded/
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## ⚙️ Requirements (without Docker)
```bash
pip install -r app/requirements.txt
```

## 🐳 Run with Docker
```bash
docker build -t object-detection-app .
docker run -p 8000:8000 object-detection-app
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🔁 Example Request
You can upload a JPEG/PNG image using Swagger UI or send it with Python using `requests`.

## 📸 Models Used
- `mobilenet_iter_73000.caffemodel`
- `deploy.prototxt.txt`

> Make sure these model files are placed in the correct location for inference to work.
