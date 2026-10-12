PLUTUS_CONTEXT_HANDOVER — FULL CONTEXT HANDOVER
================================
Paste into a local TUI in this order:

1. 00_HANDOVER/PLUTUS_CONTEXT_HANDOVER.md
   Primary-agent memory. Rulings, freeze internals, dead paths.

2. 01_BINDING_SPEC/PLUTUS_5.0_MIMOCODE_ARCHITECTURE_SPEC.md
   The only build spec. Law.

3. Optional short inject in 00_HANDOVER/ if context is tight.

4. Everything else is reference or negative example.
   02_SUPERSEDED_READ_ONLY — do not implement rejected drives.
   03_HOST_BIBLES — later depth only.
   04_ADJACENT — other products in the same workspace.

Conflict rule:
  BINDING wins on implementation detail.
  Handover wins on session rulings and named dead paths.
  Superseded specs are APIs + history.
If handover conflicts with BINDING spec on implementation detail, BINDING wins. Handover wins on session rulings and dead-path names. Superseded specs are history only. Adjacent products are other deliverables.
