# Generated by lcg_generate_env...
if [ -z "${LCG_RELEASE_BASE}" ]; then
   export LCG_RELEASE_BASE=/cvmfs/atlas.cern.ch/repo/sw/software/21.0/sw/lcg/releases
fi
if [ -z "${LCG_PLATFORM}" ]; then
   export LCG_PLATFORM=x86_64-slc6-gcc62-opt
fi
export ROOTSYS=${LCG_RELEASE_BASE}/LCG_88/ROOT/6.08.06/x86_64-slc6-gcc62-opt
export PYTHONHOME=${LCG_RELEASE_BASE}/LCG_88/Python/2.7.13/x86_64-slc6-gcc62-opt
if [ -z "${GAUDI_ROOT}" ]; then
   export GAUDI_ROOT=/cvmfs/atlas.cern.ch/repo/sw/software/21.0/GAUDI/21.0.83/InstallArea/x86_64-slc6-gcc62-opt
fi
if [ -z "${JOBOPTSEARCHPATH}" ]; then
   export JOBOPTSEARCHPATH=${GAUDI_ROOT}/jobOptions
else
   export JOBOPTSEARCHPATH=${GAUDI_ROOT}/jobOptions:${JOBOPTSEARCHPATH}
fi
if [ -z "${DATAPATH}" ]; then
   export DATAPATH=${GAUDI_ROOT}/share
else
   export DATAPATH=${GAUDI_ROOT}/share:${DATAPATH}
fi
if [ -z "${PYTHONPATH}" ]; then
   export PYTHONPATH=${ROOTSYS}/lib:${LCG_RELEASE_BASE}/LCG_88/CORAL/3_1_8/x86_64-slc6-gcc62-opt/python:${LCG_RELEASE_BASE}/LCG_88/CORAL/3_1_8/x86_64-slc6-gcc62-opt/lib:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/AthenaExternals/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/python:${GAUDI_ROOT}/python:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/Athena/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/python
else
   export PYTHONPATH=${ROOTSYS}/lib:${LCG_RELEASE_BASE}/LCG_88/CORAL/3_1_8/x86_64-slc6-gcc62-opt/python:${LCG_RELEASE_BASE}/LCG_88/CORAL/3_1_8/x86_64-slc6-gcc62-opt/lib:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/AthenaExternals/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/python:${GAUDI_ROOT}/python:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/Athena/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/python:${PYTHONPATH}
fi
if [ -z "${PATH}" ]; then
   export PATH=${ROOTSYS}/bin:${LCG_RELEASE_BASE}/LCG_88/CORAL/3_1_8/x86_64-slc6-gcc62-opt/bin:${PYTHONHOME}/bin:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/AthenaExternals/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/bin:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/Athena/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/bin
else
   export PATH=${ROOTSYS}/bin:${LCG_RELEASE_BASE}/LCG_88/CORAL/3_1_8/x86_64-slc6-gcc62-opt/bin:${PYTHONHOME}/bin:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/AthenaExternals/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/bin:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/Athena/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/bin:${PATH}
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then
   export LD_LIBRARY_PATH=${LCG_RELEASE_BASE}/LCG_88/Boost/1.62.0/x86_64-slc6-gcc62-opt/lib::${LCG_RELEASE_BASE}/LCG_88/Boost/1.62.0/x86_64-slc6-gcc62-opt/lib::::${ROOTSYS}/lib:${LCG_RELEASE_BASE}/LCG_88/tbb/44_20160413/x86_64-slc6-gcc62-opt/lib:${PYTHONHOME}/lib:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/AthenaExternals/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/lib:${LCG_RELEASE_BASE}/LCG_88/CORAL/3_1_8/x86_64-slc6-gcc62-opt/lib:${GAUDI_ROOT}/lib:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/Athena/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/lib
else
   export LD_LIBRARY_PATH=${LCG_RELEASE_BASE}/LCG_88/Boost/1.62.0/x86_64-slc6-gcc62-opt/lib::${LCG_RELEASE_BASE}/LCG_88/Boost/1.62.0/x86_64-slc6-gcc62-opt/lib::::${ROOTSYS}/lib:${LCG_RELEASE_BASE}/LCG_88/tbb/44_20160413/x86_64-slc6-gcc62-opt/lib:${PYTHONHOME}/lib:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/AthenaExternals/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/lib:${LCG_RELEASE_BASE}/LCG_88/CORAL/3_1_8/x86_64-slc6-gcc62-opt/lib:${GAUDI_ROOT}/lib:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/Athena/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/lib:${LD_LIBRARY_PATH}
fi
if [ -z "${ROOT_INCLUDE_PATH}" ]; then
   export ROOT_INCLUDE_PATH=${LCG_RELEASE_BASE}/LCG_88/Boost/1.62.0/x86_64-slc6-gcc62-opt/include/boost-1_62::${LCG_RELEASE_BASE}/LCG_88/Boost/1.62.0/x86_64-slc6-gcc62-opt/include/boost-1_62::::${ROOTSYS}/include::${LCG_RELEASE_BASE}/LCG_88/tbb/44_20160413/x86_64-slc6-gcc62-opt/include::${PYTHONHOME}/include/python2.7::${LCG_RELEASE_BASE}/LCG_88/eigen/3.2.9/x86_64-slc6-gcc62-opt/include/eigen3::/cvmfs/atlas.cern.ch/repo/sw/software/21.0/AthenaExternals/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/include::${LCG_RELEASE_BASE}/LCG_88/CORAL/3_1_8/x86_64-slc6-gcc62-opt/include::/cvmfs/atlas.cern.ch/repo/sw/software/21.0/AthenaExternals/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/include:${GAUDI_ROOT}/include:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/Athena/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/include
else
   export ROOT_INCLUDE_PATH=${LCG_RELEASE_BASE}/LCG_88/Boost/1.62.0/x86_64-slc6-gcc62-opt/include/boost-1_62::${LCG_RELEASE_BASE}/LCG_88/Boost/1.62.0/x86_64-slc6-gcc62-opt/include/boost-1_62::::${ROOTSYS}/include::${LCG_RELEASE_BASE}/LCG_88/tbb/44_20160413/x86_64-slc6-gcc62-opt/include::${PYTHONHOME}/include/python2.7::${LCG_RELEASE_BASE}/LCG_88/eigen/3.2.9/x86_64-slc6-gcc62-opt/include/eigen3::/cvmfs/atlas.cern.ch/repo/sw/software/21.0/AthenaExternals/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/include::${LCG_RELEASE_BASE}/LCG_88/CORAL/3_1_8/x86_64-slc6-gcc62-opt/include::/cvmfs/atlas.cern.ch/repo/sw/software/21.0/AthenaExternals/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/include:${GAUDI_ROOT}/include:/cvmfs/atlas.cern.ch/repo/sw/software/21.0/Athena/21.0.83/InstallArea/x86_64-slc6-gcc62-opt/include:${ROOT_INCLUDE_PATH}
fi