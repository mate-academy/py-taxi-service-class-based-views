FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    libjpeg-dev \
    libtiff-dev \
    zlib1g-dev \
    libfreetype6-dev \
    libffi-dev \
    meson \
    cmake \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /main_app/requirements.txt
COPY . /main_app/
WORKDIR /main_app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password main_app-user
USER main_app-user

EXPOSE 8000