# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/trusty64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 8080, host: 18080 # Tileserver
  config.vm.network "forwarded_port", guest: 5432, host: 15432 # PostgreSQL

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder ".", "/opt/src/vector-datasource"
  config.vm.synced_folder "../tilequeue", "/opt/src/tilequeue"
  config.vm.synced_folder "../tileserver", "/opt/src/tileserver"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
    vb.memory = "2048"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    set -x
    set -e
    echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
    export DEBIAN_FRONTEND=noninteractive
    apt-add-repository -y ppa:tilezen
    apt-get -qq update
    apt-get -qq install -y git unzip \
        postgresql postgresql-contrib postgis postgresql-9.3-postgis-2.1 \
        build-essential autoconf libtool pkg-config \
        python-dev python-virtualenv libgeos-dev libpq-dev python-pip python-pil libmapnik2.2 libmapnik-dev mapnik-utils python-mapnik \
        osm2pgsql

    sudo -u postgres psql -c "CREATE ROLE osm WITH NOSUPERUSER LOGIN UNENCRYPTED PASSWORD 'osmpassword';"
    sudo -u postgres createdb -E UTF-8 -T template0 -O osm osm
    sudo -u postgres psql -d osm -c 'CREATE EXTENSION postgis; CREATE EXTENSION hstore;'

    export PGPASSWORD=osmpassword

    rm -f /opt/data
    mkdir -p /opt/data /opt/src /opt/virtualenv
    chown vagrant:vagrant -R /opt
    su vagrant

    # Download and import OSM data
    echo "Downloading New York OSM data"
    wget --quiet -P /opt/data/ https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm.pbf
    osm2pgsql -s -C 512 -S /opt/src/vector-datasource/osm2pgsql.style -j /opt/data/new-york_new-york.osm.pbf -U osm -d osm -H localhost

    # Download and import supporting data
    cd /opt/src/vector-datasource
    virtualenv /opt/virtualenv/vector-datasource
    source /opt/virtualenv/vector-datasource/bin/activate
    pip -q install -U jinja2 pyaml
    cd data
    python bootstrap.py
    make -f Makefile-import-data
    ./import-shapefiles.sh | psql -d osm -U osm -h localhost
    ./perform-sql-updates.sh -d osm -U osm -h localhost
    make -f Makefile-import-data clean
    deactivate

    echo "Downloading Who's on First neighbourhoods data"
    wget --quiet -P /opt/data/ https://s3.amazonaws.com/mapzen-tiles-assets/wof/dev/wof_neighbourhoods.pgdump
    pg_restore --clean -d osm -U osm -h localhost -O /opt/data/wof_neighbourhoods.pgdump

    # Set up tileserver
    cd /opt/src/tileserver
    virtualenv /opt/virtualenv/tileserver
    source /opt/virtualenv/tileserver/bin/activate
    pip -q install -U -r requirements.txt
    python setup.py -q develop
    (cd ../tilequeue && python setup.py -q develop)
    (cd ../vector-datasource && python setup.py -q develop)
    deactivate
  SHELL
end
