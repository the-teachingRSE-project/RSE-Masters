import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

base_dir = Path("../components").resolve()
output_dir = Path("generated")
output_dir.mkdir(exist_ok=True)
template_dir = Path("templates")

env = Environment(loader=FileSystemLoader(template_dir))
module_template = env.get_template("module.qmd.j2")


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def read_file(path):
    return path.read_text() if path.exists() else ""


def process_component(comp_dir):
    try:
        description = read_file(comp_dir / "description.qmd")
        meta = load_yaml(comp_dir / "meta.yml")["meta"]
        wildcard = meta.get("wildcard", False)
        lectures = load_yaml(comp_dir / "lectures.yml")["entries"]

        for lecture in lectures:
            filename = lecture.get("quarto_filename")
            lecture["content"] = read_file(comp_dir / filename) if filename else ""

        sources, competences = {}, {}
        if not wildcard:
            sources = load_yaml(comp_dir / "sources.yml")["sources"]
            competences = load_yaml(comp_dir / "competences.yml")

        rendered = module_template.render(
            description=description,
            lectures=lectures,
            **sources,
            **competences
        ) if not wildcard else module_template.render(
            description=description,
            lectures=lectures,
        )

        module_output_path = output_dir / f"{comp_dir.name}.qmd"
        module_output_path.write_text(rendered)
        print(f"Generated module: {module_output_path.name}")

        module_summary = {
            "name": meta.get("name", comp_dir.name),
            "content": rendered,
            "file": f"{comp_dir.name}.qmd",
            "competences": competences.get("competences", []),
        }

        module_data = {"meta": meta,
                       "lectures": lectures,
                       "competences": competences,
                       "sources": sources}
        dependencies = {meta["id"]: module_data}

        return module_summary, dependencies

    except Exception as e:
        print(f"Skipped {comp_dir.name}: {e}")
        return None, None


def process_components():
    module_summaries = []
    dependencies = {}
    for comp_dir in base_dir.iterdir():
        if comp_dir.is_dir():
            summary, mod_dependency = process_component(comp_dir)
            if summary:
                module_summaries.append(summary)
                dependencies.update(mod_dependency)
    return module_summaries, dependencies
