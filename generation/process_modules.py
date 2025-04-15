import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Set paths
base_dir = Path("../components").resolve()
template_path = Path("module.qmd.j2")  # path to your Jinja template
output_dir = Path("generated")  # where generated qmds will go
output_dir.mkdir(exist_ok=True)

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader("templates"))
# current dir for template
template = env.get_template(template_path.name)

# Process each component
for comp_dir in base_dir.iterdir():
    if comp_dir.is_dir():
        try:
            # Read intro
            description_path = comp_dir / "description.qmd"
            description = description_path.read_text() if description_path.exists() else ""

            # Read lectures
            lectures_path = comp_dir / "lectures.yml"
            with open(lectures_path, "r") as f:
                lecture_entries = yaml.safe_load(f)["entries"]

            for lecture in lecture_entries:
                filename = lecture.get("quarto_filename")
                if filename:
                    qmd_file = comp_dir / filename
                    if qmd_file.exists():
                        lecture["content"] = qmd_file.read_text()
                    else:
                        lecture["content"] = ""
                else:
                    lecture["content"] = ""

            competences_path = comp_dir / "competences.yml"
            with open(competences_path, "r") as f:
                competence_data = yaml.safe_load(f)

            # Render the template
            rendered = template.render(description=description, lectures=lecture_entries, **competence_data)

            # Write to file
            output_file = output_dir / f"{comp_dir.name}.qmd"
            output_file.write_text(rendered)
            print(f"Generated: {output_file}")
        except Exception as e:
            print(f"Skipped {comp_dir.name} due to error:\n   {e}")

print("finished generating module descriptions")