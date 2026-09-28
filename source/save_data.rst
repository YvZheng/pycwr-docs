导出数据
==============

.. container:: lang-switch

   English version: :doc:`/en/save_data`

这页讲的是“导出工作流怎么走”，参数和接口清单请继续看 :doc:`api/io` 和 :doc:`api/prd`。

PyCWR 1.0.9 当前公开的导出路径不再只限于 Py-ART。

推荐对象式导出
----------------

.. code-block:: python

    radar.to_pyart_radar(...)
    radar.to_xradar(...)
    radar.to_wsr98d(...)
    radar.to_nexrad_level2_msg31(...)
    radar.to_nexrad_level2_msg1(...)

也支持函数式 writer：

.. code-block:: python

    from pycwr.io import (
        write_wsr98d,
        write_nexrad_level2_msg31,
        write_nexrad_level2_msg1,
    )

Py-ART / CfRadial
------------------

.. code-block:: python

    from pycwr.io import read_auto

    radar = read_auto("./data/file.bin.bz2")
    pyart_radar = radar.to_pyart_radar()

如果环境中安装了 Py-ART，可以继续写 `cfradial`：

.. code-block:: python

    import pyart
    pyart.io.write_cfradial("./cfradial.nc", pyart_radar)

WSR98D / NEXRAD
------------------

.. code-block:: python

    radar.to_wsr98d("./export.bin")
    radar.to_nexrad_level2_msg31("./export_msg31.ar2v")
    radar.to_nexrad_level2_msg1("./export_msg1.ar2v")

说明
------------------

- `WSR98D` 写出用于项目内 round-trip 和兼容验证
- `NEXRAD` 导出主要用于和 Py-ART / 外部工作流互通
- corrected 字段和原始字段仍然作为独立变量保留在 `PRD` 中
- 在导出到标准接口时，项目会按当前公开规则选择合适的数据源字段
- ``WSR98D`` / ``NEXRAD MSG31`` 按字段选择偏移和存储宽度，保留既定量化精度，避免有效低值和高值丢失；无法表示的值会报错
- ``WSR98D`` / ``NEXRAD`` 导出要求距离库等间隔；``NEXRAD`` 的起始距离和间隔还必须能以整数米表示
- ``to_xradar_sweeps()`` 返回的 sweep 数据集可通过 ``to_netcdf()`` 写出，datetime 时间坐标使用 NetCDF encoding
