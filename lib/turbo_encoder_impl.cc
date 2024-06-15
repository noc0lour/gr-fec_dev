/* -*- c++ -*- */
/*
 * Copyright 2024 gr-fec_dev author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "turbo_encoder_impl.h"
#include <gnuradio/fec/generic_encoder.h>
#include <aff3ct.hpp>
#include <volk/volk.h>
#include <sstream>

namespace gr {
namespace fec_dev {

fec::generic_encoder::sptr turbo_encoder::make(int frame_size,
                                               enc_standard_t standard,
                                               enc_sub_type_t subencoder,
                                               bool buffered,
                                               std::vector<int> polys)
{
    return fec::generic_encoder::sptr(new turbo_encoder_impl(frame_size, standard, subencoder, buffered, polys));
}

/*
* The private constructor
*/
turbo_encoder_impl::turbo_encoder_impl(int frame_size,
                                       enc_standard_t standard,
                                       enc_sub_type_t subencoder,
                                       bool buffered,
                                       std::vector<int> polys)
    : generic_encoder("turbo_encoder")
{
    d_max_frame_size = frame_size;
    set_frame_size(frame_size);
}

/*
* Our virtual destructor.
*/
turbo_encoder_impl::~turbo_encoder_impl()
{
}

int turbo_encoder_impl::get_output_size() { 
    return d_frame_size * 3;
}

int turbo_encoder_impl::get_input_size() { return d_frame_size; }

bool turbo_encoder_impl::set_frame_size(unsigned int frame_size)
{
    bool ret = true;
    if (frame_size > d_max_frame_size) {
        d_logger->info("tried to set frame to {:d}; max possible is {:d}",
                    frame_size,
                    d_max_frame_size);
        frame_size = d_max_frame_size;
        ret = false;
    }

    d_frame_size = frame_size;

    return ret;
}

double turbo_encoder_impl::rate() { return 1.0; }

void turbo_encoder_impl::generic_work(const void* inbuffer, void* outbuffer)
{
    // const unsigned char* in = (const unsigned char*)inbuffer;
    // unsigned char* out = (unsigned char*)outbuffer;
    // memcpy(out, in, d_frame_size * sizeof(char));

    const int* in = (const int*)inbuffer;
    int* out = (int*)outbuffer;

    int K = get_input_size();
    int N = get_output_size();
    auto enco_n = aff3ct::module::Encoder<>(K, N);
    auto enco_i = aff3ct::module::Encoder<>(K, N);

    aff3ct::tools::Interleaver_core_random<> core(N);
	aff3ct::module::Interleaver<int32_t> pi(core);

    auto encoder = std::unique_ptr<aff3ct::module::Encoder_turbo<>>(new aff3ct::module::Encoder_turbo<>(K, N, enco_n, enco_i, pi));;
    encoder->encode(in, out);
}

} /* namespace fec_dev */
} /* namespace gr */