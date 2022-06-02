EE_PRODUCTS = {
    'ECMWF_ERA5_DAILY': {
        'total_precipitation': {
            'description': 'Total precipitation (daily sums)',
            'collection': 'ECMWF/ERA5/DAILY',
            'band': 'total_precipitation',
            'vis_params': {
                'min': 0,
                'max': 0.1,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
                },
            'date': '2020-07-09T00:00:00',
            'start_date': '1979-01-02T00:00:00Z',
            'end_date': None
        }
    },
    'GLDAS2_1': {
        'Albedo_inst': {
            'description': 'Albedo',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Albedo_inst',
            'vis_params': {
                'min': 4.5,
                'max': 82.5,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2022-01-01',
            'end_date': '2022-01-02'
        },
        'AvgSurfT_inst': {
            'description': 'Average surface skin temperature',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'AvgSurfT_inst',
            'vis_params': {
                'min': 187.0,
                'max': 1323.5,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'CanopInt_inst': {
            'description': 'Plant canopy surface water',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'CanopInt_inst',
            'vis_params': {
                'min': 0,
                'max': 1,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'ECanop_tavg': {
            'description': 'Canopy water evaporation',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'ECanop_tavg',
            'vis_params': {
                'min': 0,
                'max': 1274,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'ESoil_tavg': {
            'description': 'Direct evaporation from bare soil',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'ESoil_tavg',
            'vis_params': {
                'min': 0,
                'max': 2276,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Evap_tavg': {
            'description': 'Evapotranspiration',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Evap_tavg',
            'vis_params': {
                'min': 0,
                'max': 0.003,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'LWdown_f_tavg': {
            'description': 'Downward long-wave radiation flux',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'LWdown_f_tavg',
            'vis_params': {
                'min': 26.85,
                'max': 600.9,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Lwnet_tavg': {
            'description': 'Net long-wave radiation flux',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Lwnet_tavg',
            'vis_params': {
                'min': -13792.7,
                'max': 196.97,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'PotEvap_tavg': {
            'description': 'Potential evaporation rate',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'PotEvap_tavg',
            'vis_params': {
                'min': -227.75,
                'max': 18977.9,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Psurf_f_inst': {
            'description': 'Pressure',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Psurf_f_inst',
            'vis_params': {
                'min': 44063.1,
                'max': 108344,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Qair_f_inst': {
            'description': 'Specific humidity',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Qair_f_inst',
            'vis_params': {
                'min': -0.02,
                'max': 0.07,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Qg_tavg': {
            'description': 'Heat flux',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Qg_tavg',
            'vis_params': {
                'min': -552.64,
                'max': 1538.41,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Qh_tavg': {
            'description': 'Sensible heat net flux',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Qh_tavg',
            'vis_params': {
                'min': -1005.15,
                'max': 18190.6,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Qle_tavg': {
            'description': 'Heat flux',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Qle_tavg',
            'vis_params': {
                'min': -227.75,
                'max': 5072.25,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Qs_acc': {
            'description': 'Storm surface runoff',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Qs_acc',
            'vis_params': {
                'min': 0,
                'max': 170.93,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Qsb_acc': {
            'description': 'Baseflow-groundwater runoff',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Qsb_acc',
            'vis_params': {
                'min': 0,
                'max': 50.6,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Qsm_acc': {
            'description': 'Snow melt',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Qsm_acc',
            'vis_params': {
                'min': 0,
                'max': 42.87,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Rainf_f_tavg': {
            'description': 'Total precipitation rate',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Rainf_f_tavg',
            'vis_params': {
                'min': 0,
                'max': 0.01,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Rainf_tavg': {
            'description': 'Rain precipitation rate',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Rainf_tavg',
            'vis_params': {
                'min': 0,
                'max': 0.01,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'RootMoist_inst': {
            'description': 'Root zone soil moisture',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'RootMoist_inst',
            'vis_params': {
                'min': 2,
                'max': 949.6,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'SWE_inst': {
            'description': 'Snow depth water equivalent',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'SWE_inst',
            'vis_params': {
                'min': 0,
                'max': 120787,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'SWdown_f_tavg': {
            'description': 'Downward short-wave radiation flux',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'SWdown_f_tavg',
            'vis_params': {
                'min': -56.93,
                'max': 30462.8,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'SnowDepth_inst': {
            'description': 'Snow depth',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'SnowDepth_inst',
            'vis_params': {
                'min': 0,
                'max': 301.96,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Snowf_tavg': {
            'description': 'Snow precipitation rate',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Snowf_tavg',
            'vis_params': {
                'min': 0,
                'max': 0.009,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'SoilMoi0_10cm_inst': {
            'description': 'Soil moisture',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'SoilMoi0_10cm_inst',
            'vis_params': {
                'min': 1.99,
                'max': 47.59,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'SoilMoi10_40cm_inst': {
            'description': 'Soil moisture',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'SoilMoi10_40cm_inst',
            'vis_params': {
                'min': 5.99,
                'max': 142.8,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'SoilMoi40_100cm_inst': {
            'description': 'Soil moisture',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'SoilMoi40_100cm_inst',
            'vis_params': {
                'min': 11.99,
                'max': 285.6,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'SoilMoi100_200cm_inst': {
            'description': 'Soil moisture',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'SoilMoi100_200cm_inst',
            'vis_params': {
                'min': 20,
                'max': 476,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'SoilTMP10_40cm_inst': {
            'description': 'Soil temperature',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'SoilTMP10_40cm_inst',
            'vis_params': {
                'min': 227.43,
                'max': 319.44,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'SoilTMP40_100cm_inst': {
            'description': 'Soil temperature',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'SoilTMP40_100cm_inst',
            'vis_params': {
                'min': 232.97,
                'max': 316.2,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Swnet_tavg': {
            'description': 'Net short wave radiation flux',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Swnet_tavg',
            'vis_params': {
                'min': -48.96,
                'max': 23741.3,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Tair_f_inst': {
            'description': 'Air temperature',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Tair_f_inst',
            'vis_params': {
                'min': 206.8,
                'max': 327.66,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Tveg_tavg': {
            'description': 'Transpiration',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Tveg_tavg',
            'vis_params': {
                'min': 0,
                'max': 3455.14,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
        'Wind_f_inst': {
            'description': 'Wind speed',
            'collection': 'NASA/GLDAS/V021/NOAH/G025/T3H',
            'band': 'Wind_f_inst',
            'vis_params': {
                'min': 0,
                'max': 57.7,
                'palette': ['#FFFFFF', '#00FFFF', '#0080FF', '#DA00FF', '#FFA400', '#FF0000'],
            },
            'date': '2020-07-09T00:00:00',
            'start_date': '2000-01-01',
            'end_date': None
        },
    },
    'elevation': {
        'USGS_10_meter': {
            'description': 'This is the highest-resolution seamless 3DEP ' +
                           'DEM dataset for the U.S. with full coverage of the 48 ' +
                           'conterminous states, Hawaii, and U.S. territories. Alaska ' +
                           'coverage is partially available now and is being expanded to ' +
                           'statewide coverage as part of the Alaska Mapping Initiative. ' +
                           'Ground spacing is approximately 10 meters north/south, but ' +
                           'variable east/west due to convergence of meridians with ' +
                           'latitude.',
            'collection': 'USGS/3DEP/10m',
            'band': 'elevation',
            'accumulation': 2000,
            'vis_params': {
                'min': 0,
                'max': 3000,
                'palette': [
                    '3ae237', 'b5e22e', 'd6e21f', 'fff705', 'ffd611', 'ffb613', 'ff8b13',
                    'ff6e08', 'ff500d', 'ff0000', 'de0101', 'c21301', '0602ff', '235cb1',
                    '307ef3', '269db1', '30c8e2', '32d3ef', '3be285', '3ff38f', '86e26f'
                ],
            },
        },
        'Netherlands_0.5m_Interpolated': {
            'description': 'The AHN DEM is a 0.5m DEM covering the Netherlands. It was generated from LIDAR data ' +
                           'taken in the spring between 2007 and 2012. It contains ground level samples with all ' +
                           'other items above ground (such as buildings, bridges, trees etc.) removed. This version ' +
                           'is interpolated; the areas where objects have been removed are filled with interpolated ' +
                           'values. The point cloud was converted to a 0.5m grid using a squared inverse distance ' +
                           'weighting method. Note: This dataset does not include a small number of tiles listed in ' +
                           'the manifest that are only available at a lower resolution.',
            'collection': 'AHN/AHN2_05M_INT',
            'band': 'elevation',
            'accumulation': 4000,
            'vis_params': {
                'min': -5.0,
                'max': 30.0,
                'palette': [
                    '3ae237', 'b5e22e', 'd6e21f', 'fff705', 'ffd611', 'ffb613', 'ff8b13',
                    'ff6e08', 'ff500d', 'ff0000', 'de0101', 'c21301', '0602ff', '235cb1',
                    '307ef3', '269db1', '30c8e2', '32d3ef', '3be285', '3ff38f', '86e26f'
                ],

            },
        },
        'SRTM_DEM4': {
            'description': 'The Shuttle Radar Topography Mission (SRTM) digital elevation dataset was originally' +
                           'produced to provide consistent, high-quality elevation data at near global scope. This ' +
                           'version of the SRTM digital elevation data has been processed to fill data voids, ' +
                           'and to facilitate its ease of use.',
            'collection': 'CGIAR/SRTM90_V4',
            'band': 'elevation',
            'accumulation': 500,
            'vis_params': {
                'min': 0,
                'max': 3000,
                'palette': [
                    '3ae237', 'b5e22e', 'd6e21f', 'fff705', 'ffd611', 'ffb613', 'ff8b13',
                    'ff6e08', 'ff500d', 'ff0000', 'de0101', 'c21301', '0602ff', '235cb1',
                    '307ef3', '269db1', '30c8e2', '32d3ef', '3be285', '3ff38f', '86e26f'
                ],
            },
        },
        'MERIT_DEM': {
            'description': 'MERIT DEM a high accuracy global DEM at 3 arc second resolution (~90 m at the equator)' +
                           'produced by eliminating major error components from existing DEMs (NASA SRTM3 DEM, JAXA ' +
                           'AW3D DEM, Viewfinder Panoramas DEM). MERIT DEM separates absolute bias, stripe noise, ' +
                           'speckle noise and tree height bias using multiple satellite datasets and filtering ' +
                           'techniques. After the error removal, land areas mapped with 2 m or better vertical ' +
                           'accuracy were increased from 39% to 58%. Significant improvements were found in flat ' +
                           'regions where height errors larger than topography variability, and landscapes such as ' +
                           'river networks and hill-valley structures became clearly represented.',
            'collection': 'MERIT/DEM/v1_0_3',
            'band': 'dem',
            'accumulation': 1000,
            'vis_params': {
                'min': 0,
                'max': 3000,
                'palette': [
                    '3ae237', 'b5e22e', 'd6e21f', 'fff705', 'ffd611', 'ffb613', 'ff8b13',
                    'ff6e08', 'ff500d', 'ff0000', 'de0101', 'c21301', '0602ff', '235cb1',
                    '307ef3', '269db1', '30c8e2', '32d3ef', '3be285', '3ff38f', '86e26f'
                ],
            },
        }
    }
}
