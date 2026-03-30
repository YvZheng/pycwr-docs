Web Viewer
==========

.. container:: lang-switch

   中文版: :doc:`/GUI`

This page covers the product-style usage path of the local ``pycwr`` Web viewer.
For the backend entrypoints and API routes, see :doc:`/api/web`.

.. container:: doc-hero

   .. container:: doc-eyebrow

      Local Browser UI

   .. container:: doc-lead

      The viewer is a lightweight local browser interface for exploring radar files,
      switching fields and sweeps, and generating quicklook PNG products.

Startup flow
------------

.. container:: step-grid

   .. container:: step-card

      **1. Launch**

      .. code-block:: bash

         python scripts/LaunchGUI.py

   .. container:: step-card

      **2. Open**

      .. code-block:: text

         http://127.0.0.1:8787/

   .. container:: step-card

      **3. Browse data**

      Choose a local directory, scan files, then pick a field and sweep.

   .. container:: step-card

      **4. Inspect results**

      Toggle map mode, continuous colorbars, and export the current PNG view.

What the viewer is good at
--------------------------

- Quickly checking whether a file reads cleanly
- Comparing ``dBZ`` with ``Zc`` or ``V`` with ``Vc``
- Browsing ``HCL`` with the unified discrete color map
- Producing quick local previews before deeper Python-side processing

Security boundaries
-------------------

- Localhost-only by default
- Token-protected backend routes
- File browsing restricted to allowed roots
- Intended as a local data browser, not a public web service
