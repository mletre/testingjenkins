FROM python:3.13.0a4-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 9696

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=9696"]