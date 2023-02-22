FROM python:3.9 as base-backend

WORKDIR /backend/src

COPY ./requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY ./src /backend/src
# folders data, logging, secrets must be mounted as volumes

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


FROM base-backend as test-backend

COPY ./tests /backend/tests
COPY ./pytest.ini /backend/pytest.ini

WORKDIR /backend

CMD ["pytest", "--disable-warnings"]


# target base-backend build command
# docker build --target base-backend -t sd_backend_img ./backend


