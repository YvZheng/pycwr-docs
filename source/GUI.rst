图形化界面显示
=================

.. container:: lang-switch

   English version: :doc:`/en/GUI`

这页讲的是 Web viewer 的完整使用路径。程序化入口和后端接口清单请继续看 :doc:`api/web`。

PyCWR 当前推荐的图形界面是本地 Web viewer，而不是旧版 PyQt GUI。

.. container:: doc-hero

   .. container:: doc-eyebrow

      Web Viewer

   .. container:: doc-lead

      这是一个轻量、本机优先的雷达数据浏览界面，目标是让你快速扫描目录、查看 metadata、
      切换 field/sweep，并生成平面图或地图模式 quicklook。

启动流程
-----------------

.. container:: step-grid

   .. container:: step-card

      **1. 启动**

      .. code-block:: bash

         python scripts/LaunchGUI.py

   .. container:: step-card

      **2. 打开页面**

      默认地址：

      .. code-block:: text

         http://127.0.0.1:8787/

   .. container:: step-card

      **3. 选择数据**

      输入目录，扫描文件，然后选择目标文件、field 和 sweep。

   .. container:: step-card

      **4. 浏览与导出**

      切换 ``Map Mode``、连续色标、时间序列，并下载当前 PNG。

页面能做什么
-----------------

- 扫描本地雷达目录
- 读取单文件 metadata
- 选择场和仰角生成 ``ppi`` / ``ppi_map`` quicklook
- 统一显示离散 ``HCL`` 色标和中文类别名
- 快速确认 reader/QC/HID 之后的数据状态

常用使用路径
-----------------

1. 启动 viewer
2. 选择样本目录
3. 打开一个体扫文件
4. 先看 ``dBZ`` / ``Zc``、再看 ``V`` / ``Vc``、最后看 ``HCL`` 或 ``PIA``
5. 需要进一步处理时，再回到 Python 工作流里用 ``PRD`` 做 QC、导出或插值

安全边界
-----------------

- viewer 默认只允许本机访问
- 页面会自动注入 token
- 手工请求 ``/api/*`` 或 ``/plot/*`` 时必须携带 token
- 文件浏览被限制在允许目录内
- 它是本地查看工具，不应该被当成开放 Web 服务直接暴露

UI 与后端 API 的关系
---------------------

- 页面入口是 ``/``
- 数据浏览主要依赖 ``/api/files`` 和 ``/api/metadata``
- 图像生成主要依赖 ``/plot/ppi.png`` 和 ``/plot/ppi_map.png``
- 如果你需要自定义部署和 token/allowed_roots，请转到 :doc:`api/web`
