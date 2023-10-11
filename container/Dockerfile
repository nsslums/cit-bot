#### Builder image ####
FROM python:3.11-slim AS builder

WORKDIR /home

# gitインストール
RUN apt update && apt install git -y

# disable cache
ARG NOCACHE=1

# clone repository
RUN git clone https://github.com/nsslums/cit-bot.git


#### app image ####
FROM python:3.11-slim

# library install
RUN pip install discord.py load_dotenv json-tricks

# disable cache
ARG NOCACHE=1

# python app
COPY --from=builder /home/cit-bot/python /home/cit-bot/python

# 起動
ENTRYPOINT ["python", "/home/cit-bot/python/Bot.py"]
