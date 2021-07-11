FROM python:3.7

ADD . .
ADD src /src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["python", "-m", "unittest", "discover", "-s","./src/Tests"]