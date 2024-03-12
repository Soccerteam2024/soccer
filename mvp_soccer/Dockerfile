FROM python:3.10.6-buster

COPY package_folder package_folder
COPY requirements.txt requirements.txt
COPY models models
COPY setup.py setup.py

#RUN pip install -r requirements.txt
RUN pip install --upgrade pip
#RUN pip install -e .
RUN pip install -r requirements.txt

# RUN CONTAINER LOCALLY
# CMD uvicorn package_folder.api_file:api --host 0.0.0.0 --port 8000

# RUN CONTAINER DEPLOYED
CMD uvicorn package_folder.api_file:api --host 0.0.0.0 --port $PORT


#EXPOSE 8080
