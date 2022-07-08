FROM python:3.10.5-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#cmd run server on the specified way
CMD ["uvicorn", "main:app", "--reload", "0.0.0.0:8000"]