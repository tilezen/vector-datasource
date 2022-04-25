-- Deletes disputed borders from the natural earth tables that we do not want to render

with ne_id as
         (select *
          from (values
-- Northern Cyprus related
                    (1746708483),
                    (1746708491),
                    (1746708497),
                    (1746708639),
                    (1746708645),
                    (1746708649),
-- Somaliland
                    (1746705343),
-- Nagorno-karabakh
                    (1746705365),
                    (1746705369),
                    (1746705567),
                    (1746705575),
                    (1746705583),
                    (1746705599),
                    (1746705625),
                    (1746705713),
                    (1746705727),
                    (1746705781),
                    (1746705489),
                    (1746705589),
                    (1746705669),
                    (1746705677),
                    (1746705687),
                    (1746705695),
                    (1746705703),
                    (1746705737),
                    (1746705745),
                    (1746705757),
                    (1746705769),
-- Donbass
                    (1763286563),
                    (1763286519),
                    (1763286559)
-- Transnistria
                    (1746705379),
               ) as b (id)),

delete from

ne_10m_admin_0_boundary_lines_land
    ne_50m_admin_0_boundary_lines_land
    ne_110m_admin_0_boundary_lines_land
    ne_10m_admin_0_boundary_lines_disputed_areas
    ne_50m_admin_0_boundary_lines_disputed_areas
    ne_110m_admin_0_boundary_lines_disputed_areas
