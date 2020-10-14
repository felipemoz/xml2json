FROM python:3.8-alpine

WORKDIR /tmp

RUN apk update
RUN apk add --no-cache curl \
    build-base \
    unixodbc-dev \
    freetds-dev \
    bash \
    && pip install pyodbc

RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.5.2.2-1_amd64.apk
RUN apk add --allow-untrusted msodbcsql17_17.5.2.2-1_amd64.apk

RUN rm -rf /var/cache/apk/*

# Application
WORKDIR /app

COPY ./app ./
RUN pip install -r requirements.txt 

EXPOSE 80

ENTRYPOINT [ "python" ]
CMD ["main.py"]