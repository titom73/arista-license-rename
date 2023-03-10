ARG PYTHON_VER=3.10

FROM python:${PYTHON_VER}-slim

RUN pip install --upgrade pip

WORKDIR /local
COPY . /local

LABEL maintainer="Thomas Grimonet <tom@inetsix.net>"
LABEL com.example.version="edge"
LABEL com.example.release-date="2022-04-05"
LABEL com.example.version.is-production="False"

ENV PYTHONPATH=/local
RUN pip --no-cache-dir install .

ENTRYPOINT [ "/usr/local/bin/ar-lic-cleaner" ]
