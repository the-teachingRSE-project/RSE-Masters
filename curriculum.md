# RSE- Master curriculum

The target audience for such a master's programme would be students holding a bachelor's degree from
a domain science, which we will call "home domain" in the following. There is explicitly
no restriction on the candidates' home domain: it may be from the \ac{STEM} disciplines, life
sciences, humanities or social sciences. Candidates with a bachelor's degree in computer science are also
explicitly included, although we acknowledge that their master's programme should include adaptations
to make their interaction effective with other domain scientists.
In order to give the future RSE the necessary breadth, we expect this to be a four semester curriculum.

The curriculum is formed from a combination of modules,
some of which are core modules teaching essential skills that must be completed by all students.
Other modules introduce more specialised concepts and skills.
During the master's programme, students should pick an RSE specialisation from the list in this paper
and attend these additional modules to deepen their knowledge in the field.

Core modules are of course drawn from the three pillars of the RSE and can be categorised accordingly.

- Software/Technical skills:
  - Foundational module: Here we have an introduction to programming: Emphasising use cases over programming paradigms, students learn at least two languages: a language that facilitates prototyping and data processing (e.g., \gls{Python} or \gls{R}) and a language for designing complex, performance-critical systems (e.g., \gls{C}/\gls{Cpp}). This exposes them to computers in a hands-on fashion and is the foundation for (\gls{DOCBB}, \gls{DIST}).
  - Computing environment module: Programming languages are not enough to work in a landscape of many interconnected software components; hence we require something like software craftsmanship, where tools such as the Unix shell, version control systems, build systems, documentation generators, package distribution platforms, and software discovery systems are taught to strengthen skills in (\gls{DIST}, \gls{DOCBB}, \gls{SWREPOS}, \gls{SRU}).
  - Software engineering module: Here we develop foundational software engineering competencies (basic knowledge and skill regarding requirements engineering, software architecture and design, implementation, quality assurance, software evolution), again emphasising and strengthening (\gls{DOCBB}, \gls{DIST}) on a more abstract level.

- Research skills:
  - Optional domain mastery module: Additional minor research courses, but students with a home-domain already have the research part well-covered.
  - Research tools module: Here we teach tools used to distribute and publish software, as well as introducing students to domain specific data repositories. Thereby gaining foundational knowledge in (\gls{SRU}, \gls{SP}, \gls{DOMREP}).
  - Meta-research module: Here we teach people how research works. The research life cycle is introduced, as well as the data life cycle and the software life cycle are abstractly introduced.

- Communication skills:
  - Project management methods: Here we teach project management methods that are useful in science, such as agile ones (\gls{PM}).
  - Communication skills module: Here we have courses focusing on interdisciplinary communication, interacting across cultures, communication in hierarchies, supporting end users effectively. These are all facets of the (\gls{USERS}) skill.
  - Teaching module: This module covers topics to effectively design courses and teaching material for the various digital tools, thereby strengthening the (\gls{TEACH}) skill.

Given that RSE work also involves a lot of craftsmanship skills,
hands-on practice is an integral part of the curriculum.
At least two lab projects are required within the mandatory curriculum.
These should be executed as a team and involve a question from a domain science.
We recommend covering both the candidate's home domain and another domain of science.
Ideally, projects stem from collaborations with scientists within the institution and RSE
students take the role of a consultant. This setup strengthens the (\gls{TEAM}, \gls{TEACH}, \gls{USERS}) skill
and most likely also the (\gls{MOD}) skill through interaction.

To emphasise the exposure to domains outside their bachelor's degree domain,
we recommend that RSEs also support their non-home-domain project by supporting it with introductory
courses from this discipline. We support the idea of broadening the interaction with other domains even more.
This schools their ability to quickly adapt their vocabulary and thinking to other disciplines. This is an aspect of (\gls{MOD}).

To align with the specialisations listed in this paper, example optional modules include topics on
\ac{HPC} engineering/parallel programming, numerical mathematics/scientific computing, web technologies,
data stewardship, AI models/statistics, and community management/training.

The programme is finalised with a master's thesis which should be dual-supervised by an
RSE supervisor from an actual project, and a domain supervisor.
The thesis should answer a relevant research question (strengthening (\gls{NEW})) from the domain using computational methods.
Software development is required, and the code is part of the gradable deliverables.
The RSE supervisor ensures and grades the software craftsmanship aspects of the project.
This setup ensures that we are grading the effectiveness of applying RSE skills in an actual research environment.