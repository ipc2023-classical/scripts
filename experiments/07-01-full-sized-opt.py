#!/usr/bin/env python3

from lab.environments import BaselSlurmEnvironment, LocalEnvironment

import benchmarks
import experiment
import planners
import report
import tracks

TRACK = tracks.OPT
TIME_LIMIT = 1800 #s
MEMORY_LIMIT = 8192 #MB
NUM_RESERVED_CORES = 10

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

exp = experiment.IPCExperiment(track=TRACK, time_limit=TIME_LIMIT, memory_limit=MEMORY_LIMIT, environment=ENVIRONMENT)
exp.add_planners(planners.get_participating(TRACK))
exp.add_suite(*benchmarks.get_benchmark_suite(TRACK, TESTRUN))

exp.add_report(report.IPCReport(attributes=report.IPCReport.DEFAULT_ATTRIBUTES), outfile=f"{exp.name}.html")
for planner in planners.get_participating(TRACK):
    exp.add_report(report.IPCReport(attributes=report.IPCReport.DEFAULT_ATTRIBUTES, filter_algorithm=planner.shortname), outfile=f"{planner.shortname}.html")
exp.add_parse_again_step()
exp.run_steps()
