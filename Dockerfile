FROM python:3.9
COPY . /app
WORKDIR /Cats and Dogs Keras-Flask Exercise
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app