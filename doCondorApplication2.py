import os,sys
import varsList

shift = sys.argv[1]
BDT = 'BDT'
varListKey = 'MAY'
templateFile = '/user_data/ssagir/CMSSW_7_4_7/src/TMVA/TMVAClassificationApplication_template2.C'
massList = ['Low','Med','800','1000','2000','3000']
weightFile = '/user_data/ssagir/CMSSW_7_4_7/src/TMVA/weights/'+BDT+'_Fnl_15vars_mDepth3/'
weightFile+= BDT+'_Config_15vars_mDepth3_MKutle/TMVAClassification_'+BDT+'.weights.xml'

#IO directories must be full paths
relbase   = '/user_data/ssagir/CMSSW_7_4_7/'
inputDir  = '/user_data/jlee/chargedHiggs/EPS2017/LJMet80X_1lep_051117_step2'
outputDir = '/user_data/ssagir/LJMet80X_1lep_051117_step2_'+BDT+'_15vars/'+shift+'/'
inputDir += '/'+shift+'/'

runDir=os.getcwd()
varList = varsList.varList[varListKey]
condorDir=runDir+'/'+outputDir.split('/')[-3]+'_condorLogs/'+shift+'/'
os.system('mkdir -p '+condorDir)

f = open(templateFile, 'rU')
templateFileLines = f.readlines()
f.close()
def makeTMVAClassAppConf(thefile):
	variableMap = {}
	with open(thefile,'w') as fout:
		for line in templateFileLines:
			if line.startswith('input ='): fout.write('input = \''+rFile+'\'')
			if 'TMVA::Reader *reader<mass>' in line:
				for mass in massList:
					fout.write('   TMVA::Reader *reader'+mass+' = new TMVA::Reader( \"!Color:!Silent\" );\n')
			elif 'Float_t var<mass><number>' in line:
				for mass in massList:
					varList = varsList.varList[mass+'Fnl']
					for i, var in enumerate(varList):
						if var[0] in variableMap.keys(): continue
						fout.write('   Float_t var'+mass+str(i+1)+';\n')
						variableMap[var[0]] = 'var'+mass+str(i+1)
			elif 'AddVariable' in line:
				for mass in massList:
					varList = varsList.varList[mass+'Fnl']
					for i, var in enumerate(varList): 
						fout.write('   reader'+mass+'->AddVariable( \"'+var[0]+'\", &'+variableMap[var[0]]+' );\n')
			elif 'BookMVA' in line:
				for mass in massList: 
					fout.write('   reader'+mass+'->BookMVA( \"BDT'+mass+' method\", \"'+weightFile.replace('_MKutle','_M'+mass).replace('_Config','_'+mass+'Fnl')+'\" );\n')
			elif 'Float_t BDT<mass>' in line:
				for mass in massList: 
					fout.write('   Float_t BDT'+mass+';\n')
					fout.write('   TBranch *b_BDT'+mass+' = newTree->Branch( \"BDT'+mass+'\", &BDT'+mass+', \"BDT'+mass+'/F\" );\n')
			elif 'SetBranchAddress' in line:
				for var in variableMap.keys(): 
					fout.write('   theTree->SetBranchAddress( \"'+var+'\", &'+variableMap[var]+' );\n')
			elif 'BDT<mass> = reader<mass>->EvaluateMVA' in line:
				for mass in massList: 
					fout.write('      BDT'+mass+' = reader'+mass+'->EvaluateMVA( \"BDT'+mass+' method\" );\n')
			elif 'delete reader<mass>' in line:
				for mass in massList: 
					fout.write('   delete reader'+mass+';\n')
			else: fout.write(line)
makeTMVAClassAppConf(condorDir+'/TMVAClassificationApplication.C')

rootfiles = os.popen('ls '+inputDir)
os.system('mkdir -p '+outputDir)

count=0
for file in rootfiles:
    if '.root' not in file: continue
    rawname = file[:-6]
    #if not file.startswith('ChargedHiggs_HplusTB_HplusToTB_M-300_13TeV'): continue
    count+=1
    dict={'RUNDIR':runDir,'INPUTDIR':inputDir,'FILENAME':rawname,'OUTPUTDIR':outputDir,'CONDORDIR':condorDir,'CMSSWBASE':relbase,'BDT':BDT}
    jdfName=condorDir+'/%(FILENAME)s.job'%dict
    print jdfName
    jdf=open(jdfName,'w')
    jdf.write(
"""universe = vanilla
Executable = %(RUNDIR)s/doCondorApplication.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
request_memory = 3072
Transfer_Input_Files = %(CONDORDIR)s/TMVAClassificationApplication.C
Output = %(FILENAME)s.out
Error = %(FILENAME)s.err
Log = %(FILENAME)s.log
Notification = Never
Arguments = %(INPUTDIR)s %(OUTPUTDIR)s %(FILENAME)s.root %(BDT)s

Queue 1"""%dict)
    jdf.close()
    os.chdir('%s/'%(condorDir))
    os.system('condor_submit %(FILENAME)s.job'%dict)
    os.system('sleep 0.5')                                
    os.chdir('%s'%(runDir))
    print count, "jobs submitted!!!"

