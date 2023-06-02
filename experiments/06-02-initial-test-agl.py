#!/usr/bin/env python3

from lab.environments import BaselSlurmEnvironment, LocalEnvironment

import benchmarks
import experiment
import planners
import report
import tracks

TRACK = tracks.AGL
TIME_LIMIT = 1800 #s
MEMORY_LIMIT = 3584 #MB

if experiment.running_on_cluster():
    TESTRUN = False
    ENVIRONMENT = BaselSlurmEnvironment(
        partition="infai_3",
        email="florian.pommerening@unibas.ch",
        memory_per_cpu="3872M",
        export=["PATH"],
    )
else:
    TESTRUN = True
    ENVIRONMENT = LocalEnvironment(processes=2)

exp = experiment.IPCExperiment(track=TRACK, time_limit=TIME_LIMIT, memory_limit=MEMORY_LIMIT, environment=ENVIRONMENT)
exp.add_planners(planners.get_participating(TRACK))
exp.add_suite(*benchmarks.get_benchmark_suite(TRACK, TESTRUN))

exp.add_report(report.IPCReport(attributes=report.IPCReport.DEFAULT_ATTRIBUTES), outfile=f"{exp.name}.html")
exp.add_parse_again_step()
exp.run_steps()
