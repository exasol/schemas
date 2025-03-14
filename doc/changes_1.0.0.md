# Summary

This release updates the Python dependency `jinja2` to prevent sandbox breakthroughs with an indirect reference to format method (CVE-2024-56326) or through malicious filenames (CVE-2024-56201).

Also started versioning the schema project as a whole.

## Changes

* #35: Updated `jinja2` to fix CVE-2024-56201 and CVE-2024-56326
* #37: Updated `jinja2` to fix CVE-2025-27516