schemas 1.0.1 — Released 2026-04-2025

# Summary

This release updates the Python dependency `urllib3` to prevent a compression bomb (CVE-2026-21441), `requests` to prevent insecure file reuse (CVE-2026-25645) and `pygments` to prevent an ReDoS attack (CVE-2026-4539).

We also updated GitHub actions to their latest versions.

This only affects the build of this project. **Schema users are not affected.**

## Changes

* #39: Updated to poetry 2.1.2 & pinned GitHub actions
* #41: Set default GitHub token permissions & replaced 3rd party plugin
* #43: Relocked dependencies for vulnerabilities found in urllib3 & requests
* #45: Publish EDML schema 2.1.0
* #46: Relocked dependencies for vulnerabilities found in urllib3 & marshmallow
* #49: Fixed CVE-2026-21441, CVE-2026-25645 and CVE-2026-4539 by updating poetry lock.
