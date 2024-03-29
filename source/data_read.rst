数据读取
=================

双偏振雷达普及之前，我国新一代天气雷达数据主要有CINRAD/SA/SB/CB、CINRAD/CC/CCJ、CINRAD/SC/CD等格式，
随着双偏振雷达数据的普及，我国逐渐将数据统一为WSR98D格式。

文档中采用的数据可通过百度网盘下载，链接: https://pan.baidu.com/s/1MhW9jE7r3LYHO7enUOfRsw 提取码: 8ba9

自动读取
-----------

可以使用read_auto函数实现雷达数据类型的识别，并转化为pycwr内置的雷达数据存储格式PRD（Polarimetry Radar Data）类型：

.. code-block:: python   
    :linenos:   
    :emphasize-lines: 3,5

    from pycwr.io import read_auto 
    PRD = read_auto(r"./data/Z_RADR_I_Z9898_20190828181529_O_DOR_SAD_CAP_FMT.bin.bz2")
    print(PRD.scan_info)
    print(PRD.fields)

read_auto函数在 ``pycwr.io`` 下，可以传入站点的经纬度高度参数，如不传入该参数，则会根据站号或者站点信息识别站点
的经纬度数据。

read_auto函数 ``read_auto(filename, station_lon=None, station_lat=None, station_alt=None)`` 共有四个参数：

    - filename : 雷达基数据路径，基数据可以是bz2和gz格式的压缩文件（不需要解压）。
    - station_lon : 雷达站点的经度信息，范围是-180 ~ 180。（units: degree east）
    - station_lat : 雷达站点的纬度信息，范围是-90 ~ 900。（units: degree north）
    - station_alt : 雷达站点的高度信息。（units: meters）

指定类型读取
--------------

如果已经知道雷达数据格式的类型，可以直接指定格式进行读取。

#. 数据类型是WSR98D：

    .. code-block:: python   
        :linenos:   
        :emphasize-lines: 3,5

        from pycwr.io import WSR98DFile
        filename = "./data/Z_RADR_I_Z9898_20190828181529_O_DOR_SAD_CAP_FMT.bin.bz2"
        PRD = WSR98DFile.WSR98D2NRadar(WSR98DFile.WSR98DBaseData(filename, station_lon=None,\
         station_lat=None, station_alt=None)).ToPRD()
        print(PRD.scan_info)
        print(PRD.fields)

#. 数据类型是SA/SB：

    .. code-block:: python   
        :linenos:   
        :emphasize-lines: 3,5

        from pycwr.io import SABFile
        filename = "./data/Z9396_BASE_SB_20180724_055400.bin.bz2"
        PRD = SABFile.SAB2NRadar(SABFile.SABBaseData(filename, station_lon=None,\
         station_lat=None, station_alt=None)).ToPRD()
        print(PRD.scan_info)
        print(PRD.fields)

#. 数据类型是CC/CCJ：

    .. code-block:: python   
        :linenos:   
        :emphasize-lines: 3,5

        from pycwr.io import CCFile
        filename = "./data/2016070817.48V.gz"
        PRD = CCFile.CC2NRadar(CCFile.CCBaseData(filename, station_lon=None,\
         station_lat=None, station_alt=None)).ToPRD()
        print(PRD.scan_info)
        print(PRD.fields)

#. 数据类型是SC/CD：

    .. code-block:: python   
        :linenos:   
        :emphasize-lines: 3,5

        from pycwr.io import SCFile
        filename = "./data/Z_RADR_I_Z9240_20190703101340_O_DOR_SC_CAP.bin.bz2"
        PRD = SCFile.SC2NRadar(SCFile.SCBaseData(filename, station_lon=None,\
         station_lat=None, station_alt=None)).ToPRD()
        print(PRD.scan_info)
        print(PRD.fields)

#. 数据类型是Phase Array：

    .. code-block:: python
        :linenos:
        :emphasize-lines: 3,5

        from pycwr.io import read_PA
        filename = "./data/Z_RADR_I_ZGZ01_20200820220246_O_DOR_DXK_CAR.bin.bz2"
        PRD = read_PA(filename)
        print(PRD.scan_info)
        print(PRD.fields)


配合 Py-ART_ 库对雷达数据进行处理
---------------------------------

.. code-block:: python   
    :linenos:   
    :emphasize-lines: 3,5

    from pycwr.io import read_auto 
    PRD = read_auto(r"./data/Z_RADR_I_Z9898_20190828181529_O_DOR_SAD_CAP_FMT.bin.bz2")
    print(PRD.scan_info)
    print(PRD.fields)
    PyartRadar = PRD.ToPyartRadar()

.. _Py-ART: https://arm-doe.github.io/pyart-docs-travis/index.html

