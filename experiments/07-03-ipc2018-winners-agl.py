#!/usr/bin/env python3

from lab.environments import BaselSlurmEnvironment, LocalEnvironment

import benchmarks
import experiment
import planners
import report
import tracks

TRACK = tracks.AGL
TIME_LIMIT = 300 #s
MEMORY_LIMIT = 8192 #MB
NUM_RESERVED_CORES = 3

if experiment.running_on_cluster():
    TESTRUN = False
    ENVIRONMENT = BaselSlurmEnvironment(
        partition="infai_3",
        email="florian.pommerening@unibas.ch",
        memory_per_cpu=f"{int(NUM_RESERVED_CORES*3.5*1024)}M",  # We reserve enough memory such that each task blocks 10 nodes (actual memory limit is set internally)
        export=["PATH"],
    )
else:
    TESTRUN = True
    ENVIRONMENT = LocalEnvironment(processes=2)

PLANNERS = [p for p in planners.get_participating(TRACK) if p.name.startswith("ipc2018_")]

exp = experiment.IPCExperiment(track=TRACK, time_limit=TIME_LIMIT, memory_limit=MEMORY_LIMIT, environment=ENVIRONMENT)
exp.add_planners(PLANNERS)
exp.add_suite(*benchmarks.get_benchmark_suite(TRACK, TESTRUN))

exp.add_report(report.IPCReport(attributes=report.IPCReport.DEFAULT_ATTRIBUTES), outfile=f"{exp.name}.html")
for planner in PLANNERS:
    exp.add_report(report.IPCReport(attributes=report.IPCReport.DEFAULT_ATTRIBUTES, filter_algorithm=planner.shortname), outfile=f"{planner.shortname}.html")
exp.add_parse_again_step()
exp.run_steps()
