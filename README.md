# TMVA

Set of scripts to perform MVA analysis on given set of input trees, containing variables to perform the training, and additional branches for cuts and weights. For detailed instructions on TMVA, please refer to its default README files. These instructions are designed to help run the scripts in this repository, a few of which are modified from TMVA examples. This README contains two sections:

	1. Training
	2. Application
	 
-----------------------------------------------------------------------------------------------

Training:

	-- Scripts: 
		1. TMVAClassification.py
		2. doCondorClassification.py
		3. doCondorClassification.sh
		4. submitTraining.sh
		5. varsList.py
		6. plotROCint.py
		7. printROCints.py
		8. utils.py

	Edit TMVAClassification.py: main script to setup TMVA

	1. Weights: "weightStrC" (common), "weightStrS" (signal), "weightStrB" (background)

	2. Cuts: "cutStrC" (common), "cutStrS" (signal), "cutStrB" (background)

	3. MVA settings: detailed settings of the BDT such as boost type (for example, Adaptive vs. Gradient)
	
	Edit varsList.py: input variables, directories, etc
	
	1. inputDir, directory containing the input root files
	
	2. List of variables to be used in the training can be defined in "varList" dictionary with a unique key, where each input directory has a list containing "[<variable in trees>, <variable name for axes and titles>, <unit>]"
	
	Edit doCondorClassification.py: condor job submitter for many different configurations
	
	1. "nTrees", "BDTlist" (as they are defined in TMVAClassification.py), "varListKeys", "massList"

	RUN:

	1. python -u doCondorClassification.py
	
	RUN (interactive):
	
	1. "submitTraining.sh" can be used to run multiple configurations interactively in the background --> should be used responsibly!!

	PLOT:

	1. "plotROCint.py" plots the ROC integrals (and relative ROC integrals) as a function of different BDT configurations
	
	2. "printROCints.py" will read ROC integral values from ".out" files after training and print them nicely for different configurations

-----------------------------------------------------------------------------------------------

Application:

	-- Scripts: 
		1. TMVAClassificationApplication_template.C
		2. TMVAClassificationApplication_template2.C
		3. TMVAClassificationApplication_test.C
		4. doCondorApplication.py
		5. doCondorApplication2.py
		6. doCondorApplication.sh
		7. submitTMVAApplication.sh
		8. resubmitFailedJobs.py
		
	Edit doCondorApplication.py: main script to setup condor jobs to apply BDT weights. It uses TMVAClassificationApplication_template.C to setup the application macro depending on the training configuration such as the input variables used in the training are loaded from "varsList.py". For most needs, this is the only script that requires user modifications.
	1. Input directory of the samples on which the BDT weights will be applied
	
	2. "weightFile" is full path to the weight file (.xml) where in the path use "MKutle" and the weight files for different signal mass points will be taken by doing a ".replace('MKutle','M<Mass>')", where <Mass> is as given in "massList"
	
	3. Specify the directory that the BDT weights applied samples should be saved.
	
	4. It has a version, doCondorApplication2.py, to submit jobs for a training with different set of variables depending on the signal mass 
	
	submitTMVAApplication.sh: submits application jobs for nominal samples together with JEC/JER shifts
	
	resubmitFailedJobs.py: performs some checks on the condor jobs to look for any obvious problems. It can also be used to resubmit the jobs that have problems by uncommenting the relevant block in the script; however, this part should be used if all the jobs are finished!!!
	
	TMVAClassificationApplication_template.C: This is the template script used for the BDT application. doCondorApplication.py uses this template and generates the final version for the specific BDT configuration as the details provided in doCondorApplication.py. For most needs, it doesn't need to be modified.

	TMVAClassificationApplication_template2.C: This is the same as above, except that it allows having different set of variables for different mass trainings.
	
	TMVAClassificationApplication_test.C: Same as above, but this one is used mostly for tests and interactive application jobs. Heavy modification may be needed. Run it as "root -l -b -q TMVAClassificationApplication_test.C"
