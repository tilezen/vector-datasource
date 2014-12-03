Mapzen Vector Tiles
========================

See info about the hosted version of this service here:

[Mapzen Vector Tile Service](https://github.com/mapzen/vector-datasource/wiki/Mapzen-Vector-Tile-Service)

Installation
------------

Requirements:

* [TileStache](http://tilestache.org)
* [PostGIS](http://postgis.net)
* An OpenStreetMap database created by [osm2pgsql](http://wiki.openstreetmap.org/wiki/Osm2pgsql)
* [Natural Earth](http://www.naturalearthdata.com) tables from contents of `data/`.


------------

#Installation Guide
(tested under Ubuntu 14.04)

The installation is performed in three steps.

![Imgur](http://i.imgur.com/mNADpl1.png)

### 1. Loading data (Make ready for using vector tiles)

#### Install postgres

```shell
sudo apt-get install postgresql postgresql-contrib postgis postgresql-9.3-postgis-2.1
```

You can find a more detailed description [here](http://wiki.openstreetmap.org/wiki/PostGIS/Installation#Ubuntu_14.04_LTS).

#### Create database and extensions

```shell
# switch to user postgres
sudo -i -u postgres

# create new database
createdb gis

# create extensions
psql -d gis -c 'CREATE EXTENSION postgis; CREATE EXTENSION hstore;'

# check the results
psql -d gis
\conninfo

# logout from db
\q

# logout user postgres
exit
```

#### Install osm2pgsql

```shell
sudo apt-get install osm2pgsql
```

#### Download data

Here we use data from [geofabrik](http://download.geofabrik.de/), but you can use other *.pbf files.

```shell
# switch to new data path
cd /path/to/your/osm/data
# download data
wget http://download.geofabrik.de/europe/austria-latest.osm.pbf
```

#### Add data to the database
Start osm2pgsql in your data folder. Before you start the osm2pgsql script you might need to check your postgresql user rights (pg_hba.conf) 
```shell
osm2pgsql --create --cache-strategy sparse -C 750 -U postgres -S osm2pgsql.style.txt -d gis -k austria-latest.osm.pbf 
```



### 2. PREPARE DATA

#### **Download** mapzen/vector-datasource:

```shell
git clone https://github.com/mapzen/vector-datasource.git
```

#### **Prepare Database**

Download the file at [https://gist.github.com/rmarianski/491e50f3dd7159ebdf23](https://gist.githubusercontent.com/rmarianski/491e50f3dd7159ebdf23/raw/c40439e9f5761d4f5ad0846a334a49ff1d6024a2/gistfile1.txt) and drop it in the *../vector-datasource/data/* folder as *gist.sh*, or just type...

```shell
# change to folder
cd vector-datasource/data
# download file
wget -O gist.sh https://gist.githubusercontent.com/rmarianski/491e50f3dd7159ebdf23/raw/c40439e9f5761d4f5ad0846a334a49ff1d6024a2/gistfile1.txt
```
Open the file *gist.sh*  and change database options [accordingly](https://gist.github.com/rmarianski)  (leave out *-h host* when using a local machine):
```shell
# database options
export PGPASSWORD=password
PGOPTS="-d database -h host -U user"

```
then run the *gist.sh* script:
```shell
# make sript executable
chmod +x gist.sh
# execute the script
./gist.sh
```

### 3. CREATE VECTOR TILES

#### Download TileStache

```shell
git clone https://github.com/mapzen/TileStache.git

# Check out to integration-1 fork for serving .mapbox vectortiles

git fetch --all
git checkout integration-1
```
You can find TileStache at [https://github.com/mapzen/TileStache/](https://github.com/mapzen/TileStache/)

#### Install dependencies

Follow the instructions at [https://github.com/TileStache/TileStache](https://github.com/TileStache/TileStache)
or do
```shell
# install pip
curl -O -L https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py
rm get-pip.py

# install other build dependecies (check if you need all of them)
sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev zlib1g-dev libjpeg-dev python-psycopg2

# install pillow (better alternative to PIL)
sudo pip install pillow

# install mapnik
sudo add-apt-repository ppa:mapnik/nightly-2.3
sudo apt-get update
sudo apt-get install -y libmapnik mapnik-utils python-mapnik

sudo pip install shapely
sudo pip install protobuf


```


#### Install TileStache
```shell
# change folder
cd TileStache/
# install TileStache
sudo python setup.py install
# start server with mapzen .cfg file
./scripts/tilestache-server.py -c path/to/mapzen-vector-datasource/tilestache.cfg

# tes your configurations
http://localhost:8080/osm/buildings/16/19293/24641.json
```
