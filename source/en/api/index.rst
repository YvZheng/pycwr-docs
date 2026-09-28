API Overview
============

.. container:: lang-switch

   中文版: :doc:`/api/index`

This page is the English reference hub for the public ``pycwr 1.0.9`` API surface.
Detailed workflow pages remain primarily Chinese, but the public entrypoints are grouped
here in an implementation-oriented way.

.. container:: doc-card-grid

   .. container:: doc-card

      **IO**

      ``read_auto``, format-specific readers, and WSR98D/NEXRAD writers.

      Detailed Chinese page: :doc:`/api/io`

   .. container:: doc-card

      **PRD Object Model**

      ``summary``, ``available_fields``, ``get_sweep_field``, and export methods.

      Detailed Chinese page: :doc:`/api/prd`

   .. container:: doc-card

      **Plotting / Products**

      PPI, map PPI, RHI, vertical sections, wind quicklooks, and ``HCL`` display.

      Detailed Chinese page: :doc:`/api/draw`

   .. container:: doc-card

      **Retrieval / QC / Interp / Viewer**

      HID, wind retrieval, dual-pol QC, attenuation correction, network gridding,
      and the local Web viewer.

      Detailed Chinese pages: :doc:`/api/retrieve`, :doc:`/api/qc_interp`, :doc:`/api/web`

How to use this hub
-------------------

- Use the Chinese API pages when you need the fuller workflow context
- Use this page when you want a clean English map of the public entrypoints
- Keep API names and call patterns exactly as documented in code; this is a presentation refresh, not an API redesign
