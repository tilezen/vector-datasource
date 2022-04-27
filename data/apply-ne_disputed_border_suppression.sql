-- Recasts the fclass for certain disputed lines from the NE border tables to mark as unrecognized or apply a viewpoint

-- Abkahzia
with abkahzia as
         (select *
          from (values
                    (1746705383)
               ) as b (ne_id)),
-- Donbass
donbass as
    (select *
    from (values

                    (1763286563),
                    (1763286519),
                    (1763286559)
               ) as b (ne_id)),
-- Nagorno-karabakh
nagorno_karabakh as
    (select *
    from (values

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
                    (1746705769)
               ) as b (ne_id)),
-- Northern Cyprus
northern_cyprus as
    (select *
    from (values
                    (1746708483),
                    (1746708491),
                    (1746708497),
                    (1746708639),
                    (1746708645),
                    (1746708649)
               ) as b (ne_id)),
-- Somaliland
somaliland as
    (select *
    from (values
                    (1746705343)
               ) as b (ne_id)),
-- South Ossetia
south_ossetia as
    (select *
    from (values
                    (1746705385)
               ) as b (ne_id)),
-- Transnistria
transnistria as
    (select *
    from (values
                    (1746705379)
               ) as b (ne_id)),

-- Initially mark all viewpoints as unrecognized. Subsequent steps will add some country specific views back.
ne_10m_admin_0_boundary_lines_land as (
update ne_10m_admin_0_boundary_lines_land l set
            featurecla = 'unrecognized',
            fclass_ar = 'unrecognized',
            fclass_bd = 'unrecognized',
            fclass_br = 'unrecognized',
            fclass_cn = 'unrecognized',
            fclass_de = 'unrecognized',
            fclass_eg = 'unrecognized',
            fclass_es = 'unrecognized',
            fclass_fr = 'unrecognized',
            fclass_gb = 'unrecognized',
            fclass_gr = 'unrecognized',
            fclass_id = 'unrecognized',
            fclass_il = 'unrecognized',
            fclass_in = 'unrecognized',
            fclass_iso = 'unrecognized',
            fclass_it = 'unrecognized',
            fclass_jp = 'unrecognized',
            fclass_ko = 'unrecognized',
            fclass_ma = 'unrecognized',
            fclass_nl = 'unrecognized',
            fclass_np = 'unrecognized',
            fclass_pk = 'unrecognized',
            fclass_pl = 'unrecognized',
            fclass_ps = 'unrecognized',
            fclass_pt = 'unrecognized',
            fclass_ru = 'unrecognized',
            fclass_sa = 'unrecognized',
            fclass_se = 'unrecognized',
            fclass_tr = 'unrecognized',
            fclass_tw = 'unrecognized',
            fclass_ua = 'unrecognized',
            fclass_us = 'unrecognized',
            fclass_vn = 'unrecognized'
where l.ne_id in (
    select ne_id from abkahzia
    union
    select ne_id from donbass
    union
    select ne_id from nagorno_karabakh
    union
    select ne_id from northern_cyprus
    union
    select ne_id from somaliland
    union
    select ne_id from south_ossetia
    union
    select ne_id from transnistria
    )),

ne_50m_admin_0_boundary_lines_land as (
update ne_50m_admin_0_boundary_lines_land l set
            featurecla = 'unrecognized',
            fclass_ar = 'unrecognized',
            fclass_bd = 'unrecognized',
            fclass_br = 'unrecognized',
            fclass_cn = 'unrecognized',
            fclass_de = 'unrecognized',
            fclass_eg = 'unrecognized',
            fclass_es = 'unrecognized',
            fclass_fr = 'unrecognized',
            fclass_gb = 'unrecognized',
            fclass_gr = 'unrecognized',
            fclass_id = 'unrecognized',
            fclass_il = 'unrecognized',
            fclass_in = 'unrecognized',
            fclass_iso = 'unrecognized',
            fclass_it = 'unrecognized',
            fclass_jp = 'unrecognized',
            fclass_ko = 'unrecognized',
            fclass_ma = 'unrecognized',
            fclass_nl = 'unrecognized',
            fclass_np = 'unrecognized',
            fclass_pk = 'unrecognized',
            fclass_pl = 'unrecognized',
            fclass_ps = 'unrecognized',
            fclass_pt = 'unrecognized',
            fclass_ru = 'unrecognized',
            fclass_sa = 'unrecognized',
            fclass_se = 'unrecognized',
            fclass_tr = 'unrecognized',
            fclass_tw = 'unrecognized',
            fclass_ua = 'unrecognized',
            fclass_us = 'unrecognized',
            fclass_vn = 'unrecognized'
where l.ne_id in (
    select ne_id from abkahzia
    union
    select ne_id from donbass
    union
    select ne_id from nagorno_karabakh
    union
    select ne_id from northern_cyprus
    union
    select ne_id from somaliland
    union
    select ne_id from south_ossetia
    union
    select ne_id from transnistria
    )),

ne_110m_admin_0_boundary_lines_land as (
update ne_110m_admin_0_boundary_lines_land l set
            featurecla = 'unrecognized',
            fclass_ar = 'unrecognized',
            fclass_bd = 'unrecognized',
            fclass_br = 'unrecognized',
            fclass_cn = 'unrecognized',
            fclass_de = 'unrecognized',
            fclass_eg = 'unrecognized',
            fclass_es = 'unrecognized',
            fclass_fr = 'unrecognized',
            fclass_gb = 'unrecognized',
            fclass_gr = 'unrecognized',
            fclass_id = 'unrecognized',
            fclass_il = 'unrecognized',
            fclass_in = 'unrecognized',
            fclass_iso = 'unrecognized',
            fclass_it = 'unrecognized',
            fclass_jp = 'unrecognized',
            fclass_ko = 'unrecognized',
            fclass_ma = 'unrecognized',
            fclass_nl = 'unrecognized',
            fclass_np = 'unrecognized',
            fclass_pk = 'unrecognized',
            fclass_pl = 'unrecognized',
            fclass_ps = 'unrecognized',
            fclass_pt = 'unrecognized',
            fclass_ru = 'unrecognized',
            fclass_sa = 'unrecognized',
            fclass_se = 'unrecognized',
            fclass_tr = 'unrecognized',
            fclass_tw = 'unrecognized',
            fclass_ua = 'unrecognized',
            fclass_us = 'unrecognized',
            fclass_vn = 'unrecognized'
where l.ne_id in (
    select ne_id from abkahzia
    union
    select ne_id from donbass
    union
    select ne_id from nagorno_karabakh
    union
    select ne_id from northern_cyprus
    union
    select ne_id from somaliland
    union
    select ne_id from south_ossetia
    union
    select ne_id from transnistria
    )),

ne_10m_admin_0_boundary_lines_disputed_areas as (
update ne_10m_admin_0_boundary_lines_disputed_areas l set
            featurecla = 'unrecognized',
            fclass_ar = 'unrecognized',
            fclass_bd = 'unrecognized',
            fclass_br = 'unrecognized',
            fclass_cn = 'unrecognized',
            fclass_de = 'unrecognized',
            fclass_eg = 'unrecognized',
            fclass_es = 'unrecognized',
            fclass_fr = 'unrecognized',
            fclass_gb = 'unrecognized',
            fclass_gr = 'unrecognized',
            fclass_id = 'unrecognized',
            fclass_il = 'unrecognized',
            fclass_in = 'unrecognized',
            fclass_iso = 'unrecognized',
            fclass_it = 'unrecognized',
            fclass_jp = 'unrecognized',
            fclass_ko = 'unrecognized',
            fclass_ma = 'unrecognized',
            fclass_nl = 'unrecognized',
            fclass_np = 'unrecognized',
            fclass_pk = 'unrecognized',
            fclass_pl = 'unrecognized',
            fclass_ps = 'unrecognized',
            fclass_pt = 'unrecognized',
            fclass_ru = 'unrecognized',
            fclass_sa = 'unrecognized',
            fclass_se = 'unrecognized',
            fclass_tr = 'unrecognized',
            fclass_tw = 'unrecognized',
            fclass_ua = 'unrecognized',
            fclass_us = 'unrecognized',
            fclass_vn = 'unrecognized'
where l.ne_id in (
    select ne_id from abkahzia
    union
    select ne_id from donbass
    union
    select ne_id from nagorno_karabakh
    union
    select ne_id from northern_cyprus
    union
    select ne_id from somaliland
    union
    select ne_id from south_ossetia
    union
    select ne_id from transnistria
    )),

ne_50m_admin_0_boundary_lines_disputed_areas as (
update ne_50m_admin_0_boundary_lines_disputed_areas l set
            featurecla = 'unrecognized',
            fclass_ar = 'unrecognized',
            fclass_bd = 'unrecognized',
            fclass_br = 'unrecognized',
            fclass_cn = 'unrecognized',
            fclass_de = 'unrecognized',
            fclass_eg = 'unrecognized',
            fclass_es = 'unrecognized',
            fclass_fr = 'unrecognized',
            fclass_gb = 'unrecognized',
            fclass_gr = 'unrecognized',
            fclass_id = 'unrecognized',
            fclass_il = 'unrecognized',
            fclass_in = 'unrecognized',
            fclass_iso = 'unrecognized',
            fclass_it = 'unrecognized',
            fclass_jp = 'unrecognized',
            fclass_ko = 'unrecognized',
            fclass_ma = 'unrecognized',
            fclass_nl = 'unrecognized',
            fclass_np = 'unrecognized',
            fclass_pk = 'unrecognized',
            fclass_pl = 'unrecognized',
            fclass_ps = 'unrecognized',
            fclass_pt = 'unrecognized',
            fclass_ru = 'unrecognized',
            fclass_sa = 'unrecognized',
            fclass_se = 'unrecognized',
            fclass_tr = 'unrecognized',
            fclass_tw = 'unrecognized',
            fclass_ua = 'unrecognized',
            fclass_us = 'unrecognized',
            fclass_vn = 'unrecognized'
where l.ne_id in (
    select ne_id from abkahzia
    union
    select ne_id from donbass
    union
    select ne_id from nagorno_karabakh
    union
    select ne_id from northern_cyprus
    union
    select ne_id from somaliland
    union
    select ne_id from south_ossetia
    union
    select ne_id from transnistria
    )),


-- Add Russian view to Abkhazia, Donbass, South Ossetia, Transnistria
ru_ne_10m_admin_0_boundary_lines_land as (
update ne_10m_admin_0_boundary_lines_land l set
            fclass_ru = 'country'
where l.ne_id in (
    select ne_id from abkahzia
    union
    select ne_id from donbass
    union
    select ne_id from south_ossetia
    union
    select ne_id from transnistria
    )),

ru_ne_50m_admin_0_boundary_lines_land as (
update ne_50m_admin_0_boundary_lines_land l set
            fclass_ru = 'country'
where l.ne_id in (
    select ne_id from abkahzia
    union
    select ne_id from donbass
    union
    select ne_id from south_ossetia
    union
    select ne_id from transnistria
    )),

ru_ne_110m_admin_0_boundary_lines_land as (
update ne_110m_admin_0_boundary_lines_land l set
            fclass_ru = 'country'
where l.ne_id in (
    select ne_id from abkahzia
    union
    select ne_id from donbass
    union
    select ne_id from south_ossetia
    union
    select ne_id from transnistria
    )),

ru_ne_10m_admin_0_boundary_lines_disputed_areas as (
update ne_10m_admin_0_boundary_lines_disputed_areas l set
            fclass_ru = 'country'
where l.ne_id in (
    select ne_id from abkahzia
    union
    select ne_id from donbass
    union
    select ne_id from south_ossetia
    union
    select ne_id from transnistria
    )),

ru_ne_50m_admin_0_boundary_lines_disputed_areas as (
update ne_50m_admin_0_boundary_lines_disputed_areas l set
            fclass_ru = 'country'
where l.ne_id in (
    select ne_id from abkahzia
    union
    select ne_id from donbass
    union
    select ne_id from south_ossetia
    union
    select ne_id from transnistria
    )),


-- Add Russian disputed view to Nagorno-Karabakh
ab_do_so_tr_ne_10m_admin_0_boundary_lines_land as (
update ne_10m_admin_0_boundary_lines_land l set
            fclass_ru = ''
where l.ne_id in (
    select ne_id from nagorno_karabakh
    )),

ab_do_so_tr_ne_50m_admin_0_boundary_lines_land as (
update ne_50m_admin_0_boundary_lines_land l set
            fclass_ru = ''
where l.ne_id in (
    select ne_id from nagorno_karabakh
    )),

ab_do_so_tr_ne_110m_admin_0_boundary_lines_land as (
update ne_110m_admin_0_boundary_lines_land l set
            fclass_ru = ''
where l.ne_id in (
    select ne_id from nagorno_karabakh
    )),

ab_do_so_tr_ne_10m_admin_0_boundary_lines_disputed_areas as (
update ne_10m_admin_0_boundary_lines_disputed_areas l set
            fclass_ru = ''
where l.ne_id in (
    select ne_id from nagorno_karabakh
    )),

ab_do_so_tr_ne_50m_admin_0_boundary_lines_disputed_areas as (
update ne_50m_admin_0_boundary_lines_disputed_areas l set
            fclass_ru = ''
where l.ne_id in (
    select ne_id from nagorno_karabakh
    )),


-- Add Turkish view to Northern Cyprus
tr_ne_10m_admin_0_boundary_lines_land as (
update ne_10m_admin_0_boundary_lines_land l set
            fclass_tr = 'country'
where l.ne_id in (
    select ne_id from northern_cyprus
    )),

tr_ne_50m_admin_0_boundary_lines_land as (
update ne_50m_admin_0_boundary_lines_land l set
            fclass_tr = 'country'
where l.ne_id in (
    select ne_id from northern_cyprus
    )),

tr_ne_110m_admin_0_boundary_lines_land as (
update ne_110m_admin_0_boundary_lines_land l set
            fclass_tr = 'country'
where l.ne_id in (
    select ne_id from northern_cyprus
    )),

tr_ne_10m_admin_0_boundary_lines_disputed_areas as (
update ne_10m_admin_0_boundary_lines_disputed_areas l set
            fclass_tr = 'country'
where l.ne_id in (
    select ne_id from northern_cyprus
    )),

tr_ne_50m_admin_0_boundary_lines_disputed_areas as (
update ne_50m_admin_0_boundary_lines_disputed_areas l set
            fclass_tr = 'country'
where l.ne_id in (
    select ne_id from northern_cyprus
    )),


-- Add Taiwanese view to Somaliland
tw_ne_10m_admin_0_boundary_lines_land as (
update ne_10m_admin_0_boundary_lines_land l set
            fclass_tw = 'country'
where l.ne_id in (
    select ne_id from somaliland
    )),

tw_ne_50m_admin_0_boundary_lines_land as (
update ne_50m_admin_0_boundary_lines_land l set
            fclass_tw = 'country'
where l.ne_id in (
    select ne_id from somaliland
    )),

tw_ne_110m_admin_0_boundary_lines_land as (
update ne_110m_admin_0_boundary_lines_land l set
            fclass_tw = 'country'
where l.ne_id in (
    select ne_id from somaliland
    )),

tw_ne_10m_admin_0_boundary_lines_disputed_areas as (
update ne_10m_admin_0_boundary_lines_disputed_areas l set
            fclass_tw = 'country'
where l.ne_id in (
    select ne_id from somaliland
    ))

update ne_50m_admin_0_boundary_lines_disputed_areas l set
            fclass_tw = 'country'
where l.ne_id in (
    select ne_id from somaliland
    )
