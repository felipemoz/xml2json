FROM python:3.8-alpine 

WORKDIR /app

COPY ./src .

RUN pip install \
    --no-cache-dir \
    --exists-action i \
    --quiet \
    --no-python-version-warning \
    --disable-pip-version-check \
    -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "gunicorn" ]
CMD ["main:app"]