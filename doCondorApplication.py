import os,sys
import varsList

shift = sys.argv[1]
fold = '123'
BDT = 'BDT'
varListKey = 'MAY'
templateFile = '/user_data/ssagir/CMSSW_7_4_7/src/TMVA/TMVAClassificationApplication_template.C'
#massList = ['Low','Med','High','180','200','220','250','300','350','400','500','800','1000','2000','3000']
massList = ['Low','Med','High','800','1000','2000','3000']
# weightFile = '/user_data/ssagir/CMSSW_7_2_4/src/TMVA/test/weights/'+BDT+'_3fold_BigComb_30vars_mDepth3/'
# weightFile+= BDT+'_fold123_BigComb_30vars_mDepth3_MKutle/TMVAClassification_'+BDT+'.weights.xml'.replace('_fold123_','_fold'+fold+'_')
weightFile = '/user_data/ssagir/CMSSW_7_4_7/src/TMVA/weights/'+BDT+'_MAY_21vars_mDepth3/'
weightFile+= BDT+'_MAY_21vars_mDepth3_MKutle/TMVAClassification_'+BDT+'.weights.xml'

#IO directories must be full paths
relbase   = '/user_data/ssagir/CMSSW_7_4_7/'
# inputDir  = '/user_data/ssagir/LJMet80X_1lep_MedMuMVAEl_031017_step2_fold'+fold[-1]
inputDir  = '/user_data/jlee/chargedHiggs/EPS2017/LJMet80X_1lep_051117_step2'
outputDir = '/user_data/ssagir/LJMet80X_1lep_051117_step2_'+BDT+'_21vars/'+shift+'/'
inputDir += '/'+shift+'/'

runDir=os.getcwd()
varList = varsList.varList[varListKey]
condorDir=runDir+'/'+outputDir.split('/')[-3]+'_condorLogs/'+shift+'/'
os.system('mkdir -p '+condorDir)

f = open(templateFile, 'rU')
templateFileLines = f.readlines()
f.close()
def makeTMVAClassAppConf(thefile):
	with open(thefile,'w') as fout:
		for line in templateFileLines:
			if line.startswith('input ='): fout.write('input = \''+rFile+'\'')
			if 'Float_t var<number>' in line:
				for i, var in enumerate(varList): 
					fout.write('   Float_t var'+str(i+1)+';\n')
			elif 'AddVariable' in line:
				for i, var in enumerate(varList): 
					fout.write('   reader->AddVariable( \"'+var[0]+'\", &var'+str(i+1)+' );\n')
			elif 'BookMVA' in line:
				for mass in massList: 
					fout.write('   reader->BookMVA( \"BDT'+mass+' method\", \"'+weightFile.replace('_MKutle','_M'+mass)+'\" );\n')
			elif 'Float_t BDT<mass>' in line:
				for mass in massList: 
					fout.write('   Float_t BDT'+mass+';\n')
					fout.write('   TBranch *b_BDT'+mass+' = newTree->Branch( \"BDT'+mass+'\", &BDT'+mass+', \"BDT'+mass+'/F\" );\n')
			elif 'SetBranchAddress' in line:
				for i, var in enumerate(varList): 
					fout.write('   theTree->SetBranchAddress( \"'+var[0]+'\", &var'+str(i+1)+' );\n')
			elif 'BDT<mass> = reader->EvaluateMVA' in line:
				for mass in massList: 
					fout.write('      BDT'+mass+' = reader->EvaluateMVA( \"BDT'+mass+' method\" );\n')
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

