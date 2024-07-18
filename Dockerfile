FROM python:3.8
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/service-account-file.json"
EXPOSE 8080
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]