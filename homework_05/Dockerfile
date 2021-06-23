# docker run -p 6001:5000 web-app

FROM python:3.9.5-buster

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./web-app .

ENV FLASK_ENV=development \
    FLASK_DEBUG=1

EXPOSE 6001

CMD ["flask", "run", "--host=0.0.0.0"]