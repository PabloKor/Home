# docker run -p 5000:5000 web-app

FROM python:3.9.5-buster

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv sync

COPY ./web-app .

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
