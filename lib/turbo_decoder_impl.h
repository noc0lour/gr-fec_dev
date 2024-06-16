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
    // plug into the generic fec api
    void generic_work(const void* inbuffer, void* outbuffer) override;
    int get_output_size() override;
    int get_input_size() override;
    int get_input_item_size() override;
    const char* get_input_conversion() override;
    // const char* get_output_conversion();

    unsigned int d_max_frame_size;
    unsigned int d_frame_size;

public:
    turbo_decoder_impl(int frame_size);
    ~turbo_decoder_impl() override;

    bool set_frame_size(unsigned int frame_size) override;
    double rate() override;
};

// template<typename B = int, typename R = float>
// class Decoder_turbo_gr : public aff3ct::module::Decoder_turbo<B, R>
// {
//   public:
//     Decoder_turbo_gr(const int& K,
//                     const int& N,
//                     const int& n_ite,
//                     const aff3ct::module::Decoder_SISO<B, R>& siso_n,
//                     const aff3ct::module::Decoder_SISO<B, R>& siso_i,
//                     const aff3ct::module::Interleaver<R>& pi,
//                     const bool buffered_encoding = true);

//     virtual Decoder_turbo_gr<B, R>* clone() const override;
// };

} /* namespace fec */
} /* namespace gr */

#endif /* INCLUDED_FEC_turbo_DECODER_IMPL_H */
