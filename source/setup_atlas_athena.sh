myrelease="21.0.83"

export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh

if [ -d '../build' ]
then
    pushd ../build
    acmSetup Athena,${myrelease}
    popd
fi

export MAKEFLAGS="-j4"

echo "---------------------------------------------------------------"
echo "Using Athena ${myrelease}"
echo "Set MAKEFLAGS=$MAKEFLAGS"
