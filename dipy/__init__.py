"""
Diffusion Imaging in Python
============================

For more information, please visit https://dipy.org

Subpackages
-----------
::

 align         -- Registration, streamline alignment, volume resampling
 core          -- Spheres, gradient tables
 core.geometry -- Spherical geometry, coordinate and vector manipulation
 core.meshes   -- Point distributions on the sphere
 data          -- Small testing datasets
 denoise       -- Denoising algorithms
 direction     -- Manage peaks and tracking
 io            -- Loading/saving of dpy datasets
 nn            -- Neural networks algorithms
 reconst       -- Signal reconstruction modules (tensor, spherical harmonics,
                  diffusion spectrum, etc.)
 segment       -- Tractography segmentation
 sims          -- MRI phantom signal simulation
 stats         -- Tractometry
 tracking      -- Tractography, metrics for streamlines
 viz           -- Visualization and GUIs
 workflows      -- Predefined Command line for common tasks

Utilities
---------
::

 test          -- Run unittests
 __version__   -- Dipy version

"""

from dipy.version import version as __version__


def get_info():
    from pathlib import Path
    import sys

    import numpy

    import dipy

    return {
        "pkg_path": Path(__file__).resolve().parent,
        "commit_hash": dipy.version.git_revision,
        "sys_version": sys.version,
        "sys_executable": sys.executable,
        "sys_platform": sys.platform,
        "np_version": numpy.__version__,
        "dipy_version": dipy.__version__,
    }


submodules = [
    "align",
    "core",
    "data",
    "denoise",
    "direction",
    "io",
    "nn",
    "reconst",
    "segment",
    "sims",
    "stats",
    "tracking",
    "utils",
    "viz",
    "workflows",
    "tests",
    "testing",
]

__all__ = submodules + ["__version__", "setup_test", "get_info"]
