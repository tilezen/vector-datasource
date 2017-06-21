def mz_building_kind_detail(val):
    # TODO should this be in yaml instead?
    if val in (
            'bangunan',
            'building',
            'other',
            'rumah',
            'Rumah',
            'Rumah Masyarakat',
            'rumah_penduduk',
            'true',
            'trullo',
            'yes'):
        return None

    if val in (
            'abandoned',
            'administrative',
            'agricultural',
            'airport',
            'allotment_house',
            'apartments',
            'arbour',
            'bank',
            'barn',
            'basilica',
            'beach_hut',
            'bell_tower',
            'boathouse',
            'brewery',
            'bridge',
            'bungalow',
            'bunker',
            'cabin',
            'carport',
            'castle',
            'cathedral',
            'chapel',
            'chimney',
            'church',
            'civic',
            'clinic',
            'clubhouse',
            'collapsed',
            'college',
            'commercial',
            'construction',
            'container',
            'convent',
            'cowshed',
            'dam',
            'damaged',
            'depot',
            'destroyed',
            'detached',
            'disused',
            'dormitory',
            'duplex',
            'factory',
            'farm',
            'farm_auxiliary',
            'fire_station',
            'garage',
            'garages',
            'gazebo',
            'ger',
            'glasshouse',
            'government',
            'grandstand',
            'greenhouse',
            'hangar',
            'healthcare',
            'hermitage',
            'hospital',
            'hotel',
            'house',
            'houseboat',
            'hut',
            'industrial',
            'kindergarten',
            'kiosk',
            'library',
            'mall',
            'manor',
            'manufacture',
            'mobile_home',
            'monastery',
            'mortuary',
            'mosque',
            'museum',
            'office',
            'outbuilding',
            'parking',
            'pavilion',
            'power',
            'prison',
            'proposed',
            'pub',
            'public',
            'residential',
            'restaurant',
            'retail',
            'roof',
            'ruin',
            'ruins',
            'school',
            'semidetached_house',
            'service',
            'shed',
            'shelter',
            'shop',
            'shrine',
            'silo',
            'slurry_tank',
            'stable',
            'stadium',
            'static_caravan',
            'storage',
            'storage_tank',
            'store',
            'substation',
            'summer_cottage',
            'summer_house',
            'supermarket',
            'synagogue',
            'tank',
            'temple',
            'terrace',
            'tower',
            'train_station',
            'transformer_tower',
            'transportation',
            'university',
            'utility',
            'veranda',
            'warehouse',
            'wayside_shrine',
            'works'):
        return val

    if val == 'barne':
        return 'barn'
    if val == 'commercial;residential':
        return 'mixed_use'
    if val == 'constructie':
        return 'construction'
    if val == 'dwelling_house':
        return 'house'
    if val == 'education':
        return 'school'
    if val == 'greenhouse_horticulture':
        return 'greenhouse'
    if val in ('apartment', 'flat'):
        return 'apartments'
    if val in ('houses', 'residences', 'residence', 'perumahan permukiman', 'residentiel1'):
        return 'residential'
    if val in ('semi_detached', 'semi-detached', 'semi'):
        return 'semidetached_house'
    if val == 'offices':
        return 'office'
    if val == 'prefab_container':
        return 'container'
    if val == 'public_building':
        return 'public'
    if val == 'railway_station':
        return 'train_station'
    if val == 'roof=permanent':
        return 'roof'
    if val == 'stables':
        return 'stable'
    if val == 'static caravan':
        return 'static_caravan'
    if val == 'station':
        return 'transportation'
    if val == 'storage tank':
        return 'storage_tank'
    if val == 'townhome':
        return 'terrace'


def mz_building_part_kind_detail(val):
    if val in ('yes', 'part', 'church:part', 'default'):
        return None
    if val in (
                'arch',
                'balcony',
                'base',
                'column',
                'door',
                'elevator',
                'entrance',
                'floor',
                'hall',
                'main',
                'passageway',
                'pillar',
                'porch',
                'ramp',
                'roof',
                'room',
                'steps',
                'stilobate',
                'tier',
                'tower',
                'verticalpassage',
                'wall',
                'window'):
        return val
    if val in ('corridor', 'Corridor', 'vertical', 'verticalpassage'):
        return 'verticalpassage'
    if val in ('stairs', 'stairway'):
        return 'steps'


# these functions were used in the yaml, but are worked around at the
# moment by continuing to call the sql and having the output
# calculation simply pick up the sql values
# def mz_get_rel_networks(osm_id):
#     return []
# def mz_cycling_network(props, osm_id):
#     pass


def trim_nz_sh(label):
    # TODO is this what the implementation should be?
    if label.startswith('NZ:SH'):
        label = label[len('NZ:SH'):]
    return label
