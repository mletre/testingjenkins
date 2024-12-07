FROM python:3.13.0a4-bookworm

WORKDIR /app

COPY /backend/requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN pip install -r requirements.txt
EXPOSE 9696

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=9696"]