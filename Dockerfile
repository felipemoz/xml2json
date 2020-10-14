FROM python:3.8-alpine

WORKDIR /tmp

RUN apk update
RUN apk add --no-cache curl \
    sudo \
    build-base \
    unixodbc-dev \
    unixodbc \
    freetds-dev \
    tzdata \
    bash \
    gcc \
    libc-dev \
    g++ \
    libffi-dev \
    libxml2 \
    && pip install pyodbc

RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.5.2.2-1_amd64.apk
RUN sudo sudo apk add --allow-untrusted msodbcsql17_17.5.2.2-1_amd64.apk

ENV TZ UTC
RUN rm -rf /var/cache/apk/*


# Application
WORKDIR /app

COPY ./app ./
RUN pip install -r requirements.txt 

EXPOSE 80

ENTRYPOINT [ "python" ] 
CMD ["main.py"]