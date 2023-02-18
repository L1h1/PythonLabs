FROM python:3.10
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . .
CMD python main.py