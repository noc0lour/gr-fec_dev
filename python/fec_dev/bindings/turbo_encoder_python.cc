/*
 * Copyright 2024 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

/***********************************************************************************/
/* This file is automatically generated using bindtool and can be manually edited  */
/* The following lines can be configured to regenerate this file during cmake      */
/* If manual edits are made, the following tags should be modified accordingly.    */
/* BINDTOOL_GEN_AUTOMATIC(0)                                                       */
/* BINDTOOL_USE_PYGCCXML(0)                                                        */
/* BINDTOOL_HEADER_FILE(turbo_encoder.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(f39799b37edd42a624ea1e5cdef566c0)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/fec_dev/turbo_encoder.h>
// pydoc.h is automatically generated in the build directory
#include <turbo_encoder_pydoc.h>

void bind_turbo_encoder(py::module& m)
{

    using turbo_encoder = ::gr::fec_dev::turbo_encoder;


    py::class_<turbo_encoder, gr::fec::generic_encoder, std::shared_ptr<turbo_encoder>>(
        m, "turbo_encoder", D(turbo_encoder))

        .def_static("make",
             &turbo_encoder::make,
             py::arg("frame_size"),
             py::arg("standard") = ::gr::fec_dev::_enc_standard_t::LTE,
             py::arg("subencoder") = ::gr::fec_dev::_enc_sub_type_t::RSC,
             py::arg("buffered") = true,
             py::arg("polys") = std::vector<int>{011, 013},
             py::arg("trellis_size") = 8,
             D(turbo_encoder, make))


        .def("set_frame_size",
             &turbo_encoder::set_frame_size,
             py::arg("frame_size"),
             D(turbo_encoder, set_frame_size))


        .def("rate", &turbo_encoder::rate, D(turbo_encoder, rate))

        ;
}
