图形化界面显示
=================

这页讲使用流程。程序化入口和后端接口清单请继续看 :doc:`api/web`。

PyCWR 当前推荐的图形界面入口是本地 Web viewer，而不是旧版 PyQt GUI。

启动方式
-----------------

.. code-block:: bash

    python scripts/LaunchGUI.py

默认页面地址：

.. code-block:: text

    http://127.0.0.1:8787/

页面能做什么
-----------------

- 输入本地雷达目录并扫描文件
- 选择文件、场和仰角
- 切换 `Map Mode`
- 切换连续色标
- 浏览时间序列并下载当前 PNG

约束
-----------------

- viewer 默认只允许本机访问
- 页面会自动注入 token
- 手工请求 `/api/*` 或 `/plot/*` 时必须携带 token
- 文件浏览被限制在允许目录内

这套 Web viewer 是轻量本地浏览器界面，不再试图完全复刻旧 PyQt 交互。
