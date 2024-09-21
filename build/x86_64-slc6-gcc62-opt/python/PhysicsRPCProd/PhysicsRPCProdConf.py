#Sun Apr 28 05:24:19 2019"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from AthenaCommon.Configurable import *

class Ath__L1MuonExtrapolator( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'debug' : False, # bool
    'debugStripPos' : False, # bool
    'selectTrackExtrapolationValid' : False, # bool
    'selectTrackExtrapolationInBounds' : False, # bool
    'useAODParticle' : False, # bool
    'minDRTrackToGasGap' : 0.50000000, # float
    'minDRTrackToReadoutElement' : 1.0000000, # float
    'boundsToleranceReadoutElement' : 100.00000, # float
    'boundsToleranceReadoutElementTight' : 20.000000, # float
  }
  _propertyDocDct = { 
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__L1MuonExtrapolator, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::L1MuonExtrapolator'
  pass # class Ath__L1MuonExtrapolator

class Ath__L1MuonGeometry( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'debug' : False, # bool
    'geometryFile' : '', # str
  }
  _propertyDocDct = { 
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__L1MuonGeometry, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::L1MuonGeometry'
  pass # class Ath__L1MuonGeometry

class Ath__L1MuonHistoTool( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'THistSvc' : ServiceHandle('THistSvc/THistSvc'), # GaudiHandle
    'RootStreamName' : '/', # str
    'RootDirName' : '', # str
    'HistNamePrefix' : '', # str
    'HistNamePostfix' : '', # str
    'HistTitlePrefix' : '', # str
    'HistTitlePostfix' : '', # str
  }
  _propertyDocDct = { 
    'HistTitlePrefix' : """ The prefix for the histogram THx title """,
    'HistNamePostfix' : """ The postfix for the histogram THx name """,
    'HistNamePrefix' : """ The prefix for the histogram THx name """,
    'HistTitlePostfix' : """ The postfix for the histogram THx title """,
    'RootDirName' : """ Name of the ROOT directory inside the ROOT file where the histograms will go """,
    'RootStreamName' : """ Name of the output ROOT stream (file) that the THistSvc uses """,
    'THistSvc' : """ Handle to a THistSvc instance: it will be used to write ROOT objects to ROOT files """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__L1MuonHistoTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::L1MuonHistoTool'
  pass # class Ath__L1MuonHistoTool

class Ath__ReadEvent( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCounter' : 0, # int
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : False, # bool
    'IsClonable' : False, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'outputStream' : '', # str
    'triggerBitsHistName' : 'trigger_bits', # str
    'containerNameEventInfoxAOD' : 'EventInfo', # str
    'containerNameEventInfoAthena' : '', # str
    'containerNameVertex' : 'PrimaryVertices', # str
    'debug' : False, # bool
    'doTrigDecision' : False, # bool
    'triggersL1' : [  ], # list
    'triggersHLT' : [  ], # list
    'triggerGroupConfigs' : [  ], # list
    'trigDecision' : PublicToolHandle('Trig::TrigDecisionTool'), # GaudiHandle
  }
  _propertyDocDct = { 
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__ReadEvent, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::ReadEvent'
  pass # class Ath__ReadEvent

class Ath__ReadL1Hit( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCounter' : 0, # int
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : False, # bool
    'IsClonable' : False, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'THistSvc' : ServiceHandle('THistSvc/THistSvc'), # GaudiHandle
    'RootStreamName' : '/', # str
    'RootDirName' : '', # str
    'HistNamePrefix' : '', # str
    'HistNamePostfix' : '', # str
    'HistTitlePrefix' : '', # str
    'HistTitlePostfix' : '', # str
    'debug' : False, # bool
    'debugHits' : False, # bool
    'printRpcIds' : False, # bool
    'readRpcPrd' : False, # bool
    'readRpcRdo' : False, # bool
    'geometryTool' : PrivateToolHandle('Ath::L1MuonGeometry'), # GaudiHandle
  }
  _propertyDocDct = { 
    'HistTitlePostfix' : """ The postfix for the histogram THx title """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'THistSvc' : """ Handle to a THistSvc instance: it will be used to write ROOT objects to ROOT files """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'RootStreamName' : """ Name of the output ROOT stream (file) that the THistSvc uses """,
    'HistTitlePrefix' : """ The prefix for the histogram THx title """,
    'HistNamePostfix' : """ The postfix for the histogram THx name """,
    'RootDirName' : """ Name of the ROOT directory inside the ROOT file where the histograms will go """,
    'Cardinality' : """ How many clones to create """,
    'HistNamePrefix' : """ The prefix for the histogram THx name """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__ReadL1Hit, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::ReadL1Hit'
  pass # class Ath__ReadL1Hit

class Ath__ReadL1Muon( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCounter' : 0, # int
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : False, # bool
    'IsClonable' : False, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'THistSvc' : ServiceHandle('THistSvc/THistSvc'), # GaudiHandle
    'RootStreamName' : '/', # str
    'RootDirName' : '', # str
    'HistNamePrefix' : '', # str
    'HistNamePostfix' : '', # str
    'HistTitlePrefix' : '', # str
    'HistTitlePostfix' : '', # str
    'debug' : False, # bool
    'debugHits' : False, # bool
    'printRpcIds' : False, # bool
    'readRpcPrd' : False, # bool
    'readRpcRdo' : False, # bool
    'fileRpcGeometry' : '', # str
    'fileRpcGeometryCheck' : '', # str
    'fileRpcPanelIds' : '', # str
    'inputVecMuon' : '', # str
    'prefixExtrapolateTrack_Primary' : 'RpcExtrapolate_', # str
    'prefixExtrapolateTrack_ID' : 'RpcExtrapolateID_', # str
    'prefixExtrapolateTrack_MS' : 'RpcExtrapolateMS_', # str
    'configCutsMuon' : [  ], # list
    'RPCRecRoiSvc' : ServiceHandle('LVL1RPC::RPCRecRoiSvc'), # GaudiHandle
    'TGCRecRoiSvc' : ServiceHandle('LVL1TGC::TGCRecRoiSvc'), # GaudiHandle
    'extrapolatorTool' : PrivateToolHandle('Ath::L1MuonExtrapolator'), # GaudiHandle
    'geometryTool' : PrivateToolHandle('Ath::L1MuonGeometry'), # GaudiHandle
  }
  _propertyDocDct = { 
    'HistTitlePostfix' : """ The postfix for the histogram THx title """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'THistSvc' : """ Handle to a THistSvc instance: it will be used to write ROOT objects to ROOT files """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'RootStreamName' : """ Name of the output ROOT stream (file) that the THistSvc uses """,
    'HistTitlePrefix' : """ The prefix for the histogram THx title """,
    'HistNamePostfix' : """ The postfix for the histogram THx name """,
    'RootDirName' : """ Name of the ROOT directory inside the ROOT file where the histograms will go """,
    'Cardinality' : """ How many clones to create """,
    'HistNamePrefix' : """ The prefix for the histogram THx name """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__ReadL1Muon, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::ReadL1Muon'
  pass # class Ath__ReadL1Muon

class Ath__ReadMuon( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCounter' : 0, # int
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : False, # bool
    'IsClonable' : False, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'outputStream' : '', # str
    'inputContainerName' : '', # str
    'outputVectorName' : '', # str
    'triggersHLT' : [  ], # list
    'triggersL1' : [  ], # list
    'auxVars' : [  ], # list
    'configMuonCuts' : [  ], # list
    'debug' : False, # bool
    'doTrigMatch' : False, # bool
    'doMuonCalibration' : True, # bool
    'doMuonSelection' : True, # bool
    'printAuxVars' : False, # bool
    'trigMatch' : PublicToolHandle('Ath::ITrigMatch'), # GaudiHandle
  }
  _propertyDocDct = { 
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__ReadMuon, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::ReadMuon'
  pass # class Ath__ReadMuon

class Ath__ReadTrack( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCounter' : 0, # int
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : False, # bool
    'IsClonable' : False, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'outputStream' : '', # str
    'inputContainerName' : '', # str
    'outputVectorName' : '', # str
    'prefixExtrapolateIDTrack' : 'RpcExtrapolateID_', # str
    'auxVars' : [  ], # list
    'configTrackCuts' : [  ], # list
    'minTrackPt' : 0.0000000, # float
    'printAuxVars' : False, # bool
    'debug' : False, # bool
    'extrapolatorTool' : PrivateToolHandle('Ath::L1MuonExtrapolator'), # GaudiHandle
  }
  _propertyDocDct = { 
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__ReadTrack, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::ReadTrack'
  pass # class Ath__ReadTrack

class Ath__SaveEvent( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCounter' : 0, # int
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : False, # bool
    'IsClonable' : False, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'writeEvent' : PublicToolHandle('Ath::IEventTool'), # GaudiHandle
    'outputStream' : '', # str
    'outputFile' : '', # str
  }
  _propertyDocDct = { 
    'outputFile' : """ Output file name """,
    'outputStream' : """ Output stream name """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__SaveEvent, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::SaveEvent'
  pass # class Ath__SaveEvent

class Ath__TrigMatch( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'TriggerTool' : PublicToolHandle('Trig::TrigDecisionTool/TrigDecisionTool'), # GaudiHandle
  }
  _propertyDocDct = { 
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__TrigMatch, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::TrigMatch'
  pass # class Ath__TrigMatch

class Ath__WriteEvent( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'debug' : False, # bool
    'print' : True, # bool
    'doDynamicConfigEvent' : False, # bool
    'doDynamicConfigVec' : False, # bool
    'keys_event' : '', # str
    'stream' : '', # str
    'treename' : '', # str
    'branches' : [  ], # list
  }
  _propertyDocDct = { 
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Ath__WriteEvent, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsRPCProd'
  def getType( self ):
      return 'Ath::WriteEvent'
  pass # class Ath__WriteEvent
