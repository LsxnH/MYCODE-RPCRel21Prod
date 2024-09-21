import PhysicsRPCProd.PhysicsRPCProdConf as conf

#======================================================================================
def getWriteAlg(ToolSvc, stream, option=''):

    evt_vars = ['Event:type=U64',
                'Run:type=Int',
                'LumiBlock:type=Int',
                'bcid:type=Int']

    prd_hit_vars  = ['identifier:type=U64',
                     'prdTime   :type=Float']
    
    prd_hit_vars_redundant  = ['stationName:type=Short',
                               'stationEta :type=Short',
                               'stationPhi :type=Short',
                               'doubletR   :type=Short',
                               'doubletZ   :type=Short',
                               'doubletPhi :type=Short',
                               'gasGap     :type=Short',
                               'measPhi    :type=Short',
                               'strip      :type=Short']

    rdo_pad_vars  = ['padSector   :type=Int',
                     'padErrorCode:type=UShort',
                     'padOnlineId :type=UShort',
                     'cmaOnlineId :type=UShort',
                     'channel     :type=UShort',
                     'ijk         :type=UShort',                  
                     'bcid        :type=UShort',
                     'time        :type=UShort',
                     'ovl         :type=UShort',
                     'thr         :type=UShort']

    rdo_pad_extra_vars = ['padStatus   :type=UShort',
                          'cmaCrc      :type=UShort',
                          'cmaFel1Id   :type=UShort',
                          'cmaOnlineId :type=UShort']

    geo_vars  = ['gapId_identifier            :type=U64',
                 'gapId_stationName           :type=Short',
                 'gapId_stationEta            :type=Short',
                 'gapId_stationPhi            :type=Short',
                 'gapId_doubletR              :type=Short',
                 'gapId_doubletZ              :type=Short',
                 'gapId_doubletPhi            :type=Short',
                 'gapId_gasGap                :type=Short',
                 'gapId_ReadoutElementHashId  :type=UInt',
                 'panelIdEta_identifier       :type=U64',
                 'panelIdEta_identifier32     :type=UInt',
                 'panelIdPhi_identifier       :type=U64',
                 'panelIdPhi_identifier32     :type=UInt',
                 'stripWidthEta:              :type=Float',
                 'stripWidthPhi:              :type=Float',
                 'stripPitchEta:              :type=Float',
                 'stripPitchPhi:              :type=Float',
                 'stripLengthEta:             :type=Float',
                 'stripLengthPhi:             :type=Float',
                 'localY                      :type=Float',
                 'localZ                      :type=Float',
                 'globalX                     :type=Float',
                 'globalY                     :type=Float',
                 'globalZ                     :type=Float',
                 'globalEta                   :type=Float',
                 'globalPhi                   :type=Float',
                 'etaStrip_stripNumber        :type=VecInt',
                 'etaStrip_containedInParentRE:type=VecInt',
                 'etaStrip_identifier         :type=VecU64',
                 'etaStrip_localY:            :type=VecFloat',
                 'etaStrip_localZ:            :type=VecFloat',
                 'phiStrip_stripNumber        :type=VecInt',
                 'phiStrip_containedInParentRE:type=VecInt',
                 'phiStrip_identifier         :type=VecU64',
                 'phiStrip_localX:            :type=VecFloat',
                 'phiStrip_localY:            :type=VecFloat',
                 'phiStrip_localZ:            :type=VecFloat']

    write_tool = conf.Ath__WriteEvent('writeEvent')
    write_tool.stream               = stream
    write_tool.doDynamicConfigVec   = False
    write_tool.debug                = False

    write_tool.treename             = 'nominal'
    write_tool.doDynamicConfigEvent = True
    write_tool.keys_event           = ','.join(evt_vars)
    write_tool.branches             = ['m_rpc_hit_|%s'    %(','.join(prd_hit_vars )),                           
                                       'm_rpc_rdo_|%s'    %(','.join(rdo_pad_vars ))]
    ToolSvc += write_tool

    save_event = conf.Ath__SaveEvent('saveEvent')
    save_event.writeEvent = write_tool
    
    return save_event

#======================================================================================
def getReadEvent(ToolSvc, stream):

    alg = conf.Ath__ReadEvent('readEvent')
    alg.OutputLevel                  = 3
    alg.debug                        = False
    alg.outputStream                 = stream
    alg.containerNameEventInfoxAOD   = ''
    alg.containerNameEventInfoAthena = 'ByteStreamEventInfo'
    alg.containerNameVertex          = ''
    alg.doTrigDecision               = False

    return alg

#======================================================================================
def getReadL1Hit(ToolSvc):

    ''' Record RPC hits and extrapolate muons to RPC panels'''

    outputLevel = 3
    outputDebug = outputLevel < 3

    geometry = conf.Ath__L1MuonGeometry('muonRPCGeometry')
    geometry.OutputLevel = outputLevel
    geometry.debug       = outputDebug

    alg = conf.Ath__ReadL1Hit('readL1Hit')
    alg.OutputLevel          = outputLevel
    alg.debug                = outputDebug
    alg.debugHits            = False
    alg.printRpcIds          = False
    alg.readRpcPrd           = True
    alg.readRpcRdo           = True
    alg.geometryTool         = geometry
    
    return alg

