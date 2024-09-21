import os

#======================================================================================
def getInputFiles(values):

    input_files = []

    if 'inputDir' in values:
        inputDir = values['inputDir']

        for f in os.listdir(inputDir):
            input_files += ['%s/%s' %(inputDir, f)]
        
    elif 'inputFile' in values:
        inputFile = values['inputFile']

        if os.path.isfile(inputFile):
            input_files += [inputFile]
        else:
            raise Exception('Invalid inputFile="%s"' %inputFile)

    elif 'inputFileList' in values:
        input_files += readInputFile(values['inputFileList'])
        
    elif os.path.isfile('input.txt'):
        input_files += readInputFile('input.txt')
    
    print '======================================================================'

    if len(input_files):
        print 'Print %d input files' %len(input_files)
        
        for f in input_files:
            print '   %s' %f
    else:
        print 'Missing input files - OK for pathena'

    print '\n======================================================================' 

    return input_files

#======================================================================================
def configAthenaSetup():

    ''' Configure athena setup '''

    # setup trigger config
    from RecExConfig.RecFlags import rec
    rec.doTrigger=True

    from RecExConfig.RecAlgsFlags import recAlgs
    recAlgs.doTrigger=True
    
    from TriggerJobOpts.TriggerFlags import TriggerFlags
    TriggerFlags.doTriggerConfigOnly=True

    # read ESD and don't write anything
    rec.readESD=True
    rec.doWriteAOD=False
    rec.doWriteESD=False
    rec.doWriteTAG=False
    rec.doAOD=False
    rec.doDPD=False
    rec.doESD=False
    doTAG=False
    
    # switch off as much as possible
    rec.doTruth=False
    rec.doRecoTiming=False
    rec.doDetStatus=True
    rec.doShowSizeStatistics=False
    rec.readTAG=False
    rec.readRDO=False
    rec.doHist=False
    rec.doContainerRemapping=False
    rec.doJiveXML=False
    rec.doEdmMonitor=False
    rec.doDumpPoolInputContent=False
    rec.doHeavyIon=False
    rec.doHIP=False
    rec.doWriteBS=False
    rec.doPhysValMonHists=False
    rec.doVP1=False
    rec.doJiveXML=False
    rec.doCheckDictionary=False
    rec.doFileMetaData=False
    rec.doAODCaloCells=False
    recAlgs.doAtlfast=False
    recAlgs.doMonteCarloReact=False
    rec.doEgamma=False
    rec.CBNTAthenaAware=False
    rec.doAODSelect=False
    rec.doWritexAOD=False
    rec.doPerfMon=False
    rec.doTagRawSummary=False
    rec.doBTagging=False
    rec.doSemiDetailedPerfMon=False
    rec.doAODall=False
    rec.doTau=False
    rec.doJetMissingETTag=False
    recAlgs.doCaloTrkMuId=False
    recAlgs.doEFlow=False
    recAlgs.doMissingET=False
    recAlgs.doMuGirl=False
    recAlgs.doMuTag=False
    recAlgs.doMuonIDCombined=False
    recAlgs.doMuonIDStandAlone=False
    recAlgs.doStaco=False
    recAlgs.doTileMuID=False
    recAlgs.doTrackParticleCellAssociation=False
    recAlgs.doTrackRecordFilter=False

    from AthenaCommon.DetFlags import DetFlags      
    DetFlags.detdescr.all_setOn()

    import MuonCnvExample.MuonCablingConfig
    import MuonRPC_Cabling.MuonRPC_CablingConfig

    #
    # TGC CABLING
    #from MuonCablingServers.MuonCablingServersConf import TGCcablingServerSvc
    #ServiceMgr += TGCcablingServerSvc()
    #theApp.CreateSvc += [ "TGCcablingServerSvc" ]
    #ServiceMgr.TGCcablingServerSvc.Atlas=True
    #ServiceMgr.TGCcablingServerSvc.forcedUse=True
    #ServiceMgr.TGCcablingServerSvc.useMuonTGC_CablingSvc=True
    #from TGC_CondCabling.TGC_CondCablingConf import TGCCablingDbTool
    #ToolSvc += TGCCablingDbTool()
    #from IOVDbSvc.CondDB import conddb
    #conddb.addFolderSplitMC('TGC','/TGC/CABLING/MAP_SCHEMA','/TGC/CABLING/MAP_SCHEMA')

#======================================================================================
def printEnvPath(env):

    import os

    dpath = os.getenv(env)

    if not dpath:
        print 'printEnvPath - invalid env: %s' %env
        return

    print '============================================================================'
    print 'printEnvPath - env=%s' %env

    printDir(dpath)

    print 'printEnvPath - env=%s - done' %env
    print '============================================================================'

#======================================================================================
def printDir(dpath, pad=''):

    import os

    if not dpath:
        print 'printDir - input dpath is none: "%s"' %dpath
        return

    if not os.path.isdir(dpath):
        return

    print pad + '----------------------------------------------------------------------------'
    print pad + 'printDir - %s' %dpath

    children = []
    
    for f in os.listdir(dpath):
        fpath = '%s/%s' %(dpath, f)
        
        if os.path.isdir(fpath):
            print pad + '   dir:  %s' %f
            children += [fpath]
        else:
            print pad + '   file: %s' %f


    for c in children:
        printDir(c, pad+'  ') 

    print pad + '----------------------------------------------------------------------------'

#======================================================================================
def readInputFile(fpath):

    if not os.path.isfile(fpath):
        return []

    ifile = open(fpath, 'r')
    flist = []
    
    for l in ifile.readlines():
        flist += [l.rstrip('\n')]

    return flist
