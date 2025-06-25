# Proposal 1: Data-Driven RSE Curriculum Development Using Data Mining and Topic Modelling


## Objectives

- Collect and preprocess a dataset of existing [RSE syllabi](https://de-rse.org/learn-and-teach/learn/#curricula-on-scientific-computing), computing curriculas [@CC2020;@DSBOK2017;@SWEBOK2014] and related documents.
- Apply data mining and natural language processing (NLP) methods to extract topics and competencies.
- Use topic modelling (e.g., LDA, BERTopic) to identify latent themes relevant to RSE education.
- Map these findings onto an evolving modular curriculum framework.

## Research Questions

- What are the dominant topics in existing RSE-related materials?
- How can topic modelling inform the structure and sequencing of curriculum components?
- What gaps exist between current RSE education and industry demands?

## Methodology

- Use data science tools (e.g., `scikit-learn`, `spaCy`, `BERTopic`) for preprocessing and analysis
- Leverage clustering and dimensionality reduction for curriculum mapping
- Compare generated topic models to existing competence frameworks (e.g., ACM, EOSC)

## Expected Outcomes

- A corpus of annotated RSE-related materials
- A topic map visualizing core and peripheral RSE themes
- A mapping of RSE-modules to respective topics/mater


# Further Ideas

- map Andreas Schwill "Fundamentale Ideen der Informatik" as cluster groups vs RSE Curriculum space -> How much CS is in these curriculums?
- map RSE publications, for example Github  [name-Space](https://github.com/the-teachingRSE-project) 

# Starting Points

## background knowledge / needed skills

- NLP basics
- dimensionality reduction/clustering -> can be acquired
- attention models / LLM -> can be acquired if some knowledge exists


## setup session

- github separate repository (->submodule))
- zotero Gruppenbibliothek
- Literaturrecherche -> existierende Mapping von Informatik-Studiengängen etc.
  - google scholar
  - web of science
  - pädagogische Literatur -> Kompetenzstufen, Grammatik von Kompetenzformulierungen
  - ev. dropbox link
  - ieee/acm digitallibrary
  - keywords, strategies
  - where to get licensed literature
  - ...
- Review Methodology (PRISMA) (eigentlich für Literaturreview -> anpassen auf Curricula)
- Datenschema -> compare with RSE Master project, 
- storage -> db-tool? yaml-storage? CSV? full-DB?
- NLP
  - https://third-bit.com/py-rse/
  - test some models
  - finetuning?
  - google collab?
- 

## first steps

- data acquisition
  - look for official downloads
  - ask the universities for an export file
  - last option: webcrawler

- data cleaning
  - filter the data that only metadata and competences are in the dataset
  - try to map to a data schema such as:
    - module name
    - module content description
    - competence description
    - context (university name etc.)
- use topic modelling or other techniques to analyze the data
  - visualizing core and peripheral RSE themes
- (optional) curriculum engineering (maybe together with Julian): generate modules for the RSE curriculum 



