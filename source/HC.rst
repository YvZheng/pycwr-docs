水凝物分类
===============

这页先讲 workflow。更细的函数入口和返回结果请继续看 :doc:`api/retrieve`。

PyCWR 当前推荐的公开入口是：

- `classify_hydrometeors(...)`
- `radar.classify_hydrometeors(...)`
- `radar.add_hydrometeor_classification(...)`

支持两种模式：

- 提供温度廓线
- 不提供廓线，走无廓线近似流程

示例
------------------

.. code-block:: python

    hcl_radar = radar.classify_hydrometeors(
        inplace=False,
        band="C",
        profile_height=[0.0, 2000.0, 4000.0, 8000.0, 12000.0],
        profile_temperature=[24.0, 12.0, 2.0, -16.0, -40.0],
        confidence_field="HCL_CONF",
        temperature_field="HCL_T",
    )

输出
------------------

分类结果会作为 gate-level 字段写回 `PRD.fields`，常见字段包括：

- `HCL`
- `HCL_CONF`
- `HCL_T`

说明
------------------

- corrected 字段存在时，分类优先使用 `Zc / ZDRc / KDPc`
- `HCL` 色标和中文类别名在当前 draw / web viewer 层已经统一
