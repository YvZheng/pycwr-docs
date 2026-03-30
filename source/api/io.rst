IO API
======

这页列出 ``pycwr.io`` 最常用的 reader / writer 入口。所有 reader 最终都返回
``pycwr.core.NRadar.PRD``。

.. container:: api-box

   **推荐入口：``read_auto``**

   .. code-block:: python

      read_auto(
          filename,
          station_lon=None,
          station_lat=None,
          station_alt=None,
          effective_earth_radius=None,
      )

   作用：

   - 自动识别雷达文件家族
   - 解析成 ``PRD``
   - 保持项目当前兼容的 sweep 布局和几何主链

   返回：

   - ``pycwr.core.NRadar.PRD``

.. container:: api-box

   **指定格式读取**

   .. code-block:: python

      read_WSR98D(...)
      read_SAB(...)
      read_CC(...)
      read_SC(...)
      read_PA(...)

   建议只在你已经明确知道输入格式时直接调用。

.. list-table:: 常用参数说明
   :header-rows: 1

   * - 参数
     - 说明
   * - ``filename``
     - 雷达文件路径，支持项目当前 reader 能识别的压缩输入
   * - ``station_lon`` / ``station_lat`` / ``station_alt``
     - 可选站点覆盖值
   * - ``effective_earth_radius``
     - 几何计算用有效地球半径，单位米

.. container:: api-box

   **写出接口**

   函数式 writer：

   .. code-block:: python

      write_wsr98d(prd, filename, **kwargs)
      write_nexrad_level2_msg31(prd, filename, **kwargs)
      write_nexrad_level2_msg1(prd, filename, **kwargs)

   更推荐对象式导出：

   .. code-block:: python

      radar.to_wsr98d(...)
      radar.to_nexrad_level2_msg31(...)
      radar.to_nexrad_level2_msg1(...)

.. rubric:: 典型示例

.. code-block:: python

   from pycwr.io import read_auto

   radar = read_auto("./data/file.bin.bz2")
   print(radar.summary())

.. rubric:: 常见注意事项

- ``read_auto`` 识别失败时会直接报错，不会静默猜测格式
- reader 返回的是统一 ``PRD``，不是各格式各自一套对象
- writer 用于兼容导出和 round-trip，不会改写 ``PRD`` 内部字段存储结构
