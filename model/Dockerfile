FROM python:3.8.13 as base

ADD requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip install tensorflow-aarch64 -f https://tf.kmtea.eu/whl/stable.html

ENV PYTHONPATH=$PYTHONPATH:/src/

ADD ./ /src/

WORKDIR /src

FROM base as test
RUN ["pytest", "-v", "/src/tests"]

FROM base as build
ENTRYPOINT ["python3", "/src/ml_service.py"]