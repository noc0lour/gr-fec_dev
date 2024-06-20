/* -*- c++ -*- */
/*
 * Copyright 2014 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

#ifndef INCLUDED_FEC_TURBO_DECODER_IMPL_H
#define INCLUDED_FEC_TURBO_DECODER_IMPL_H

#include <gnuradio/fec_dev/turbo_decoder.h>
#include <map>
#include <string>
#include <aff3ct.hpp>

namespace gr {
namespace fec_dev {

class FEC_API turbo_decoder_impl : public turbo_decoder
{
private:
    int get_output_size() override;
    int get_input_size() override;
    int get_input_item_size() override;
    const char* get_input_conversion() override;

    unsigned int d_max_frame_size;
    unsigned int d_frame_size;
    int d_input_size;
    int d_trellis_size;
    std::shared_ptr<aff3ct::tools::Interleaver_core<>> d_interleaver_core;
    std::unique_ptr<aff3ct::module::Decoder_turbo<>> d_decoder;

public:
    turbo_decoder_impl(int frame_size,
                      enc_standard_t standard=LTE,
                      enc_sub_type_t subencoder=RSC,
                      bool buffered=true,
                      std::vector<int> polys={013,015},
                      int trellis_size = 8,
                      int n_iterations = 6);
    ~turbo_decoder_impl() override;

    bool set_frame_size(unsigned int frame_size) override;
    double rate() override;
    void generic_work(const void* inbuffer, void* outbuffer) override;
};

} /* namespace fec */
} /* namespace gr */

#endif /* INCLUDED_FEC_turbo_DECODER_IMPL_H */
