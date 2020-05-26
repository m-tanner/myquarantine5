FROM python:3.7-alpine

RUN echo Copying the MYQ5 service into a service directory.
COPY . /MyQuarantine5Service
WORKDIR /MyQuarantine5Service

RUN echo Adding the new folder to the Python path so that Flask works.
ENV PYTHONPATH /MyQuarantine5Service

RUN echo Installing APK and Python packages listed in setup.py
RUN apk update
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install ".[tests]" --no-cache-dir && \
 apk --purge del .build-deps

RUN echo Exposing the port where Waitress will listen.
EXPOSE 8080

RUN echo Starting python and starting the Flask service...
CMD ["myq5_svc"]
