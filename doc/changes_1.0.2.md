schemas 1.0.2 — Released 2026-10-27

# Summary

This release regenerates the Poetry lock file, updating transitive dependencies to their latest versions allowed by the declared constraints.

We also updated the GitHub actions to their latest versions.

## Security

* CVE-2026-111497: Raised the optional `urllib3` Brotli-extra bounds to require patched `Brotli` and `brotlicffi` versions.
