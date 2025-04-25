import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from solver import create_curriculum_solver

output_dir = Path("generated")
template_dir = Path("templates")

env = Environment(loader=FileSystemLoader(template_dir))
curriculum_template = env.get_template("curriculum.qmd.j2")


def generate_curriculum(module_summaries, dependencies):
    distribute_courses(dependencies)
    try:

        with open("data/curriculum.yml") as f:
            curriculum_data = yaml.safe_load(f)

        with open("data/competences.yml") as f:
            competence_data = yaml.safe_load(f)

        curriculum_render = curriculum_template.render(
            **curriculum_data,
            **competence_data,
            modules=module_summaries
        )

        output_path = output_dir / "curriculum.qmd"
        output_path.write_text(curriculum_render)
        print(f"Curriculum generated: {output_path.name}")

    except Exception as e:
        print(f"Failed to generate curriculum.qmd: {e}")



def distribute_courses(dependencies):
    optimal_solution = create_curriculum_solver(dependencies)

    pass