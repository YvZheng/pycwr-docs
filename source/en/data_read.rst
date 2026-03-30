Read Data
=========

.. container:: lang-switch

   中文版: :doc:`/data_read`

This page answers two practical questions:

- Where should you start when you first receive a radar file?
- What object do you get back after reading it?

Public readers currently focus on:

- ``WSR98D``
- ``SAB``
- ``CC``
- ``SC``
- ``PA``

All readers return the same core object: ``pycwr.core.NRadar.PRD``.

Recommended entrypoint
----------------------

The recommended starting point is ``read_auto``:

.. code-block:: python

   from pycwr.io import read_auto

   radar = read_auto("./data/Z_RADR_I_Z9046_20260317065928_O_DOR_SAD_CAP_FMT.bin.bz2")
   print(radar.summary())
   print(radar.available_fields())

What ``read_auto`` does
-----------------------

- Detects the radar file family automatically
- Parses it into a ``PRD``
- Preserves the sweep layout and geometry behavior expected by current ``pycwr`` workflows

Call signature
--------------

.. code-block:: python

   read_auto(
       filename,
       station_lon=None,
       station_lat=None,
       station_alt=None,
       effective_earth_radius=None,
   )

Parameter notes
---------------

- ``filename``: path to the radar file; compressed ``bz2`` / ``gz`` inputs are supported
- ``station_lon`` / ``station_lat`` / ``station_alt``: optional station overrides
- ``effective_earth_radius``: optional geometry parameter in meters

Format-specific readers
-----------------------

If you already know the exact file family, you can call:

.. code-block:: python

   from pycwr.io import read_WSR98D, read_SAB, read_CC, read_SC, read_PA

   radar = read_WSR98D("./data/file.bin.bz2")

These functions still return the same ``PRD`` object type.

Working with Py-ART
-------------------

.. code-block:: python

   from pycwr.io import read_auto

   radar = read_auto("./data/file.bin.bz2")
   pyart_radar = radar.to_pyart_radar()

If Py-ART is installed, ``pycwr`` can export the volume into a Py-ART ``Radar`` object.

Related pages
-------------

- :doc:`/api/io`
- :doc:`/api/prd`
- :doc:`/data_structure`
