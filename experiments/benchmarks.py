import logging
import os
from pathlib import Path
import sys

import tracks

if "IPC_BENCHMARKS" not in os.environ:
    print("Set environment variable IPC_BENCHMARKS to directory containing PDDL benchmarks.")
    sys.exit(1)
BENCHMARK_DIR = Path(os.environ["IPC_BENCHMARKS"])


def get_benchmark_suite(track, test_run):
    # TODO: use correct domains for each track (use full domains normally and only one problem per domain if test_run is true)
    if track == tracks.OPT:
        benchmarks = ["barman-lmg", "miconic-fulladl", "schedule"]
        if test_run:
            benchmarks = [f"{domain}:prob.pddl" for domain in benchmarks]
    elif track == tracks.SAT:
        benchmarks = ["barman-lmg", "miconic-fulladl", "schedule"]
        if test_run:
            benchmarks = [f"{domain}:prob.pddl" for domain in benchmarks]
    elif track == tracks.AGL:
        benchmarks = ["barman-lmg", "miconic-fulladl", "schedule"]
        if test_run:
            benchmarks = [f"{domain}:prob.pddl" for domain in benchmarks]
    else:
        logging.critical(f"Unknown track {track}")
    
    return BENCHMARK_DIR, benchmarks


BEST_KNOWN_BOUNDS = {
    "barman-lmg": {
        "prob.pddl": (59, 59),
    },
    "miconic-fulladl": {
        "prob.pddl": (8,8),
    },
    "schedule": {
        "prob.pddl": (2,2),
    },
}

def get_best_bounds(domain, problem):
    return BEST_KNOWN_BOUNDS.get(domain, {}).get(problem, (0, float("inf")))
