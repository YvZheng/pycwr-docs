绘图
==========

这页适合先找“怎么快速画图”，更细的函数入口请继续看 :doc:`api/draw`。

PyCWR 1.0.4 当前推荐的绘图入口分两类：

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
- `plot_rhi` 用于单层或指定方位剖面
- `plot_section` / `plot_section_lonlat` 用于垂直剖面
- 如果低层反射率 native 距离比速度长，可通过 `range_mode="native"` 访问
- `HCL` 会走离散色标和中文类别名，不使用普通连续色带
