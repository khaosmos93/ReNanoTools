# ReNanoTools
Tools to Re-Nano UL samples for dilepton + b-jets

## CMSSW setup:

```
cmsrel CMSSW_10_6_30
cd CMSSW_10_6_30/src
cmsenv
git cms-merge-topic JanFSchulte:nanoProd
scram b -j 4
```

## Job submission setup

```
git clone https://github.com/JanFSchulte/ReNanoTools.git
cd ReNanoTools
```

The repository contains 3 types of files:

* CMSSW python configuration files for NanoAOD production for Data and MC in the four running periods of the UL campaign
* .txt files containing a full list of all data and background samples that are needed for the dilepton + b-jets analysis (need to add signal samples)
* four python scripts to submit crab jobs for the Nano workflows in the four data taking periods, in a loop over all the samples in the corresponding text files

