FROM python:3.8-alpine 


WORKDIR /app

COPY ./src .
RUN ls -ltha 

RUN apk update \
    && apk add --no-cache curl \
    build-base \
    unixodbc-dev \
    freetds-dev \
    bash \
    gcc \
    && pip install --no-cache-dir pyodbc

RUN curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.5.2.2-1_amd64.apk \
    && apk add --allow-untrusted msodbcsql17_17.5.2.2-1_amd64.apk \
    && rm -rf msodbcsql17_17.5.2.2-1_amd64.apk \
    && rm -rf /var/cache/apk/*



RUN pip install \
    --no-cache-dir \
    --exists-action i \
    --verbose \
    #--quiet \
    --no-python-version-warning \
    --disable-pip-version-check \
    -r requirements.txt

EXPOSE 80

ENTRYPOINT [ "python" ]
CMD ["main.py"]