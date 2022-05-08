ARG PYTHON_VERSION

FROM ghcr.io/beartype/bearboto3-base:${PYTHON_VERSION}

ARG PYPROJECT_PATH
ARG WORKDIR=/__w/bearboto3/bearboto3

COPY ${PYPROJECT_PATH}/pyproject.toml ${WORKDIR}/

RUN poetry install
