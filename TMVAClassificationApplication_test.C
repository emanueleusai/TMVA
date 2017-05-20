/**********************************************************************************
 * Project   : TMVA - a Root-integrated toolkit for multivariate data analysis    *
 * Package   : TMVA                                                               *
 * Exectuable: TMVAClassificationApplication                                      *
 *                                                                                *
 * This macro provides a simple example on how to use the trained classifiers     *
 * within an analysis module                                                      *
 **********************************************************************************/

#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <string>

#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TStopwatch.h"

#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include "TMVA/MethodCuts.h"

using namespace TMVA;

void TMVAClassificationApplication_new( TString myMethodList = "BDT" ) 
{   

   //---------------------------------------------------------------

   // This loads the library
   TMVA::Tools::Instance();

   // Default MVA methods to be trained + tested
   std::map<std::string,int> Use;

   // --- Cut optimisation
   Use["Cuts"]            = 1;
   Use["CutsD"]           = 1;
   Use["CutsPCA"]         = 0;
   Use["CutsGA"]          = 0;
   Use["CutsSA"]          = 0;
   // 
   // --- 1-dimensional likelihood ("naive Bayes estimator")
   Use["Likelihood"]      = 1;
   Use["LikelihoodD"]     = 0; // the "D" extension indicates decorrelated input variables (see option strings)
   Use["LikelihoodPCA"]   = 1; // the "PCA" extension indicates PCA-transformed input variables (see option strings)
   Use["LikelihoodKDE"]   = 0;
   Use["LikelihoodMIX"]   = 0;
   //
   // --- Mutidimensional likelihood and Nearest-Neighbour methods
   Use["PDERS"]           = 1;
   Use["PDERSD"]          = 0;
   Use["PDERSPCA"]        = 0;
   Use["PDEFoam"]         = 1;
   Use["PDEFoamBoost"]    = 0; // uses generalised MVA method boosting
   Use["KNN"]             = 1; // k-nearest neighbour method
   //
   // --- Linear Discriminant Analysis
   Use["LD"]              = 1; // Linear Discriminant identical to Fisher
   Use["Fisher"]          = 0;
   Use["FisherG"]         = 0;
   Use["BoostedFisher"]   = 0; // uses generalised MVA method boosting
   Use["HMatrix"]         = 0;
   //
   // --- Function Discriminant analysis
   Use["FDA_GA"]          = 1; // minimisation of user-defined function using Genetics Algorithm
   Use["FDA_SA"]          = 0;
   Use["FDA_MC"]          = 0;
   Use["FDA_MT"]          = 0;
   Use["FDA_GAMT"]        = 0;
   Use["FDA_MCMT"]        = 0;
   //
   // --- Neural Networks (all are feed-forward Multilayer Perceptrons)
   Use["MLP"]             = 0; // Recommended ANN
   Use["MLPBFGS"]         = 0; // Recommended ANN with optional training method
   Use["MLPBNN"]          = 1; // Recommended ANN with BFGS training method and bayesian regulator
   Use["CFMlpANN"]        = 0; // Depreciated ANN from ALEPH
   Use["TMlpANN"]         = 0; // ROOT's own ANN
   //
   // --- Support Vector Machine 
   Use["SVM"]             = 1;
   // 
   // --- Boosted Decision Trees
   Use["BDT"]             = 1; // uses Adaptive Boost
   Use["BDTG"]            = 0; // uses Gradient Boost
   Use["BDTB"]            = 0; // uses Bagging
   Use["BDTD"]            = 0; // decorrelation + Adaptive Boost
   // 
   // --- Friedman's RuleFit method, ie, an optimised series of cuts ("rules")
   Use["RuleFit"]         = 1;
   // ---------------------------------------------------------------
   Use["Plugin"]          = 0;
   Use["Category"]        = 0;
   Use["SVM_Gauss"]       = 0;
   Use["SVM_Poly"]        = 0;
   Use["SVM_Lin"]         = 0;

   std::cout << std::endl;
   std::cout << "==> Start TMVAClassificationApplication" << std::endl;

   // Select methods (don't look at this code - not of interest)
   if (myMethodList != "") {
      for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) it->second = 0;

      std::vector<TString> mlist = gTools().SplitString( myMethodList, ',' );
      for (UInt_t i=0; i<mlist.size(); i++) {
         std::string regMethod(mlist[i]);

         if (Use.find(regMethod) == Use.end()) {
            std::cout << "Method \"" << regMethod 
                      << "\" not known in TMVA under this name. Choose among the following:" << std::endl;
            for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) {
               std::cout << it->first << " ";
            }
            std::cout << std::endl;
            return;
         }
         Use[regMethod] = 1;
      }
   }

   // --------------------------------------------------------------------------------------------------

   // --- Create the Reader object

   TMVA::Reader *reader = new TMVA::Reader( "!Color:!Silent" );    

   // Create a set of variables and declare them to the reader
   // - the variable names MUST corresponds in name and type to those given in the weight file(s) used
   Float_t var1;
   Float_t var2;
   Float_t var3;
   Float_t var4;
   Float_t var5;
   Float_t var6;
   Float_t var7;
   Float_t var8;
   Float_t var9;
   Float_t var10;
   Float_t var11;
   Float_t var12;
   Float_t var13;
   Float_t var14;
   Float_t var15;
   Float_t var16;
   Float_t var17;
   Float_t var18;
   Float_t var19;
   Float_t var20;
   Float_t var21;
   Float_t var22;
   Float_t var23;
   Float_t var24;
   Float_t var25;
   Float_t var26;
   Float_t var27;
   Float_t var28;
   Float_t var29;
   Float_t var30;
   Float_t var31;
   Float_t var32;
   Float_t var33;
   reader->AddVariable( "AK4HTpMETpLepPt", &var1 );
   reader->AddVariable( "corr_met", &var2 );
   reader->AddVariable( "minMleppBjet", &var3 );
   reader->AddVariable( "mass_lepJets0", &var4 );
   reader->AddVariable( "mass_lepJets1", &var5 );
   reader->AddVariable( "mass_lepJets2", &var6 );
   reader->AddVariable( "deltaR_lepBJets0", &var7 );
   reader->AddVariable( "lepDR_minBBdr", &var8 );
   reader->AddVariable( "BJetLeadPt", &var9 );
   reader->AddVariable( "aveBBdr", &var10 );
   reader->AddVariable( "mass_maxBBmass", &var11 );
   reader->AddVariable( "mass_maxJJJpt", &var12 );
   reader->AddVariable( "AK4HT", &var13 );
   reader->AddVariable( "mass_minBBdr", &var14 );
   reader->AddVariable( "mass_lepBJet_mindr", &var15 );
   reader->AddVariable( "MT_lepMet", &var16 );
   reader->AddVariable( "MT2bb", &var17 );
   reader->AddVariable( "MT2bbl", &var18 );
   reader->AddVariable( "centrality", &var19 );
   reader->AddVariable( "hemiout", &var20 );
   reader->AddVariable( "deltaEta_maxBB", &var21 );
   reader->AddVariable( "deltaR_minBB", &var22 );
   reader->AddVariable( "deltaR_lepBJet_maxpt", &var23 );
   reader->AddVariable( "mass_minLLdr", &var24 );
   reader->AddVariable( "theJetLeadPt", &var25 );
   reader->AddVariable( "deltaR_lepJets0", &var26 );
   reader->AddVariable( "deltaR_lepJets1", &var27 );
   reader->AddVariable( "deltaR_lepJets2", &var28 );
   reader->AddVariable( "minDR_lepBJet", &var29 );
   reader->AddVariable( "mass_lepBJet0", &var30 );
   reader->AddVariable( "aveCSVpt", &var31 );
   reader->AddVariable( "PtFifthJet", &var32 );
   reader->AddVariable( "FW_momentum_2", &var33 );

   // --- Book the MVA methods

   reader->BookMVA( "BDTLow method", "/user_data/ssagir/CMSSW_7_4_7/src/TMVA/weights/BDT_APR9_33vars_mDepth3/BDT_APR9_33vars_mDepth3_MLow/TMVAClassification_BDT.weights.xml" );
   reader->BookMVA( "BDTMed method", "/user_data/ssagir/CMSSW_7_4_7/src/TMVA/weights/BDT_APR9_33vars_mDepth3/BDT_APR9_33vars_mDepth3_MMed/TMVAClassification_BDT.weights.xml" );
   reader->BookMVA( "BDTHigh method", "/user_data/ssagir/CMSSW_7_4_7/src/TMVA/weights/BDT_APR9_33vars_mDepth3/BDT_APR9_33vars_mDepth3_MHigh/TMVAClassification_BDT.weights.xml" );
   reader->BookMVA( "BDT800 method", "/user_data/ssagir/CMSSW_7_4_7/src/TMVA/weights/BDT_APR9_33vars_mDepth3/BDT_APR9_33vars_mDepth3_M800/TMVAClassification_BDT.weights.xml" );
   reader->BookMVA( "BDT1000 method", "/user_data/ssagir/CMSSW_7_4_7/src/TMVA/weights/BDT_APR9_33vars_mDepth3/BDT_APR9_33vars_mDepth3_M1000/TMVAClassification_BDT.weights.xml" );
   reader->BookMVA( "BDT2000 method", "/user_data/ssagir/CMSSW_7_4_7/src/TMVA/weights/BDT_APR9_33vars_mDepth3/BDT_APR9_33vars_mDepth3_M2000/TMVAClassification_BDT.weights.xml" );
   reader->BookMVA( "BDT3000 method", "/user_data/ssagir/CMSSW_7_4_7/src/TMVA/weights/BDT_APR9_33vars_mDepth3/BDT_APR9_33vars_mDepth3_M3000/TMVAClassification_BDT.weights.xml" );

   // Prepare input tree (this must be replaced by your data source)
   // in this example, there is a toy tree with signal and one with background events
   // we'll later on use only the "signal" events for the test in this example.
   //   
   TFile *input(0);
   TString fname = "/user_data/ssagir/LJMet80X_1lep_MedMuMVAEl_031017_step2sfs/nominal/ChargedHiggs_HplusTB_HplusToTB_M-300_13TeV_amcatnlo_pythia8_hadd.root";   
   if (!gSystem->AccessPathName( fname )) 
      input = TFile::Open( fname ); // check if file in local directory exists
   else    
      input = TFile::Open( "http://root.cern.ch/files/tmva_class_example.root" ); // if not: download from ROOT server
   
   if (!input) {
      std::cout << "ERROR: could not open data file" << std::endl;
      exit(1);
   }
   std::cout << "--- TMVAClassificationApp    : Using input file: " << input->GetName() << std::endl;
   
   // --- Event loop

   // Prepare the event tree
   // - here the variable names have to corresponds to your tree
   // - you can use the same variables as above which is slightly faster,
   //   but of course you can use different ones and copy the values inside the event loop
   //
   std::cout << "--- Select signal sample" << std::endl;
   TTree* theTree = (TTree*)input->Get("ljmet");
   theTree->SetBranchAddress( "AK4HTpMETpLepPt", &var1 );
   theTree->SetBranchAddress( "corr_met", &var2 );
   theTree->SetBranchAddress( "minMleppBjet", &var3 );
   theTree->SetBranchAddress( "mass_lepJets0", &var4 );
   theTree->SetBranchAddress( "mass_lepJets1", &var5 );
   theTree->SetBranchAddress( "mass_lepJets2", &var6 );
   theTree->SetBranchAddress( "deltaR_lepBJets0", &var7 );
   theTree->SetBranchAddress( "lepDR_minBBdr", &var8 );
   theTree->SetBranchAddress( "BJetLeadPt", &var9 );
   theTree->SetBranchAddress( "aveBBdr", &var10 );
   theTree->SetBranchAddress( "mass_maxBBmass", &var11 );
   theTree->SetBranchAddress( "mass_maxJJJpt", &var12 );
   theTree->SetBranchAddress( "AK4HT", &var13 );
   theTree->SetBranchAddress( "mass_minBBdr", &var14 );
   theTree->SetBranchAddress( "mass_lepBJet_mindr", &var15 );
   theTree->SetBranchAddress( "MT_lepMet", &var16 );
   theTree->SetBranchAddress( "MT2bb", &var17 );
   theTree->SetBranchAddress( "MT2bbl", &var18 );
   theTree->SetBranchAddress( "centrality", &var19 );
   theTree->SetBranchAddress( "hemiout", &var20 );
   theTree->SetBranchAddress( "deltaEta_maxBB", &var21 );
   theTree->SetBranchAddress( "deltaR_minBB", &var22 );
   theTree->SetBranchAddress( "deltaR_lepBJet_maxpt", &var23 );
   theTree->SetBranchAddress( "mass_minLLdr", &var24 );
   theTree->SetBranchAddress( "theJetLeadPt", &var25 );
   theTree->SetBranchAddress( "deltaR_lepJets0", &var26 );
   theTree->SetBranchAddress( "deltaR_lepJets1", &var27 );
   theTree->SetBranchAddress( "deltaR_lepJets2", &var28 );
   theTree->SetBranchAddress( "minDR_lepBJet", &var29 );
   theTree->SetBranchAddress( "mass_lepBJet0", &var30 );
   theTree->SetBranchAddress( "aveCSVpt", &var31 );
   theTree->SetBranchAddress( "PtFifthJet", &var32 );
   theTree->SetBranchAddress( "FW_momentum_2", &var33 );
   
   TFile *target  = new TFile( "sinan.root","RECREATE" );
   target->cd();
   TTree *newTree = theTree->CloneTree(0);
   Float_t BDTLow;
   TBranch *b_BDTLow = newTree->Branch( "BDTLow", &BDTLow, "BDTLow/F" );
   Float_t BDTMed;
   TBranch *b_BDTMed = newTree->Branch( "BDTMed", &BDTMed, "BDTMed/F" );
   Float_t BDTHigh;
   TBranch *b_BDTHigh = newTree->Branch( "BDTHigh", &BDTHigh, "BDTHigh/F" );
   Float_t BDT800;
   TBranch *b_BDT800 = newTree->Branch( "BDT800", &BDT800, "BDT800/F" );
   Float_t BDT1000;
   TBranch *b_BDT1000 = newTree->Branch( "BDT1000", &BDT1000, "BDT1000/F" );
   Float_t BDT2000;
   TBranch *b_BDT2000 = newTree->Branch( "BDT2000", &BDT2000, "BDT2000/F" );
   Float_t BDT3000;
   TBranch *b_BDT3000 = newTree->Branch( "BDT3000", &BDT3000, "BDT3000/F" );

   // Efficiency calculator for cut method
   Int_t    nSelCutsGA = 0;
   Double_t effS       = 0.7;

   std::cout << "--- Processing: " << theTree->GetEntries() << " events" << std::endl;
   TStopwatch sw;
   sw.Start();
   for (Long64_t ievt=0; ievt<theTree->GetEntries();ievt++) {

      if (ievt%1000 == 0) std::cout << "--- ... Processing event: " << ievt << std::endl;

      theTree->GetEntry(ievt);

      // --- Return the MVA outputs and fill into histograms

      if (Use["CutsGA"]) {
         // Cuts is a special case: give the desired signal efficienciy
         Bool_t passed = reader->EvaluateMVA( "CutsGA method", effS );
         if (passed) nSelCutsGA++;
      }
      BDTLow = reader->EvaluateMVA( "BDTLow method" );
      BDTMed = reader->EvaluateMVA( "BDTMed method" );
      BDTHigh = reader->EvaluateMVA( "BDTHigh method" );
      BDT800 = reader->EvaluateMVA( "BDT800 method" );
      BDT1000 = reader->EvaluateMVA( "BDT1000 method" );
      BDT2000 = reader->EvaluateMVA( "BDT2000 method" );
      BDT3000 = reader->EvaluateMVA( "BDT3000 method" );
      
      newTree->Fill();
   }

   // Get elapsed time
   sw.Stop();
   std::cout << "--- End of event loop: "; sw.Print();

   // Get efficiency for cuts classifier
   if (Use["CutsGA"]) std::cout << "--- Efficiency for CutsGA method: " << double(nSelCutsGA)/theTree->GetEntries()
                                << " (for a required signal efficiency of " << effS << ")" << std::endl;

   if (Use["CutsGA"]) {

      // test: retrieve cuts for particular signal efficiency
      // CINT ignores dynamic_casts so we have to use a cuts-secific Reader function to acces the pointer  
      TMVA::MethodCuts* mcuts = reader->FindCutsMVA( "CutsGA method" ) ;

      if (mcuts) {      
         std::vector<Double_t> cutsMin;
         std::vector<Double_t> cutsMax;
         mcuts->GetCuts( 0.7, cutsMin, cutsMax );
         std::cout << "--- -------------------------------------------------------------" << std::endl;
         std::cout << "--- Retrieve cut values for signal efficiency of 0.7 from Reader" << std::endl;
         for (UInt_t ivar=0; ivar<cutsMin.size(); ivar++) {
            std::cout << "... Cut: " 
                      << cutsMin[ivar] 
                      << " < \"" 
                      << mcuts->GetInputVar(ivar)
                      << "\" <= " 
                      << cutsMax[ivar] << std::endl;
         }
         std::cout << "--- -------------------------------------------------------------" << std::endl;
      }
   }
   // --- Write tree
   newTree->Write();
   target->Close();

   std::cout << "--- Created root file: \"TMVApp.root\" containing the MVA output histograms" << std::endl;
  
   delete reader;
    
   std::cout << "==> TMVAClassificationApplication is done!" << std::endl << std::endl;
} 

int main( int argc, char** argv )
{
   TString methodList; 
   for (int i=1; i<argc; i++) {
      TString regMethod(argv[i]);
      if(regMethod=="-b" || regMethod=="--batch") continue;
      if (!methodList.IsNull()) methodList += TString(","); 
      methodList += regMethod;
   }
   TMVAClassificationApplication_new(methodList); 
   return 0; 
}
