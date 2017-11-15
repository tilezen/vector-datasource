FROM ubuntu:14.04

# install osm2pgsql build deps
RUN apt-get update \
 && apt-get -y install software-properties-common \
 && apt-add-repository -y ppa:tilezen \
 && apt-get update \
 && apt-get -y install \
    libpq-dev \
    osm2pgsql \
    python \
    libxml2-dev \
    libxslt1-dev \
    postgresql-client \
    python-dev \
    python-jinja2 \
    python-yaml \
    python-pip \
    git-core \
    make \
    wget \
    unzip \
 && rm -rf /var/lib/apt/lists/*

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
RUN pip install -e .

CMD ["/bin/bash", "scripts/docker_boostrap.sh"]
