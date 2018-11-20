From alpine:3.7

RUN apk add --update py-pip

RUN pip install flask

COPY api_flask.py /src/api_flask.py

EXPOSE 3000

CMD ["python", "/src/api_flask.py"]
