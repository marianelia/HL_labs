FROM python:3.12
WORKDIR /init

COPY ./requirements.txt /init/requirements.txt
RUN pip install -r requirements.txt

COPY . /init

ENTRYPOINT ["bash", "-c", "python3 init_bd_script.py"]