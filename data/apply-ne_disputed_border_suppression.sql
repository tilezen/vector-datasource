-- Recasts the fclass for certain disputed lines from the NE border tables to mark as Unrecognized or apply a viewpoint

-- Dispute brk_a3 ids for reference
-- Abkahzia
-- 'B35'
-- Donbass
-- 'C02'
-- 'B90'
-- 'C03'
-- Nagorno-karabakh
-- 'B38'
-- Northern Cyprus
-- 'B20'
-- 'B43'
-- Somaliland
-- 'B30'
-- South Ossetia
-- 'B37'
-- Transnistria
-- 'B36'

-- Initially mark all viewpoints as Unrecognized. Subsequent steps will add some country specific views back.
update ne_10m_admin_0_boundary_lines_land set
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
where brk_a3 in ('B35', 'C02', 'C03', 'B90', 'B38', 'B20', 'B30', 'B43', 'B37', 'B36');

update ne_50m_admin_0_boundary_lines_land set
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
where brk_a3 in ('B35', 'C02', 'C03', 'B90', 'B38', 'B20', 'B30', 'B43', 'B37', 'B36');

update ne_110m_admin_0_boundary_lines_land set
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
where brk_a3 in ('B35', 'C02', 'C03', 'B90', 'B38', 'B20', 'B30', 'B43', 'B37', 'B36');

update ne_10m_admin_0_boundary_lines_disputed_areas set
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
where brk_a3 in ('B35', 'C02', 'C03', 'B90', 'B38', 'B20', 'B30', 'B43', 'B37', 'B36');

update ne_50m_admin_0_boundary_lines_disputed_areas set
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
where brk_a3 in ('B35', 'C02', 'C03', 'B90', 'B38', 'B20', 'B30', 'B43', 'B37', 'B36');


-- Add Russian view to Abkhazia, Donbass, South Ossetia, Transnistria
update ne_10m_admin_0_boundary_lines_land set
            fclass_ru = 'country'
where brk_a3 in ('B35', 'C02', 'C03', 'B90', 'B37', 'B36');

update ne_50m_admin_0_boundary_lines_land set
            fclass_ru = 'country'
where brk_a3 in ('B35', 'C02', 'C03', 'B90', 'B37', 'B36');

update ne_110m_admin_0_boundary_lines_land set
            fclass_ru = 'country'
where brk_a3 in ('B35', 'C02', 'C03', 'B90', 'B37', 'B36');

update ne_10m_admin_0_boundary_lines_disputed_areas set
            fclass_ru = 'country'
where brk_a3 in ('B35', 'C02', 'C03', 'B90', 'B37', 'B36');

update ne_50m_admin_0_boundary_lines_disputed_areas set
            fclass_ru = 'country'
where brk_a3 in ('B35', 'C02', 'C03', 'B90', 'B37', 'B36');


-- Add Russian disputed view to Nagorno-Karabakh
update ne_10m_admin_0_boundary_lines_land set
            fclass_ru = 'Reference line'
where brk_a3 in ('B38');

update ne_50m_admin_0_boundary_lines_land set
            fclass_ru = 'Reference line'
where brk_a3 in ('B38');

update ne_110m_admin_0_boundary_lines_land set
            fclass_ru = 'Reference line'
where brk_a3 in ('B38');

update ne_10m_admin_0_boundary_lines_disputed_areas set
            fclass_ru = 'Reference line'
where brk_a3 in ('B38');

update ne_50m_admin_0_boundary_lines_disputed_areas set
            fclass_ru = 'Reference line'
where brk_a3 in ('B38');


-- Add Turkish view to Northern Cyprus
update ne_10m_admin_0_boundary_lines_land set
            fclass_tr = 'country'
where brk_a3 in ('B20', 'B43');

update ne_50m_admin_0_boundary_lines_land set
            fclass_tr = 'country'
where brk_a3 in ('B20', 'B43');

update ne_110m_admin_0_boundary_lines_land set
            fclass_tr = 'country'
where brk_a3 in ('B20', 'B43');

update ne_10m_admin_0_boundary_lines_disputed_areas set
            fclass_tr = 'country'
where brk_a3 in ('B20', 'B43');

update ne_50m_admin_0_boundary_lines_disputed_areas set
            fclass_tr = 'country'
where brk_a3 in ('B20', 'B43');


-- Add Taiwanese view to Somaliland
update ne_10m_admin_0_boundary_lines_land set
            fclass_tw = 'country'
where brk_a3 in ('B30');

update ne_50m_admin_0_boundary_lines_land set
            fclass_tw = 'country'
where brk_a3 in ('B30');

update ne_110m_admin_0_boundary_lines_land set
            fclass_tw = 'country'
where brk_a3 in ('B30');

update ne_10m_admin_0_boundary_lines_disputed_areas set
            fclass_tw = 'country'
where brk_a3 in ('B30');

update ne_50m_admin_0_boundary_lines_disputed_areas set
            fclass_tw = 'country'
where brk_a3 in ('B30');


-- Remove Taiwanese view for nine dash line
update ne_10m_admin_0_boundary_lines_maritime_indicator_chn set
            fclass_tw = 'Unrecognized';

update ne_50m_admin_0_boundary_lines_maritime_indicator_chn set
            fclass_tw = 'Unrecognized';
