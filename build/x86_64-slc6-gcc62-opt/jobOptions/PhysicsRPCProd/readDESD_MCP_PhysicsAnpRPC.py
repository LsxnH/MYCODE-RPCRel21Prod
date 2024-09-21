############################################################################################################
### Input stream
############################################################################################################
from AthenaCommon.AthenaCommonFlags import athenaCommonFlags

import PhysicsRPCProd.PhysicsRPCProdConfig as Config
import PhysicsRPCProd.PhysicsRPCProdRead   as AthRead

import os

if 'EvtMax' in dir():
    athenaCommonFlags.EvtMax = EvtMax
else:
    athenaCommonFlags.EvtMax = -1

athenaCommonFlags.FilesInput = Config.getInputFiles(locals())

if 'outfile' not in dir():
    outfile = 'out.root'

print '======================================================================'    
print 'Output file name: %s\n' %outfile
print '======================================================================'    

############################################################################################################
### Configure tools and services
############################################################################################################
if 'debug' in dir():
    Config.printEnvPath('TestArea')
    Config.printEnvPath('SourceArea')
    Config.printEnvPath('WorkDir_DIR')

if 'writeGeo' not in dir():
    writeGeo = False
    
if 'writeIDTracks' not in dir():
    writeIDTracks = True

#--------------------------------------------------------------------------------------
# Include and configure RecExCommon
#
include('PhysicsRPCProd/CommonConfig_PhysicsAnpRPC.py')

include('RecExCommon/RecExCommon_topOptions.py')

#--------------------------------------------------------------------------------------
# Must setup cabling services AFTER RecExCommon
#
import MuonCnvExample.MuonCablingConfig
import MuonRPC_Cabling.MuonRPC_CablingConfig

#--------------------------------------------------------------------------------------
# Configure region selector tools
#
from RegionSelector.RegSelSvcDefault import RegSelSvcDefault
theRegSelSvc = RegSelSvcDefault()
theRegSelSvc.enableMuon = True
theRegSelSvc.enableMDT  = False
theRegSelSvc.enableCSC  = False
theRegSelSvc.enableTGC  = False
theRegSelSvc.enableRPC  = True
ServiceMgr += theRegSelSvc

#--------------------------------------------------------------------------------------
# Set output using thistsvc
#
from GaudiSvc.GaudiSvcConf import THistSvc
svcMgr += THistSvc()
svcMgr.THistSvc.Output += ["out DATAFILE='%s' OPT='RECREATE'" %outfile]

svcMgr.MessageSvc.OutputLevel = INFO
svcMgr.MessageSvc.infoLimit = 0

#--------------------------------------------------------------------------------------
# Configure algorithm sequence
#
from AthenaCommon.AlgSequence import AlgSequence
job = AlgSequence()

trig_decision_tool = CfgMgr.Trig__TrigDecisionTool('TrigDecisionTool', TrigDecisionKey = 'xTrigDecision')
ToolSvc += trig_decision_tool

trig_match_muon_tool = CfgMgr.Ath__TrigMatch('trigMatch')
trig_match_muon_tool.TriggerTool = trig_decision_tool
ToolSvc += trig_match_muon_tool

job += AthRead.getReadEvent (ToolSvc, trig_decision_tool, stream='out')
job += AthRead.getReadMuon  (ToolSvc, 'Muons', trig_match_muon_tool, stream='out')
job += AthRead.getReadL1Muon(ToolSvc, writeGeo=writeGeo)

if writeIDTracks:
    job += AthRead.getReadTrack(ToolSvc, 'InDetTrackParticles', stream='out')

save_event = AthRead.getWriteAlg(ToolSvc, stream='out', writeGeo=writeGeo, writeIDTracks=writeIDTracks)

job += save_event

#--------------------------------------------------------------------------------------
# Print debug info
#
print job

if 'debug' in dir():
    print ToolSvc
    print ServiceMgr
    print svcMgr.MessageSvc

if 'dumpSG' in dir():
    StoreGateSvc = Service('StoreGateSvc')
    StoreGateSvc.Dump = dumpSG

