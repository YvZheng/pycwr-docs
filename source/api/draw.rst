绘图 API
========

这页汇总 ``pycwr.draw`` 的常用入口。适合查“应该画哪个函数”和“字段显示会长什么样”。

.. container:: api-box

   **快捷绘图接口**

   .. code-block:: python

      plot_ppi(radar, field="dBZ", sweep=0, show=True, **kwargs)
      plot_ppi_map(radar, field="dBZ", sweep=0, show=True, **kwargs)
      plot_rhi(radar, field="dBZ", sweep=0, show=True, **kwargs)
      plot_section(radar, field="dBZ", start_xy=None, end_xy=None, show=True, **kwargs)
      plot_section_lonlat(radar, field="dBZ", start_lonlat=None, end_lonlat=None, show=True, **kwargs)
      plot_vvp(...)
      plot_wind_profile(...)

.. container:: api-box

   **旧式兼容入口**

   .. code-block:: python

      from pycwr.draw.RadarPlot import Graph
      from pycwr.draw.SingleRadarPlotMap import GraphMap

   这组接口主要用于兼容旧项目或旧示例。

.. rubric:: ``HCL`` 特殊说明

- ``HCL`` 是离散分类字段，不走普通连续色带
- 当前 ``draw`` 和 Web viewer 使用统一的离散色标和中文类别名
- 文档和页面看到的 ``HCL`` 颜色、类别名称应该保持一致

.. rubric:: 典型示例

.. code-block:: python

   from pycwr.io import read_auto
   from pycwr.draw import plot_ppi, plot_section

   radar = read_auto("./data/file.bin.bz2")
   plot_ppi(radar, field="dBZ", sweep=0, show=True)
   plot_section(radar, field="HCL", start_xy=(-30000, 0), end_xy=(30000, 0), show=True)

.. rubric:: 相关页面

- :doc:`../draw`
- :doc:`../HC`
- :doc:`web`
