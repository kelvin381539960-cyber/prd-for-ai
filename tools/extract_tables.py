#!/usr/bin/env python3
"""
Compatibility wrapper.

The old extract_tables.py was a one-off script with a hard-coded DOCX filename and
table indexes. Use extract_docx_tables.py for reusable table extraction.
"""

from __future__ import annotations

from extract_docx_tables import main

if __name__ == "__main__":
    raise SystemExit(main())
