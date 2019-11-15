FROM alpine:3.5
RUN apk add --update --no-cache python py-pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY my_random /src/my_random
CMD python /src/app.py
