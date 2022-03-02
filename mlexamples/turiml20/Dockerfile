FROM tensorflow/tensorflow:2.8.0-gpu

RUN python --version && pip install matplotlib keras scipy turicreate tensorflow torch spotlight

COPY . /opt/app

WORKDIR /opt/app

CMD ["python", "pyytton.py"]