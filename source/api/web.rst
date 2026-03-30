Web / Viewer API
================

这页汇总本地 Web viewer 相关的公开入口和使用边界。

.. container:: api-box

   **推荐启动方式**

   .. code-block:: bash

      python scripts/LaunchGUI.py

   默认地址：

   .. code-block:: text

      http://127.0.0.1:8787/

.. container:: api-box

   **程序化入口**

   .. code-block:: python

      from pycwr.GraphicalInterface.web_app import create_app, launch

      app = create_app(allowed_roots=["/path/to/data"], auth_token="your-token")
      launch(host="127.0.0.1", port=8787, open_browser=True)

.. container:: api-box

   **常见接口**

   - ``GET /``
   - ``GET /api/files?...``
   - ``GET /api/metadata?...``
   - ``GET /plot/ppi.png?...``
   - ``GET /plot/ppi_map.png?...``

.. rubric:: 约束与边界

- viewer 默认只允许本机访问
- 页面会自动注入 token
- 手工请求 ``/api/*`` 或 ``/plot/*`` 时必须自行携带 token
- 文件浏览被限制在允许目录内

.. rubric:: 相关页面

- :doc:`../GUI`
- :doc:`draw`
