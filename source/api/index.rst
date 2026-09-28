API 手册
========

.. container:: lang-switch

   English version: :doc:`/en/api/index`

这组页面专门讲 ``pycwr 1.0.9`` 的公开接口，不再把 API 信息分散在 workflow 页面里。

.. container:: section-note

   阅读建议：

   - 想先跑通工作流，先看用户指南页
   - 想查函数、对象方法、参数和返回值，再看这组 API 页面

.. container:: doc-card-grid

   .. container:: doc-card

      **读取与写出**

      :doc:`IO API <io>`

      入口包括 ``read_auto``、格式 reader、WSR98D/NEXRAD writer。

   .. container:: doc-card

      **PRD 主对象**

      :doc:`PRD API <prd>`

      包括 ``summary``、``get_sweep_field``、导出接口和字段访问约定。

   .. container:: doc-card

      **绘图与产品**

      :doc:`绘图 API <draw>`

      包括 PPI、RHI、剖面、风场 quicklook 以及 ``HCL`` 色标说明。

   .. container:: doc-card

      **检索、QC、插值与 Viewer**

      :doc:`处理 / Viewer API <web>`

      包括 HID、风场反演、QC、组网插值和本地 Web viewer。

.. container:: compare-grid

   .. container:: compare-card

      **如果你是第一次使用**

      先看 :doc:`/data_read`、:doc:`/data_structure`、:doc:`/draw` 这三页，
      先把 workflow 跑通。

   .. container:: compare-card

      **如果你已经在写脚本**

      直接进入 ``IO``、``PRD``、``QC`` 和 ``retrieve`` 相关 API 页，
      查参数、返回值和字段约定。

API 组织方式
----------------

这组页面按“用户要完成什么任务”组织，而不是按源码目录逐层展开：

- ``IO``：先把文件读成 ``PRD``，或把 ``PRD`` 导出到标准格式
- ``PRD``：查看 sweep、字段、``aligned/native`` 和对象方法
- ``draw``：快速出图和兼容旧接口
- ``retrieve``：HID 和风场反演
- ``qc_interp``：QC、衰减订正和组网插值
- ``web``：本地 viewer、后端入口和使用边界

.. toctree::
   :maxdepth: 1
   :hidden:

   io
   prd
   draw
   retrieve
   qc_interp
   web
