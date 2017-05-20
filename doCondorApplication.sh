#!/bin/sh

inDir=${1}
outDir=${2}
fileName=${3}
BDT=${4}

source /cvmfs/cms.cern.ch/cmsset_default.sh
# scl enable python27 bash &
# source /cvmfs/sft.cern.ch/lcg/contrib/gcc/4.8/x86_64-centos7-gcc48-opt/setup.sh ''
# source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.08.02/x86_64-centos7-gcc48-opt/root/bin/thisroot.sh

source /cvmfs/sft.cern.ch/lcg/external/gcc/4.9.1/x86_64-slc6-gcc48-opt/setup.sh ''
source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.06.04/x86_64-slc6-gcc49-opt/root/bin/thisroot.sh
# env
# which root

root -l -b -q TMVAClassificationApplication.C\(\"$BDT\",\"$inDir/$fileName\",\"$fileName\"\)

cp $fileName $outDir/
rm $fileName 
rm TMVAClassificationApplication.C
