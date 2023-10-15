FROM python:3.10-alpine

WORKDIR /flight

COPY . /flight

RUN pip3.10 install -r requirements.txt

EXPOSE 8060

CMD ["python3", "main.py"]
