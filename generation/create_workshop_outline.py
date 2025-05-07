import os
import glob
from jinja2 import Template

# Define paths
components_dir = "../components"
output_file = "generated/compiled_rse_invitation.qmd"

# Collect all matching description files from rse_* folders
description_files = sorted(glob.glob(os.path.join(components_dir, "rse_*/description.qmd")))

# Read in descriptions
descriptions = []
for file in description_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        dirname = os.path.basename(os.path.dirname(file))
        descriptions.append({"name": dirname.replace("rse_", "").replace("_", " ").title(), "content": content})

# Template for the full document
template_str = """
---
title: "Contribute to the RSE Master's Curriculum"
format:
  pdf:
    bibliography:
      - ../../external/bibliography/bibliography.bib
      - ../../references.bib
---

# Invitation to the RSE Community-Master Development

We invite all members of the **Research Software Engineering (RSE)** community and interested scientists and educators to join us in developing a Master's curriculum tailored to the unique needs, interests, and challenges of RSE.  
Each module represents a specific area of the RSE landscape and will be shaped by community-driven short online workshops (2–3 hours each).

The main idea is to supplement general courses on software engineering, data science and advanced science classes with RSE-specific courses tailored to the growing field of software engineering in research.
These example modules will be new in structure and content and provide universities a suggestion how to hire and support the growing need for RSE competencies. These courses will be optional in the sense that alternatives or similar
existing classes will be suggested if a spezialized lecturer is not available.

In these workshops, we collaboratively define:

- Relevant competences
- Suggested course structures
- RSE-specific perspectives

These efforts will feed directly into the development of a comprehensive and inclusive RSE Master's curriculum.  
You can explore the broader project here: [RSE Masters Curriculum GitHub Repository](https://github.com/the-teachingRSE-project/RSE-Masters/tree/tschira-funding)



# RSE Workshops

The following topics will be dealt with in seperate workshops. These are compiled from the current module descriptions.

{% for d in descriptions %}
- {{ d.name }}
{% endfor %}

Ideas and possible contents of these workshops are listed in more detail below:

{% for d in descriptions %}

{{ d.content }}

{% endfor %}

# Join Us!

To get involved, please reach out via the repository or contact the organizing team directly at julian.dehne@gi.de.

{% raw %}

# References

::: {#refs}
:::

{% endraw %}

"""

# Render template
template = Template(template_str)
rendered = template.render(descriptions=descriptions)

# Write output
with open(output_file, "w", encoding="utf-8") as f:
    f.write(rendered)

print(f"Compiled Quarto document written to {output_file}")
