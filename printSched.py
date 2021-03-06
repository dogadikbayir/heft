from heft import heft, gantt
from collections import deque, namedtuple
import numpy as np
import os
import math
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
os.chdir("/mnt/home/dikbayir/CSE845/dev/heft/1000nodes_high_CCR/data")
file_names = [name for name in os.listdir(".") if os.path.isdir(name)]

# get the schedule lengths
sch_ls = {}
mappings = {}
for fn in file_names:
	os.chdir(fn)
	ScheduleEvent = namedtuple('ScheduleEvent', 'task start end proc')
	comp_matrix_1 = heft.readCsvToNumpyMatrix('task_exe_time.csv')
	comm_matrix_1 = heft.readCsvToNumpyMatrix('resource_BW.csv')
	dag1 = heft.readDagMatrix('task_connectivity.csv')


	params = fn.split("_")
	proc = params[1]
	depth = params[2]
	
	unq_tag = params[0] +  "_" + depth
	if unq_tag not in sch_ls:
		sch_ls[unq_tag] = [0] * 5
		mappings[unq_tag] = [0] * 5
	sched1, proc_sch, _, _ = heft.schedule_dag(dag1, 
                                communication_matrix=comm_matrix_1, 
                                computation_matrix=comp_matrix_1)
	
	#Get the processor mapping for initial pop
	mapping = [0] * 1000 
	#print(proc_sch)
	for pr, tasks in proc_sch.items():
		for sch in tasks:
			mapping[sch.task] = pr
	(mappings[unq_tag])[int(math.log2(int(proc))) - 1] = mapping 	
	(sch_ls[unq_tag])[int(math.log2(int(proc))) - 1] = sched1
	os.chdir("..")

for key, value in mappings.items():
	print("Graph: ",key, ":")
	print("\n")
	for p in value:
		#print("\t 2: ")
		print(p)  
sched2 = {0: [ScheduleEvent(task=2, start=8.195663,end=18.339127,proc=0), ScheduleEvent(task=41, start=18.339127,end=28.266556,proc=0), ScheduleEvent(task=77, start=28.266556,end=32.289907,proc=0), ScheduleEvent(task=45, start=32.289907,end=41.129029,proc=0), ScheduleEvent(task=55, start=41.129029,end=47.850615,proc=0), ScheduleEvent(task=80, start=47.850615,end=56.204986,proc=0), ScheduleEvent(task=4, start=56.204986,end=62.434107,proc=0), ScheduleEvent(task=66, start=62.434107,end=66.521128,proc=0), ScheduleEvent(task=10, start=66.521128,end=73.070098,proc=0), ScheduleEvent(task=25, start=73.070098,end=82.766764,proc=0), ScheduleEvent(task=59, start=82.766764,end=88.788983,proc=0), ScheduleEvent(task=15, start=88.788983,end=98.367312,proc=0), ScheduleEvent(task=38, start=98.367312,end=105.273486,proc=0), ScheduleEvent(task=32, start=105.273486,end=111.079116,proc=0), ScheduleEvent(task=20, start=111.079116,end=114.487236,proc=0), ScheduleEvent(task=46, start=114.487236,end=124.540610,proc=0), ScheduleEvent(task=54, start=124.540610,end=129.374874,proc=0), ScheduleEvent(task=53, start=129.374874,end=135.948732,proc=0), ScheduleEvent(task=78, start=135.948732,end=139.727072,proc=0), ScheduleEvent(task=51, start=139.727072,end=142.646535,proc=0), ScheduleEvent(task=71, start=142.646535,end=146.230241,proc=0), ScheduleEvent(task=64, start=146.230241,end=151.134625,proc=0), ScheduleEvent(task=76, start=151.134625,end=156.190371,proc=0), ScheduleEvent(task=37, start=156.190371,end=158.244658,proc=0), ScheduleEvent(task=34, start=158.244658,end=168.795571,proc=0), ScheduleEvent(task=70, start=168.795571,end=175.593494,proc=0), ScheduleEvent(task=85, start=175.593494,end=181.358331,proc=0), ScheduleEvent(task=109, start=181.358331,end=185.891673,proc=0), ScheduleEvent(task=75, start=185.891673,end=188.420961,proc=0), ScheduleEvent(task=94, start=188.420961,end=192.482298,proc=0), ScheduleEvent(task=12, start=192.482298,end=195.561989,proc=0), ScheduleEvent(task=116, start=195.561989,end=200.325021,proc=0), ScheduleEvent(task=21, start=200.325021,end=209.642381,proc=0), ScheduleEvent(task=108, start=209.642381,end=214.594115,proc=0), ScheduleEvent(task=103, start=214.594115,end=220.513271,proc=0), ScheduleEvent(task=82, start=220.513271,end=228.137486,proc=0), ScheduleEvent(task=61, start=228.137486,end=232.272585,proc=0), ScheduleEvent(task=117, start=232.272585,end=238.299361,proc=0), ScheduleEvent(task=97, start=238.299361,end=243.755387,proc=0), ScheduleEvent(task=111, start=243.755387,end=246.291494,proc=0), ScheduleEvent(task=98, start=246.291494,end=251.743603,proc=0), ScheduleEvent(task=119, start=251.743603,end=254.921308,proc=0), ScheduleEvent(task=112, start=254.921308,end=258.538852,proc=0), ScheduleEvent(task=113, start=258.538852,end=261.029026,proc=0), ScheduleEvent(task=88, start=261.029026,end=262.958152,proc=0), ScheduleEvent(task=130, start=262.958152,end=268.883515,proc=0), ScheduleEvent(task=81, start=268.883515,end=271.162101,proc=0), ScheduleEvent(task=104, start=271.162101,end=275.374019,proc=0), ScheduleEvent(task=126, start=275.374019,end=278.204117,proc=0), ScheduleEvent(task=147, start=278.204117,end=282.983493,proc=0), ScheduleEvent(task=140, start=282.983493,end=287.544635,proc=0), ScheduleEvent(task=89, start=287.544635,end=290.641171,proc=0), ScheduleEvent(task=136, start=290.641171,end=292.507240,proc=0), ScheduleEvent(task=149, start=293.059799,end=296.832581,proc=0)], 1: [ScheduleEvent(task=23, start=6.987255,end=11.077534,proc=1), ScheduleEvent(task=33, start=11.077534,end=20.107973,proc=1), ScheduleEvent(task=29, start=20.107973,end=23.729850,proc=1), ScheduleEvent(task=58, start=23.729850,end=30.935825,proc=1), ScheduleEvent(task=1, start=30.935825,end=38.262774,proc=1), ScheduleEvent(task=50, start=38.262774,end=45.214603,proc=1), ScheduleEvent(task=13, start=45.214603,end=49.298526,proc=1), ScheduleEvent(task=39, start=49.298526,end=54.972049,proc=1), ScheduleEvent(task=16, start=54.972049,end=60.915771,proc=1), ScheduleEvent(task=22, start=60.915771,end=65.293781,proc=1), ScheduleEvent(task=30, start=65.293781,end=67.118236,proc=1), ScheduleEvent(task=67, start=67.118236,end=72.603849,proc=1), ScheduleEvent(task=24, start=72.603849,end=83.148169,proc=1), ScheduleEvent(task=60, start=83.148169,end=88.057993,proc=1), ScheduleEvent(task=6, start=88.057993,end=90.676895,proc=1), ScheduleEvent(task=44, start=90.676895,end=93.982589,proc=1), ScheduleEvent(task=47, start=93.982589,end=96.132387,proc=1), ScheduleEvent(task=73, start=96.132387,end=99.797610,proc=1), ScheduleEvent(task=14, start=99.797610,end=102.187929,proc=1), ScheduleEvent(task=74, start=102.187929,end=108.141175,proc=1), ScheduleEvent(task=128, start=108.141175,end=114.909762,proc=1), ScheduleEvent(task=42, start=114.909762,end=120.510765,proc=1), ScheduleEvent(task=11, start=120.510765,end=124.765561,proc=1), ScheduleEvent(task=57, start=124.765561,end=127.841283,proc=1), ScheduleEvent(task=49, start=127.841283,end=131.369082,proc=1), ScheduleEvent(task=63, start=131.369082,end=133.462887,proc=1), ScheduleEvent(task=5, start=133.462887,end=137.687737,proc=1), ScheduleEvent(task=106, start=137.687737,end=146.410876,proc=1), ScheduleEvent(task=124, start=146.410876,end=152.249290,proc=1), ScheduleEvent(task=120, start=152.249290,end=156.892680,proc=1), ScheduleEvent(task=115, start=156.892680,end=166.580249,proc=1), ScheduleEvent(task=127, start=166.580249,end=175.004546,proc=1), ScheduleEvent(task=31, start=175.004546,end=175.795341,proc=1), ScheduleEvent(task=83, start=175.795341,end=178.642418,proc=1), ScheduleEvent(task=99, start=178.642418,end=186.894169,proc=1), ScheduleEvent(task=92, start=186.894169,end=189.094227,proc=1), ScheduleEvent(task=114, start=189.094227,end=193.638441,proc=1), ScheduleEvent(task=96, start=196.561989,end=199.167172,proc=1), ScheduleEvent(task=122, start=199.167172,end=202.101768,proc=1), ScheduleEvent(task=86, start=202.101768,end=209.205904,proc=1), ScheduleEvent(task=145, start=216.001522,end=220.509602,proc=1), ScheduleEvent(task=141, start=220.807567,end=222.078451,proc=1), ScheduleEvent(task=132, start=229.081930,end=230.242445,proc=1), ScheduleEvent(task=138, start=238.780842,end=242.439972,proc=1), ScheduleEvent(task=142, start=244.162794,end=246.127286,proc=1), ScheduleEvent(task=139, start=246.680383,end=254.508507,proc=1), ScheduleEvent(task=134, start=255.569456,end=259.615308,proc=1), ScheduleEvent(task=135, start=259.615308,end=262.300707,proc=1), ScheduleEvent(task=144, start=262.300707,end=264.504545,proc=1)], 2: [ScheduleEvent(task=0, start=0.000000,end=6.580279,proc=2), ScheduleEvent(task=69, start=6.580279,end=11.312264,proc=2), ScheduleEvent(task=26, start=11.312264,end=18.134406,proc=2), ScheduleEvent(task=62, start=18.134406,end=23.919918,proc=2), ScheduleEvent(task=18, start=23.919918,end=26.848848,proc=2), ScheduleEvent(task=72, start=26.848848,end=35.464884,proc=2), ScheduleEvent(task=65, start=35.464884,end=40.119507,proc=2), ScheduleEvent(task=27, start=40.119507,end=44.523975,proc=2), ScheduleEvent(task=9, start=44.523975,end=48.623472,proc=2), ScheduleEvent(task=7, start=48.623472,end=55.024436,proc=2), ScheduleEvent(task=35, start=55.024436,end=59.174054,proc=2), ScheduleEvent(task=79, start=59.174054,end=66.807630,proc=2), ScheduleEvent(task=56, start=66.807630,end=70.083880,proc=2), ScheduleEvent(task=8, start=70.083880,end=74.322876,proc=2), ScheduleEvent(task=28, start=74.322876,end=81.003498,proc=2), ScheduleEvent(task=3, start=81.003498,end=86.345804,proc=2), ScheduleEvent(task=52, start=86.345804,end=89.763743,proc=2), ScheduleEvent(task=40, start=89.763743,end=92.582004,proc=2), ScheduleEvent(task=125, start=92.582004,end=99.316585,proc=2), ScheduleEvent(task=36, start=99.316585,end=107.046751,proc=2), ScheduleEvent(task=87, start=107.046751,end=113.362944,proc=2), ScheduleEvent(task=101, start=113.362944,end=122.410348,proc=2), ScheduleEvent(task=43, start=122.410348,end=129.324397,proc=2), ScheduleEvent(task=48, start=129.324397,end=130.645744,proc=2), ScheduleEvent(task=68, start=130.645744,end=133.200483,proc=2), ScheduleEvent(task=90, start=133.200483,end=141.758945,proc=2), ScheduleEvent(task=100, start=141.758945,end=147.277687,proc=2), ScheduleEvent(task=93, start=147.277687,end=153.801427,proc=2), ScheduleEvent(task=123, start=153.801427,end=161.923090,proc=2), ScheduleEvent(task=107, start=161.923090,end=167.042154,proc=2), ScheduleEvent(task=102, start=167.042154,end=172.050737,proc=2), ScheduleEvent(task=17, start=172.050737,end=173.931477,proc=2), ScheduleEvent(task=95, start=173.931477,end=179.331469,proc=2), ScheduleEvent(task=129, start=179.331469,end=185.054212,proc=2), ScheduleEvent(task=91, start=185.054212,end=190.404680,proc=2), ScheduleEvent(task=19, start=190.404680,end=194.030511,proc=2), ScheduleEvent(task=121, start=194.030511,end=195.897390,proc=2), ScheduleEvent(task=105, start=195.897390,end=202.885433,proc=2), ScheduleEvent(task=110, start=202.885433,end=206.317814,proc=2), ScheduleEvent(task=84, start=206.317814,end=211.833679,proc=2), ScheduleEvent(task=148, start=211.833679,end=217.029850,proc=2), ScheduleEvent(task=118, start=217.029850,end=220.284311,proc=2), ScheduleEvent(task=143, start=261.240564,end=268.482300,proc=2), ScheduleEvent(task=131, start=268.482300,end=269.697441,proc=2), ScheduleEvent(task=137, start=269.845054,end=273.948728,proc=2), ScheduleEvent(task=146, start=279.031040,end=282.420050,proc=2), ScheduleEvent(task=133, start=291.237325,end=292.752107,proc=2)]}

#gantt.showGanttChart(sched1)
#gantt.showGanttChart(sched2)
