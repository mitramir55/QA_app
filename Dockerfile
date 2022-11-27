#  dockerfile, Image, Container
FROM python:3.9.13

ADD app.py .

RUN pip install -r requirements.txt 

CMD [ "python", "./app.py" ]