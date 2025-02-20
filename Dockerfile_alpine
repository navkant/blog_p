FROM python:3.8.18-alpine3.18

RUN apk add --update alpine-sdk
RUN apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN curl -sSL https://install.python-poetry.org | python3.8 - --version 1.8.0
ENV PATH="/root/.local/bin:$PATH"
EXPOSE 8000

COPY . /app
WORKDIR /app
RUN poetry install --no-dev

RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]


