PyCWR简介
===================

中国天气雷达基数据格式历史包袱较重，不同厂家、不同年代、不同业务链路之间差异很大。
PyCWR 的目标是把这些输入统一成可读、可画、可处理、可导出的 Python 工作流。

当前版本重点能力
------------------

- 常见中国业务天气雷达格式 reader
- 统一的 `PRD` 体扫对象
- `aligned/native` 反射率双工作流
- 绘图、QC、水凝物分类、风场反演
- 多雷达组网插值
- Py-ART / xradar / WSR98D / NEXRAD 导出
- 本地 Web viewer

项目特点
------------------

- reader 侧优先保证行为兼容和结果一致
- `PRD` 基于 `xarray.Dataset`，便于后续分析
- 核心几何与部分热点路径带有 Cython 加速
- corrected 字段和原始字段分离存储，便于科研对照与业务落地

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
