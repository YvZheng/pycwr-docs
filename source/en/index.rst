PyCWR Documentation
===================

:Release: 1.0.9

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

In 1.0.9, QC, HID, wind retrieval, and CR / VIL / ET computations treat masked
samples as missing data. See the `v1.0.9 release notes
<https://github.com/YvZheng/pycwr/releases/tag/v1.0.9>`_ for the complete fixes.

Installation
------------

``pycwr 1.0.9`` requires Python ``>=3.9``. For normal users, install from PyPI:

.. code-block:: bash

   python -m pip install pycwr

For plotting, QC, the Web viewer, and Py-ART / xradar interoperability:

.. code-block:: bash

   python -m pip install "pycwr[full]"

On Python 3.9, the full install includes plotting, QC, and the Web viewer, but
excludes Py-ART and xradar, which require Python ``>=3.10``.
See :doc:`/installation` for source installation and extension builds.

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
