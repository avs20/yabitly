FROM python:3
ENV PYBASE /pybase
ENV PYTHONUSERBASE $PYBASE
ENV PATH $PYBASE:bin/$PATH

WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . /app/yabitly
WORKDIR /app/yabitly
ENV FLASK_APP /app/yabitly/src/yabitly
EXPOSE 80

CMD ["flask", "run", "--port=80", "--host=0.0.0.0"]
