import PhysicsRPCProd.PhysicsRPCProdConf as conf

#======================================================================================
def getWriteAlg(ToolSvc, stream='out', option='', writeGeo=False, writeIDTracks=False):

    evt_vars = ['Event:type=U64',
                'Run:type=Int',
                'LumiBlock:type=Int',
                'bcid:type=Int',
                'backgroundFlags:type=UInt',
                'MCChannel:type=Int',                
                'ActualInteractions:type=Float',
                'AverageInteractions:type=Float',
                'NRecoVtx:type=Short',
                'HasPriVtx:type=Short',
                'EventFlag_Core:type=Short',
                'ErrorState_Core:type=Short',
                'ErrorState_Background:type=Short',
                'ErrorState_LAr:type=Short',
                'ErrorState_Tile:type=Short',
                'ErrorState_SCT:type=Short',
                'ErrorState_Pixel:type=Short',
                'ErrorState_TRT:type=Short',
                'ErrorState_Muon:type=Short',
                'BeamPosX:type=Float',
                'BeamPosY:type=Float',
                'BeamPosZ:type=Float',
                'BeamPosSigmaX:type=Float',
                'BeamPosSigmaY:type=Float',
                'BeamPosSigmaZ:type=Float',
                'PassedTriggerBitNumbers:type=VecInt',
                ]

    muon_vars = ['Pt                          :type=Float',
                 'Eta                         :type=Float',
                 'Phi                         :type=Float',
                 'PDG                         :type=Short',
                 'D0                          :type=Float',
                 'D0Sig                       :type=Float',
                 'Z0Sin                       :type=Float',
                 'Loose                       :type=Short',
                 'Medium                      :type=Short',
                 'Tight                       :type=Short',
                 'PrimaryTrackNdof            :type=Short',
                 'PrimaryTrackChi2            :type=Float',
                 'PrimaryTrackPt              :type=Float',
                 'PrimaryTrackQoverPErr       :type=Float',
                 'ExtrapMSTrackNdof           :type=Short',
                 'ExtrapMSTrackChi2           :type=Float',
                 'ExtrapMSTrackPt             :type=Float',
                 'ExtrapMSTrackQoverPErr      :type=Float',
                 'readL1Muon_selectMuon       :type=Short',
                 ] 

    rpc_track_vars = ['NGasGapInBounds           :type=Int',
                      'NGasGapInBoundsTight      :type=Int',
                      'gapId_identifier          :type=VecU64',
                      'localTrackPosValid        :type=VecInt',
                      'localTrackPosInBounds     :type=VecInt',
                      'localTrackPosInBoundsTight:type=VecInt',
                      'localTrackPosY            :type=VecFloat',
                      'localTrackPosZ            :type=VecFloat',
                      'minTrackGasGapDEta        :type=VecFloat',
                      'minTrackGasGapDPhi        :type=VecFloat',
                      ]

    rpc_track_vars_redundant = ['gapId_stationName:type=VecInt',
                                'gapId_stationEta :type=VecInt',
                                'gapId_stationPhi :type=VecInt',
                                'gapId_doubletR   :type=VecInt',
                                'gapId_doubletZ   :type=VecInt',
                                'gapId_doubletPhi :type=VecInt',
                                'gapId_gasGap     :type=VecInt',
                                ]

    roi_vars  = ['roiWord           :type=UInt',
                 'roiPosInSector    :type=Int',
                 'roiSectorAddress  :type=Int',
                 'roiSource         :type=Int',
                 'roiHemisphere     :type=Int',
                 'roiEta            :type=Float',
                 'roiPhi            :type=Float',
                 'roiSide           :type=Int',
                 'roiSector         :type=Int',
                 'roiNumber         :type=Int',
                 'thrNumber         :type=Int',
                 'isFirstCandidate  :type=Short',
                 'isMoreCandInRoi   :type=Short',
                 'isMoreCandInSector:type=Short',
                 'isVetoed          :type=Short',
                 ]

    rdo_roi_vars  = ['dataWord          :type=UInt',
                     'roiWord           :type=UInt',
                     'eta               :type=Float',
                     'phi               :type=Float',
                     'roiNumber         :type=Int',
                     'source            :type=Int',
                     'hemisphere        :type=Int',
                     'sectorID          :type=Int',
                     'thrNumber         :type=Int',
                     'overlapFlags      :type=Short',
                     'bcid              :type=Short',
                     'bcid_rel          :type=Short',
                     ]

    prd_hit_vars  = ['identifier:type=U64',
                     'prdTime   :type=Float',
                     ]
    
    prd_hit_vars_redundant  = ['stationName:type=Short',
                               'stationEta :type=Short',
                               'stationPhi :type=Short',
                               'doubletR   :type=Short',
                               'doubletZ   :type=Short',
                               'doubletPhi :type=Short',
                               'gasGap     :type=Short',
                               'measPhi    :type=Short',
                               'strip      :type=Short',]

    rdo_pad_vars  = ['padSector   :type=Int',
                     'padErrorCode:type=UShort',
                     'padOnlineId :type=UShort',
                     'cmaOnlineId :type=UShort',
                     'channel     :type=UShort',
                     'ijk         :type=UShort',                  
                     'bcid        :type=UShort',
                     'time        :type=UShort',
                     'ovl         :type=UShort',
                     'thr         :type=UShort',
                  ]

    rdo_pad_extra_vars = ['padStatus   :type=UShort',
                          'cmaCrc      :type=UShort',
                          'cmaFel1Id   :type=UShort',
                          'cmaOnlineId :type=UShort',
                          ]

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
                 'etaStrip_localX:            :type=VecFloat',
                 'etaStrip_localY:            :type=VecFloat',
                 'etaStrip_localZ:            :type=VecFloat',
                 'etaStrip_globalX:           :type=VecFloat',
                 'etaStrip_globalY:           :type=VecFloat',
                 'etaStrip_globalZ:           :type=VecFloat',
                 'phiStrip_stripNumber        :type=VecInt',
                 'phiStrip_containedInParentRE:type=VecInt',
                 'phiStrip_identifier         :type=VecU64',
                 'phiStrip_localX:            :type=VecFloat',
                 'phiStrip_localY:            :type=VecFloat',
                 'phiStrip_localZ:            :type=VecFloat',
                 'phiStrip_globalX:           :type=VecFloat',
                 'phiStrip_globalY:           :type=VecFloat',
                 'phiStrip_globalZ:           :type=VecFloat',
                 ]

    id_track_vars = ['Pt                          :type=Float',
                     'Eta                         :type=Float',
                     'Phi                         :type=Float'] 

    for track in ['RpcExtrapolate', 'RpcExtrapolateID', 'RpcExtrapolateMS']:
        for track_var in rpc_track_vars:
            muon_vars += ['%s_%s' %(track, track_var)]

    muon_vars += getMuonAuxVars(option)

    id_track_vars += getTrackAuxVars(option)

    for track in ['RpcExtrapolateID']:
        for track_var in rpc_track_vars:
            id_track_vars += ['%s_%s' %(track, track_var)]

    for trig in getTriggersPrimary(): 
        evt_vars  += ['%s:type=Short' %trig]

    for trig in getTriggersL1Muon():
        evt_vars  += ['%s_TBP:type=Short' %trig]
        evt_vars  += ['%s_TAP:type=Short' %trig]
        evt_vars  += ['%s_TAV:type=Short' %trig]

    for trig in getTriggersPrimary('Muon'):
        muon_vars += ['match_%s:type=Short' %trig]

    write_tool = conf.Ath__WriteEvent('writeEvent')
    write_tool.stream               = stream
    write_tool.doDynamicConfigVec   = False
    write_tool.debug                = False

    if writeGeo:
        write_tool.treename             = 'geometry'
        write_tool.doDynamicConfigEvent = False
        write_tool.keys_event           = ''
        write_tool.branches             = ['m_rpc_geo_|%s' %(','.join(geo_vars))]
    else:
        write_tool.treename             = 'nominal'
        write_tool.doDynamicConfigEvent = True
        write_tool.keys_event           = ','.join(evt_vars)
        write_tool.branches             = ['m_muon_|%s'       %(','.join(muon_vars)),
                                           'm_rpc_hit_|%s'    %(','.join(prd_hit_vars )),                           
                                           'm_rpc_rdo_|%s'    %(','.join(rdo_pad_vars )),
                                           'm_l1mu_roi_|%s'   %(','.join(roi_vars )),
                                           'm_l1mu_ctpi_|%s'  %(','.join(rdo_roi_vars ))]

        if writeIDTracks:
            write_tool.branches += ['m_id_track_|%s'   %(','.join(id_track_vars))]

    ToolSvc += write_tool

    save_event = conf.Ath__SaveEvent('saveEvent')
    save_event.writeEvent = write_tool
    
    return save_event

#======================================================================================
def getTriggersPrimary(key=''):

    muon_triggers = [
        'HLT_mu20_iloose_L1MU15',
        'HLT_mu24_imedium',
        'HLT_mu24_ivarmedium',
        'HLT_mu26_imedium',
        'HLT_mu26_ivarmedium',
        'HLT_mu40',
        'HLT_mu50',
        'HLT_mu60',
        'HLT_mu22_mu8noL1',
        'HLT_mu22_mu8noL1_calotag_0eta010',
        'HLT_mu24_mu8noL1',
        'HLT_mu24_mu8noL1_calotag_0eta010',
        'HLT_2mu14',
        ]

    elec_triggers = [        
        'HLT_e24_lhtight_nod0_ivarloose',
        'HLT_e26_lhmedium_nod0_ivarloose',
        'HLT_e60_medium',
        'HLT_e60_lhmedium',
        'HLT_e60_lhmedium_nod0_L1EM24VHI',
        'HLT_e60_lhmedium_nod0',
        'HLT_e24_lhmedium_L1EM18VH',
        'HLT_e24_lhmedium_L1EM20VH',
        'HLT_e120_lhloose',
        'HLT_e26_lhtight_nod0_ivarloose',
        'HLT_e26_lhtight_nod0_ivarloose_L1EM22VHIM',
        'HLT_e28_lhtight_nod0_ivarloose',
        'HLT_e28_lhtight_nod0_ivarloose_L1EM24VHIM',
        'HLT_e140_lhloose_nod0',
        'HLT_e140_lhloose_nod0_L1EM24VHI',
        'HLT_e300_etcut',
        'HLT_e300_etcut_L1EM24VHI',
    ]

    if key.lower().count('muon'):
        return muon_triggers

    return muon_triggers + elec_triggers

#======================================================================================
def getTriggersL1Muon():
    
    triggers = ['L1_MU4',
                'L1_MU6',
                'L1_MU10',
                'L1_MU11',
                'L1_MU15',
                'L1_MU20',
                ]

    return triggers


#======================================================================================
def getTriggerGroups():
    
    rpc_monitor = ['HLT_(xe.*|[0-9]?j[0-9]*|j[0-9]*_(jes|lcw|nojcalib|sub|L1RD0|280eta320|320eta490).*|[0-9]?j[0-9]*_b.*|j[0-9]*_[0-9]j[0-9]*_b.*|tau.*|[0-9]?e[0-9]*_(iloose|loose|medium|lhloose|lhmedium|lhtight|etcut)|[0-9]?e[0-9]*_(iloose|loose|medium|lhloose|lhmedium|lhtight|etcut)_(iloose|nod0|HLTCalo|cutd0dphideta|smooth|L1EM[0-9]*VH|L1EM[0-9]*)|[0-9]?e[0-9]*_(iloose|loose|medium|lhloose|lhmedium|lhtight)_(iloose|nod0|HLTCalo|cutd0dphideta|smooth)_(HLTCalo|iloose|L1EM[0-9]*VH|L1EM[0-9]*)|[0-9]?g[0-9]*_(loose|medium|tight|etcut)|g[0-9]*_(loose|etcut)_(L1EM[0-9]*|L1EM[0-9]*VH)|(e|g)[0-9]*_(loose|medium|lhmedium|tight)_g.*|ht.*|te.*|xs.*|mb.*)']

    groups = ['TRIG_GROUP_zb    :HLT_.*L1ZB.*',
              'TRIG_GROUP_mu    :HLT_.*mu.*',
              'TRIG_GROUP_met   :HLT_xe.*|HLT_xs.*',
              'TRIG_GROUP_energy:HLT_ht.*|HLT_te.*',
              'TRIG_GROUP_1jet  :HLT_j[0-9]*|j[0-9]*_(jes|lcw|nojcalib|sub|L1RD0|280eta320|320eta490).*|[0-9]',
              'TRIG_GROUP_njet  :HLT_[2-9]j[0-9]*|j[0-9]*_(jes|lcw|nojcalib|sub|L1RD0|280eta320|320eta490).*|[0-9]',
              'TRIG_GROUP_bjet  :HLT_j[0-9].*_bmv.*|HLT_2j[0-9].*_bmv.*',
              'TRIG_GROUP_elec1 :HLT_e[0-9]*_(iloose|loose|medium|lhloose|lhmedium|lhtight|etcut)|[0-9]',
              'TRIG_GROUP_elec2 :HLT_e[0-9]*_(iloose|loose|medium|lhloose|lhmedium|lhtight|etcut)_(iloose|nod0|HLTCalo|cutd0dphideta|smooth|L1EM[0-9]*VH|L1EM[0-9]*)|[0-9]',
              'TRIG_GROUP_elec3 :HLT_e[0-9]*_(iloose|loose|medium|lhloose|lhmedium|lhtight)_(iloose|nod0|HLTCalo|cutd0dphideta|smooth)_(HLTCalo|iloose|L1EM[0-9]*VH|L1EM[0-9]*)|[0-9]',
              'TRIG_GROUP_photon:HLT_g[0-9]*_(loose|medium|tight|etcut)|g[0-9]*_(loose|etcut)_(L1EM[0-9]*|L1EM[0-9]*VH)|(e|g)[0-9]*_(loose|medium|lhmedium|tight)',
              'TRIG_GROUP_cosmic:HLT_.*cosmic.*']

    return groups

#======================================================================================
def getReadEvent(ToolSvc, trig_decision, stream):

    alg = conf.Ath__ReadEvent('readEvent')
    alg.OutputLevel  = 3
    alg.debug        = False
    alg.outputStream = stream

    alg.triggersHLT    = getTriggersPrimary()
    alg.triggersL1     = getTriggersL1Muon()

    alg.trigDecision   = trig_decision
    alg.doTrigDecision = True

    alg.triggerGroupConfigs = getTriggerGroups()

    return alg

#======================================================================================
def getReadMuon(ToolSvc, input_name, match_tool, stream):

    ''' Process muons - MuonSelectionTool requires variables not stored with EGAM1 so it is disabled '''

    alg = conf.Ath__ReadMuon('%s_readMuons' %input_name)
    alg.inputContainerName = input_name
    alg.outputVectorName   = 'm_muon_'
    alg.printAuxVars       = False
    alg.debug              = False
    alg.OutputLevel        = 3
    alg.outputStream       = stream
    alg.configMuonCuts     = getAnalysisCuts_Muon()
    alg.auxVars            = getMuonAuxVars()

    alg.triggersL1         = getTriggersL1Muon()
    alg.triggersHLT        = getTriggersPrimary('Muon')
    alg.trigMatch          = match_tool
    alg.doTrigMatch        = True

    return alg

#======================================================================================
def getReadL1Muon(ToolSvc, writeGeo=False):

    ''' Record RPC hits and extrapolate muons to RPC panels'''

    outputLevel = 3
    outputDebug = outputLevel < 3

    extrapolator = conf.Ath__L1MuonExtrapolator('muonRPCExtrapolator')
    extrapolator.OutputLevel                      = outputLevel
    extrapolator.debug                            = outputDebug
    extrapolator.selectTrackExtrapolationValid    = True
    extrapolator.selectTrackExtrapolationInBounds = True

    geometry = conf.Ath__L1MuonGeometry('muonRPCGeometry')
    geometry.OutputLevel = outputLevel
    geometry.debug       = outputDebug

    alg = conf.Ath__ReadL1Muon('readL1Muon')
    alg.OutputLevel          = outputLevel
    alg.debug                = outputDebug
    alg.debugHits            = False
    alg.printRpcIds          = False
    alg.readRpcPrd           = True
    alg.readRpcRdo           = True
    alg.configCutsMuon       = getRPCAnalysisCuts_Muon()
    alg.inputVecMuon         = 'm_muon_'

    if writeGeo:
        alg.fileRpcGeometry      = 'rpc_geometry.txt'
        alg.fileRpcGeometryCheck = 'rpc_geometry_check.txt'
        alg.fileRpcPanelIds      = 'rpc_panel_ids.txt'

    alg.extrapolatorTool  = extrapolator
    alg.geometryTool      = geometry

    return alg

#======================================================================================
def getReadTrack(ToolSvc, input_name, stream):

    ''' Process muons - MuonSelectionTool requires variables not stored with EGAM1 so it is disabled '''

    outputLevel = 3
    outputDebug = False

    extrapolator = conf.Ath__L1MuonExtrapolator('IDTrackRPCExtrapolator')
    extrapolator.OutputLevel                      = outputLevel
    extrapolator.debug                            = outputDebug
    extrapolator.selectTrackExtrapolationValid    = True
    extrapolator.selectTrackExtrapolationInBounds = True
    extrapolator.useAODParticle                   = True


    alg = conf.Ath__ReadTrack('%s_readTrack' %input_name)
    alg.inputContainerName = input_name
    alg.outputVectorName   = 'm_id_track_'
    alg.printAuxVars       = False
    alg.debug              = outputDebug
    alg.OutputLevel        = outputLevel
    alg.outputStream       = stream

    alg.auxVars            = getTrackAuxVars()
    alg.configTrackCuts    = getAnalysisCuts_Track()    
    alg.extrapolatorTool   = extrapolator

    return alg

#======================================================================================
def getMuonAuxVars(option=''):

    ignrVars = [('ET_Core'                                              , 'Float'),
                ('ET_EMCore'                                            , 'Float'),
                ('ET_HECCore'                                           , 'Float'),
                ('ET_TileCore'                                          , 'Float'),
                ('EnergyLoss'                                           , 'Float'),
                ('EnergyLossSigma'                                      , 'Float'),
                ('charge'                                               , 'Short'),
                ('etaLayer1Hits'                                        , 'UInt'),
                ('etaLayer1Holes'                                       , 'UInt'),
                ('etaLayer1RPCHits'                                     , 'UInt'),
                ('etaLayer1RPCHoles'                                    , 'UInt'),
                ('etaLayer2Hits'                                        , 'UInt'),
                ('etaLayer2Holes'                                       , 'UInt'),
                ('etaLayer2RPCHits'                                     , 'UInt'),
                ('etaLayer2RPCHoles'                                    , 'UInt'),
                ('etaLayer3Hits'                                        , 'UInt'),
                ('etaLayer3Holes'                                       , 'UInt'),
                ('etaLayer3RPCHits'                                     , 'UInt'),
                ('etaLayer3RPCHoles'                                    , 'UInt'),
                ('etaLayer4Hits'                                        , 'UInt'),
                ('etaLayer4Holes'                                       , 'UInt'),
                ('etaLayer4RPCHits'                                     , 'UInt'),
                ('etaLayer4RPCHoles'                                    , 'UInt'),
                ('extendedClosePrecisionHits'                           , 'UInt'),
                ('extendedLargeHits'                                    , 'UInt'),
                ('extendedLargeHoles'                                   , 'UInt'),
                ('extendedOutBoundsPrecisionHits'                       , 'UInt'),
                ('extendedSmallHits'                                    , 'UInt'),
                ('extendedSmallHoles'                                   , 'UInt'),
                ('innerClosePrecisionHits'                              , 'UInt'),
                ('innerLargeHits'                                       , 'UInt'),
                ('innerLargeHoles'                                      , 'UInt'),
                ('innerOutBoundsPrecisionHits'                          , 'UInt'),
                ('innerSmallHits'                                       , 'UInt'),
                ('innerSmallHoles'                                      , 'UInt'),
                ('middleClosePrecisionHits'                             , 'UInt'),
                ('middleLargeHits'                                      , 'UInt'),
                ('middleLargeHoles'                                     , 'UInt'),
                ('middleOutBoundsPrecisionHits'                         , 'UInt'),
                ('middleSmallHits'                                      , 'UInt'),
                ('middleSmallHoles'                                     , 'UInt'),
                ('msOuterMatchDOF'                                      , 'Int'),
                ('numberOfPhiHoleLayers'                                , 'UInt'),
                ('numberOfPhiLayers'                                    , 'UInt'),
                ('numberOfTriggerEtaHoleLayers'                         , 'UInt'),
                ('numberOfTriggerEtaLayers'                             , 'UInt'),
                ('outerClosePrecisionHits'                              , 'UInt'),
                ('outerLargeHits'                                       , 'UInt'),
                ('outerLargeHoles'                                      , 'UInt'),
                ('outerOutBoundsPrecisionHits'                          , 'UInt'),
                ('outerSmallHits'                                       , 'UInt'),
                ('outerSmallHoles'                                      , 'UInt'),
                ('phiLayer1Hits'                                        , 'UInt'),
                ('phiLayer1Holes'                                       , 'UInt'),
                ('phiLayer1RPCHits'                                     , 'UInt'),
                ('phiLayer1RPCHoles'                                    , 'UInt'),
                ('phiLayer2Hits'                                        , 'UInt'),
                ('phiLayer2Holes'                                       , 'UInt'),
                ('phiLayer2RPCHits'                                     , 'UInt'),
                ('phiLayer2RPCHoles'                                    , 'UInt'),
                ('phiLayer3Hits'                                        , 'UInt'),
                ('phiLayer3Holes'                                       , 'UInt'),
                ('phiLayer3RPCHits'                                     , 'UInt'),
                ('phiLayer3RPCHoles'                                    , 'UInt'),
                ('phiLayer4Hits'                                        , 'UInt'),
                ('phiLayer4Holes'                                       , 'UInt'),
                ('phiLayer4RPCHits'                                     , 'UInt'),
                ('phiLayer4RPCHoles'                                    , 'UInt'),
                ('primarySector'                                        , 'UInt'),
                ('secondarySector'                                      , 'UInt'),
                ]

    saveVars = [('allAuthors'                                           , 'UInt'),
                ('author'                                               , 'UInt'),
                ('muonType'                                             , 'UInt'),
                ('quality'                                              , 'UInt'),
                ('ptvarcone20'                                          , 'Float'),
                ('ptvarcone30'                                          , 'Float'),
                ('topoetcone20'                                         , 'Float'),
                ('topoetcone30'                                         , 'Float'),
                ('scatteringCurvatureSignificance'                      , 'Float'),
                ('scatteringNeighbourSignificance'                      , 'Float'),
                ('momentumBalanceSignificance'                          , 'Float'),
                ('msInnerMatchChi2'                                     , 'Float'),
                ('msInnerMatchDOF'                                      , 'Int'),
                ('numberOfGoodPrecisionLayers'                          , 'UInt'),
                ('numberOfPrecisionLayers'                              , 'UInt'),
                ('numberOfPrecisionHoleLayers'                          , 'UInt'),
                ]

    outVars = []
    
    for v in saveVars:
        outVars += ['%s:type=%s' %(v[0], v[1])]

    return outVars

#======================================================================================
def getTrackAuxVars(option=''):

    auxVars = ['numberOfPrecisionHoleLayers:                  type=Short',
               'numberOfPrecisionLayers:                      type=Short',
               'expectInnermostPixelLayerHit:                 type=Short',
               'expectNextToInnermostPixelLayerHit:           type=Short',
               'numberOfInnermostPixelLayerHits:              type=Short',
               'numberOfInnermostPixelLayerSharedHits:        type=Short',
               'numberOfNextToInnermostPixelLayerHits:        type=Short',
               'numberOfNextToInnermostPixelLayerSharedHits:  type=Short',
               'numberOfPixelHits:                            type=Short',
               'numberOfPixelSharedHits:                      type=Short',
               'numberOfPixelHoles:                           type=Short',
               'numberOfSCTHits:                              type=Short',
               'numberOfSCTSharedHits:                        type=Short',
               'numberOfSCTHoles:                             type=Short',
               'numberDoF:                                    type=Float',               
               'chiSquared:                                   type=Float',
               'd0:                                           type=Float',
               'd0err:                                        type=Float',
               'theta:                                        type=Float',
               'z0:                                           type=Float',
               'z0err:                                        type=Float',
               ]

    return auxVars

#======================================================================================
def getRPCAnalysisCuts_Muon():
    
    cuts = ['Pt > 10.0e3',
            'Loose > 0']

    return []

#======================================================================================
def getAnalysisCuts_Muon():
    
    cuts = ['Pt > 10.0e3',
            'Abs[Eta] < 1.4',
            'Loose > 0']

    return []

#======================================================================================
def getAnalysisCuts_Track():
    
    cuts = ['Pt > 10.0e3',
            'numberOfPixelHits > 1',
            'numberOfSCTHits > 4',
            'Abs[Eta] < 1.2']

    return cuts
