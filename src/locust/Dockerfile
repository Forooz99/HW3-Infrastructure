FROM python:3.8

RUN pip install locust

COPY . .

WORKDIR /locust


CMD ["locust", "-f", "locustfile.py"]