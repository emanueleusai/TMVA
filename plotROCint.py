#!/usr/bin/python

from ROOT import TH1D,gROOT,TGraph,TCanvas,TLatex,TLine,TLegend
import os,sys,math,itertools,fnmatch
from numpy import linspace
from array import array

gROOT.SetBatch(1)

from tdrStyle import *
setTDRStyle()

inputDirs = {
             'Low':'weights/BDT_24varsScan_mDepth3_MLow/',
             'Med':'weights/BDT_24varsScan_mDepth3_MMed/',
             '800':'weights/BDT_24varsScan_mDepth3_M800/',
             '1000':'weights/BDT_24varsScan_mDepth3_M1000/',
             '2000':'weights/BDT_24varsScan_mDepth3_M2000/',
             '3000':'weights/BDT_24varsScan_mDepth3_M3000/',
             }

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)

hists = {}
relhists = {}
for train in inputDirs.keys():          
	filelist = []
	for afile in findfiles(inputDirs[train], '*.out'): filelist.append(afile)

	ROCints = {}
	for thefile in filelist:
		ftemp = open(thefile, 'rU')
		lines = ftemp.readlines()
		for ind in range(len(lines)):
			if 'ROC-integ.' in lines[ind]: 
				ROCints[thefile.split('/')[-1].split('_')[2].replace('vars','')] = lines[ind+2].split()[-4]
				break
	ftemp.close()

	hists[train] = TH1D("ROC_"+train,"",len(filelist),0,len(filelist))
	relhists[train] = TH1D("ROC_rel_"+train,"",len(filelist),0,len(filelist))
	for ibin in ROCints.keys(): 
		hists[train].SetBinContent(int(ibin), float(ROCints[ibin]))
		hists[train].GetXaxis().SetBinLabel(int(ibin),ibin)
		relhists[train].SetBinContent(int(ibin), float(ROCints[ibin])/float(ROCints['24']))
		relhists[train].GetXaxis().SetBinLabel(int(ibin),ibin)

canv = TCanvas("canv","ROCs", 1000, 800)
canv.SetBottomMargin(0.15)
canv.SetRightMargin(0.06)
hists['Low'].GetXaxis().LabelsOption("u")
hists['Low'].GetXaxis().SetLabelSize(0.05)
hists['Low'].GetYaxis().SetRangeUser(0.5,1.0)
hists['Low'].GetXaxis().SetTitle('N_{variables}')
hists['Low'].GetYaxis().SetTitle('ROC-integral')
hists['Low'].GetYaxis().SetNdivisions(505)
hists['Low'].SetLineColor(1)
hists['Low'].SetLineStyle(1)
hists['Low'].SetLineWidth(2)
hists['Low'].Draw('HIST')
colind=2
for train in inputDirs.keys(): 
	if train=='Low':
		colind+=1
		continue
	if colind==5: colind+=1
	hists[train].SetLineColor(colind)
	hists[train].SetLineStyle(1)
	hists[train].SetLineWidth(2)
	hists[train].Draw('SAMEHIST')
	colind+=1

leg = TLegend(.55,.2,.93,.4)
try: leg.AddEntry(hists['Low'], 'Low', "l")
except: pass
try: leg.AddEntry(hists['Med'], 'Med', "l")
except: pass
try: leg.AddEntry(hists['800'], '800', "l")
except: pass
try: leg.AddEntry(hists['1000'], '1000', "l")
except: pass
try: leg.AddEntry(hists['2000'], '2000', "l")
except: pass
try: leg.AddEntry(hists['3000'], '3000', "l")
except: pass
leg.SetShadowColor(0)
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.SetNColumns(2)
leg.Draw() 

canv.SaveAs('ROCscan24vars.png')

canvrel = TCanvas("canvrel","relROCs", 1000, 800)
#canvrel.SetLogy()
canvrel.SetBottomMargin(0.15)
canvrel.SetRightMargin(0.06)
relhists['Low'].GetXaxis().LabelsOption("u")
relhists['Low'].GetXaxis().SetLabelSize(0.05)
relhists['Low'].GetYaxis().SetRangeUser(0.7,1.0)
relhists['Low'].GetXaxis().SetTitle('N_{variables}')
relhists['Low'].GetYaxis().SetTitle('relative ROC-integral')
relhists['Low'].GetYaxis().SetNdivisions(505)
relhists['Low'].SetLineColor(1)
relhists['Low'].SetLineStyle(1)
relhists['Low'].SetLineWidth(2)
relhists['Low'].Draw('HIST')
colind=2
for train in inputDirs.keys(): 
	if train=='Low':
		colind+=1
		continue
	if colind==5: colind+=1
	relhists[train].SetLineColor(colind)
	relhists[train].SetLineStyle(1)
	relhists[train].SetLineWidth(2)
	relhists[train].Draw('SAMEHIST')
	colind+=1

legrel = TLegend(.55,.2,.93,.4)
try: legrel.AddEntry(hists['Low'], 'Low', "l")
except: pass
try: legrel.AddEntry(hists['Med'], 'Med', "l")
except: pass
try: legrel.AddEntry(hists['800'], '800', "l")
except: pass
try: legrel.AddEntry(hists['1000'], '1000', "l")
except: pass
try: legrel.AddEntry(hists['2000'], '2000', "l")
except: pass
try: legrel.AddEntry(hists['3000'], '3000', "l")
except: pass
legrel.SetShadowColor(0)
legrel.SetFillColor(0)
legrel.SetLineColor(0)
legrel.SetNColumns(2)
legrel.Draw() 

canvrel.SaveAs('relROCscan24vars.png')

