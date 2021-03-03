FROM python:3.6.6-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_ENV='production'

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]