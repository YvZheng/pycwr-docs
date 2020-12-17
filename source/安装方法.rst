安装方法
===================

Anaconda
------------
目前 *PyCWR* 仅支持Python3，推荐使用Python3.6及以上版本的Anaconda。

由于国内墙下载速度的限制，推荐在 清华镜像站_ 下载并安装Anaconda，提高下载速度。

Anaconda安装完毕后请按照 conda源修改教程_ 修改conda源为清华源，按照以下教程修改pip源为豆瓣源以提高库的安装速度，节省您的时间。

#. Linux/Mac平台

    Linux/Mac用户将它命名为pip.conf ::

        [global]
        timeout = 60
        index-url = http://pypi.douban.com/simple
        trusted-host = pypi.douban.com

    然后将该文件放在 ``$HOME/.pip/pip.conf`` 位置

#. Windows平台


    Windows用户将它命名为pip.ini ::

        [global]
        timeout = 60
        index-url = http://pypi.douban.com/simple
        trusted-host = pypi.douban.com

    然后将该文件放在 ``%HOME%\pip\pip.ini`` 位置


直接安装 *PyCWR* 在base环境
---------------------------

由于Cartopy采用pip安装容易出错，但 *PyCWR* 画图部分需要依赖 Cartopy_， 因此需要先采用conda来安装 Cartopy_，再使用pip安装 *PyCWR*。

#. 首先使用conda安装Cartopy

    .. code-block:: sh

        conda install cartopy -c conda-forge --yes

#. 然后使用pip安装PyCWR

    .. code-block:: sh

        pip install pycwr==0.3.1

隔离环境安装 *PyCWR* （推荐）
---------------------------

为防止 *PyCWR* 环境与base环境冲突，推荐使用隔离环境的方式安装。

#. 首先使用conda隔离环境并安装Cartopy

    .. code-block:: sh

        conda create -n cwr cartopy -c conda-forge --yes

#. 再切换到隔离的cwr环境

    .. code-block:: sh

        conda activate cwr

#. 最后在cwr环境中使用pip安装PyCWR

    .. code-block:: sh

        pip install pycwr==0.3.1



.. _清华镜像站: https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
.. _conda源修改教程: https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/
.. _Cartopy: https://scitools.org.uk/cartopy/docs/latest/