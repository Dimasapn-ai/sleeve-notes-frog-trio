# Sleeve Notes for the Frog Trio — notes

## Concept

Back-cover sleeve notes for a jazz trio made entirely of frogs — alto
saxophone, bass, drums — played completely straight, as if reviewing a
real working band with a real residency. The title is short, evocative
and file-able in a record shop ("Sessions" carries the jazz flavour);
it is deliberately not a pun. The blurb is specific about the trio,
their sound, and the room they play: a one-night recording at the
Boathouse, their Friday residency, the sax close and dry, the bass
"walking the shallow end" (the one quiet nod to the pond), brushes on a
nine-summers-old kit. It closes on the band's ethic — listening hard,
leaving space, swinging — rather than on a joke.

## The text (exactly as written to entry.txt)

Lily Pad Sessions
The trio's fifth record, cut in one night at the Boathouse, where they hold the Friday residency. Alto sax close and dry, the bass walking the shallow end, brushes on a kit that has weathered nine summers. No guests, no gimmicks — three players listening hard, leaving space, and swinging.

## Format

- Title and blurb joined by a single newline; no trailing newline.
- Total length is within the 1–400 character gate (verified by the
  test run: title + newline + blurb, UTF-8).
- `main.py` (Python standard library only) resolves the output
  directory first — `$MAKEFUN_OUTPUT_DIR` if set, else `/output` —
  creates it, and writes only `entry.txt` there. Deterministic:
  two runs produce byte-identical output.
