find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_FEC_DEV gnuradio-fec_dev)

FIND_PATH(
    GR_FEC_DEV_INCLUDE_DIRS
    NAMES gnuradio/fec_dev/api.h
    HINTS $ENV{FEC_DEV_DIR}/include
        ${PC_FEC_DEV_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_FEC_DEV_LIBRARIES
    NAMES gnuradio-fec_dev
    HINTS $ENV{FEC_DEV_DIR}/lib
        ${PC_FEC_DEV_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-fec_devTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_FEC_DEV DEFAULT_MSG GR_FEC_DEV_LIBRARIES GR_FEC_DEV_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_FEC_DEV_LIBRARIES GR_FEC_DEV_INCLUDE_DIRS)
