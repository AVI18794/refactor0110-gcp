FROM python:3.11
EXPOSE 8080
RUN pip install -U pip
COPY requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt
COPY . /app
WORKDIR app
 
# Run
ENTRYPOINT ["streamlit", "run", "main.py",  "--server.port=8080", "--server.address=0.0.0.0"]