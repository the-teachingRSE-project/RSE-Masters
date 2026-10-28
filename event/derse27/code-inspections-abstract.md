# deRSE27 talk abstract

**Title:** Marking What Needs Trust: Decorator-Based Code Inspections for Research Software

**Type:** Talk

**Focus area:** 1 — RSEng in the age of generative and agentic AI

**Authors:** Julian Dehne (lead)

## Abstract

Most of a research code base is plumbing. A few steps decide whether its results can be trusted: a random draw, a call to a language model, a formula taken from a paper, the reading of human-coded data, numerics that depend on the hardware. Reviewers of research software rarely know where these steps are, and the claims about them, such as "the seed is fixed" or "the prompt and model version are recorded", live in docstrings and papers where nothing checks them. With more research code written with the help of generative AI, and with language-model calls inside the pipelines themselves, finding and inspecting these steps becomes a task of its own.

We present `rse_annotations`, an open-source Python package that turns such steps into inspectable units. A researcher marks a function with a decorator such as `@stochastic`, `@model_call` or `@calculations`. Each decorator stands for a concern, a kind of step on which trust depends, and each concern carries an assertion that should hold for every function it marks, for example "this is a pure function whose formula matches the method described in the paper". A static scan parses the code without importing or running it and reports two lists: functions that show the signature of a concern but are not marked, and marked functions the scan cannot confirm. An interactive review then walks a human through every marked function, shows its source and asks whether the assertion holds. The verdicts (accepted, declined, pending) are stored in a file next to the code, so a review can span several sessions and becomes part of the repository's history. The set of concerns is open: a new concern is a new folder with a detection rule and an assertion.

The talk shows the tool on a real research pipeline, a study that codes conference papers with language models, and discusses what the unmarked-but-detected list reveals there. It also reports on its use in teaching: in the Responsible RSE course piloted at the University of Potsdam in the winter term 2026/27, student groups fork the repository and contribute new concerns by pull request. Participants take away a lightweight way to make the trust-relevant parts of their own code visible and reviewable, and an invitation to contribute concerns from their own disciplines.
