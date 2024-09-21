#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "WorkDir::PhysicsRPCProd" for configuration "RelWithDebInfo"
set_property(TARGET WorkDir::PhysicsRPCProd APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(WorkDir::PhysicsRPCProd PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libPhysicsRPCProd.so"
  IMPORTED_NO_SONAME_RELWITHDEBINFO "TRUE"
  )

list(APPEND _IMPORT_CHECK_TARGETS WorkDir::PhysicsRPCProd )
list(APPEND _IMPORT_CHECK_FILES_FOR_WorkDir::PhysicsRPCProd "${_IMPORT_PREFIX}/lib/libPhysicsRPCProd.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
