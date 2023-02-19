FROM python:3.10

COPY requirements.txt .
COPY helloworld.py .
COPY main.py .
COPY operation.py .
COPY randeven.py .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]
