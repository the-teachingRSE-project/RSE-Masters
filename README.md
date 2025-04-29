# RSE-Masters


## How to Contribute a Component/Module

- go to components 
- examine files in gen_programming 
- copy cat the structure

## Folder Descriptions

- general: contains texts that do not apply to target groups or disciplinary focus
- generation: scripts for combination and generation of quarto project
- root_dir: contains the basic quarto structure files, as well as design elements for html/latex rendering
- components: contains detailed texts and the datastructure for the different templates, here you can add new didactical ideas in a structurered format
- external/bibliography is a submodule for the common literature from deRSE


## How To Run

- cd generation # go in generation dir
- python generate_all.py # run the templating logic
- cd .. # go back in root dir
- Windows PS:
  - quarto render --profile doc; quarto preview --profile website
- Linux/ Windows CMD:
  - quarto render --profile doc && quarto preview --profile website

