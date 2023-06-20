
import json
import logging
import os
from pathlib import Path
import sys

import tracks

if "IPC_BENCHMARKS" not in os.environ:
    print("Set environment variable IPC_BENCHMARKS to directory containing PDDL benchmarks.")
    sys.exit(1)
TEST_BENCHMARK_DIR = Path(os.environ["IPC_TEST_BENCHMARKS"])
BENCHMARK_DIR = Path(os.environ["IPC_BENCHMARKS"])


def get_benchmark_suite(track, test_run):
    if test_run:
        benchmark_dir = TEST_BENCHMARK_DIR
        if track == tracks.OPT:
            benchmarks = ["barman-lmg", "miconic-fulladl", "schedule", "rubiks-cube", "recharging-robots", "ricochet-robots", "slitherlink"]
        elif track == tracks.SAT:
            benchmarks = ["barman-lmg", "miconic-fulladl", "schedule", "rubiks-cube", "recharging-robots", "ricochet-robots", "slitherlink"]
        elif track == tracks.AGL:
            benchmarks = ["barman-lmg", "miconic-fulladl", "schedule", "rubiks-cube", "recharging-robots", "ricochet-robots", "slitherlink"]
        else:
            logging.critical(f"Unknown track {track}")
    else:
        if track == tracks.OPT:
            benchmark_dir = BENCHMARK_DIR + "/opt"
            benchmarks = [
                "folding",
                "folding-norm",
                "labyrinth",
                "quantum-layout",
                "recharging-robots",
                "recharging-robots-norm",
                "ricochet-robots",
                "rubiks-cube",
                "rubiks-cube-norm",
                "slitherlink",
                "slitherlink-norm",
            ]
        elif track == tracks.SAT:
            benchmark_dir = BENCHMARK_DIR + "/sat"
            benchmarks = [
                "folding",
                "folding-norm",
                "labyrinth",
                "quantum-layout",
                "recharging-robots",
                "recharging-robots-norm",
                "ricochet-robots",
                "rubiks-cube",
                "rubiks-cube-norm",
                "slitherlink",
                "slitherlink-norm",
            ]
        elif track == tracks.AGL:
            benchmark_dir = BENCHMARK_DIR + "/agl"
            benchmarks = [
                "folding",
                "folding-norm",
                "labyrinth",
                "quantum-layout",
                "recharging-robots",
                "recharging-robots-norm",
                "ricochet-robots",
                "rubiks-cube",
                "rubiks-cube-norm",
                "slitherlink",
                "slitherlink-norm",
            ]
    
    return benchmark_dir, benchmarks


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
    "rubiks-cube": {
        "p01.pddl": (1,1),
        "p02.pddl": (2,2),
        "p03.pddl": (3,3),
        "p10.pddl": (10,10),
    },
    "recharging-robots": {
        "p01.pddl": (13,13),
        "p02.pddl": (13,13),
    },
    "ricochet-robots": {
        "p01.pddl": (12,12),
        "p02.pddl": (17,17),
        "p-20-20.pddl": (20,20),
    },
    "slitherlink": {
        "p01.pddl": (1,16),
        "p02.pddl": (1,24),
    },
}

with open(f"{BENCHMARK_DIR}/bounds.json") as f:
    BEST_KNOWN_BOUNDS.update(json.load(f))

def get_best_bounds(domain, problem, track=None):
    lb, ub = BEST_KNOWN_BOUNDS.get(domain, {}).get(problem, (0, float("inf")))
    if lb == 0 and ub == float("inf"):
        short_track = tracks.TRACK_ABBRV.get(track)
        lb, ub = BEST_KNOWN_BOUNDS.get(f"{short_track}/{domain}/{problem}", (0, float("inf")))
    return lb, ub
        
