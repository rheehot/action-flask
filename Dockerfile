FROM python:3.7

RUN pip install flask
RUN pip install pylint

ADD app.py .

EXPOSE 5000

CMD python app.py
