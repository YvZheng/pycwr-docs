雷达数据插值
=================

PyCWR 当前插值主入口是多雷达组网接口：

.. code-block:: python

    from pycwr.interp import run_radar_network_3d

常见能力包括：

- 单雷达网格化
- 多雷达 3D 组网
- 组合反射率、CAPPI、VIL、ET
- 组网前可选 QC

最常用场景
------------------

.. code-block:: python

    dataset = run_radar_network_3d(
        radars=[radar1, radar2],
        grid_x=x,
        grid_y=y,
        level_heights=z,
        field_names=["dBZ"],
        use_qc=False,
    )

说明
------------------

- 当前主线仍以反射率类场为主
- 需要低层完整覆盖时，可对反射率指定 `range_mode="native"`
- 速度场不建议直接走组网主接口
