
FROM python:3.10-slim


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN chmod +x run_app.sh


EXPOSE 7860

CMD ["./run_app.sh"]