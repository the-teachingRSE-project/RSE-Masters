
Welcome, below is the Agenda for the workshop.

*Some Random Comments*

- The links show the format required to integrate the workshop outcomes in the curriculum later on. It shows the level of detail/abstraction needed.
- If you want to write down arguments/ideas and not module content, use: https://github.com/the-teachingRSE-project/RSE-Masters/discussions/24


Join the mailinglist: https://www.listserv.dfn.de/sympa/info/rse-master

# RSE Computing / HPC Computing

What is the core of RSE performance computing?
What are the requirements to work as a professional RSE in computing?


## General Questions


- Should the RSE-Curriculum be a [recomposition](https://github.com/the-teachingRSE-project/RSE-Masters/wiki/recomposition) of existing courses?
- Should there be an extra/new module in the RSE curriculum like this?
- Where does the Computing Course fit in : https://the-teachingrse-project.github.io/RSE-Masters/generation/generated/curriculum.html
- What is the relationship with the module and profiles/versions of the curriculum (part of STEM profile, part of each profile, new profile), see https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/generation/profiles/science.yml
- What are the requirement competences/BAs/modules?



## Module Outline [see description.qmd](https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/components/gen_programming/description.qmd)

What do RSEs need as an applied background in tools and technical skills that is different from other professionals?




## Existing educational sources and syllabi ([see sources.yml](https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/components/gen_programming/sources.yml))

## Curriculums

- Have a look here for everything: https://de-rse.org/learn-and-teach/learn/
- HPC Masters https://eumaster4hpc.eu/studies/curriculum/


- HPC Carpentry https://www.hpc-carpentry.org/index.html
- Performance:  https://viralinstruction.com/posts/hardware/


## Classes

- paderborn: https://en.cs.uni-paderborn.de/hpc/teaching/courses/ss-2024/introduction-to-high-performance-computing



## What should the student learn [see competences.yml](https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/components/gen_programming/competences.yml)

Subgoal:
Within the Computing module have some HPC topics so they become unknowns of the first kind.

### STEM Profile (no CS background)


#### Technical Informatics
- hardware:
    * CPUs (+AVX)
    * GPUs
    * memory systems
    * network topology
    * typical bottlenecks


#### Math-like
- more advanced numerics (depending on the Bachelor courses)
    * ODEs/PDEs, finite differences (PT: typically taught in "Numerical Mathematics II"/"Numerical Methods for PDEs")


#### Parallel Programming
- parallel programming
    * intro for principles, concepts (shared vs. distributed mem), and common frameworks

#### Basic Programming
- how to debug something(FLO: this is not necessarily HPC specific...., Magi: yeah but parallel programming makes it much more difficult)


#### Basic Math


#### Self Contained and Taught in the Module,
- how to properly benchmark something
- primer/refreshed on approximation theory/ precision!
- common simulation techniques and libraries
    * primer on floating points
    * BLAS/Lapack, IO libs, PETSc/Trilinos/Hypre... (aka. roughly know what is out there to prevent them from writing it themselves)
- accelerator (esp. GPU) programming
    * intro for principles, concepts (e.g. kernels), and common frameworks
- using a cluster
    * basic batch jobs
    * array jobs
    * dependencies
- challenges when using HPC and other computing systems
    * IO
    * threading
    * NUMA
- Maintaining research computing software?
    * continuous benchmarking

- use bash to start jobs on cluster -> this might go to the rse_missingsemester maybe?
    * array jobs
    * dependencies

- programmiersprachenemulation
    * fließkomma-ahlen (mit Relevanz zu Performance)
    * interpretierte vs. kompilierte Sprachen (mit Relevanz zu Performance)



### CS Profile
(not complete yet)

- simulation techniques (and libraries)
- types of problems:
    * (memory parallel) PDEs -> sparse matrices -> distributed mem
    * (compute parallel) Optimisation/ML/spectral methods -> dense matrices -> shared mem
    * (tasks parallel) embarassingly parallel problems -> no worries but you need to keep track of the tasks
- approximation theory (floating point inaccuracy, algorithmic inaccuracy, approximate solutions)
- Maybe! (depending on bachelor modules) basic primer on simulation hardware/architecture: GPU, AVX, etc. -> Goal: Awareness, name dropping to know what to search for if needed in the future

-> plug in the paderborn [HPC course](https://en.cs.uni-paderborn.de/hpc/teaching/courses/ss-2024/introduction-to-high-performance-computing) here?


## How should the lectures be organize? ([see lectures.yml](https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/components/gen_programming/lectures.yml))

- how many lectures?
- ECTS points


## Meta Data ([see meta.yml](https://github.com/the-teachingRSE-project/RSE-Masters/blob/tschira-funding/components/gen_programming/meta.yml))

- semester?
- dependencies on other modules?
- relevant [profiles](https://github.com/the-teachingRSE-project/RSE-Masters/wiki/profiles)?


## Job Roles

see https://github.com/the-teachingRSE-project/RSE-Masters/blob/main/general/job_roles.qmd



# Integration into Curriculum

If you have the time, have a look at the specific [component](https://github.com/the-teachingRSE-project/RSE-Masters/tree/tschira-funding/components/rse_computing) and the [showcase component](https://github.com/the-teachingRSE-project/RSE-Masters/tree/tschira-funding/components/gen_programming)

# Related Project

- 6 page paper on Competences and Curriculum for RSE with focus on MINT: https://github.com/the-teachingRSE-project/RSECurriculum4NaturalScience
