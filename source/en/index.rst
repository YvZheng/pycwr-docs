PyCWR Documentation
===================

.. container:: lang-switch

   中文主页: :doc:`/index`

.. container:: doc-hero

   .. container:: doc-eyebrow

      China Weather Radar Toolkit

   ``pycwr`` is a Python toolkit for reading, inspecting, plotting, correcting,
   exporting, and browsing Chinese weather radar base data.

   .. container:: doc-lead

      This English entry is a focused public-facing guide. The Chinese pages remain
      the primary full manual, while this section covers the most visible pages:
      landing, introduction, GUI, API overview, and attenuation correction.

.. container:: doc-card-grid

   .. container:: doc-card

      **Start Here**

      - :doc:`Introduction <PyCWR_intro>`
      - :doc:`Read Data <data_read>`
      - :doc:`PRD Structure <data_structure>`
      - :doc:`Export Data <save_data>`
      - :doc:`Web Viewer <GUI>`
      - :doc:`API Overview <api/index>`
      - :doc:`Attenuation Correction <PIA>`

   .. container:: doc-card

      **What You Can Do**

      - Read common Chinese radar formats
      - Work with a unified ``PRD`` volume model
      - Plot PPI, RHI, and vertical sections
      - Run QC, HID, wind retrieval, and network interpolation

   .. container:: doc-card

      **Detailed Chinese Guides**

      - :doc:`/data_read`
      - :doc:`/data_structure`
      - :doc:`/draw`
      - :doc:`/save_data`

   .. container:: doc-card

      **Project Positioning**

      - Behavior compatibility first
      - Raw and corrected fields remain separate
      - Good fit for Py-ART / xradar interoperability

.. toctree::
   :maxdepth: 1
   :hidden:

   PyCWR_intro
   data_read
   data_structure
   save_data
   GUI
   api/index
   PIA
