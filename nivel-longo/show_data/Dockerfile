FROM python:3.9-slim

WORKDIR /app

COPY show_data.py /app/
COPY requirements.txt /app/
COPY /wait-for-it.sh /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /app/wait-for-it.sh

CMD ["/app/wait-for-it.sh", "api:5000", "--", "python", "show_data.py"]
