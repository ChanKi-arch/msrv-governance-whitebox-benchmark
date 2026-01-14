> MSR-V Governance Whitebox Benchmark is a reproducible evaluation suite for measuring how well a white-box reasoning engine can detect legal, logical, and causal failures in LLM-generated text.

Unlike traditional black-box classifiers or RAG-based filters, MSR-V analyzes structural coherence, contradiction, legal impossibility, and causal integrity directly from the input text — without external knowledge retrieval.

This repository provides:

A tiered multilingual test corpus (G01–G25)

Full JSON / JSONL outputs

A deterministic Python benchmark runner

A transparent breakdown of fracture vs alignment detection


It is not a language model.
It is a reasoning governor for auditing LLM outputs.
