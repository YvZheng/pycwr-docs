检索 API
========

这页汇总 ``retrieve`` 相关的公开入口，主要包括水凝物分类和单雷达风场反演。

.. container:: api-box

   **水凝物分类**

   .. code-block:: python

      classify_hydrometeors(...)
      radar.classify_hydrometeors(sweeps=None, inplace=False, **kwargs)
      radar.add_hydrometeor_classification(sweeps=None, **kwargs)

   常用输出字段：

   - ``HCL``
   - ``HCL_CONF``
   - ``HCL_T``

.. container:: api-box

   **风场反演**

   .. code-block:: python

      retrieve_vad(...)
      retrieve_vvp(...)
      retrieve_vwp(...)

      radar.retrieve_vad(...)
      radar.retrieve_vvp(...)
      radar.retrieve_vwp(...)

.. rubric:: 温度廓线说明

- HID 支持输入温度廓线
- 也支持无廓线近似流程
- corrected 字段存在时，优先使用 ``Zc`` / ``ZDRc`` / ``KDPc`` 等订正场

.. rubric:: 常见注意事项

- ``HCL`` 结果写回 ``PRD.fields``，不是写到 ``product`` 里
- 风场反演对输入速度场质量更敏感，通常建议先走 QC 或显式选择合适字段
- 示例 workflow 请优先看 :doc:`../HC` 和 :doc:`../VR`
