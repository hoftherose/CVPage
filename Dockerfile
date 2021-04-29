FROM python:3.8-buster

WORKDIR /home/app

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends gfortran libopenblas-dev liblapack-dev && pip3 install  --user -r requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python run.py
