.. image:: _static/NJIAS.png
    :height: 200px
    :width: 733px
    :align: center
    :alt: reStructuredText, the markup syntax

===========================================
*PyCWR*：天气雷达数据处理工具库
===========================================

:Release: V0.3.4
:Date: |today|

PyCWR_  （Python based China Weather Radar Toolkit）主要面向中国天气雷达基数据的科研和应用，
广泛支持中国业务天气雷达基数据（WSR98D、CINRAD/SA/SB/CB、CINRAD/CC/CCJ和CINRAD/SC/CD等），
方便用于科研和业务上数据处理和分析，PyCWR现阶段主要由NJIAS团队进行维护和更新。

.. _PyCWR: https://github.com/YvZheng/pycwr

使用文档
-------------------------------
**开始使用**

* :doc:`PyCWR简介`
* :doc:`安装方法`
* :doc:`图形化界面显示`
* :doc:`常见问题`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: 开始使用

   PyCWR_intro
   installation
   GUI
   questions

**用户指南**

* :doc:`数据读取`
* :doc:`数据结构`
* :doc:`绘图`
* :doc:`导出数据`
* :doc:`选取数据`
* :doc:`水凝物分类`
* :doc:`衰减订正`
* :doc:`雷达数据插值`
* :doc:`组合反射率产品`
* :doc:`CAPPI产品`
* :doc:`风场反演`


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


开发者信息
-----------

   .. bibliographic fields :
   :作者: 郑玉 [#f1]_ ; 李南 [#f2]_ ; 魏鸣 [#f2]_ ; 楚志刚 [#f2]_
   :地址: 南京市建邺区雨顺路6号江苏省气象预警中心
   :邮箱: yuzheng1206@outlook.com; zhengyu@cma.gov.cn
   :贡献: 特别感谢李扬、张昕、贾鹏程、吕星超和樊丝慧等人对项目的支持。



.. [#f1] 中国气象局交通气象重点开放实验室，南京气象科技创新研究院
.. [#f2] 大气物理学院，南京信息工程大学