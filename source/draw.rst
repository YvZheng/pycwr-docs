绘图
==========

这页适合先找“怎么快速画图”，更细的函数入口请继续看 :doc:`api/draw`。

PyCWR 1.0.9 当前推荐的绘图入口分两类：

- 简单场景：直接用 `pycwr.draw` 下的快捷函数
- 需要和旧项目兼容：继续使用 `Graph` / `GraphMap`

快捷绘图接口
----------------

.. code-block:: python

    from pycwr.io import read_auto
    from pycwr.draw import plot_ppi, plot_ppi_map, plot_rhi, plot_section

    radar = read_auto("./data/file.bin.bz2")
    plot_ppi(radar, field="dBZ", sweep=0, show=True)

常见接口：

- `plot_ppi`
- `plot_ppi_map`
- `plot_rhi`
- `plot_section`
- `plot_section_lonlat`
- `plot_vvp`
- `plot_wind_profile`

旧式 `Graph` 接口
------------------

.. code-block:: python

    import matplotlib.pyplot as plt
    from pycwr.draw.RadarPlot import Graph

    fig, ax = plt.subplots()
    graph = Graph(radar)
    graph.plot_ppi(ax, 0, "dBZ", cmap="CN_ref")

说明
------------------

- `plot_ppi` / `plot_ppi_map` 适合平面快速出图
- `plot_rhi` 通过 ``azimuth`` 指定剖面方位角，单位为度，并支持 ``range_mode``
- `plot_section` 用 ``start`` / ``end`` 指定平面端点，默认单位为 km；米制坐标需设置 ``point_units="m"``
- `plot_section_lonlat` 用 ``start_lonlat`` / ``end_lonlat`` 指定数值型 ``(经度, 纬度)`` 端点，单位为度；缩放后经纬度刻度会随之更新
- 如果低层反射率 native 距离比速度长，可通过 `range_mode="native"` 访问
- ``Graph`` / ``GraphMap`` 的 CR、CAPPI 绘图按 ``range_mode`` 使用对应的 aligned 或 native 产品
- ZDR 默认色图在未注册 Py-ART 色图时会使用内置副本，无需手动注册
- `HCL` 会走离散色标和中文类别名，不使用普通连续色带
