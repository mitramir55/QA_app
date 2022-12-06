#  dockerfile, Image, Container
FROM python:3.9

WORKDIR /QA_APP

ADD app.py .
ADD assets assets

CMD [ "python", "app.py" ]

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt