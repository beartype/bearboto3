ARG PYTHON_VERSION

FROM ghcr.io/beartype/bearboto3-base:${PYTHON_VERSION}

ARG PYPROJECT_PATH

COPY ${PYPROJECT_PATH}/pyproject.toml ./

RUN poetry install
