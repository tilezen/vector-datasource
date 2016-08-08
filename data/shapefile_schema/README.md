create tables matching the schema of the static asset shapefiles.

this is an edited version of the output of:

```
mkdir shapefiles; cd shapefiles/
tar zxf ../shapefiles.tar.gz
for i in *.zip; do unzip $i; done
for i in `find . -name "*.shp"`; do
  j=`echo $i | sed "s,.*/,,;s,-merc,,;s,\.shp\$,,"`
  shp2pgsql -p -s 3857 -g the_geom $i $j >> $j.sql
done
```
