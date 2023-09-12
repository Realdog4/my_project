FROM python:3.11-rc-slim

RUN apt update
RUN mkdir /authoshipping

WORKDIR /authoshipping

COPY ./src ./src
COPY ./requirements.txt ./requirements.txt

RUN  python -m pip install --upgrade pip & pip install -r ./requirements.txt

CMD ["python", "src/manage.py", "runserver", "8008"]