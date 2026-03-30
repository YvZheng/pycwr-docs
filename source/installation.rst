安装方法
===================

PyCWR 1.0.4 当前要求：

- Python `>=3.9`
- 基础功能可直接用 `pip`
- 如果需要绘图、QC、Web viewer、Py-ART / xradar 互操作，建议安装 full 依赖

基础安装
------------

.. code-block:: bash

    python -m pip install -r requirements-core.txt
    python -m pip install .

这条路径足够支持：

- reader
- `PRD`
- 几何计算
- 插值
- NetCDF 风格导出

全功能安装
------------

.. code-block:: bash

    python -m pip install -r requirements-full.txt
    python -m pip install ".[full]"

这条路径额外覆盖：

- 绘图和地图绘图
- 双偏振 QC
- 本地 Web viewer
- Py-ART / xradar 互操作

说明
------------

- 上游 `arm_pyart` 和 `xradar` 当前要求 Python `>=3.10`
- 因此在 Python `3.9` 上，full 安装仍然可以用于绘图、QC 和 Web viewer，但不包含这两类互操作能力
- `pandas` 在 `1.0.4` 中限制为 `<3`，优先保证发布稳定性

从源码重编译 Cython 扩展
---------------------------

如果修改了 `pycwr/core/RadarGridC.pyx`，重编译方式为：

.. code-block:: bash

    python setup.py build_ext --inplace

构建发布产物
---------------------------

.. code-block:: bash

    python -m build
