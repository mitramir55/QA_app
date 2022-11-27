#  dockerfile, Image, Container
FROM python:3.9.13

ADD app.py .

RUN pip install streamlit==1.5.1
RUN pip install torch==1.10.2
RUN pip install transformers==4.16.2
RUN pip install wikipedia==1.4.0
RUN pip install pillow

CMD [ "python", "./app.py" ]