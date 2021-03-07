FROM python:3.6.6-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV ENV='production'
ENV HOST='wools.joalex.dev'

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]