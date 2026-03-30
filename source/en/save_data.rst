Export Data
===========

.. container:: lang-switch

   中文版: :doc:`/save_data`

This page focuses on export workflows. For the public writer and object-method list,
see :doc:`/api/io` and :doc:`/api/prd`.

``pycwr 1.0.4`` does not limit export to Py-ART anymore.

Recommended object-style export
-------------------------------

.. code-block:: python

   radar.to_pyart_radar(...)
   radar.to_xradar(...)
   radar.to_wsr98d(...)
   radar.to_nexrad_level2_msg31(...)
   radar.to_nexrad_level2_msg1(...)

Function-style writers are also available:

.. code-block:: python

   from pycwr.io import (
       write_wsr98d,
       write_nexrad_level2_msg31,
       write_nexrad_level2_msg1,
   )

Py-ART / CfRadial
-----------------

.. code-block:: python

   from pycwr.io import read_auto

   radar = read_auto("./data/file.bin.bz2")
   pyart_radar = radar.to_pyart_radar()

If Py-ART is installed, you can continue and write CfRadial:

.. code-block:: python

   import pyart
   pyart.io.write_cfradial("./cfradial.nc", pyart_radar)

WSR98D / NEXRAD export
----------------------

.. code-block:: python

   radar.to_wsr98d("./export.bin")
   radar.to_nexrad_level2_msg31("./export_msg31.ar2v")
   radar.to_nexrad_level2_msg1("./export_msg1.ar2v")

Notes
-----

- ``WSR98D`` export is mainly used for project round-trip and compatibility verification
- ``NEXRAD`` export is mainly for interoperability with Py-ART and external workflows
- Corrected fields and raw fields remain separate variables inside ``PRD``
- When exporting to standard interfaces, ``pycwr`` chooses a suitable source field according to the current public rules

Related pages
-------------

- :doc:`/api/io`
- :doc:`/api/prd`
- :doc:`/PIA`
