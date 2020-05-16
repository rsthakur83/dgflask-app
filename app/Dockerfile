FROM python:3.6.1-alpine
RUN pip install --upgrade pip
WORKDIR /app
COPY app.py /app
COPY requirements.txt /app
RUN  pip install -r /app/requirements.txt && mkdir /app/templates
ADD  templates /app/templates
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
