PRD API
=======

``PRD`` 是 ``pycwr`` 的中心对象。读取、绘图、QC、HID、插值和导出几乎都围绕它展开。

.. container:: api-box

   **核心属性**

   - ``fields``：每层一个 ``xarray.Dataset``
   - ``scan_info``：站点和扫描元数据
   - ``extended_fields``：原生距离 sidecar
   - ``product``：派生产品结果集
   - ``nsweeps`` / ``nrays``：体扫规模信息

.. container:: api-box

   **体扫查看接口**

   .. code-block:: python

      radar.summary()
      radar.available_fields(sweep=None, range_mode=None)
      radar.sweep_summary()
      radar.get_sweep_field(sweep, field_name, range_mode=None, sort_by_azimuth=False)
      radar.get_native_sweep_field(sweep, field_name)
      radar.has_extended_field(sweep, field_name)
      radar.ordered_az(inplace=False)

.. container:: api-box

   **导出接口**

   .. code-block:: python

      radar.to_pyart_radar(...)
      radar.to_xradar(...)
      radar.to_wsr98d(...)
      radar.to_nexrad_level2_msg31(...)
      radar.to_nexrad_level2_msg1(...)

.. rubric:: ``range_mode`` 约定

- ``range_mode="aligned"``：历史兼容的共享距离库
- ``range_mode="native"``：反射率原生距离库

建议：

- 做旧流程兼容或逐项对照时，用 ``aligned``
- 需要原生反射率覆盖范围时，用 ``native``

.. rubric:: 字段访问约定

当前版本里，原始字段和订正字段是独立变量，不合并存储。例如：

- ``dBZ`` 与 ``Zc``
- ``V`` 与 ``Vc``
- ``W`` 与 ``Wc``
- ``ZDR`` 与 ``ZDRc``

这意味着：

- 你可以显式选择要访问原始场还是订正场
- 导出到标准接口时，项目会按公开规则选择合适的数据源字段
- 但 ``PRD`` 内部不会因为导出或 QC 自动覆盖原始变量

.. rubric:: 典型示例

.. code-block:: python

   radar = read_auto("./data/file.bin.bz2")
   print(radar.summary())
   print(radar.available_fields())
   dbz = radar.get_sweep_field(0, "dBZ", range_mode="native")

.. rubric:: 相关页面

- :doc:`../data_structure`
- :doc:`../select_data`
- :doc:`../save_data`
