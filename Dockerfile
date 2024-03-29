FROM ubuntu:latest
MAINTAINER Marco Chan "chantinghin0203@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["-mpytest"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]