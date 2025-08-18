#!/usr/bin/env python3
import argparse

from process_components import process_components
from process_curriculum import generate_curriculum
from solver import create_curriculum_solver
from load_profiles import load_profile

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate the Curriculum files.") # required positional argument
    parser.add_argument("--profile", default="science")
    parser.add_argument("--generate", default="false")
    # optional

    args = parser.parse_args()

    print(f"{args.profile}, {args.generate}!")

    print("collect components")
    module_summaries, dependencies = process_components()
    if args.generate == "true":
        optimal_solution = create_curriculum_solver(dependencies)
    else:
        ## load profiles
        optimal_solution = load_profile(args.profile, dependencies)
    print("generate ")
    generate_curriculum(module_summaries, optimal_solution)
