schemas 1.0.1 — Released 2026-04-2025

# Summary

This release updates the Python dependency `urllib3` to prevent a compression bomb (CVE-2026-21441), `requests` to prevent insecurt file reuse (CVE-2026-25645) and `pygments` to prevent an ReDoS attack (CVE-2026-4539).

This only affects the build of this project. **Schema users are not affected.**

## Changes

* #35: Fixed CVE-2026-21441, CVE-2026-25645 and CVE-2026-4539 by updating poetry lock.