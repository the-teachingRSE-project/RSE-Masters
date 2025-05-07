from process_components import process_components
from process_curriculum import generate_curriculum
from solver import create_curriculum_solver

if __name__ == "__main__":
    module_summaries, dependencies = process_components()
    optimal_solution = create_curriculum_solver(dependencies)
    print("generate ")
    generate_curriculum(module_summaries, optimal_solution)
