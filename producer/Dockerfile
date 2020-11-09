FROM python:3.6

RUN apt-get update
RUN apt-get -y install libsnappy-dev

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app
COPY . /app

# RUN mkdir data
# RUN curl --fail "https://lsst.ncsa.illinois.edu/~ebellm/sample_precursor_alerts/latest_single_ccd_sample.avro" > data/rubin_single_ccd_sample.avro

CMD ["python", "scripts/run_step.py"]