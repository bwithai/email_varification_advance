FROM  --platform=linux/amd64 python:3

RUN apt-get update
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
RUN mv /code/app/.env.sample /code/app/.env
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers", "--root-path", "/api/notifications"]
