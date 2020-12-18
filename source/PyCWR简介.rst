PyCWR简介
===================

中国天气雷达基数据的格式由于历史遗留问题多种多样，文件复杂，雷达数据的处理和应用往往需要重要的先验知识和技能，各种算法难以统一实施。
基于Python的中国天气雷达（PyCWR）库旨在解决这些问题并使雷达数据变得易于使用。

.. Important::
    - 它支持几乎所有中国业务天气雷达基数据格式，包含WSR98D、CINRAD/SA/SB/CB、CINRAD/CC/CCJ、CINRAD/SC/CD等雷达基数据格式；
    - 定义用于表示雷达数据的核心Python对象，而该对象是使用xarray的Dataset构建的，Dataset是类似dict的具有对齐尺寸的带标签数组的容器；
    - 提供了经过良好测试的算法（数据质量控制，水凝物分类，定量降水估计等），并使用Cython加速核心算法；
    - 建立开放的平台，供研究人员从天气雷达观测中开发复杂的分析和应用程序，它还提供了图形用户界面工具，以方便进行水文学和气象学分析。


#. 天气雷达PPI扫描显示：

    .. image:: _static/PPI.png
        :height: 500px
        :width: 583px
        :align: center
        :alt: reStructuredText, the markup syntax

#. 天气雷达RHI扫描显示：

    .. image:: _static/RHI.png
        :height: 500px
        :width: 608px
        :align: center
        :alt: reStructuredText, the markup syntax

#. 天气雷达CAPPI插值显示：

    .. image:: _static/CAPPI.png
        :height: 500px
        :width: 583px
        :align: center
        :alt: reStructuredText, the markup syntax

#. 天气雷达组合反射率因子显示：

    .. image:: _static/CRF.png
        :height: 500px
        :width: 583px
        :align: center
        :alt: reStructuredText, the markup syntax

#. 天气雷达VCS垂直剖面图：

    .. image:: _static/VCS.png
        :height: 500px
        :width: 592px
        :align: center
        :alt: reStructuredText, the markup syntax

#. 水凝物分类算法： 

    .. image:: _static/HC.png
        :height: 500px
        :width: 623px
        :align: center
        :alt: reStructuredText, the markup syntax

#. 更多功能更新中...


