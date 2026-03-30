Attenuation Correction
======================

.. container:: lang-switch

   中文版: :doc:`/PIA`

This page documents the public attenuation-correction workflow in ``pycwr`` and shows
copyable Python examples for both array-level and ``PRD``-level usage.

.. container:: doc-hero

   .. container:: doc-eyebrow

      Recommended Path

   .. container:: doc-lead

      For modern dual-polarization workflows, the recommended public path is
      ``run_dualpol_qc`` / ``apply_dualpol_qc``. These routines produce corrected
      reflectivity, corrected ZDR, path-integrated attenuation, and related QC fields.

Where it fits in the workflow
-----------------------------

1. Read the radar file into a ``PRD``
2. Run dual-pol QC / attenuation correction
3. Use corrected fields in plotting, HID, or export workflows

Inputs and outputs
------------------

Typical inputs:

- ``dBZ``
- ``KDP`` or ``PhiDP``
- optionally ``ZDR``, ``CC``, and ``SNRH``

Typical outputs:

- ``Zc``
- ``ZDRc``
- ``PIA``
- ``PIA_ZDR``
- ``KDPc``
- ``PhiDP_smooth``
- ``QC_MASK``

Raw vs corrected behavior
-------------------------

- Raw and corrected fields remain separate variables
- Running ``radar.apply_dualpol_qc`` does not overwrite ``dBZ`` or ``ZDR``
- Corrected fields are written back into ``PRD.fields[sweep]``

Quick start
-----------

.. code-block:: python

   from pycwr.io import read_auto

   radar = read_auto("./data/file.bin.bz2")
   qc_radar = radar.apply_dualpol_qc(inplace=False, band="C")

   corrected_dbz = qc_radar.get_sweep_field(0, "Zc")
   pia = qc_radar.get_sweep_field(0, "PIA")

Array-level API example
-----------------------

.. code-block:: python

   from pycwr.qc import correct_attenuation_kdp

   z_corr, pia, zdr_corr, pia_zdr = correct_attenuation_kdp(
       ref=dbz_2d,
       kdp=kdp_2d,
       dr=0.075,
       zdr=zdr_2d,
   )

PRD workflow example
--------------------

.. code-block:: python

   from pycwr.io import read_auto
   from pycwr.qc import run_dualpol_qc

   radar = read_auto("./data/file.bin.bz2")
   sweep = radar.fields[0]
   gate_length_km = float((sweep["range"].values[1] - sweep["range"].values[0]) / 1000.0)

   results = run_dualpol_qc(
       ref=sweep["dBZ"].values,
       zdr=None if "ZDR" not in sweep else sweep["ZDR"].values,
       phidp=None if "PhiDP" not in sweep else sweep["PhiDP"].values,
       kdp=None if "KDP" not in sweep else sweep["KDP"].values,
       rhohv=None if "CC" not in sweep else sweep["CC"].values,
       snr=None if "SNRH" not in sweep else sweep["SNRH"].values,
       dr=gate_length_km,
       band="C",
   )

   print(results["ref_corrected"].shape)
   print(results["pia"].shape)

Downstream usage
----------------

- Plot ``Zc`` or ``PIA`` explicitly; do not assume ``dBZ`` is automatically replaced
- HID workflows can prefer corrected fields when they are present
- Export workflows may choose corrected fields according to public rules, but the original variables remain in ``PRD``
