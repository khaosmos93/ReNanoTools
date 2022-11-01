from CRABClient.UserUtilities import config
import CRABClient

import datetime
now = datetime.datetime.now()
date = now.strftime('%Y%m%d')

with open('samples2018_tmp.txt') as file:
    datasets = file.readlines()
    datasets = [line.rstrip() for line in datasets]

config = config()
config.General.workArea        = 'crab_nanoProd2018_'+date
config.General.transferOutputs = True
config.General.transferLogs    = False
config.JobType.sendExternalFolder = True
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'NanoAODv9_2018_cfg.py'
#config.JobType.numCores    = 4
config.JobType.maxMemoryMB = 3500
#config.JobType.maxJobRuntimeMin= 180
#config.Data.ignoreLocality = True
config.JobType.sendPythonFolder=True
#config.Data.inputDBS = 'phys03'
config.Data.splitting   = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.totalUnits  = -1
config.Data.outLFNDirBase = '/store/user/moh/DileptonReNanoUL/'+date+'/'
config.JobType.outputFiles  = ['nano.root']
config.Data.publication = False
config.Data.allowNonValidInputDataset = True
#config.Data.outputPrimaryDataset = 'Ztest-7TeV_M-1400To2300_13TeV-pythia8'
#config.Data.outputDatasetTag     = 'RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v7'
config.JobType.allowUndistributedCMSSW=True
config.section_('Site')
#config.Site.blacklist = ['T2_US_Caltech','T2_US_Florida','T2_US_MIT','T2_US_Nebraska','T2_US_Vanderbilt','T2_US_Wisconsin']
#config.Site.whitelist = ['T2_US_Purdue', 'T3_KR_KNU']
#config.Site.whitelist = ['T2_US_Purdue']
config.Site.storageSite = 'T1_DE_KIT_Disk'
config.section_('Debug')
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
config.section_('User')
config.User.voGroup = 'dcms'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    for data in datasets:
        print (data)
        config.Data.inputDataset = data
        if "upgrade2018" in data:
            dirName = data.split('/')[1]
            print (dirName)
            config.General.requestName = dirName
            config.Data.outputDatasetTag = 'RunIISummer20UL18MiniAODv2-NANOAOD'
        else:
            config.JobType.psetName = "NanoAODv9_2018_Data_cfg.py"        
            dirName = data.split('/')[1] + "_" + data.split('/')[2].split("-")[0] 
            print (dirName)
            config.General.requestName = dirName
            config.Data.outputDatasetTag = data.split('/')[2] + "-NANOAOD"
        try:
            crabCommand('submit', config = config, proxy = '/tmp/x509up_u12060')
        except:
            print ("submit failed")
