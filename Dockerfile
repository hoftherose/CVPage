FROM python:3.8-buster

RUN apt-get -o Acquire::Check-Valid-Until=false update
RUN apt-get install -y --no-install-recommends gfortran libopenblas-dev liblapack-dev && pip3 install  --user -r requirements.txt

WORKDIR /home/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD python run.py
