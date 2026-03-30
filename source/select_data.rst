选取数据
================

`PRD.fields` 存放逐层雷达体扫数据，每一层是一个 `xarray.Dataset`。

最推荐的访问方式
------------------

.. code-block:: python

    from pycwr.io import read_auto

    radar = read_auto("./data/file.bin.bz2")
    print(radar.fields[0])
    print(radar.get_sweep_field(0, "dBZ"))

按层索引
------------------

.. code-block:: python

    sweep0 = radar.fields[0]
    dBZ0 = radar.fields[0]["dBZ"]

更推荐显式走：

.. code-block:: python

    dBZ0 = radar.get_sweep_field(0, "dBZ", range_mode="aligned")
    dBZ0_native = radar.get_sweep_field(0, "dBZ", range_mode="native")

`scan_info`
------------------

`scan_info` 存放站点和扫描方式信息，例如：

- `latitude`
- `longitude`
- `altitude`
- `scan_type`
- `frequency`
- `start_time`
- `end_time`
- `nyquist_velocity`
- `unambiguous_range`
- `rays_per_sweep`
- `fixed_angle`

字段关键词
------------------

表 1 给出当前常见字段和变量含义：

.. list-table:: 字段关键词
   :header-rows: 1
   :widths: 18 42

   * - key
     - variable
   * - dBT
     - total_power
   * - dBZ
     - reflectivity
   * - V
     - velocity
   * - W
     - spectrum_width
   * - ZDR
     - differential_reflectivity
   * - CC
     - cross_correlation_ratio
   * - PhiDP
     - differential_phase
   * - KDP
     - specific_differential_phase
   * - HCL
     - hydro_class
   * - CF
     - clutter_flag
   * - Zc
     - corrected_reflectivity
   * - Vc
     - corrected_velocity
   * - Wc
     - spectrum_width_corrected
   * - ZDRc
     - corrected_differential_reflectivity
   * - KDPc
     - corrected_specific_differential_phase
   * - SNRH
     - horizontal_signal_noise_ratio
   * - SNRV
     - vertical_signal_noise_ratio

注意
------------------

- `dBZ/Zc`、`V/Vc`、`W/Wc`、`ZDR/ZDRc` 都是独立变量
- corrected 字段不是对原始字段的原地覆盖
- 需要排序后的方位视图时，可用 `sort_by_azimuth=True`
