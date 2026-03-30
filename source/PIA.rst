衰减订正
===============

.. container:: lang-switch

   English version: :doc:`/en/PIA`

这页介绍 ``pycwr`` 中和衰减订正最相关的公开用法，重点是：

- 什么时候应该做衰减订正
- 原始场和订正场会怎么存放
- 哪条 API 适合数组级处理，哪条适合 ``PRD`` 工作流

.. container:: doc-hero

   .. container:: doc-eyebrow

      Attenuation Correction

   .. container:: doc-lead

      在双偏振 workflow 里，衰减订正通常和 KDP / PhiDP 处理、非气象回波剔除、
      后续绘图与导出连在一起。``pycwr`` 推荐优先走 ``run_dualpol_qc`` /
      ``apply_dualpol_qc`` 这条公开链路。

在工作流中的位置
------------------

典型顺序通常是：

1. 读取文件得到 ``PRD``
2. 对目标 sweep 或整卷运行双偏振 QC
3. 得到订正反射率、订正差分反射率、``PIA`` 等结果
4. 在绘图、HID 或导出时显式使用订正后的字段

输入与输出
------------------

.. list-table:: 常见输入输出字段
   :header-rows: 1

   * - 类型
     - 字段
     - 说明
   * - 输入
     - ``dBZ``
     - 原始反射率
   * - 输入
     - ``KDP`` 或 ``PhiDP``
     - 双偏振衰减订正的关键输入
   * - 输入
     - ``ZDR``、``CC``、``SNRH``
     - 可选辅助双偏振/QC字段
   * - 输出
     - ``Zc``
     - 订正后的反射率
   * - 输出
     - ``ZDRc``
     - 订正后的差分反射率
   * - 输出
     - ``PIA``、``PIA_ZDR``
     - 积分衰减量
   * - 输出
     - ``KDPc``、``PhiDP_smooth``、``QC_MASK``
     - QC / 补充结果

字段行为
------------------

- 原始字段和订正字段分开存储，不会覆盖原始 ``dBZ`` / ``ZDR``
- 跑完 ``PRD.apply_dualpol_qc`` 后，订正字段会写回 ``PRD.fields[sweep]``
- 后续绘图可以显式用 ``Zc``、``ZDRc``、``PIA`` 等字段

快速开始
------------------

.. code-block:: python

   from pycwr.io import read_auto

   radar = read_auto("./data/file.bin.bz2")
   qc_radar = radar.apply_dualpol_qc(inplace=False, band="C")

   raw_dbz = radar.get_sweep_field(0, "dBZ")
   corrected_dbz = qc_radar.get_sweep_field(0, "Zc")
   pia = qc_radar.get_sweep_field(0, "PIA")

   print(qc_radar.available_fields(0))

数组级 API 示例
------------------

如果你已经拿到了二维 sweep 数组，也可以直接使用 ``pycwr.qc`` 下的公开函数：

.. code-block:: python

   from pycwr.qc import correct_attenuation_kdp

   z_corr, pia, zdr_corr, pia_zdr = correct_attenuation_kdp(
       ref=dbz_2d,
       kdp=kdp_2d,
       dr=0.075,
       zdr=zdr_2d,
   )

适用场景：

- 你已经在自定义 workflow 里单独处理某个二维 sweep
- 你只需要数组结果，不需要把结果写回 ``PRD``

完整 ``PRD`` 工作流示例
------------------------

.. code-block:: python

   from pycwr.io import read_auto
   from pycwr.qc import run_dualpol_qc

   radar = read_auto("./data/file.bin.bz2")
   sweep = radar.fields[0]
   gate_length_km = float((sweep["range"].values[1] - sweep["range"].values[0]) / 1000.0)

   results = run_dualpol_qc(
       ref=sweep["dBZ"].values,
       zdr=None if "ZDR" not in sweep else sweep["ZDR"].values,
       phidp=None if "PhiDP" not in sweep else sweep["PhiDP"].values,
       kdp=None if "KDP" not in sweep else sweep["KDP"].values,
       rhohv=None if "CC" not in sweep else sweep["CC"].values,
       snr=None if "SNRH" not in sweep else sweep["SNRH"].values,
       dr=gate_length_km,
       band="C",
   )

   print(results.keys())
   # ref_corrected, zdr_corrected, pia, pia_zdr, phidp_smooth, kdp_used, ...

下游怎么使用
------------------

- 绘图：显式画 ``Zc``、``ZDRc``、``PIA``，不要假设项目会自动替换 ``dBZ``
- HID：如果 corrected 字段存在，分类流程会优先使用 ``Zc`` / ``ZDRc`` / ``KDPc``
- 导出：标准接口导出会按当前公开规则选择合适数据源字段，但不会修改 ``PRD`` 的原始变量

补充说明
------------------

- 单偏振历史接口 ``correct_attenuation`` / ``correct_attenuation_HB`` 仍然保留，但新 workflow 更推荐 ``correct_attenuation_kdp`` 或 ``apply_dualpol_qc``
- 如果 sweep 缺少 ``KDP`` 和 ``PhiDP``，双偏振 QC 无法完成衰减订正
