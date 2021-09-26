选取数据
================

fields属性存放了雷达体扫数据:

>>> from pycwr.io import read_auto
>>> PRD = read_auto("./data/NUIST.20150627.002438.AR2.bz2")

通过[层数]方法索引对应产品, 层数从0开始:

>>> print(PRD.fields[0])
<xarray.Dataset>
Dimensions:    (range: 1933, time: 668)
Coordinates:
    azimuth    (time) float64 9.149 9.69 10.22 10.77 ... 8.094 8.611 9.168 9.693
    elevation  (time) float64 0.5933 0.5933 0.5933 ... 0.5054 0.5054 0.5054
    x          (time, range) float64 11.92 23.85 35.77 ... 2.439e+04 2.44e+04
    y          (time, range) float64 74.04 148.1 222.1 ... 1.428e+05 1.429e+05
    z          (time, range) float64 174.8 175.6 176.3 ... 2.688e+03 2.689e+03
    lat        (time, range) float64 32.21 32.21 32.21 ... 33.49 33.49 33.49
    lon        (time, range) float64 118.7 118.7 118.7 ... 119.0 119.0 119.0
  * range      (range) float64 75.0 150.0 225.0 ... 1.448e+05 1.449e+05 1.45e+05
  * time       (time) datetime64[ns] 2015-06-27T00:24:38.640231 ... 2015-06-2...
Data variables:
    dBZ        (time, range) float64 -13.6 17.34 24.1 ... 18.62 18.24 19.32
    dBT        (time, range) float64 -13.6 17.34 24.1 ... 18.62 18.24 19.32
    V          (time, range) float64 0.0 -0.08 -1.12 -1.55 ... -1.76 -3.22 -3.41
    W          (time, range) float64 0.01 0.01 0.01 1.12 ... 1.63 1.43 1.5 1.68
    ZDR        (time, range) float64 -0.81 13.73 0.41 -0.39 ... 1.1 0.67 0.43
    KDP        (time, range) float64 7.03 6.13 5.44 4.78 ... 0.5 0.47 0.48 0.51
    PhiDP      (time, range) float64 100.0 33.3 1.02 2.86 ... 103.2 104.5 102.6
    CC         (time, range) float64 1.0 0.57 0.938 0.994 ... 0.923 0.938 0.96
    SQI        (time, range) float64 1.0 1.0 1.0 0.966 ... 0.913 0.905 0.898
    SNRH       (time, range) float64 67.77 81.21 81.95 ... 14.46 14.08 15.16

通过[层数][关键词]方法索引对应产品,关键词详见表1:

>>> print(PRD.fields[0]["dBZ"])
<xarray.DataArray 'dBZ' (time: 668, range: 1933)>
array([[-13.60000038,  17.34000015,  24.10000038, ...,  16.87999916,
         16.76000023,  17.52000046],
       [-13.60000038,  16.65999985,  24.09000015, ...,  18.37000084,
         16.42000008,  17.86000061],
       [-13.60000038,  18.03000069,  23.57999992, ...,  16.98999977,
         20.04000092,  20.85000038],
       ...,
       [-13.60000038,  12.61999989,  24.        , ...,  15.63000011,
         14.63000011,  13.81000042],
       [-13.60000038,  15.75      ,  25.35000038, ...,  12.85999966,
         17.29999924,  14.15999985],
       [-13.60000038,  14.97999954,  24.55999947, ...,  18.62000084,
         18.23999977,  19.31999969]])
Coordinates:
    azimuth    (time) float64 9.149 9.69 10.22 10.77 ... 8.094 8.611 9.168 9.693
    elevation  (time) float64 0.5933 0.5933 0.5933 ... 0.5054 0.5054 0.5054
    x          (time, range) float64 11.92 23.85 35.77 ... 2.439e+04 2.44e+04
    y          (time, range) float64 74.04 148.1 222.1 ... 1.428e+05 1.429e+05
    z          (time, range) float64 174.8 175.6 176.3 ... 2.688e+03 2.689e+03
    lat        (time, range) float64 32.21 32.21 32.21 ... 33.49 33.49 33.49
    lon        (time, range) float64 118.7 118.7 118.7 ... 119.0 119.0 119.0
  * range      (range) float64 75.0 150.0 225.0 ... 1.448e+05 1.449e+05 1.45e+05
  * time       (time) datetime64[ns] 2015-06-27T00:24:38.640231 ... 2015-06-2...
Attributes:
    units:          dBZ
    standard_name:  equivalent_reflectivity_factor
    long_name:      Reflectivity
    valid_max:      80.0
    valid_min:      -30.0
    coordinates:    elevation azimuth range

scan_info存放了雷达位置信息以及扫描方式:

>>> print(PRD.scan_info)
<xarray.Dataset>
Dimensions:            (sweep: 15)
Coordinates:
  * sweep              (sweep) int64 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Data variables:
    latitude           float64 32.21
    longitude          float64 118.7
    altitude           int64 87
    scan_type          <U3 'ppi'
    frequency          float64 5.592
    start_time         datetime64[ns] 2015-06-27T00:24:38.640231
    end_time           datetime64[ns] 2015-06-27T00:31:47.207645
    nyquist_velocity   (sweep) float32 13.4 13.4 13.4 13.4 ... 26.81 26.81 26.81
    unambiguous_range  (sweep) int32 145000 145000 145000 ... 70000 70000 10000
    rays_per_sweep     (sweep) int64 668 668 668 668 668 ... 669 668 668 668 668
    fixed_angle        (sweep) float32 0.5 1.5 2.4 3.4 ... 14.0 16.7 19.5 90.0
    beam_width         (sweep) float64 0.5389 0.5389 0.5389 ... 0.5389 0.5389

表1，不同变量对应索引的关键词:

+-------+------------------------------+
|key    |variable                      |
+=======+==============================+
|dBT    |total_power                   |
+-------+------------------------------+
|dBZ    |reflectivity                  |
+-------+------------------------------+
|V      |velocity                      |
+-------+------------------------------+
|W      |spectrum_width                |
+-------+------------------------------+
|SQI    |normalized_coherent_power     |
+-------+------------------------------+
|CPA    |clutter_phase_alignment       |
+-------+------------------------------+
|ZDR    |differential_reflectivity     |
+-------+------------------------------+
|LDR    |linear_depolarization_ratio   |
+-------+------------------------------+
|CC     |cross_correlation_ratio       |
+-------+------------------------------+
|PhiDP  |differential_phase            |
+-------+------------------------------+
|KDP    |specific_differential_phase   |
+-------+------------------------------+
|CP     |clutter_probability           |
+-------+------------------------------+
|Flag   |flag_of_rpv_data              |
+-------+------------------------------+
|HCL    |hydro_class                   |
+-------+------------------------------+
|CF     |clutter_flag                  |
+-------+------------------------------+
|Zc     |corrected_reflectivity        |
+-------+------------------------------+
|Vc     |corrected_velocity            |
+-------+------------------------------+
|Wc     |spectrum_width_corrected      |
+-------+------------------------------+
|SNRH   |horizontal_signal_noise_ratio |
+-------+------------------------------+
|SNRV   |vertical_signal_noise_ratio   |
+-------+------------------------------+