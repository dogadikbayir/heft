import os
import numpy as np
from heft import heft, gantt
import pandas as pd
import math
import matplotlib.pyplot as plt
import os.path
from os import path
import pathlib

def computeMSDict(root_dir):

    os.chdir(root_dir)
    folder_names = [name for name in os.listdir(".") if os.path.isdir(name)]

# Max and ave dictionaries: These contain the absolute best makespan and the average makespan for the experiments. Each key is an experiment id which is unique

# We'll generate charts from these two dictionaries
    best_res = {}
    ave_res = {}


    for fn in folder_names:

        # Get the experiment parameters from file_name
        params = fn.split("__")

        rc = (params[2].split("_"))[1]
        gh = (params[3].split("_"))[1]
        ccr = (params[4].split("_"))[1]
        hf = (params[5].split("_"))[1]
        mpr = (params[6].split("_"))[1]

        #create unique experiment tag
        unq_tag = rc + "_" + gh + "_" + ccr + "_" + hf + "_" + mpr
        os.chdir(fn)
        reps = [name for name in os.listdir(".") if os.path.isdir(name)]

        best_res[unq_tag] = math.inf
        ave_res[unq_tag] = 0.0
        ave_ms = 0.0
        num_reps = len(reps)

        #print("Processing experiment ", unq_tag)
        for rep in reps:
            #print("Processing replica ", str(rep))
            os.chdir(rep)
            #print(pathlib.Path().absolute())
            df_max = pd.read_csv('max.csv')
            df_ave = pd.read_csv('pop.csv')

            # update best makespan
            if (df_max['SL_AVE'].min() < best_res[unq_tag]):
                best_res[unq_tag] = df_max['SL_AVE'].min()

            # calculate the average makespan
            ave_ms = ave_ms + df_ave['SL_AVE'][len(df_ave['SL_AVE'])-1]
            os.chdir("..")


        ave_ms = ave_ms / num_reps
        ave_res[unq_tag] = ave_ms
        os.chdir("..")

    #print("Finished processing, printing the best makespans...")

    return best_res, ave_res

def pickBestMPR(best_dict, ave_dict):
    best_res = {}
    ave_res = {}
    best_mprs_best = {}
    best_mprs_ave = {}
    for key,val in best_dict.items():
        params = key.split("_")
        unq_tag = params[0] + "_" + params[1] + "_" + params[2] + "_" + params[3]
        if unq_tag not in best_res:
            best_res[unq_tag] = val
            best_mprs_best[unq_tag] = params[4]
        else:
            if val < best_res[unq_tag]:
                best_res[unq_tag] = val
                best_mprs_best[unq_tag] = params[4]

    for key,val in ave_dict.items():
        params = key.split("_")
        unq_tag = params[0] + "_" + params[1] + "_" + params[2] + "_" + params[3]
        if unq_tag not in ave_res:
            ave_res[unq_tag] = val
            best_mprs_ave[unq_tag] = params[4]
        else:
            if val < ave_res[unq_tag]:
                ave_res[unq_tag] = val
                best_mprs_ave[unq_tag] = params[4]

    return best_res, ave_res, best_mprs_best, best_mprs_ave

# generates bar charts to compare makespan between different selection methods
def generateBars(lexiLP_dict, simple_dict, lexiLIB_dict,nsgaLP_dict, heft_dict):

    simple_data = {}
    lexiLIB_data = {}
    lexiLP_data = {}
    nsgalp_data = {}
    heft_data = {}

    #for key,val in heft_dict.items():
    #    params = key.split("_")
    #    unq_tag = params[1] + "_" + params[2] + "_" + params[3]
    #    if unq_tag not in heft_data:
    #        heft_data[unq_tag] = [0,0,0,0]
    #        idx = int(math.log2(int(params[0]))) - 2
    #        (heft_data[unq_tag])[idx] = val
    #    else:
    #        idx = int(math.log2(int(params[0]))) - 2
    #        (heft_data[unq_tag])[idx] = val

    for key,val in simple_dict.items():
        params = key.split("_")
        unq_tag = params[1] + "_" + params[2] + "_" + params[3]
        if unq_tag not in simple_data:
            simple_data[unq_tag] = [0,0,0,0]
            idx = int(math.log2(int(params[0]))) - 2
            (simple_data[unq_tag])[idx] = val
        else:
            idx = int(math.log2(int(params[0]))) - 2
            (simple_data[unq_tag])[idx] = val

    for key,val in lexiLIB_dict.items():
        params = key.split("_")
        unq_tag = params[1] + "_" + params[2] + "_" + params[3]
        if unq_tag not in lexiLIB_data:
            lexiLIB_data[unq_tag] = [0,0,0,0]
            idx = int(math.log2(int(params[0]))) - 2
            (lexiLIB_data[unq_tag])[idx] = val
        else:
            idx = int(math.log2(int(params[0]))) - 2
            (lexiLIB_data[unq_tag])[idx] = val

    for key,val in lexiLP_dict.items():
        params = key.split("_")
        unq_tag = params[1] + "_" + params[2] + "_" + params[3]
        if unq_tag not in lexiLP_data:
            lexiLP_data[unq_tag] = [0,0,0,0]
            idx = int(math.log2(int(params[0]))) - 2
            (lexiLP_data[unq_tag])[idx] = val
        else:
            idx = int(math.log2(int(params[0]))) - 2
            (lexiLP_data[unq_tag])[idx] = val

    for key,val in nsgaLP_dict.items():
        params = key.split("_")
        unq_tag = params[1] + "_" + params[2] + "_" + params[3]
        if unq_tag not in nsgalp_data:
            nsgalp_data[unq_tag] = [0,0,0,0]
            idx = int(math.log2(int(params[0]))) - 2
            (nsgalp_data[unq_tag])[idx] = val
        else:
            idx = int(math.log2(int(params[0]))) - 2
            (nsgalp_data[unq_tag])[idx] = val



    for key,val in lexiLIB_data.items():
        barWidth = 0.1
        bars_lexiLIB = val
        bars_lexiLP = lexiLP_data[key]
        bars_simple = simple_data[key]
        bars_nsgalp = nsgalp_data[key]
        bars_heft = heft_dict[key]
        #print(key)
        #print(bars_nsgalp)
        fig = plt.figure()
        # Set position of bar on X axis
        r1 = np.arange(len(bars_lexiLIB))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]
        r4 = [x + barWidth for x in r3]
        r5 = [x + barWidth for x in r4]
        plt.bar(r1, bars_simple, color='#7f6d5f', width=barWidth, edgecolor='white', label='Simple')
        plt.bar(r2, bars_lexiLIB, color='#557f2d', width=barWidth, edgecolor='white', label='Lexi-LIB')
        plt.bar(r3, bars_lexiLP, color='red', width=barWidth, edgecolor='white', label='Lexi-LP')
        plt.bar(r4, bars_nsgalp, color='blue', width=barWidth, edgecolor='white', label='NSGA-LP')
        plt.bar(r5, bars_heft, color='black', width=barWidth, edgecolor='white', label='HEFT')

        plt.xlabel('#procs' , fontweight='bold')
        plt.xticks([r + barWidth for r in range(len(bars_simple))], ['4', '8', '16', '32'])

        # Create legend & Show graphic
        plt.legend()

        file_name = key + ".png"
        fig.savefig(file_name)

def computeMSDictHEFT(root_dir):
    res_heft = {}
    if path.exists(root_dir):
        os.chdir(root_dir)
        file_names = [name for name in os.listdir(".") if os.path.isdir(name)]
        for fn in file_names:
            params = fn.split("_")
            rc = params[1]
            gh = params[2]
            ccr = params[3]
            hf = params[4]

            unq_tag = gh + "_" + ccr + "_" + hf

            cm_path = fn + "/task_exe_time.csv"
            comp_matrix = heft.readCsvToNumpyMatrix(cm_path)
            cmm_path = fn + "/resource_BW.csv"
            comm_matrix = heft.readCsvToNumpyMatrix(cmm_path)
            dag_path = fn + "/task_connectivity.csv"
            dag = heft.readDagMatrix(dag_path)
            sched, _,_,_ = heft.schedule_dag(dag,communication_matrix=comm_matrix, computation_matrix=comp_matrix)

            if unq_tag not in res_heft:
                res_heft[unq_tag] = [0,0,0,0]

            if int(rc) > 2:
                (res_heft[unq_tag])[int(math.log2(int(rc)))-2] = sched

        return res_heft
    else:
        print("PATH DOESNT EXIST")


heft_res = computeMSDictHEFT("/Users/dogadikbayir/200nodeLexiLIB/200nodeLexiLIB/200data/")

print(heft_res)
lexiLP_best, lexiLP_ave = computeMSDict("/Users/dogadikbayir/200nodeLexiLIB/200nodeLexiLIB/lexiLP")
lexiLP_best, lexiLP_ave, bestMPRsLP, _ = pickBestMPR(lexiLP_best,lexiLP_ave)

print("Best MPRs for LP Lexi: ")
print(bestMPRsLP)

nsgaLP_best, nsgaLP_ave = computeMSDict("/Users/dogadikbayir/200nodeLexiLIB/200nodeLexiLIB/nsgalp")
nsgaLP_best, nsgaLP_ave,_,_ = pickBestMPR(nsgaLP_best, nsgaLP_ave)

print(nsgaLP_best)
lexiLIB_best, lexiLIB_ave = computeMSDict("/Users/dogadikbayir/200nodeLexiLIB/200nodeLexiLIB/lexiLIB")
simple_best, simple_ave = computeMSDict("/Users/dogadikbayir/200nodeLexiLIB/200nodeLexiLIB/simple200")

lexiLIB_best, lexiLIB_ave,_,_ = pickBestMPR(lexiLIB_best,lexiLIB_ave)
simple_best, simple_ave,_,_ = pickBestMPR(simple_best,simple_ave)

os.chdir("..")
try:
    os.mkdir("./charts")
except OSError:
    print ("Cannot create folder ''charts'")
else:
    print ("Successfully created the charts directory")

os.chdir("charts")
generateBars(lexiLP_best, simple_best, lexiLIB_best, nsgaLP_best, heft_res)
