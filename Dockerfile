FROM python:3

RUN mkdir /usr/sample
COPY getcomputername.py /usr/sample/
COPY requirements.txt /usr/sample/
WORKDIR /usr/sample/
RUN pip install -r requirements.txt

EXPOSE 8081
CMD python3 getcomputername.py