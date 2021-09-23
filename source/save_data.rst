导出数据
==============

目前可以通过pyart将数据导出为cfradial/UF格式

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,5

    from pycwr.io import read_auto
    import pyart
    import warnings
    warnings.filterwarnings("ignore")

    file = "./data/Z_RADR_I_Z9898_20190828181529_O_DOR_SAD_CAP_FMT.bin.bz2"
    PRD = read_auto(file)
    pyart_radar = PRD.ToPyartRadar()
    pyart.io.write_cfradial("./cfradial.nc", pyart_radar)