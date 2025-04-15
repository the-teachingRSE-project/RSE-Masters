import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Setup paths
base_dir = Path("../components").resolve()
output_dir = Path("generated")
output_dir.mkdir(exist_ok=True)
template_dir = Path("templates")

# Jinja setup
env = Environment(loader=FileSystemLoader(template_dir))
module_template = env.get_template("module.qmd.j2")
curriculum_template = env.get_template("curriculum.qmd.j2")

# 1. Process modules
module_summaries = []
for comp_dir in base_dir.iterdir():
    if comp_dir.is_dir():
        try:
            description_path = comp_dir / "description.qmd"
            description = description_path.read_text() if description_path.exists() else ""

            lectures_path = comp_dir / "lectures.yml"
            with open(lectures_path, "r") as f:
                lecture_entries = yaml.safe_load(f)["entries"]

            for lecture in lecture_entries:
                filename = lecture.get("quarto_filename")
                if filename:
                    qmd_file = comp_dir / filename
                    lecture["content"] = qmd_file.read_text() if qmd_file.exists() else ""
                else:
                    lecture["content"] = ""

            competences_path = comp_dir / "competences.yml"
            with open(competences_path, "r") as f:
                competence_data = yaml.safe_load(f)

            # Render module template
            rendered_module = module_template.render(
                description=description,
                lectures=lecture_entries,
                **competence_data
            )

            module_output_path = output_dir / f"{comp_dir.name}.qmd"
            module_output_path.write_text(rendered_module)
            print(f"Generated module: {module_output_path.name}")

            # Store full module content for inclusion in curriculum
            module_summaries.append({
                "name": comp_dir.name,
                "content": rendered_module,
                "file": f"{comp_dir.name}.qmd",
                "competences": competence_data.get("competences", []),
            })

        except Exception as e:
                    print(f"Skipped {comp_dir.name}: {e}")

# 2. Generate curriculum.qmd
try:
    with open("data/curriculum.yml") as f:
        curriculum_data = yaml.safe_load(f)

    with open("data/competences.yml") as f:
        competence_data = yaml.safe_load(f)

    # Merge data
    curriculum_render = curriculum_template.render(
        **curriculum_data,
        **competence_data,
        modules=module_summaries  # optional for future TODO section
    )

    curriculum_output_path = output_dir / "curriculum.qmd"
    curriculum_output_path.write_text(curriculum_render)
    print(f"Curriculum generated: {curriculum_output_path.name}")

except Exception as e:
    print(f"Failed to generate curriculum.qmd: {e}")
