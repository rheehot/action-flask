FROM python:3.7

RUN pip install flask
RUN pip install pylint
RUN pip install pytest

ADD app.py .

EXPOSE 5000

CMD python app.py
