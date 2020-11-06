
SCHEMA = {
    "type": "record",
    "name": "lsst.v3_0.alert",
    "fields": [
        {
            "doc": "unique alert identifer",
            "name": "alertId",
            "type": "long"
        },
        {
            "name": "diaSource",
            "type": {
                "type": "record",
                "name": "lsst.v3_0.diaSource",
                "fields": [
                    {
                        "name": "diaSourceId",
                        "type": "long"
                    },
                    {
                        "name": "ccdVisitId",
                        "type": "long"
                    },
                    {
                        "default": None,
                        "name": "diaObjectId",
                        "type": [
                            "null",
                            "long"
                        ]
                    },
                    {
                        "default": None,
                        "name": "ssObjectId",
                        "type": [
                            "null",
                            "long"
                        ]
                    },
                    {
                        "default": None,
                        "name": "parentDiaSourceId",
                        "type": [
                            "null",
                            "long"
                        ]
                    },
                    {
                        "name": "midPointTai",
                        "type": "double"
                    },
                    {
                        "name": "filterName",
                        "type": "string"
                    },
                    {
                        "name": "programId",
                        "type": "int"
                    },
                    {
                        "name": "ra",
                        "type": "double"
                    },
                    {
                        "name": "decl",
                        "type": "double"
                    },
                    {
                        "default": None,
                        "name": "raErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "declErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "ra_decl_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "name": "x",
                        "type": "float"
                    },
                    {
                        "name": "y",
                        "type": "float"
                    },
                    {
                        "default": None,
                        "name": "xErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "yErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "x_y_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "name": "apFlux",
                        "type": "float"
                    },
                    {
                        "name": "apFluxErr",
                        "type": "float"
                    },
                    {
                        "name": "snr",
                        "type": "float"
                    },
                    {
                        "name": "psFlux",
                        "type": "float"
                    },
                    {
                        "name": "psFluxErr",
                        "type": "float"
                    },
                    {
                        "default": None,
                        "name": "psRa",
                        "type": [
                            "null",
                            "double"
                        ]
                    },
                    {
                        "default": None,
                        "name": "psDecl",
                        "type": [
                            "null",
                            "double"
                        ]
                    },
                    {
                        "default": None,
                        "name": "psRaErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "psDeclErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "psFlux_psRa_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "psFlux_psDecl_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "psRa_psDecl_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "psLnL",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "psChi2",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "psNdata",
                        "type": [
                            "null",
                            "int"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailFlux",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailRa",
                        "type": [
                            "null",
                            "double"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailDecl",
                        "type": [
                            "null",
                            "double"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailLength",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailAngle",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailFluxErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailRaErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailDeclErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailLengthErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailAngleErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailFlux_trailRa_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailFlux_trailDecl_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailFlux_trailLength_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailFlux_trailAngle_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailRa_trailDecl_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailRa_trailLength_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailRa_trailAngle_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailDecl_trailLength_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailDecl_trailAngle_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailLength_trailAngle_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailLnL",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailChi2",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "trailNdata",
                        "type": [
                            "null",
                            "int"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipMeanFlux",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipFluxDiff",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipRa",
                        "type": [
                            "null",
                            "double"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipDecl",
                        "type": [
                            "null",
                            "double"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipLength",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipAngle",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipMeanFluxErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipFluxDiffErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipRaErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipDeclErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipLengthErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipAngleErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipMeanFlux_dipFluxDiff_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipMeanFlux_dipRa_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipMeanFlux_dipDecl_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipMeanFlux_dipLength_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipMeanFlux_dipAngle_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipFluxDiff_dipRa_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipFluxDiff_dipDecl_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipFluxDiff_dipLength_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipFluxDiff_dipAngle_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipRa_dipDecl_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipRa_dipLength_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipRa_dipAngle_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipDecl_dipLength_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipDecl_dipAngle_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipLength_dipAngle_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipLnL",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipChi2",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "dipNdata",
                        "type": [
                            "null",
                            "int"
                        ]
                    },
                    {
                        "default": None,
                        "aliases": [
                            "fpFlux"
                        ],
                        "name": "totFlux",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "totFluxErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "diffFlux",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "diffFluxErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "aliases": [
                            "fpSky"
                        ],
                        "name": "fpBkgd",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "fpBkgdErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "ixx",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "iyy",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "ixy",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "ixxErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "iyyErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "ixyErr",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "ixx_iyy_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "ixx_ixy_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "iyy_ixy_Cov",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "ixxPSF",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "iyyPSF",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "ixyPSF",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "extendedness",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "default": None,
                        "name": "spuriousness",
                        "type": [
                            "null",
                            "float"
                        ]
                    },
                    {
                        "name": "flags",
                        "type": "long"
                    }
                ]
            }
        },
        {
            "default": None,
            "name": "prvDiaSources",
            "type": [
                "null",
                {
                    "type": "array",
                    "items": "lsst.v3_0.diaSource"
                }
            ]
        },
        {
            "default": None,
            "name": "prvDiaForcedSources",
            "type": [
                "null",
                {
                    "type": "array",
                    "items": {
                        "type": "record",
                        "name": "lsst.v3_0.diaForcedSource",
                        "fields": [
                            {
                                "name": "diaForcedSourceId",
                                "type": "long"
                            },
                            {
                                "name": "ccdVisitId",
                                "type": "long"
                            },
                            {
                                "name": "diaObjectId",
                                "type": "long"
                            },
                            {
                                "name": "midPointTai",
                                "type": "double"
                            },
                            {
                                "name": "filterName",
                                "type": "string"
                            },
                            {
                                "name": "psFlux",
                                "type": "float"
                            },
                            {
                                "name": "psFluxErr",
                                "type": "float"
                            },
                            {
                                "name": "totFlux",
                                "type": "float"
                            },
                            {
                                "name": "totFluxErr",
                                "type": "float"
                            }
                        ]
                    }
                }
            ]
        },
        {
            "default": None,
            "name": "prvDiaNondetectionLimits",
            "type": [
                "null",
                {
                    "type": "array",
                    "items": {
                        "type": "record",
                        "name": "lsst.v3_0.diaNondetectionLimit",
                        "fields": [
                            {
                                "name": "ccdVisitId",
                                "type": "long"
                            },
                            {
                                "name": "midPointTai",
                                "type": "double"
                            },
                            {
                                "name": "filterName",
                                "type": "string"
                            },
                            {
                                "name": "diaNoise",
                                "type": "float"
                            }
                        ]
                    }
                }
            ]
        },
        {
            "default": None,
            "name": "diaObject",
            "type": [
                "null",
                {
                    "type": "record",
                    "name": "lsst.v3_0.diaObject",
                    "fields": [
                        {
                            "name": "diaObjectId",
                            "type": "long"
                        },
                        {
                            "name": "ra",
                            "type": "double"
                        },
                        {
                            "name": "decl",
                            "type": "double"
                        },
                        {
                            "default": None,
                            "name": "raErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "declErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "ra_decl_Cov",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "name": "radecTai",
                            "type": "double"
                        },
                        {
                            "default": None,
                            "name": "pmRa",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "pmDecl",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "parallax",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "pmRaErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "pmDeclErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "parallaxErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "pmRa_pmDecl_Cov",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "pmRa_parallax_Cov",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "pmDecl_parallax_Cov",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "pmParallaxLnL",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "pmParallaxChi2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "pmParallaxNdata",
                            "type": [
                                "null",
                                "int"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uPSFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uPSFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uPSFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uPSFluxChi2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uPSFluxNdata",
                            "type": [
                                "null",
                                "int"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gPSFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gPSFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gPSFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gPSFluxChi2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gPSFluxNdata",
                            "type": [
                                "null",
                                "int"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rPSFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rPSFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rPSFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rPSFluxChi2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rPSFluxNdata",
                            "type": [
                                "null",
                                "int"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iPSFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iPSFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iPSFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iPSFluxChi2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iPSFluxNdata",
                            "type": [
                                "null",
                                "int"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zPSFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zPSFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zPSFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zPSFluxChi2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zPSFluxNdata",
                            "type": [
                                "null",
                                "int"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yPSFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yPSFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yPSFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yPSFluxChi2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yPSFluxNdata",
                            "type": [
                                "null",
                                "int"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uFPFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uFPFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uFPFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gFPFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gFPFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gFPFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rFPFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rFPFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rFPFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iFPFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iFPFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iFPFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zFPFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zFPFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zFPFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yFPFluxMean",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yFPFluxMeanErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yFPFluxSigma",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic21",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic22",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic23",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic24",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic25",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic26",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic27",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic28",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic29",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic30",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic31",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcPeriodic32",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic21",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic22",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic23",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic24",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic25",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic26",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic27",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic28",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic29",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic30",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic31",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcPeriodic32",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic21",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic22",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic23",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic24",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic25",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic26",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic27",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic28",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic29",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic30",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic31",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcPeriodic32",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic21",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic22",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic23",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic24",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic25",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic26",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic27",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic28",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic29",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic30",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic31",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcPeriodic32",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic21",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic22",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic23",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic24",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic25",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic26",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic27",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic28",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic29",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic30",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic31",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcPeriodic32",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic21",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic22",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic23",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic24",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic25",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic26",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic27",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic28",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic29",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic30",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic31",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcPeriodic32",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uLcNonPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gLcNonPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rLcNonPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iLcNonPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zLcNonPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic01",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic02",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic03",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic04",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic05",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic06",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic07",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic08",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic09",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic10",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic11",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic12",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic13",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic14",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic15",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic16",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic17",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic18",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic19",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yLcNonPeriodic20",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "nearbyObj1",
                            "type": [
                                "null",
                                "long"
                            ]
                        },
                        {
                            "default": None,
                            "name": "nearbyObj1Dist",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "nearbyObj1LnP",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "nearbyObj2",
                            "type": [
                                "null",
                                "long"
                            ]
                        },
                        {
                            "default": None,
                            "name": "nearbyObj2Dist",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "nearbyObj2LnP",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "nearbyObj3",
                            "type": [
                                "null",
                                "long"
                            ]
                        },
                        {
                            "default": None,
                            "name": "nearbyObj3Dist",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "nearbyObj3LnP",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "name": "flags",
                            "type": "long"
                        }
                    ]
                }
            ]
        },
        {
            "default": None,
            "name": "ssObject",
            "type": [
                "null",
                {
                    "type": "record",
                    "name": "lsst.v3_0.ssObject",
                    "fields": [
                        {
                            "name": "ssObjectId",
                            "type": "long"
                        },
                        {
                            "default": None,
                            "name": "q",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "e",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "i",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "lan",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "aop",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "M",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "epoch",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "qSigma",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "eSigma",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iSigma",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "lanSigma",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "aopSigma",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "MSigma",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "epochSigma",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "q_e_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "q_i_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "q_lan_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "q_aop_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "q_M_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "q_epoch_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "e_i_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "e_lan_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "e_aop_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "e_M_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "e_epoch_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "i_lan_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "i_aop_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "i_M_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "i_epoch_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "lan_aop_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "lan_M_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "lan_epoch_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "aop_M_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "aop_epoch_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "M_epoch_Cov",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "arc",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "orbFitLnL",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "orbFitChi2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "orbFitNdata",
                            "type": [
                                "null",
                                "int"
                            ]
                        },
                        {
                            "default": None,
                            "name": "MOID1",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "MOID2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "moidLon1",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "moidLon2",
                            "type": [
                                "null",
                                "double"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uH",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uHErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uG1",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uG1Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uG2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "uG2Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gH",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gHErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gG1",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gG1Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gG2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "gG2Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rH",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rHErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rG1",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rG1Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rG2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "rG2Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iH",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iHErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iG1",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iG1Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iG2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "iG2Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zH",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zHErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zG1",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zG1Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zG2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "zG2Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yH",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yHErr",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yG1",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yG1Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yG2",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "default": None,
                            "name": "yG2Err",
                            "type": [
                                "null",
                                "float"
                            ]
                        },
                        {
                            "name": "flags",
                            "type": "long"
                        }
                    ]
                }
            ]
        },
        {
            "default": None,
            "name": "cutoutDifference",
            "type": [
                "null",
                "bytes"
            ]
        },
        {
            "default": None,
            "name": "cutoutTemplate",
            "type": [
                "null",
                "bytes"
            ]
        }
    ]
}
