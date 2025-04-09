import yaml
import jinja2
import os

# Load data
with open("data/curriculum.yml") as f:
    curriculum_data = yaml.safe_load(f)

with open("data/competences.yml") as f:
    competence_data = yaml.safe_load(f)

# Setup Jinja
env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
template = env.get_template("curriculum.qmd.j2")

# Merge data
data = {**curriculum_data, **competence_data}

# Render and write to file
output = template.render(**data)
os.makedirs("generated", exist_ok=True)
with open("generated/curriculum.qmd", "w") as f:
    f.write(output)

print("Curriculum generated at generated/curriculum.qmd")
