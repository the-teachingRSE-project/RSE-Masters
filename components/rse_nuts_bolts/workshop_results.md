

# The Missing Semester - a RSE unicorn


compare with [MIT missing semester](https://missing.csail.mit.edu/)


## General Questions


- Should the RSE-Curriculum be a [recomposition](https://github.com/the-teachingRSE-project/RSE-Masters/wiki/recomposition) of existing courses?
- Should there be an extra/new module in the RSE curriculum like the missing semester?

- Seeing that MIT identified the need for CS/SE - who may not even do that much actual coding and more sw design in their actual work after graduation compared to many RSEs (statistically) - I'd say yes

- The MIT missing semester feels like key competencies in RSE that need to be part of the curriculum for sure (but should not feel like a special "missing semester")

- Offers opportunity as a homogenization module, to get more Bachelor graduates homogenized.
- Can be offered as an open module to other interested faculties as well.

- I think a lot of that material is integral for the RSE Master so it shouldn't be just a minor add-on. There might be a point in offering some pre-course workshops to bring everybody up to speed.

## Module Outline [see description.qmd](https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/components/gen_programming/description.qmd)

What do RSEs need as an applied background in tools and technical skills that is different from other professionals?



## What should the student learn [see comptences.yml](https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/components/gen_programming/competences.yml)

### Canonical Knowledge

- 1 version control (git)
- virtualization concepts
- Data Life Cycle
- Good coding practices
    - Reproducible code
    - Documentation and error messages
    - Testing
    - Modular software
    - Fast running code
    - Easily installable software
    - Standards like formatting, linting, ...

- 1 Data and Software Management plans (rse_management)
- 2 a compiled language (I'd argue for Fortran but C might be more useful)(I'd argue for C... it exposes more of the hardware intricacies)
- Maintenance
    - Git, versions and issues
    - Long term maintenance
    - Sustainable software community building



### General competencies
- Getting funding for software projects (rse_management ?)
- Project Management (rse_management)
    - Name and organise files
    - Collaboration through GitHub/GitLab
    - Being able to figure out what research really want
    - Working in an agile way
    - Build a team/community
    - Manage data
- Being able to publish code and software
    - licensing
    - open source + FAIR
    - Where and how to publish code/software + ways to get (academic) credit
    - Knowing how to archive code

##### clustered
- rse_softwareng
    - Software Discovery [rse_softwareengineering]
    - 2 REST APIs [rse_softwareengineering]
    - 2 generalizing tools & scripts and publish them [rse_software_engineering]
    - compiling complex modular sw (with build tools (make, just, CMake))[rse_softwareengineering]
    - 2 building containers (docker or singularity)[rse_software_engineering]
    - 1 Organize processes [rse_management or rse_softwareengineering]
- gen_datascience
    - 1 storing structured data (netCDF, HDF5, hadoop, zarr, csv) [gen_datascience]
    - 2 databases [gen_datascience]
    - 2 advanced finding of things (regex) [gen_datascience]
    - 1 visualization
- rse_computing
    - 2 HPC middleware (eg slurm) [rse_computing]
    - also hardware, CPUs, accesserators, network, memory [rse_computing]
- programming or SE
    - 1 read and understand error messages [programming or software engineering]
- rse_management
    - 1 Organize processes [rse_management or rse_softwareengineering]


##### unclustered
- 1 literate programming (Quarto, Marimo, Pluto.jl, Jupyter)
- 1 documentation generators (doxygen, sphinx, ...)
- 1 python (visualisation, as glue, web stuff, templating) -> probably that does go in the programming module, but we should discuss this
- 1 bash!
- 2 teach other people version control
- selection techniques when to use which tools
- 2 Automate things and scale up processes
- 2 workflow languages (cwl, nextflow)
- 2 logging and debugging
- 2 package managers and virtual environments (conda, nix, ...)
- 2 Writing (different types of) documentation
- 2 be able to talk about RSE things with non-tech people
- 2 authentication/authorisation (ldap, ACLs, AD)
- 2 know when to switch eg from a Jupyter notebook to script, or python/bash "main script" to workflow tool
    - also when to move from own computer to HPC/cloud
- 2 estimate resource requirements (profiling)
- 2 real collaborative code development and be able to teach to others
- code review, giving feedback
- 2 testing (both how and what)
- 2 mentoring
- 3 web servers
- 3 improving reusability
- file systems (local, network attached)


### Educational (innovative) Concepts

- portfolio learning (i.e. with jupyterbooks)-> might be used, too but the lecture structure is based on the peer teaching idea
- peer teaching -> we decided on this



## How should the lectures be organized? ([see lectures.yml](https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/components/gen_programming/lectures.yml))

- how many lectures?
    - two lectures, one for beginners and one for teaching
- ECTS points
    - how many ECTS per lecture?
      -3-6



## Meta Data ([see meta.yml](https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/components/gen_programming/meta.yml))

- semester? -> 1th and peer-teaching in higher
- dependencies on other modules?
- relevant [profiles](https://github.com/the-teachingRSE-project/RSE-Masters/wiki/profiles)?


## Existing educational sources and syllabi ([see sources.yml](https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/components/gen_programming/sources.yml))

- existing classes?
- concepts
- [Heidi's RSE Miro (ideas for learning objectives etc.)](https://miro.com/welcomeonboard/YVROMkRLekRETitwTmt3TkxMVmV2QXVDUHpOZGc1Z1Y1MDZNQmlQL3dmRE84bEh3OGxKaWFha1NyeXh3QkJjdzgzbS92MzZFYldzaGl4N1J5RUVQU0RjeENIVG5uVnMvcUZmRXRtOUQ3Z1JiMDB1U2ozbm4xUkg5djhmV0pkZXpyVmtkMG5hNDA3dVlncnBvRVB2ZXBnPT0hdjE=?share_link_id=311718450912)
- [CodeRefinery](https://coderefinery.org/lessons/)
- [INTERSECT](https://intersect-training.org/training-material/)
- [Digital Research Academy materials](https://zenodo.org/communities/digiresacademy/records?q=&f=subject%3AResearch%20Software&f=subject%3AGit&f=subject%3AHPC&f=subject%3AReproducibility&l=list&p=1&s=10&sort=newest)
- "building better research software" by SSI: https://carpentries-incubator.github.io/fair-research-software/

# Integration into Curriculum

If you have the time, have a look at the specific [component](https://github.com/the-teachingRSE-project/RSE-Masters/tree/tschira-funding/components/rse_missingsemester) and the [showcase component](https://github.com/the-teachingRSE-project/RSE-Masters/tree/tschira-funding/components/gen_programming)

Technical Pipeline for the curriculum:
https://github.com/user-attachments/files/20673622/presentation.pdf

Existing Module Structure (scroll to bottom):
https://the-teachingrse-project.github.io/RSE-Masters/generation/generated/curriculum.html


