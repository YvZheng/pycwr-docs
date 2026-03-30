风场反演
=============

PyCWR 当前公开的单雷达风场反演接口包括：

- `retrieve_vad`
- `retrieve_vvp`
- `retrieve_vwp`

它们都基于 `PRD` 对象工作。

示例
------------------

.. code-block:: python

    vad = radar.retrieve_vad(sweeps=0)
    vvp = radar.retrieve_vvp(0)
    vwp = radar.retrieve_vwp(sweeps=[0, 1, 2])

速度场选择
------------------

如果同时存在原始速度和订正速度：

- 默认优先使用 `Vc`
- 不存在 `Vc` 时回退到 `V`

这条规则主要是为了让当前业务样本更稳地进入风场反演链路。
