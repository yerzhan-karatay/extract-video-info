# Security Policy

## Supported Versions

Security fixes target the latest released version.

## Reporting a Vulnerability

Use GitHub private vulnerability reporting if it is available for this repository. If it is not available, open a public issue only to request a private reporting channel; do not include exploit details, secrets, private URLs, cookies, or credentials in public issues, discussions, pull requests, logs, screenshots, or generated evidence files.

## Scope

In scope:

- Command injection risks.
- Unsafe handling of local paths.
- Accidental credential exposure in logs or outputs.
- Unsafe use of downloaded media, OCR data, or metadata.

Out of scope:

- Requests to bypass Instagram, TikTok, YouTube, or other platform access controls.
- Issues caused by user-provided credentials, browser cookies, or private videos used outside their intended access rights.

## Safety Rules

The project should support public URLs, user-provided local files, and user-authorized authenticated downloads only. It should not include scraping workarounds that evade access controls.
