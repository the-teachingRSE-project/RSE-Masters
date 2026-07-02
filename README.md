# RSE-Masters (Technical Prototype and Current State)

We started the community process to develop an RSE curriculum in spring 2025. Even though we organized a technical pipeline and some modularization, we have not progressed to the point where you should place too much weight on the current state of the prototype in terms of content. 

If you want to be part of the community, join our mailinglist [https://www.listserv.dfn.de/sympa/info/rse-master](https://www.listserv.dfn.de/sympa/info/rse-master).

The current version of the generated curriculum can be found [here](https://the-teachingrse-project.github.io/RSE-Masters/). This is built with Github Actions.


## How to Contribute to the Publication

You can edit the texts that are going to be the foundation of the publication. You can contribute text to the [static markdown files](https://github.com/the-teachingRSE-project/RSE-Masters/tree/main/general):

- [ideas and principles](https://github.com/the-teachingRSE-project/RSE-Masters/blob/main/general/ideas.qmd)
- [job roles](https://github.com/the-teachingRSE-project/RSE-Masters/blob/main/general/job_roles.qmd)
- [preambel and general introductions](https://github.com/the-teachingRSE-project/RSE-Masters/blob/main/general/preambel_general.qmd)


## How to Contribute to a Component/Module
In parallel to the main publication, small teams are working on particular components. These are the people leading the elaboration of the respective modules so far:
- Scientific (High Performance) Computing: [@jpthiele](https://github.com/jpthiele)
- Advanced Software Engineering for RSE: [@juliandehne](https://github.com/juliandehne)
- RSE Nuts and Bolts (Tooling): [@captainsifff](https://github.com/CaptainSifff)
- RSE Management (and Communication): [@majatoebs](https://github.com/MajaToebs)
- RSE & Society: hopefully, students of the Digital Changemaker Initiative by the Hochschulforum Digitalisierung
- RSE Philosophy: ?
- RSE Thesis: ?

If you are interested in joining any of the teams, we will be happy to hear from you!


## How to Contribute a whole Component/Module

- go to [modules](https://github.com/the-teachingRSE-project/RSE-Masters/tree/main/modules)
- examine `modules/gen_programming.qmd`
- copy cat the structure into a new `modules/<component>.qmd` and add it to the relevant curriculum page(s)

## How to Contribute a new Profile / University Adaptation

- add the modules for your university under [modules](https://github.com/the-teachingRSE-project/RSE-Masters/tree/main/modules)
- create a new `curricula/<profile_name>.qmd` (copy an existing one, e.g. `curricula/cs.qmd`): a linked module list, the suggested study-plan table, and the PDF-only `{{< include >}}` block
- add the profile to `_quarto-website.yml` as a new navbar tab

## Folder Descriptions

### Curriculum Content

- general: contains texts that do not apply to target groups or disciplinary focus
- modules: one self-contained `.qmd` per module (description, sources & implementations, references) — the module pages of the site
- curricula: one `.qmd` per profile/track (cs, mnt, up); links its modules, shows the study plan, and includes the module pages for the PDF build
- root_dir: contains the basic quarto structure files, as well as design elements for html/latex rendering
- components: supplementary material referenced by modules (e.g. OER pages, slides, piloting artefacts)

### Organisational Folders

- event contains the input for the community events etc.
- presentation contains a presentation of the existing concept
- thesis contains ideas for ba/ma theses situated in the project


### Submodules

- ds_thesis submodule is optional. If you don't have access, you can skip initializing it and still work with the main repo.
- external/bibliography is a submodule for the common literature from deRSE
  initialize with `git submodule init external/bibliography`


## How To Run

This is a plain static Quarto project — no code generation step is needed. Just render/preview:

- Windows PS:
  - `quarto render --profile doc; quarto preview --profile website`
- Linux/ Windows CMD:
  - `quarto render --profile doc && quarto preview --profile website`
