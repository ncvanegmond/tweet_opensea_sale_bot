FROM python:3.7-alpine
#FROM nickgryg/alpine-pandas

COPY bots/config.py /bots/
COPY bots/opensea_api.py /bots/
COPY bots/tweet_opensea_recent_sale_bot.py /bots/
COPY requirements.txt /tmp
COPY .env /bots/
RUN pip3 install --no-cache -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "tweet_opensea_recent_sale_bot.py"]