PyCWR简介
===================

.. container:: lang-switch

   English version: :doc:`/en/PyCWR_intro`

.. container:: doc-hero

   .. container:: doc-eyebrow

      Toolkit Overview

   PyCWR 解决的是中国天气雷达基数据“格式多、年代跨度大、业务链路不一致”的现实问题。

   .. container:: doc-lead

      它把 reader、体扫对象、绘图、QC、HID、风场反演、插值和标准格式导出连成一条
      连贯的 Python 工作流，让你不必为每一种输入格式单独重写处理逻辑。

.. container:: doc-card-grid

   .. container:: doc-card

      **适合谁**

      - 业务研发和科研用户
      - 需要统一 reader / PRD 工作流的人
      - 需要对接 Py-ART / xradar / Web viewer 的用户

   .. container:: doc-card

      **你可以做什么**

      - 读取主流中国业务雷达格式
      - 浏览体扫结构和字段
      - 做绘图、QC、HID、风场和组网
      - 导出到 Py-ART / xradar / WSR98D / NEXRAD

   .. container:: doc-card

      **项目约束**

      - 优先保证 reader 行为兼容和结果一致
      - corrected 字段和原始字段分开存储
      - 不把历史兼容行为随意重写掉

能力摘要
------------------

- 常见中国业务天气雷达格式 reader
- 统一的 ``PRD`` 体扫对象
- ``aligned/native`` 反射率双工作流
- 绘图、QC、水凝物分类、风场反演
- 多雷达组网插值
- Py-ART / xradar / WSR98D / NEXRAD 导出
- 本地 Web viewer

建议阅读路径
------------------

.. container:: step-grid

   .. container:: step-card

      **1. 安装**

      先看 :doc:`installation`，确认 Python 版本和可选依赖。

   .. container:: step-card

      **2. 读取**

      再看 :doc:`data_read`，用 ``read_auto`` 得到第一个 ``PRD``。

   .. container:: step-card

      **3. 理解数据结构**

      看 :doc:`data_structure` 和 :doc:`select_data`，理解 ``aligned/native`` 和 corrected 字段。

   .. container:: step-card

      **4. 进入任务页**

      再按需要进入 :doc:`draw`、:doc:`PIA`、:doc:`HC`、:doc:`interp`、:doc:`VR` 或 :doc:`GUI`。

示意图
------------------

#. 天气雷达 PPI 扫描显示

    .. image:: _static/PPI.png
        :height: 500px
        :width: 583px
        :align: center
        :alt: PPI

#. 天气雷达 RHI 扫描显示

    .. image:: _static/RHI.png
        :height: 500px
        :width: 608px
        :align: center
        :alt: RHI

#. 天气雷达 CAPPI 插值显示

    .. image:: _static/CAPPI.png
        :height: 500px
        :width: 583px
        :align: center
        :alt: CAPPI

#. 水凝物分类示意

    .. image:: _static/HC.png
        :height: 500px
        :width: 623px
        :align: center
        :alt: HC
