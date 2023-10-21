FROM python:3.10-alpine

WORKDIR /bonus

COPY ../config.yaml /
COPY ../requirements.txt /bonus
COPY . /bonus

RUN pip3.10 install -r requirements.txt

EXPOSE 8050

CMD ["python3", "bonus_service/main.py"]
