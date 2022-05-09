ARG PYTHON_VERSION

FROM ghcr.io/beartype/bearboto3-base:${PYTHON_VERSION}

ARG PYPROJECT_PATH

COPY ${PYPROJECT_PATH} ./

RUN poetry install
