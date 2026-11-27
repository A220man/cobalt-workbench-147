# Changelog

## 1.3.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.2.1 — work-in-progress checkpoint

- Added input validation to the `/generate` endpoint: `class_name` and `variable_name`
  must be valid Dart identifiers (start with a letter or underscore, followed by
  letters, digits, or underscores). Invalid inputs return HTTP 422 with a descriptive
  detail message.

## 1.2.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.1.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.0.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.0.0 — generate endpoint added

- Implemented /generate endpoint returning Dart code for a StatefulWidget with a TextEditingController.
- Added test coverage for the endpoint.
- Added UI mockup planning.
