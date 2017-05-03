UPDATE
  planet_osm_polygon p
  SET mz_poi_min_zoom = mz_calculate_min_zoom_pois(p.*),
      mz_landuse_min_zoom = mz_calculate_min_zoom_landuse(p.*)
  WHERE
    (
      tags -> 'aerialway' = 'pylon'
      OR tags -> 'aeroway' IN ('gate', 'helipad')
      OR tags -> 'amenity' IN ('atm', 'bbq', 'bench', 'bicycle_parking', 'bicycle_rental',
        'bicycle_repair_station', 'boat_storage', 'car_sharing', 'fuel',
        'life_ring', 'parking', 'picnic_table', 'post_box', 'ranger_station', 'recycling',
        'shelter', 'shower', 'telephone', 'toilets', 'waste_basket', 'waste_disposal',
        'water_point', 'watering_place')
      OR tags -> 'barrier' IN ('cycle_barrier', 'gate', 'toll_booth')
      OR tags -> 'emergency' IN ('lifeguard_tower', 'phone')
      OR tags -> 'highway' IN ('bus_stop', 'ford', 'mini_roundabout', 'motorway_junction',
        'platform', 'rest_area', 'traffic_signals', 'trailhead')
      OR tags -> 'historic' = 'landmark'
      OR tags -> 'landuse' IN ('village_green', 'quarry')
      OR tags -> 'leisure' IN ('garden', 'dog_park', 'firepit', 'fishing', 'pitch',
        'slipway', 'swimming_area')
      OR tags -> 'lock' = 'yes'
      OR tags -> 'man_made' IN ('adit', 'communications_tower', 'mast', 'mineshaft',
        'observatory', 'offshore_platform', 'petroleum_well', 'pier', 'power_wind', 'telescope',
        'water_tower', 'water_well', 'windmill')
      OR tags -> 'natural' IN ('cave_entrance', 'peak', 'volcano', 'forest', 'geyser',
        'hot_spring', 'rock', 'saddle', 'stone', 'spring', 'tree', 'waterfall', 'wood')
      OR tags -> 'power' IN ('pole', 'tower')
      OR tags -> 'public_transport' IN ('platform', 'stop_area')
      OR tags -> 'railway' IN ('halt', 'level_crossing', 'platform', 'stop',
        'subway_entrance', 'tram_stop')
      OR tags -> 'icn_ref' = 'true'
      OR tags -> 'iwn_ref' = 'true'
      OR tags -> 'lcn_ref' = 'true'
      OR tags -> 'lwn_ref' = 'true'
      OR tags -> 'ncn_ref' = 'true'
      OR tags -> 'nwn_ref' = 'true'
      OR tags -> 'rcn_ref' = 'true'
      OR tags -> 'rwn_ref' = 'true'
      OR tags -> 'whitewater' IN ('egress', 'hazard', 'put_in', 'put_in;egress',
        'rapid')
      OR tags -> 'tourism' IN ('alpine_hut', 'information', 'picnic_site', 'viewpoint',
        'wilderness_hut')
      OR tags -> 'waterway' IN ('dam', 'lock', 'waterfall')
      OR (NOT tags ? 'name' AND mz_poi_min_zoom IS NOT NULL)
    )
    AND (
      COALESCE(mz_poi_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_pois(p.*), 999) OR
      COALESCE(mz_landuse_min_zoom, 999) <> COALESCE(mz_calculate_min_zoom_landuse(p.*), 999)
    );
