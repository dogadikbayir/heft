from heft import heft, gantt
from collections import deque, namedtuple
import numpy as np
import sys
import os
import os.path
from os import path

'''
{0: [ScheduleEvent(task=3, start=18.0, end=31.0, proc=0), ScheduleEvent(task=2, start=31.0, end=42.0, proc=0)], 1: [ScheduleEvent(task=4, start=20.0, end=33.0, proc=1), ScheduleEvent(task=8, start=54.0, end=66.0, proc=1), ScheduleEvent(task=9, start=67.0, end=74.0, proc=1)], 2: [ScheduleEvent(task=0, start=0, end=9.0, proc=2), ScheduleEvent(task=1, start=9.0, end=27.0, proc=2), ScheduleEvent(task=5, start=27.0, end=36.0, proc=2)]}

Schedule:
Processor 0:
{Start: 18.000000/End: 31.000000/TaskProc: 0/TaskID: 3}, {Start: 31.000000/End: 42.000000/TaskProc: 0/TaskID: 2}, {Start: 42.000000/End: 49.000000/TaskProc: 0/TaskID: 6}, {Start: 51.000000/End: 56.000000/TaskProc: 0/TaskID: 7},
Processor 1:
{Start: 20.000000/End: 33.000000/TaskProc: 1/TaskID: 4}, {Start: 54.000000/End: 66.000000/TaskProc: 1/TaskID: 8}, {Start: 67.000000/End: 74.000000/TaskProc: 1/TaskID: 9},
Processor 2:
{Start: 0.000000/End: 9.000000/TaskProc: 2/TaskID: 0}, {Start: 9.000000/End: 27.000000/TaskProc: 2/TaskID: 1}, {Start: 27.000000/End: 36.000000/TaskProc: 2/TaskID: 5},

'''
if len(sys.argv) == 1:
	print("Please provide a data path to compute schedule lengths")
	sys.exit()

data_path = sys.argv[1] # get the data path

if path.exists(data_path):
	os.chdir(data_path)
	file_names = [name for name in os.listdir(".") if os.path.isdir(name)]
	for fn in file_names:
		cm_path = fn + "/task_exe_time.csv"
		#print(cm_path)
		comp_matrix = heft.readCsvToNumpyMatrix(cm_path)
		#print(comp_matrix)
		cmm_path = fn + "/resource_BW.csv"
		comm_matrix = heft.readCsvToNumpyMatrix(cmm_path)
		dag_path = fn + "/task_connectivity.csv"
		dag = heft.readDagMatrix(dag_path)
		sched, _,_,_ = heft.schedule_dag(dag,communication_matrix=comm_matrix, computation_matrix=comp_matrix)

		print("Finish time for " + fn + ": " + str(sched))

	print("Finished computing FTs for the experiments")

else:
	print("Please try again with a valid path...")

