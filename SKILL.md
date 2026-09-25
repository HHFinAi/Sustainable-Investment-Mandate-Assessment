---
name: sustainable-investment-mandate-agent
description: Does the evidence support the stated fund mandate under the versioned prospectus and applicable rulebook, and where is the result unknown? Institutional buy-side research workflow with auditable evidence, calculations and human review; no autonomous trading.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Sustainable-Investment Mandate Assessment Agent

Use for mandate assessment under a specified investment mandate. Read `AGENTS.md`, then select a route from `agent.json`. Follow `WORKFLOW.md` and the CLI research loop. Copy the entire repository, not just this file: scripts, prompts, schemas and references are required.

A compatible filesystem-enabled agent host may discover this skill; activation has not been certified for specific products. Text-only use applies the methodology manually and does not enforce the Python controls.

This is evidence and arithmetic support, not legal advice, automatic SFDR classification, fund certification or a full EU Taxonomy calculator. Unknown evidence is not a pass. Proposed legislation is not silently applied as an operative requirement.

Do not run a synthetic fixture as live research. Start with `examples/research-request-template.json`, replace every placeholder and register permitted evidence. Inspect `docs/INSTITUTIONAL_QUALITY.md` and `docs/AUDIT.md` before relying on outputs.
