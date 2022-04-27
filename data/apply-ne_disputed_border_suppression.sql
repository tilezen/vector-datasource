-- Recasts the fclass for certain disputed lines from the NE border tables to mark as Unrecognized or apply a viewpoint

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

-- Initially mark all viewpoints as Unrecognized. Subsequent steps will add some country specific views back.
ne_10m_admin_0_boundary_lines_land as (
update ne_10m_admin_0_boundary_lines_land l set
            featurecla = 'Unrecognized',
            fclass_ar = 'Unrecognized',
            fclass_bd = 'Unrecognized',
            fclass_br = 'Unrecognized',
            fclass_cn = 'Unrecognized',
            fclass_de = 'Unrecognized',
            fclass_eg = 'Unrecognized',
            fclass_es = 'Unrecognized',
            fclass_fr = 'Unrecognized',
            fclass_gb = 'Unrecognized',
            fclass_gr = 'Unrecognized',
            fclass_id = 'Unrecognized',
            fclass_il = 'Unrecognized',
            fclass_in = 'Unrecognized',
            fclass_iso = 'Unrecognized',
            fclass_it = 'Unrecognized',
            fclass_jp = 'Unrecognized',
            fclass_ko = 'Unrecognized',
            fclass_ma = 'Unrecognized',
            fclass_nl = 'Unrecognized',
            fclass_np = 'Unrecognized',
            fclass_pk = 'Unrecognized',
            fclass_pl = 'Unrecognized',
            fclass_ps = 'Unrecognized',
            fclass_pt = 'Unrecognized',
            fclass_ru = 'Unrecognized',
            fclass_sa = 'Unrecognized',
            fclass_se = 'Unrecognized',
            fclass_tr = 'Unrecognized',
            fclass_tw = 'Unrecognized',
            fclass_ua = 'Unrecognized',
            fclass_us = 'Unrecognized',
            fclass_vn = 'Unrecognized'
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
            featurecla = 'Unrecognized',
            fclass_ar = 'Unrecognized',
            fclass_bd = 'Unrecognized',
            fclass_br = 'Unrecognized',
            fclass_cn = 'Unrecognized',
            fclass_de = 'Unrecognized',
            fclass_eg = 'Unrecognized',
            fclass_es = 'Unrecognized',
            fclass_fr = 'Unrecognized',
            fclass_gb = 'Unrecognized',
            fclass_gr = 'Unrecognized',
            fclass_id = 'Unrecognized',
            fclass_il = 'Unrecognized',
            fclass_in = 'Unrecognized',
            fclass_iso = 'Unrecognized',
            fclass_it = 'Unrecognized',
            fclass_jp = 'Unrecognized',
            fclass_ko = 'Unrecognized',
            fclass_ma = 'Unrecognized',
            fclass_nl = 'Unrecognized',
            fclass_np = 'Unrecognized',
            fclass_pk = 'Unrecognized',
            fclass_pl = 'Unrecognized',
            fclass_ps = 'Unrecognized',
            fclass_pt = 'Unrecognized',
            fclass_ru = 'Unrecognized',
            fclass_sa = 'Unrecognized',
            fclass_se = 'Unrecognized',
            fclass_tr = 'Unrecognized',
            fclass_tw = 'Unrecognized',
            fclass_ua = 'Unrecognized',
            fclass_us = 'Unrecognized',
            fclass_vn = 'Unrecognized'
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
            featurecla = 'Unrecognized',
            fclass_ar = 'Unrecognized',
            fclass_bd = 'Unrecognized',
            fclass_br = 'Unrecognized',
            fclass_cn = 'Unrecognized',
            fclass_de = 'Unrecognized',
            fclass_eg = 'Unrecognized',
            fclass_es = 'Unrecognized',
            fclass_fr = 'Unrecognized',
            fclass_gb = 'Unrecognized',
            fclass_gr = 'Unrecognized',
            fclass_id = 'Unrecognized',
            fclass_il = 'Unrecognized',
            fclass_in = 'Unrecognized',
            fclass_iso = 'Unrecognized',
            fclass_it = 'Unrecognized',
            fclass_jp = 'Unrecognized',
            fclass_ko = 'Unrecognized',
            fclass_ma = 'Unrecognized',
            fclass_nl = 'Unrecognized',
            fclass_np = 'Unrecognized',
            fclass_pk = 'Unrecognized',
            fclass_pl = 'Unrecognized',
            fclass_ps = 'Unrecognized',
            fclass_pt = 'Unrecognized',
            fclass_ru = 'Unrecognized',
            fclass_sa = 'Unrecognized',
            fclass_se = 'Unrecognized',
            fclass_tr = 'Unrecognized',
            fclass_tw = 'Unrecognized',
            fclass_ua = 'Unrecognized',
            fclass_us = 'Unrecognized',
            fclass_vn = 'Unrecognized'
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
            featurecla = 'Unrecognized',
            fclass_ar = 'Unrecognized',
            fclass_bd = 'Unrecognized',
            fclass_br = 'Unrecognized',
            fclass_cn = 'Unrecognized',
            fclass_de = 'Unrecognized',
            fclass_eg = 'Unrecognized',
            fclass_es = 'Unrecognized',
            fclass_fr = 'Unrecognized',
            fclass_gb = 'Unrecognized',
            fclass_gr = 'Unrecognized',
            fclass_id = 'Unrecognized',
            fclass_il = 'Unrecognized',
            fclass_in = 'Unrecognized',
            fclass_iso = 'Unrecognized',
            fclass_it = 'Unrecognized',
            fclass_jp = 'Unrecognized',
            fclass_ko = 'Unrecognized',
            fclass_ma = 'Unrecognized',
            fclass_nl = 'Unrecognized',
            fclass_np = 'Unrecognized',
            fclass_pk = 'Unrecognized',
            fclass_pl = 'Unrecognized',
            fclass_ps = 'Unrecognized',
            fclass_pt = 'Unrecognized',
            fclass_ru = 'Unrecognized',
            fclass_sa = 'Unrecognized',
            fclass_se = 'Unrecognized',
            fclass_tr = 'Unrecognized',
            fclass_tw = 'Unrecognized',
            fclass_ua = 'Unrecognized',
            fclass_us = 'Unrecognized',
            fclass_vn = 'Unrecognized'
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
            featurecla = 'Unrecognized',
            fclass_ar = 'Unrecognized',
            fclass_bd = 'Unrecognized',
            fclass_br = 'Unrecognized',
            fclass_cn = 'Unrecognized',
            fclass_de = 'Unrecognized',
            fclass_eg = 'Unrecognized',
            fclass_es = 'Unrecognized',
            fclass_fr = 'Unrecognized',
            fclass_gb = 'Unrecognized',
            fclass_gr = 'Unrecognized',
            fclass_id = 'Unrecognized',
            fclass_il = 'Unrecognized',
            fclass_in = 'Unrecognized',
            fclass_iso = 'Unrecognized',
            fclass_it = 'Unrecognized',
            fclass_jp = 'Unrecognized',
            fclass_ko = 'Unrecognized',
            fclass_ma = 'Unrecognized',
            fclass_nl = 'Unrecognized',
            fclass_np = 'Unrecognized',
            fclass_pk = 'Unrecognized',
            fclass_pl = 'Unrecognized',
            fclass_ps = 'Unrecognized',
            fclass_pt = 'Unrecognized',
            fclass_ru = 'Unrecognized',
            fclass_sa = 'Unrecognized',
            fclass_se = 'Unrecognized',
            fclass_tr = 'Unrecognized',
            fclass_tw = 'Unrecognized',
            fclass_ua = 'Unrecognized',
            fclass_us = 'Unrecognized',
            fclass_vn = 'Unrecognized'
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
            fclass_ru = 'Reference line'
where l.ne_id in (
    select ne_id from nagorno_karabakh
    )),

ab_do_so_tr_ne_50m_admin_0_boundary_lines_land as (
update ne_50m_admin_0_boundary_lines_land l set
            fclass_ru = 'Reference line'
where l.ne_id in (
    select ne_id from nagorno_karabakh
    )),

ab_do_so_tr_ne_110m_admin_0_boundary_lines_land as (
update ne_110m_admin_0_boundary_lines_land l set
            fclass_ru = 'Reference line'
where l.ne_id in (
    select ne_id from nagorno_karabakh
    )),

ab_do_so_tr_ne_10m_admin_0_boundary_lines_disputed_areas as (
update ne_10m_admin_0_boundary_lines_disputed_areas l set
            fclass_ru = 'Reference line'
where l.ne_id in (
    select ne_id from nagorno_karabakh
    )),

ab_do_so_tr_ne_50m_admin_0_boundary_lines_disputed_areas as (
update ne_50m_admin_0_boundary_lines_disputed_areas l set
            fclass_ru = 'Reference line'
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
