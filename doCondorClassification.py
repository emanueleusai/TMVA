import os,sys
import varsList

nTrees = '1000'
BDTlist = ['BDT']
#varListKeys = ['Low'+str(i) for i in range(1,20)]
#varListKeys = ['Med'+str(i) for i in range(1,20)]
#varListKeys = ['0p8TeV'+str(i) for i in range(1,20)]
#varListKeys = ['1TeV'+str(i) for i in range(1,20)]
#varListKeys = ['2TeV'+str(i) for i in range(1,20)]
#varListKeys = ['3TeV'+str(i) for i in range(1,20)]
varListKeys = ['MAY15']
#massList = ['Low','Med','High','180','200','220','250','300','350','400','500','800','1000','2000','3000']
massList = ['Low','Med','High','800','1000','2000','3000']

runDir=os.getcwd()
condorDir=runDir+'/weights/'

count=0
for method in BDTlist:
    for mass in massList:
    	for vListKey in varListKeys:
    		for mDepth in ['3']:
				count+=1
				fileName = method+'_'+vListKey+'_'+str(len(varsList.varList[vListKey]))+'vars_mDepth'+mDepth+'_M'+mass
				dict={'RUNDIR':runDir,'FILENAME':fileName,'METHOD':method,'MASS':mass,'vListKey':vListKey,'mDepth':mDepth,'nTrees':nTrees}
				jdfName=condorDir+'/%(FILENAME)s.job'%dict
				print jdfName
				jdf=open(jdfName,'w')
				jdf.write(
"""universe = vanilla
Executable = %(RUNDIR)s/doCondorClassification.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
request_memory = 3072
Output = %(FILENAME)s.out
Error = %(FILENAME)s.err
Log = %(FILENAME)s.log
Notification = Never
Arguments = %(RUNDIR)s %(FILENAME)s %(METHOD)s %(MASS)s %(vListKey)s %(nTrees)s %(mDepth)s

Queue 1"""%dict)
				jdf.close()
				os.chdir('%s/'%(condorDir))
				os.system('condor_submit %(FILENAME)s.job'%dict)
				os.system('sleep 0.5')                                
				os.chdir('%s'%(runDir))
				print count, "jobs submitted!!!"

