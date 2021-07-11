FROM python:3.7

ADD . .

RUN pip install --upgrade pip
RUN pip install -r requirements


CMD ["python", "-m", "unittest", "discover", "-s","./src/Tests"]