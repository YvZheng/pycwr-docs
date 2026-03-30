数据结构
========

PyCWR 的中心对象是 ``PRD`` (Polarimetry Radar Data)。

reader 把原始雷达基数据统一转换成 ``PRD``，后续绘图、QC、插值、导出基本都围绕它展开。

.. container:: section-note

   如果你第一次接触 ``pycwr``，建议先掌握这页，再去看绘图、导出和 API 手册。

``PRD`` 的主要部分
------------------

- ``fields``：每层一个 ``xarray.Dataset``
- ``scan_info``：站点和扫描元数据
- ``extended_fields``：当 aligned/native 距离库不同步时的原生 sidecar
- ``product``：产品结果集

最常用的查看接口
------------------

.. code-block:: python

    radar.summary()
    radar.available_fields()
    radar.sweep_summary()
    radar.get_sweep_field(0, "dBZ")
    radar.get_native_sweep_field(0, "dBZ")

aligned 与 native
-----------------

当前 `PRD` 支持两种反射率访问方式：

- ``range_mode="aligned"``：历史兼容的共享距离库
- ``range_mode="native"``：反射率原生距离库

建议：

- 需要和旧流程严格对齐时，用 ``aligned``
- 需要低层完整反射率覆盖范围时，用 ``native``

示例：

.. code-block:: python

    aligned = radar.get_sweep_field(0, "dBZ", range_mode="aligned")
    native = radar.get_sweep_field(0, "dBZ", range_mode="native")

字段是独立变量
----------------

当前版本里，原始字段和订正字段是独立变量，不会在存储层被合并。

例如：

- ``dBZ`` 与 ``Zc``
- ``V`` 与 ``Vc``
- ``W`` 与 ``Wc``
- ``ZDR`` 与 ``ZDRc``

都应当按独立变量理解和访问。

更多对象方法请看 :doc:`api/prd`。
