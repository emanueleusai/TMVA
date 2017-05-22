#!/bin/sh

runDir=${1}
fileName=${2}
method=${3}
mass=${4}
vListKey=${5}
nTrees=${6}
mDepth=${7}

source /cvmfs/cms.cern.ch/cmsset_default.sh

cd $runDir
eval `scramv1 runtime -sh`

# scl enable python27 bash &
# source /cvmfs/sft.cern.ch/lcg/contrib/gcc/4.8/x86_64-centos7-gcc48-opt/setup.sh ''
# source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.08.02/x86_64-centos7-gcc48-opt/root/bin/thisroot.sh

source /cvmfs/sft.cern.ch/lcg/external/gcc/4.9.1/x86_64-slc6-gcc48-opt/setup.sh ''
source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.06.04/x86_64-slc6-gcc49-opt/root/bin/thisroot.sh
# env
# which root

python TMVAClassification.py -m $method -k $mass -l $vListKey -n $nTrees -d $mDepth
