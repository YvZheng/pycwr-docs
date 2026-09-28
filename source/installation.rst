安装方法
===================

PyCWR 1.0.9 当前要求：

- Python `>=3.9`
- 普通用户推荐从 PyPI 安装
- 如果需要绘图、QC、Web viewer、Py-ART / xradar 互操作，建议安装 full 依赖

基础安装
------------

.. code-block:: bash

    python -m pip install pycwr

这条路径足够支持：

- reader
- `PRD`
- 几何计算
- 插值
- NetCDF 风格导出

全功能安装
------------

.. code-block:: bash

    python -m pip install "pycwr[full]"

这条路径额外覆盖：

- 绘图和地图绘图
- 双偏振 QC
- 本地 Web viewer
- Py-ART / xradar 互操作

说明
------------

- 上游 `arm_pyart` 和 `xradar` 当前要求 Python `>=3.10`
- 因此在 Python `3.9` 上，full 安装仍然可以用于绘图、QC 和 Web viewer，但不包含这两类互操作能力
- `pandas` 在 `1.0.9` 中限制为 `<3`，优先保证发布稳定性
- `1.0.9` 提供 CPython 3.9–3.12 的预编译 wheel，覆盖 Linux x86_64、Windows x64 和 macOS Intel / Apple silicon

从源码安装
---------------------------

本地开发或重编译扩展时，先检出主仓库并进入项目根目录：

.. code-block:: bash

    git clone --branch v1.0.9 https://github.com/YvZheng/pycwr.git
    cd pycwr

基础依赖安装：

.. code-block:: bash

    python -m pip install -r requirements-core.txt
    python -m pip install .

需要完整依赖时，改用：

.. code-block:: bash

    python -m pip install -r requirements-full.txt
    python -m pip install ".[full]"

从源码重编译 Cython 扩展
---------------------------

如果修改了 `pycwr/core/RadarGridC.pyx`，重编译方式为：

.. code-block:: bash

    python setup.py build_ext --inplace

构建发布产物
---------------------------

.. code-block:: bash

    python -m build
