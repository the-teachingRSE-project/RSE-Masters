# RSE-Masters (Technical Prototype and Current State)

We just started the community process. Even though we organized a technical pipeline and some modularization, we have not progressed to the point where you should place to much weight on the current state of the prototype in terms of content. 

Active work is going on in the tschira-funding branch. 

The current version of the generated curriculum can be found [here](https://the-teachingrse-project.github.io/RSE-Masters/). This is build with Github Actions.

## How to Contribute a Component/Module

- go to components 
- examine files in gen_programming 
- copy cat the structure

## Folder Descriptions

- general: contains texts that do not apply to target groups or disciplinary focus
- generation: scripts for combination and generation of quarto project
- root_dir: contains the basic quarto structure files, as well as design elements for html/latex rendering
- components: contains detailed texts and the datastructures for the different templates, here you can add new didactic ideas in a structured format
- external/bibliography is a submodule for the common literature from deRSE


## How To Run

- cd generation # go in generation dir
- install python requirements from requirement.txt
- python generate_all.py # run the templating logic
- cd .. # go back in root dir
- Windows PS:
  - quarto render --profile doc; quarto preview --profile website
- Linux/ Windows CMD:
  - quarto render --profile doc && quarto preview --profile website
