#!/usr/bin/python

import os,sys,math,fnmatch
from utils import *

massList = ['Low','Med','800','1000','2000','3000']
Configs = ['33vars','24vars','NoST','NoHT','NoMET','NoLepPt','NoLeadJetPt',
           'NoLeadBJetPt','NoHemiOut','NoLepMETHT','NoLepJetBJetMETHT',
           'NoLepBJetMETHTHemiOut','NoLepJetMETHTHemiOut','19vars','15vars',
           #'16vars','17vars','18vars',
           'Final15',
           #'Final15samevars'
           ]

inputDirs = {
             'NoST':'weights/Nminus1trainings/BDT_MAY24NoST/',
             'NoHT':'weights/Nminus1trainings/BDT_MAY24NoHT/',
             'NoMET':'weights/Nminus1trainings/BDT_MAY24NoMET/',
             'NoLepPt':'weights/Nminus1trainings/BDT_MAY24NoLepPt/',
             'NoLeadJetPt':'weights/Nminus1trainings/BDT_MAY24NoLeadJetPt/',
             'NoLeadBJetPt':'weights/Nminus1trainings/BDT_MAY24NoLeadBJetPt/',
             'NoHemiOut':'weights/Nminus1trainings/BDT_MAY24NoHemiOut/',
             'NoLepMETHT':'weights/Nminus1trainings/BDT_MAY24NoLepMETHTvsST/',
             'NoLepJetBJetMETHT':'weights/Nminus1trainings/BDT_MAY24NoLepJetBJetMETHTvsST/',
             'NoLepJetMETHTHemiOut':'weights/BDT_MAY19_19vars_mDepth3/',
             'NoLepBJetMETHTHemiOut':'weights/BDT_MAY19_19vars_mDepth3_BJetPt/',
             '15vars':'weights/BDT_MAY15_15vars_mDepth3/',
             '16vars':'weights/BDT_MAY16_16vars_mDepth3/',
             '17vars':'weights/BDT_MAY17_17vars_mDepth3/',
             '18vars':'weights/BDT_MAY18_18vars_mDepth3/',
             'Final15':'weights/BDT_Fnl_15vars_mDepth3/',
             'Final15samevars':'weights/BDT_MAY15_same15vars_mDepth3/',
             '24vars':'weights/BDT_MAY24_24vars_mDepth3/',
             '33vars':'weights/BDT_APR9_33vars_mDepth3/',
             '19vars':'weights/BDT_MAY19_19vars_mDepth3/',
             }

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)

ROCints = {}
for train in inputDirs.keys():          
	filelist = []
	for afile in findfiles(inputDirs[train], '*.out'): filelist.append(afile)

	ROCints[train] = {}
	for thefile in filelist:
		ftemp = open(thefile, 'rU')
		lines = ftemp.readlines()
		for ind in range(len(lines)):
			if 'ROC-integ.' in lines[ind]: 
				ROCints[train][thefile.split('/')[-1].split('_')[-1].replace('.out','')] = lines[ind+2].split()[-4]
				break
	ftemp.close()

table = []
row = ['Mass:']
for mass in massList: row.append(mass)
table.append(row)
table.append(['break'])
table.append(['break'])
for train in Configs:
	row = [train]
	for mass in massList:
		row.append(ROCints[train]['M'+mass])
	if train=='19vars': table.append(['break'])
	table.append(row)
	if train=='33vars' or train=='24vars' or train=='19vars': table.append(['break'])
out=open('Nminus1trainings.txt','w')
printTable(table,out)
