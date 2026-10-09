# JA Certifier Grammar Publication System

## Visual idea

The suite uses the visual metaphor of a **proof press**: dark ink for source truth, warm paper for study, copper for transformation, teal for analysis, green for admitted proof, amber for unresolved evidence, and red for rejected gates. Decoration never outranks evidence.

## Information hierarchy

1. Suite and artifact identity
2. Claim and explicit exclusions
3. Source and semantic hashes
4. Grammar analysis and diagnostics
5. Policy and validator decisions
6. R12/MCRT and replay evidence
7. Certification or unresolved result
8. Provenance, limitations, and next native test

## Evidence cards

Use compact cards with six labeled fields: `OBJECT`, `PROFILE`, `STAGE`, `RESULT`, `IDENTITY`, and `LIMIT`. Cards must not use color alone to communicate status.

## Air-gap rules

- Markdown, JSON, CSV, EBNF, and local SVG only
- No remote fonts, scripts, styles, trackers, or linked images
- System-font fallbacks only
- Short Windows-safe paths
- Print and monochrome legibility

## Podium rule

A page is beautiful when a reviewer can find the governing claim, evidence, failure stage, provenance, and limitation without searching through decorative noise.
