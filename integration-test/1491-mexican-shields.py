from . import FixtureTest


class MexicanShieldText(FixtureTest):
    def test_mx_mex_prefix(self):
        import dsl

        z, x, y = (16, 13978, 28930)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/285597347
            dsl.way(
                285597347,
                dsl.tile_diagonal(z, x, y),
                {
                    "lanes": "2",
                    "name": "Guadalajara - Zapotlanejo",
                    "oneway": "yes",
                    "source": "openstreetmap.org",
                    "toll": "yes",
                    "ref": "MEX 15D",
                    "highway": "motorway",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 285597347,
                "shield_text": "15D",
                "network": "MX:MEX",
            },
        )

    def test_mx_mex_prefix_no_space(self):
        import dsl

        z, x, y = (16, 14871, 29411)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/184722720
            dsl.way(
                184722720,
                dsl.tile_diagonal(z, x, y),
                {
                    "source": "openstreetmap.org",
                    "ref": "MEX610",
                    "name": u"Las Palomas - Tecomatl\xe1n",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 184722720,
                "shield_text": "610",
                "network": "MX:MEX",
            },
        )

    def test_mx_mex_country_code(self):
        import dsl

        z, x, y = (16, 14581, 28924)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/317748112
            dsl.way(
                317748112,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "80",
                    "lanes": "2",
                    "name": u"San Juan del R\xedo - Xilitla",
                    "source": "openstreetmap.org",
                    "surface": "asphalt",
                    "width": "10.0",
                    "oneway": "yes",
                    "nat_ref": "120",
                    "ref": "MEX 120",
                    "highway": "primary",
                },
            ),
            dsl.relation(
                1,
                {
                    "distance": "718.31",
                    "name": "Carretera Federal 120",
                    "type": "route",
                    "route": "road",
                    "source": "openstreetmap.org",
                    "ref": "MEX 120",
                    "network": "MEX",
                },
                ways=[317748112],
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 317748112,
                "shield_text": "120",
                "network": "MX:MEX",
            },
        )

    def test_mx_mex_country_code_only_relation(self):
        import dsl

        z, x, y = (16, 14581, 28924)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/317748112
            # note: with the "ref" tag removed from the way - to test we get
            # the information from the relation and normalize it to MX:MEX.
            dsl.way(
                317748112,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "80",
                    "lanes": "2",
                    "name": u"San Juan del R\xedo - Xilitla",
                    "source": "openstreetmap.org",
                    "surface": "asphalt",
                    "width": "10.0",
                    "oneway": "yes",
                    "nat_ref": "120",
                    "highway": "primary",
                },
            ),
            dsl.relation(
                1,
                {
                    "distance": "718.31",
                    "name": "Carretera Federal 120",
                    "type": "route",
                    "route": "road",
                    "source": "openstreetmap.org",
                    "ref": "MEX 120",
                    "network": "MEX",
                },
                ways=[317748112],
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 317748112,
                "shield_text": "120",
                "network": "MX:MEX",
            },
        )

    def test_mx_ags(self):
        import dsl

        z, x, y = (16, 14139, 28659)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/95067892
            dsl.way(
                95067892,
                dsl.tile_diagonal(z, x, y),
                {
                    "lanes": "2",
                    "name": "Carretera a Valladolid",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "ref": "AGS 18",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 95067892,
                "shield_text": "18",
                "network": "MX:AGU",
            },
        )

    def test_mx_bc(self):
        import dsl

        z, x, y = (16, 11769, 26490)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/32838789
            dsl.way(
                32838789,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "60",
                    "name": "Carretera Mexicali-Algodones",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "no",
                    "ref": "BC 2",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 32838789,
                "shield_text": "2",
                "network": "MX:BCN",
            },
        )

    def test_mx_bcs(self):
        import dsl

        z, x, y = (16, 12706, 28295)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/313016682
            dsl.way(
                313016682,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "40",
                    "name": "Camino Rancho San Isidro",
                    "surface": "unpaved",
                    "source": "openstreetmap.org",
                    "oneway": "no",
                    "ref": "BCS 3",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 313016682,
                "shield_text": "3",
                "network": "MX:BCS",
            },
        )

    def test_mx_cam(self):
        import dsl

        z, x, y = (16, 16413, 29103)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/437130142
            dsl.way(
                437130142,
                dsl.tile_diagonal(z, x, y),
                {
                    "name": u"Carretera Hopelch\xe9n-Dzibalch\xe9n",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "yes",
                    "ref": "CAM 269",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 437130142,
                "shield_text": "269",
                "network": "MX:CAM",
            },
        )

    def test_mx_chis(self):
        import dsl

        z, x, y = (16, 15973, 30018)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/229011988
            dsl.way(
                229011988,
                dsl.tile_diagonal(z, x, y),
                {
                    "lanes": "2",
                    "name": "8 Avenida Norte",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "yes",
                    "ref": "CHIS 229",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 229011988,
                "shield_text": "229",
                "network": "MX:CHP",
            },
        )

    def test_mx_chih(self):
        import dsl

        z, x, y = (16, 13639, 27527)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/28049838
            dsl.way(
                28049838,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "80",
                    "name": "Entrada La Perla-La Mula",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "ref": "CHIH 67",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 28049838,
                "shield_text": "67",
                "network": "MX:CHH",
            }
        )

    def test_mx_coah(self):
        import dsl

        z, x, y = (16, 14168, 27974)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/121175840
            dsl.way(
                121175840,
                dsl.tile_diagonal(z, x, y),
                {
                    "source": "openstreetmap.org",
                    "ref": "COAH 102",
                    "highway": "secondary",
                    "oneway": "yes",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 121175840,
                "shield_text": "102",
                "network": "MX:COA",
            }
        )

    def test_mx_col(self):
        import dsl

        z, x, y = (16, 13824, 29168)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/398850236
            dsl.way(
                398850236,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "60",
                    "lanes": "2",
                    "name": u"Carretera Villa de \xc1lvarez-Minatitl\xe1n",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "yes",
                    "ref": "COL 3",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 398850236,
                "shield_text": "3",
                "network": "MX:COL",
            }
        )

    def test_mx_dgo(self):
        import dsl

        z, x, y = (16, 13642, 28286)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/60750191
            dsl.way(
                60750191,
                dsl.tile_diagonal(z, x, y),
                {
                    "source": "openstreetmap.org",
                    "ref": "DGO 73",
                    "name": "DGO 73",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 60750191,
                "shield_text": "73",
                "network": "MX:DUR",
            }
        )

    def test_mx_gto(self):
        import dsl

        z, x, y = (16, 14385, 28867)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/67627985
            dsl.way(
                67627985,
                dsl.tile_diagonal(z, x, y),
                {
                    "source": "openstreetmap.org",
                    "ref": "GTO 110",
                    "surface": "asphalt",
                    "highway": "secondary",
                    "oneway": "no",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 67627985,
                "shield_text": "110",
                "network": "MX:GUA",
            }
        )

    def test_mx_gro(self):
        import dsl

        z, x, y = (16, 14706, 29391)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/401747860
            dsl.way(
                401747860,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "20",
                    "lanes": "1",
                    "name": u"Carretera Atenango del R\xedo",
                    "tunnel": "yes",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "yes",
                    "ref": "GRO 1",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 401747860,
                "shield_text": "1",
                "network": "MX:GRO",
            }
        )

    def test_mx_hgo(self):
        import dsl

        z, x, y = (16, 14805, 28959)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/303422979
            dsl.way(
                303422979,
                dsl.tile_diagonal(z, x, y),
                {
                    "source": "openstreetmap.org",
                    "ref": "HGO 37",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 303422979,
                "shield_text": "37",
                "network": "MX:HID",
            }
        )

    def test_mx_jal(self):
        import dsl

        z, x, y = (16, 14095, 28769)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/106292685
            dsl.way(
                106292685,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "80",
                    "name": "Carretera Villa Hidalgo-Teocaltiche",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "no",
                    "ref": "JAL 211",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 106292685,
                "shield_text": "211",
                "network": "MX:JAL",
            }
        )

    def test_mx_mich(self):
        import dsl

        z, x, y = (16, 14209, 29030)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/112474675
            dsl.way(
                112474675,
                dsl.tile_diagonal(z, x, y),
                {
                    "name": u"Carretera Zin\xe1paro-Villa Morelos",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "no",
                    "ref": "MICH 27",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 112474675,
                "shield_text": "27",
                "network": "MX:MIC",
            }
        )

    def test_mx_mor(self):
        import dsl

        z, x, y = (16, 14698, 29296)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/53542659
            dsl.way(
                53542659,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "40",
                    "lanes": "1",
                    "name": "Carretera Jojutla-Alpuyeca",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "yes",
                    "ref": "MOR 21",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 53542659,
                "shield_text": "21",
                "network": "MX:MOR",
            }
        )

    def test_mx_nay(self):
        import dsl

        z, x, y = (16, 13627, 28820)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/272209751
            dsl.way(
                272209751,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "60",
                    "name": u"Ramal a Ixtapan de la Concepci\xf3n",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "ref": "NAY 16",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 272209751,
                "shield_text": "16",
                "network": "MX:NAY",
            }
        )

    def test_mx_nl(self):
        import dsl

        z, x, y = (16, 14542, 27909)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/94987221
            dsl.way(
                94987221,
                dsl.tile_diagonal(z, x, y),
                {
                    "source": "openstreetmap.org",
                    "ref": "NL 54",
                    "highway": "secondary",
                    "oneway": "yes",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 94987221,
                "shield_text": "54",
                "network": "MX:NLE",
            }
        )

    def test_mx_oax(self):
        import dsl

        z, x, y = (16, 15430, 29698)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/253923941
            dsl.way(
                253923941,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "60",
                    "name": "Carretera Guevea de Humboldt-Ciudad Ixtepec",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "no",
                    "ref": "OAX 49",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 253923941,
                "shield_text": "49",
                "network": "MX:OAX",
            }
        )

    def test_mx_pue(self):
        import dsl

        z, x, y = (16, 14842, 29257)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/40128815
            dsl.way(
                40128815,
                dsl.tile_diagonal(z, x, y),
                {
                    "bridge": "yes",
                    "layer": "1",
                    "source": "openstreetmap.org",
                    "oneway": "no",
                    "ref": "PUE 438D",
                    "highway": "motorway",
                },
            ),
            dsl.relation(
                1,
                {
                    "name": "Autopista Siglo XXI",
                    "route": "road",
                    "source:date": "01-15-2017",
                    "source": "openstreetmap.org",
                    "type": "route",
                    "highway": "secondary",
                },
                ways=[40128815],
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 40128815,
                "shield_text": "438D",
                "network": "MX:PUE"}
        )

    def test_mx_qro(self):
        import dsl

        z, x, y = (16, 14493, 28930)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/60930132
            dsl.way(
                60930132,
                dsl.tile_diagonal(z, x, y),
                {
                    "lanes": "2",
                    "name": u"Anillo Vial Jun\xedpero Serra",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "yes",
                    "ref": "QRO 40",
                    "highway": "primary",
                },
            ),
            dsl.relation(
                1,
                {
                    "distance": "27.93Km",
                    "name": u"Anillo Vial Jun\xedpero Serra",
                    "type": "route",
                    "route": "road",
                    "source": "openstreetmap.org",
                    "operator": "CECQRO",
                    "ref": "QRO 40",
                    "network": "QRO",
                },
                ways=[60930132],
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 60930132,
                "shield_text": "40",
                "network": "MX:QUE",
            }
        )

    def test_mx_qroo(self):
        import dsl

        z, x, y = (16, 16851, 28789)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/399152055
            dsl.way(
                399152055,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "80",
                    "name": "Carretera Chiquila-El Ideal",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "no",
                    "ref": "Q. ROO 5",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 399152055,
                "shield_text": "5",
                "network": "MX:ROO",
            }
        )

    def test_mx_qroo2(self):
        import dsl

        z, x, y = (16, 16658, 29216)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/27577748
            dsl.way(
                27577748,
                dsl.tile_diagonal(z, x, y),
                {
                    "source": "openstreetmap.org",
                    "ref": "ROO 16",
                    "name": "Ramal a Margarita Maza",
                    "highway": "secondary",
                    "surface": "asphalt",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 27577748,
                "shield_text": "16",
                "network": "MX:ROO",
            }
        )

    def test_mx_sin(self):
        import dsl

        z, x, y = (16, 12892, 27878)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/113581011
            dsl.way(
                113581011,
                dsl.tile_diagonal(z, x, y),
                {
                    "source": "openstreetmap.org",
                    "ref": "SIN 102",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 113581011,
                "shield_text": "102",
                "network": "MX:SIN",
            }
        )

    def test_mx_slp(self):
        import dsl

        z, x, y = (16, 14396, 28636)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/28926839
            dsl.way(
                28926839,
                dsl.tile_diagonal(z, x, y),
                {
                    "lanes": "3",
                    "name": "Antonio Rocha Cordero",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "yes",
                    "ref": "SLP 32",
                    "highway": "primary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 28926839,
                "shield_text": "32",
                "network": "MX:SLP",
            }
        )

    def test_mx_son(self):
        import dsl

        z, x, y = (16, 12740, 27561)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/29943430
            dsl.way(
                29943430,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "60",
                    "lanes": "4",
                    "name": u"Boulevard Rodolfo El\xedas Calles",
                    "surface": "paved",
                    "source": "openstreetmap.org",
                    "oneway": "no",
                    "ref": "SON 132",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 29943430,
                "shield_text": "132",
                "network": "MX:SON",
            }
        )

    def test_mx_ver(self):
        import dsl

        z, x, y = (16, 15047, 28999)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/323155576
            dsl.way(
                323155576,
                dsl.tile_diagonal(z, x, y),
                {
                    "maxspeed": "70",
                    "lanes": "2",
                    "name": "Ramal a Coyutla",
                    "source": "openstreetmap.org",
                    "surface": "asphalt",
                    "width": "6",
                    "ref": "VER 127",
                    "smoothness": "intermediate",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 323155576,
                "shield_text": "127",
                "network": "MX:VER",
            }
        )

    def test_mx_yuc(self):
        import dsl

        z, x, y = (16, 16692, 28851)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/131913202
            dsl.way(
                131913202,
                dsl.tile_diagonal(z, x, y),
                {
                    "source:name": "INEGI",
                    "maxspeed": "80",
                    "name": u"Carretera Sucil\xe1 - Calotmul",
                    "source:maxspeed": "INEGI",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "no",
                    "ref": "YUC 33",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 131913202,
                "shield_text": "33",
                "network": "MX:YUC",
            }
        )

    def test_mx_zac(self):
        import dsl

        z, x, y = (16, 14024, 28373)

        self.generate_fixtures(
            dsl.is_in("MX", z, x, y),
            # https://www.openstreetmap.org/way/29183967
            dsl.way(
                29183967,
                dsl.tile_diagonal(z, x, y),
                {
                    "name": "Carretera Plateros-La Salada-Rancho Grande",
                    "surface": "asphalt",
                    "source": "openstreetmap.org",
                    "oneway": "no",
                    "ref": "ZAC 77",
                    "highway": "secondary",
                },
            ),
        )

        self.assert_has_feature(
            z, x, y, "roads", {
                "id": 29183967,
                "shield_text": "77",
                "network": "MX:ZAC",
            }
        )

    def test_mx_cmx_circuito_interior(self):
        import dsl

        z, x, y = (16, 14720, 29154)

        self.generate_fixtures(
            dsl.is_in('MX', z, x, y),
            # https://www.openstreetmap.org/way/123899735
            dsl.way(123899735, dsl.tile_diagonal(z, x, y), {
                'name': 'Circuito Interior', 'source': 'openstreetmap.org',
                'alt_name': 'Circuito Bicentenario', 'oneway': 'yes',
                'foot': 'no', 'ref': 'INT', 'highway': 'motorway',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 123899735,
                'shield_text': type(None),
                'network': 'MX:CMX:INT',
            })

    def test_mx_cmx_ext(self):
        import dsl

        z, x, y = (16, 14746, 29161)

        self.generate_fixtures(
            dsl.is_in('MX', z, x, y),
            # https://www.openstreetmap.org/way/107457633
            dsl.way(107457633, dsl.tile_diagonal(z, x, y), {
                'source': 'openstreetmap.org', 'ref': 'EXT',
                'highway': 'motorway', 'oneway': 'yes',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 107457633,
                'shield_text': type(None),
                'network': 'MX:CMX:EXT',
            })
