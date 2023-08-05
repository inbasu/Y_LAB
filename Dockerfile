#
FROM python:3.10.12-slim-bookworm
#
WORKDIR /Y_LAB
#
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

#
#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
