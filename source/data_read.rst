数据读取
=================

这页解决两个问题：

- 第一次拿到雷达文件时应该从哪里读
- 读出来以后你会得到什么对象

PyCWR 当前公开 reader 主要面向：

- `WSR98D`
- `SAB`
- `CC`
- `SC`
- `PA`

所有 reader 最终都返回同一个核心对象：`pycwr.core.NRadar.PRD`。

自动读取
-----------

最推荐的入口是 ``read_auto``：

.. code-block:: python

    from pycwr.io import read_auto

    radar = read_auto("./data/Z_RADR_I_Z9046_20260317065928_O_DOR_SAD_CAP_FMT.bin.bz2")
    print(radar.summary())
    print(radar.available_fields())

`read_auto` 会：

- 自动识别雷达文件家族
- 解析成 `PRD`
- 保持当前项目兼容的 sweep 结构和几何主链

接口形式：

.. code-block:: python

    read_auto(
        filename,
        station_lon=None,
        station_lat=None,
        station_alt=None,
        effective_earth_radius=None,
    )

参数说明：

- `filename`：雷达文件路径，可直接读取 `bz2` / `gz` 压缩文件
- `station_lon`、`station_lat`、`station_alt`：站点信息覆盖值
- `effective_earth_radius`：几何计算使用的有效地球半径，单位米

指定格式读取
--------------

如果你已经明确知道文件格式，也可以直接调用指定 reader：

.. code-block:: python

    from pycwr.io import read_WSR98D, read_SAB, read_CC, read_SC, read_PA

    radar = read_WSR98D("./data/file.bin.bz2")

这些函数返回的仍然是同一个 `PRD` 对象类型。

配合 Py-ART
---------------------------------

`PRD` 现在推荐用对象方法导出到 Py-ART：

.. code-block:: python

    from pycwr.io import read_auto

    radar = read_auto("./data/file.bin.bz2")
    pyart_radar = radar.to_pyart_radar()

如果环境里安装了上游 Py-ART，就会优先导出为上游 `Radar` 对象。

更多接口细节请继续看 :doc:`api/io` 和 :doc:`api/prd`。
