# Project Carbox - Documentation Repository

Structural Identification of Anomalous Carboxyl Protonation States, Low-Barrier Hydrogen Bonds, and Microenvironment Dielectric Shielding

- Read the Docs: [https://project-carbox.readthedocs.io/en/latest/](https://project-carbox.readthedocs.io/en/latest/)
- Web Portal: [https://project-carbox.github.io/](https://project-carbox.github.io/)
- Contact: [suleyman.hacizade1@gmail.com](mailto:suleyman.hacizade1@gmail.com)

## Author and Academic Affiliations

- **Suleiman M. Hajizadeh** (Author and Developer): Institute of Molecular Biology, Ministry of Science and Education of the Republic of Azerbaijan; Western Caspian University, Baku, Azerbaijan
- **Prof. Garib N. Murshudov** (Scientific Inspiration and Theoretical Reference): MRC Laboratory of Molecular Biology (LMB), Cambridge Biomedical Campus, Cambridge, United Kingdom

## Overview

This repository contains the Sphinx documentation sources for Project Carbox, published on Read the Docs at [https://project-carbox.readthedocs.io/en/latest/](https://project-carbox.readthedocs.io/en/latest/).

Core computational pipeline sources (`carbox`), 7,230-structure PDB screening matrices, and electron density correlation tables are maintained in the private repository (`project-carbox/carbox`). To request access for academic collaboration or peer review, contact [suleyman.hacizade1@gmail.com](mailto:suleyman.hacizade1@gmail.com).

## Contents

1. **Multilingual Documentation:**
   - English (`docs/en/`): Algorithmic theory, command-line interfaces, Python API, and REFMAC5/Servalcat restraints.
   - Azerbaijani (`docs/az/`): Complete documentation of the crystallographic methodology, equations, and software tools.
   - Hebrew (`docs/he/`): Right-to-left localized documentation.
2. **Scientific Memoranda and Manuals:**
   - `CARBOX_MASTER_MANUAL.md` / `CARBOX_MASTER_MANUAL.pdf`: Technical manual and reference guide.
   - `CARBOX_CRYSTALLOGRAPHIC_VALIDATION_MEMORANDUM.md`: Crystallographic validation protocol specification.
3. **Refinement Restraints:**
   - Specification of geometric, distance, and protonation restraints for REFMAC5 and Servalcat.

## Local Build Instructions

```bash
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
```

## License

Mozilla Public License 2.0 (MPL-2.0). See [LICENSE](LICENSE) for details.
