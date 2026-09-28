.. image:: _static/NJIAS.png
    :height: 200px
    :width: 733px
    :align: center
    :alt: pycwr

===========================================
*PyCWR*：中国天气雷达处理工具库
===========================================

:Release: 1.0.9
:Date: |today|

.. container:: lang-switch

   Switch language: :doc:`English overview </en/index>`

.. container:: doc-hero

   .. container:: doc-eyebrow

      Radar Toolkit Documentation

   PyCWR_（Python based China Weather Radar Toolkit）面向中国天气雷达业务和科研流程。

   .. container:: doc-lead

      这套手册围绕 ``pycwr 1.0.9`` 的公开能力组织，目标是让你能够快速完成
      读取、检查、绘图、QC、HID、风场反演、组网插值和标准格式导出。

   .. container:: doc-callout

      推荐阅读顺序：先看安装与第一次读取，再看 ``PRD`` 数据结构，最后按你的任务进入
      绘图、导出、QC、HID、风场或 Web viewer 页面。

当前公开能力覆盖：

- 常见中国业务天气雷达基数据读取与写出
- `PRD` 体扫数据模型与 `aligned/native` 距离工作流
- PPI / RHI / 垂直剖面绘图
- 双偏振质量控制
- 水凝物分类与单雷达风场反演
- 多雷达组网插值
- Py-ART / xradar / WSR98D / NEXRAD 导出
- 本地 Web viewer

``1.0.9`` 中，QC、HID、风场反演及 CR / VIL / ET 计算将掩码样本作为缺测处理。
绘图和导出的使用说明见 :doc:`draw` 与 :doc:`save_data`；完整修复记录见
`v1.0.9 发布说明 <https://github.com/YvZheng/pycwr/releases/tag/v1.0.9>`_。

.. _PyCWR: https://github.com/YvZheng/pycwr

快速导航
-------------------------------

.. container:: doc-card-grid

   .. container:: doc-card

      **开始使用**

      - :doc:`PyCWR简介 <PyCWR_intro>`
      - :doc:`安装方法 <installation>`
      - :doc:`图形化界面显示 <GUI>`
      - :doc:`常见问题 <questions>`

   .. container:: doc-card

      **用户指南**

      - :doc:`数据读取 <data_read>`
      - :doc:`数据结构 <data_structure>`
      - :doc:`绘图 <draw>`
      - :doc:`导出数据 <save_data>`
      - :doc:`选取数据 <select_data>`

   .. container:: doc-card

      **高级处理**

      - :doc:`水凝物分类 <HC>`
      - :doc:`衰减订正 <PIA>`
      - :doc:`雷达数据插值 <interp>`
      - :doc:`组合反射率产品 <CR>`
      - :doc:`风场反演 <VR>`

   .. container:: doc-card

      **API 手册**

      - :doc:`API 总览 <api/index>`
      - :doc:`IO API <api/io>`
      - :doc:`PRD API <api/prd>`
      - :doc:`绘图 API <api/draw>`
      - :doc:`处理与 Viewer API <api/web>`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 开始使用

   PyCWR_intro
   installation
   GUI
   questions

**用户指南**

* :doc:`数据读取 <data_read>`
* :doc:`数据结构 <data_structure>`
* :doc:`绘图 <draw>`
* :doc:`导出数据 <save_data>`
* :doc:`选取数据 <select_data>`
* :doc:`水凝物分类 <HC>`
* :doc:`衰减订正 <PIA>`
* :doc:`雷达数据插值 <interp>`
* :doc:`组合反射率产品 <CR>`
* :doc:`CAPPI产品 <CAPPI_product>`
* :doc:`风场反演 <VR>`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 用户指南

   data_read
   data_structure
   draw
   save_data
   select_data
   HC
   PIA
   interp
   CR
   CAPPI_product
   VR

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: API 手册

   api/index

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: English

   en/index

开发者信息
-----------

:作者: 郑玉；pycwr contributors
:项目主页: https://github.com/YvZheng/pycwr
:当前手册版本: 1.0.9
