FROM python:3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
CMD ["cli.py"]
ENTRYPOINT ["python3"]
