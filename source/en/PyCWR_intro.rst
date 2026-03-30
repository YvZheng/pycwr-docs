Introduction
============

.. container:: lang-switch

   中文版: :doc:`/PyCWR_intro`

.. container:: doc-hero

   .. container:: doc-eyebrow

      Why PyCWR

   Chinese weather radar base data often comes from multiple vendors, generations,
   and business pipelines. ``pycwr`` turns that fragmented input space into one
   consistent Python workflow.

.. container:: doc-card-grid

   .. container:: doc-card

      **Core capabilities**

      - Radar readers for common operational formats
      - A unified ``PRD`` object model
      - ``aligned`` / ``native`` reflectivity workflows
      - Plotting, QC, HID, wind retrieval, interpolation, and export

   .. container:: doc-card

      **Design priorities**

      - Preserve reader behavior and result consistency
      - Keep corrected and raw fields separate
      - Remain practical for scientific and operational workflows

   .. container:: doc-card

      **Where to go next**

      - :doc:`/installation`
      - :doc:`/data_read`
      - :doc:`/data_structure`
      - :doc:`/api/index`

This toolkit is especially useful if you need to move between raw radar files,
``xarray``-style analysis, visualization, and interoperability with Py-ART or xradar
without rebuilding a full parsing stack for each format.
