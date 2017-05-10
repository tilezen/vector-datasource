# block between mission & 6th and howard & 5th in SF.
# appears to have lots of buses.
# https://www.openstreetmap.org/way/88572932 -- Mission St
# https://www.openstreetmap.org/relation/3406710 -- 14X to Daly City
# https://www.openstreetmap.org/relation/3406709 -- 14X to Downtown
# https://www.openstreetmap.org/relation/3406708 -- 14R to Mission
# https://www.openstreetmap.org/relation/3000713 -- 14R to Downtown
# ... and many more bus route relations
test.assert_has_feature(
    16, 10484, 25329, 'roads',
    {'name': 'Mission St.', 'is_bus_route': True})
