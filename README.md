# RSE-Masters (Technical Prototype and Current State)

We just started the community process. Even though we organized a technical pipeline and some modularization, we have not progressed to the point where you should place to much weight on the current state of the prototype in terms of content. 

If you want to be part of the community, join our mailinglist [https://www.listserv.dfn.de/sympa/info/rse-master](https://www.listserv.dfn.de/sympa/info/rse-master)

Active work is going on in the tschira-funding branch. 

The current version of the generated curriculum can be found [here](https://the-teachingrse-project.github.io/RSE-Masters/). This is build with Github Actions.

## How to Contribute to the Publication

You can edit the texts that are going to be the foundation of the publication. You can contribute text to the [static markdown files](https://github.com/the-teachingRSE-project/RSE-Masters/tree/main/general):

- [ideas and principles](https://github.com/the-teachingRSE-project/RSE-Masters/blob/main/general/ideas.qmd)
- [job roles](https://github.com/the-teachingRSE-project/RSE-Masters/blob/main/general/job_roles.qmd)
- [preambel and general introductions](https://github.com/the-teachingRSE-project/RSE-Masters/blob/main/general/preambel_general.qmd)
- 



## How to Contribute a Component/Module

- go to [components](https://github.com/the-teachingRSE-project/RSE-Masters/tree/main/components) 
- examine files in gen_programming 
- copy cat the structure

## Folder Descriptions

### Curriculum Content

- general: contains texts that do not apply to target groups or disciplinary focus
- generation: scripts for combination and generation of quarto project
- root_dir: contains the basic quarto structure files, as well as design elements for html/latex rendering
- components: contains detailed texts and the datastructures for the different templates, here you can add new didactic ideas in a structured format

### Organisational Folders

- event contains the input for the community events etc.
- presentation contains the presentation of the existing concepts
- thesis contains ideas for ba/ma thesis situated in the project


### Submodules

- ds_thesis submodule is optional. If you don't have access, you can skip initializing it and still work with the main repo.
- external/bibliography is a submodule for the common literature from deRSE


## How To Run

- install submodules: git submodule update --init --remote --recursive
- cd generation # go in generation dir
- install python requirements from requirement.txt
- python generate_all.py # run the templating logic
- cd .. # go back in root dir
- Windows PS:
  - quarto render --profile doc; quarto preview --profile website
- Linux/ Windows CMD:
  - quarto render --profile doc && quarto preview --profile website
