FROM python:3.7

RUN pip install flask

ADD app.py .

EXPOSE 5000

CMD python app.py
