API 手册
========

这组页面专门讲 ``pycwr 1.0.4`` 的公开接口，不再把 API 信息分散在 workflow 页面里。

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

.. toctree::
   :maxdepth: 1
   :hidden:

   io
   prd
   draw
   retrieve
   qc_interp
   web
