FROM alpine:latest
WORKDIR /app
ADD . /app
RUN apk add python3-dev \
    && apk add cmd:pip3 

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
Expose 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
