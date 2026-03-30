QC 与插值 API
==============

这页汇总质量控制与多雷达组网插值接口。

.. container:: api-box

   **双偏振质量控制**

   .. code-block:: python

      run_dualpol_qc(radar, **kwargs)
      apply_dualpol_qc(radar, **kwargs)
      radar.apply_dualpol_qc(...)

   常见结果：

   - ``Zc``
   - ``ZDRc``
   - ``PhiDPc``
   - ``KDPc``
   - 相关 QC 掩码或辅助字段

.. container:: api-box

   **多雷达组网插值**

   .. code-block:: python

      run_radar_network_3d(radars, grid_config=None, field_name=None, **kwargs)
      radar_network_3d_to_netcdf(dataset, output_path)

.. rubric:: 使用建议

- QC 需要反射率或双偏振字段时，优先走公开字段选择规则
- 组网通常以反射率主场为主，不要求字段名必须是某个硬编码名字
- 先保证单雷达 ``PRD`` 结构正确，再做插值，问题会更容易定位

.. rubric:: 相关页面

- :doc:`../interp`
- :doc:`../select_data`
