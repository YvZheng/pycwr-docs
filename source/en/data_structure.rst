Data Structure
==============

.. container:: lang-switch

   中文版: :doc:`/data_structure`

The central object in ``pycwr`` is ``PRD`` (Polarimetric Radar Data).

Readers convert raw radar base data into a ``PRD`` first; plotting, QC, retrieval,
interpolation, and export workflows are then built around that object.

.. container:: section-note

   If you are new to ``pycwr``, learn this page before you dive into plotting or export.

Main parts of ``PRD``
---------------------

- ``fields``: one ``xarray.Dataset`` per sweep
- ``scan_info``: site and scan metadata
- ``extended_fields``: native-range sidecars when aligned/native layouts differ
- ``product``: derived product collection

Most useful inspection methods
------------------------------

.. code-block:: python

   radar.summary()
   radar.available_fields()
   radar.sweep_summary()
   radar.get_sweep_field(0, "dBZ")
   radar.get_native_sweep_field(0, "dBZ")

``aligned`` vs ``native``
-------------------------

Current ``PRD`` workflows support two reflectivity access modes:

- ``range_mode="aligned"``: the historical shared range-grid workflow
- ``range_mode="native"``: the original reflectivity range layout

Recommendations:

- Use ``aligned`` when you need compatibility with older workflows
- Use ``native`` when you need the true low-level reflectivity coverage

Example:

.. code-block:: python

   aligned = radar.get_sweep_field(0, "dBZ", range_mode="aligned")
   native = radar.get_sweep_field(0, "dBZ", range_mode="native")

Fields remain separate variables
--------------------------------

Raw and corrected fields are stored separately. For example:

- ``dBZ`` and ``Zc``
- ``V`` and ``Vc``
- ``W`` and ``Wc``
- ``ZDR`` and ``ZDRc``

Treat them as distinct variables when you inspect, plot, or export data.

Related pages
-------------

- :doc:`/api/prd`
- :doc:`/select_data`
- :doc:`/save_data`
