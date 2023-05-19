FROM python:3.7

ARG DEBIAN_FRONTEND=noninteractive
# Pybossa python requirements

WORKDIR /app

RUN apt-get update -y 

RUN apt-get install -y build-essential libjpeg-dev libssl-dev libffi-dev dbus libdbus-1-dev libdbus-glib-1-dev libldap2-dev libsasl2-dev

## NOTE: You need to create a symbolic link to the translations folder, otherwise
## this wont work.
## ln -s pybossa/themes/your-theme/translations pybossa/translations

## --> From settings_local.py

COPY requirements.txt .
COPY setup.py .
COPY pybossa/version.txt pybossa/version.txt

RUN pip install -r requirements.txt


COPY . /app
RUN ln -s pybossa/themes/default/translations /app/pybossa/translations

RUN ls pybossa/themes/default/

CMD ["python", "run.py"]

