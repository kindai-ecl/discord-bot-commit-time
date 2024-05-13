FROM python:3.12

RUN apt-get update && apt-get install -y \
sqlite3


RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY . .

WORKDIR /bot
CMD ["python3", "bot.py"]