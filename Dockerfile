FROM ubuntu:14.04

# install osm2pgsql build deps
RUN apt-get update \
 && apt-get -y install software-properties-common \
 && apt-add-repository -y ppa:tilezen \
 && apt-get update \
 && apt-get -y install postgresql osm2pgsql python python-jinja2 python-yaml make wget unzip \
 && rm -rf /var/lib/apt/lists/*

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["/bin/bash", "scripts/docker_boostrap.sh"]
