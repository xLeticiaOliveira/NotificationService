FROM python:3.11

WORKDIR /src
COPY . /src


RUN pip install poetry
RUN poetry install

CMD ["bash"]
