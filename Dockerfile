ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

ARG WORKDIR=/__w/bearboto3/bearboto3

RUN pip3 install poetry

COPY . ${WORKDIR}

WORKDIR ${WORKDIR}

VOLUME ${WORKDIR}

RUN poetry config virtualenvs.create false

RUN poetry install --remove-untracked