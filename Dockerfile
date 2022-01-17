FROM python:3.9.5-alpine

RUN apk add python3-dev build-base linux-headers pcre-dev && \
    addgroup -S user && \
    adduser -S user -G user -u 1001 && \
    mkdir /opt/app
WORKDIR /opt/app
COPY . .
RUN pip install -r requirements.txt 
USER user
ENTRYPOINT [ "flask", "run" ]