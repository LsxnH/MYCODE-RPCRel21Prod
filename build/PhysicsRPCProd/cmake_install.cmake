# Install script for directory: /hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/InstallArea/x86_64-slc6-gcc62-opt")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/src/PhysicsRPCProd" TYPE DIRECTORY FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/" USE_SOURCE_PERMISSIONS REGEX "/\\.svn$" EXCLUDE REGEX "/\\.git$" EXCLUDE REGEX "/[^/]*\\~$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xDebugx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE OPTIONAL FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/lib/libPhysicsRPCProd.so.dbg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE MODULE OPTIONAL FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/lib/libPhysicsRPCProd.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libPhysicsRPCProd.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libPhysicsRPCProd.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/cvmfs/sft.cern.ch/lcg/releases/binutils/2.28-19981/x86_64-slc6-gcc62-opt/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libPhysicsRPCProd.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/PhysicsRPCProd" TYPE FILE OPTIONAL FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/PhysicsRPCProdConf.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process( COMMAND ${CMAKE_COMMAND} -E touch
      $ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/python/PhysicsRPCProd/__init__.py )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share" TYPE PROGRAM RENAME "CommonConfig_PhysicsAnpRPC.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/share/CommonConfig_PhysicsAnpRPC.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share" TYPE PROGRAM RENAME "L1RPC_NTUP_tf.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/share/L1RPC_NTUP_tf.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share" TYPE PROGRAM RENAME "readDESD_MCP_PhysicsAnpRPC.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/share/readDESD_MCP_PhysicsAnpRPC.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share" TYPE PROGRAM RENAME "readRAW_PhysicsAnpRPC.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/share/readRAW_PhysicsAnpRPC.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/PhysicsRPCProd" TYPE FILE RENAME "CommonConfig_PhysicsAnpRPC.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/share/CommonConfig_PhysicsAnpRPC.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/PhysicsRPCProd" TYPE FILE RENAME "L1RPC_NTUP_tf.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/share/L1RPC_NTUP_tf.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/PhysicsRPCProd" TYPE FILE RENAME "readDESD_MCP_PhysicsAnpRPC.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/share/readDESD_MCP_PhysicsAnpRPC.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/PhysicsRPCProd" TYPE FILE RENAME "readRAW_PhysicsAnpRPC.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/share/readRAW_PhysicsAnpRPC.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/PhysicsRPCProd" TYPE FILE RENAME "PhysicsRPCProdConfig.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/python/PhysicsRPCProdConfig.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/PhysicsRPCProd" TYPE FILE RENAME "PhysicsRPCProdNoise.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/python/PhysicsRPCProdNoise.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/PhysicsRPCProd" TYPE FILE RENAME "PhysicsRPCProdRead.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/python/PhysicsRPCProdRead.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/PhysicsRPCProd" TYPE FILE RENAME "__init__.py" FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/source/PhysicsRPCProd/python/__init__.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/PhysicsRPCProd" TYPE FILE FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/PhysicsRPCProdConfig.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/PhysicsRPCProd" TYPE FILE FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/PhysicsRPCProdNoise.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/PhysicsRPCProd" TYPE FILE FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/PhysicsRPCProdRead.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/PhysicsRPCProd" TYPE FILE FILES "/hepustc/home/hengli/testarea/RPCRel21Prod/build/x86_64-slc6-gcc62-opt/python/PhysicsRPCProd/__init__.pyc")
endif()

