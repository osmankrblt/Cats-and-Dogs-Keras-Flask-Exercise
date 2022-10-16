FROM python:3.9-buster
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update && apt-get install libgl1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]