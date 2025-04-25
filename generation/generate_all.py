from process_components import process_components
from process_curriculum import generate_curriculum

if __name__ == "__main__":
    module_summaries, dependencies = process_components()
    generate_curriculum(module_summaries, dependencies)
