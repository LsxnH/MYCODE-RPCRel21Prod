'''
Job options to read RAW BS data for RPC hits
'''

import PhysicsRPCProd.PhysicsRPCProdConfig as Config
import PhysicsRPCProd.PhysicsRPCProdNoise  as Noise

from AthenaCommon.AthenaCommonFlags import athenaCommonFlags

input_files = Config.getInputFiles(locals())

athenaCommonFlags.FilesInput = input_files

from ByteStreamCnvSvc import ReadByteStream
ServiceMgr.ByteStreamInputSvc.FullFileName = input_files

from AthenaCommon.AppMgr import theApp
import AthenaCommon.AtlasUnixStandardJob

if 'EvtMax' in dir():
    theApp.EvtMax = EvtMax

from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()

from AthenaCommon.AppMgr import ServiceMgr

from AthenaCommon import CfgGetter
from AthenaCommon.CfgGetter import getPublicTool, getPrivateTool, getService, getAlgorithm

#=====================================================================================
# Global conditions and detector configuration
#
if not 'ConditionsTag' in dir():
    ConditionsTag='CONDBR2-BLKPA-2018-06'

if not 'DetDescrVersion' in dir():
    DetDescrVersion='ATLAS-R2-2016-01-00-01'

from AthenaCommon.GlobalFlags import globalflags
globalflags.DataSource = 'data'          # or set this to 'geant4' if running on MC! ...
globalflags.DatabaseInstance = 'CONDBR2' # e.g. if you want run 2 data, set to COMP200 if you want run1

from IOVDbSvc.CondDB import conddb
import IOVDbSvc.IOVDb

from AthenaCommon.JobProperties import jobproperties

ServiceMgr.IOVDbSvc.GlobalTag        = ConditionsTag
jobproperties.Global.DetDescrVersion = DetDescrVersion

#=====================================================================================
# Set up detector flags
#
from AthenaCommon.DetFlags import DetFlags 
DetFlags.detdescr.ID_setOff()
DetFlags.detdescr.LAr_setOff()
DetFlags.detdescr.Tile_setOff()
DetFlags.detdescr.Muon_setOn()
DetFlags.readRDOBS.RPC_setOn() 

from AtlasGeoModel import SetGeometryVersion
from AtlasGeoModel import GeoModelInit

import MuonCnvExample.MuonCablingConfig
import MuonRPC_Cabling.MuonRPC_CablingConfig

#=====================================================================================
# RPC BS to RDO offline algorithms
#
import MuonCnvExample.MuonReadBSConfig

include('MuonCnvExample/MuonReadBS_jobOptions.py')

#=====================================================================================
# RPC rdo to prd
#
from MuonRPC_CnvTools.MuonRPC_CnvToolsConf import Muon__RpcRdoToPrepDataTool

RpcRdoToPrepDataTool = Muon__RpcRdoToPrepDataTool('RpcPrepDataProviderTool')
RpcRdoToPrepDataTool.OutputLevel = INFO

ToolSvc += RpcRdoToPrepDataTool

PrcRdoDec = getPublicTool('RpcROD_Decoder')
PrcRdoDec.OutputLevel = INFO

from MuonRdoToPrepData.MuonRdoToPrepDataConf import RpcRdoToRpcPrepData

RpcRdoToRpcPrepData = RpcRdoToRpcPrepData()
RpcRdoToRpcPrepData.PrintPrepData = False

topSequence += RpcRdoToRpcPrepData

#=====================================================================================
# Read and save RPC hits
#
if 'outfile' not in dir():
    outfile = 'hit.root'

if 'outstream' not in dir():
    outstream = 'hit'

topSequence += Noise.getReadEvent(ToolSvc, stream=outstream)
topSequence += Noise.getReadL1Hit(ToolSvc)
topSequence += Noise.getWriteAlg (ToolSvc, stream=outstream)

from GaudiSvc.GaudiSvcConf import THistSvc
svcMgr += THistSvc()
svcMgr.THistSvc.Output += ["%s DATAFILE='%s' OPT='RECREATE'" %(outstream, outfile)]

svcMgr.MessageSvc.OutputLevel = INFO
svcMgr.MessageSvc.infoLimit = 99999999

#=====================================================================================
# Debugging and messaging flags
#
ServiceMgr.MessageSvc.defaultLimit=99999999
MessageSvc.OutputLevel = INFO
MessageSvc.defaultLimit = 99999999
MessageSvc.Format = '% F%50W%S%7W%R%T %0W%M'

if 'dumpSG' in dir():
    StoreGateSvc = Service('StoreGateSvc')
    StoreGateSvc.Dump = dumpSG


