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
                                               std::vector<int> polys,
                                               int trellis_size)
{
    return fec::generic_encoder::sptr(new turbo_encoder_impl(frame_size, standard, subencoder, buffered, polys, trellis_size));
}

    /*
     * The private constructor
     */
    turbo_encoder_impl::turbo_encoder_impl(int frame_size,
                                           enc_standard_t standard,
                                           enc_sub_type_t subencoder,
                                           bool buffered,
                                           std::vector<int> polys,
                                           int trellis_size)
        : generic_encoder("turbo_encoder"),
        d_max_frame_size(frame_size),
        d_trellis_size(trellis_size)
    {
        set_frame_size(frame_size);

        int N_rsc = 2 * (frame_size+std::log2(trellis_size));
        d_enco_n = std::make_shared<aff3ct::module::Encoder_RSC_generic_sys<>>(frame_size, N_rsc, buffered, polys);
        d_enco_i = std::make_shared<aff3ct::module::Encoder_RSC_generic_sys<>>(frame_size, N_rsc, buffered, polys);
        
        d_interleaver_core = std::make_shared<aff3ct::tools::Interleaver_core_LTE<>>(frame_size);
        d_pi = std::make_shared<aff3ct::module::Interleaver<int32_t>>(*d_interleaver_core);

        std::cout << "Creating d_encoder" << std::endl;
        d_encoder = std::make_unique<aff3ct::module::Encoder_turbo<>>(frame_size, d_output_size, *d_enco_n, *d_enco_i, *d_pi);
        std::cout << "d_encoder created successfully" << std::endl;

        // Call a method to verify initialization
        try {
            std::cout << "Encoder tail_length: " << d_encoder->tail_length() << std::endl;
        }
        catch (const std::exception &e) {
            std::cerr << "Exception during method call: " << e.what() << std::endl;
        }
}

/*
* Our virtual destructor.
*/
turbo_encoder_impl::~turbo_encoder_impl()
{
}

int turbo_encoder_impl::get_output_size() { return d_output_size; }
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
    d_output_size = 3*frame_size + 4*int(std::log2(d_trellis_size));

    return ret;
}

double turbo_encoder_impl::rate() { return d_frame_size / d_output_size; }

void turbo_encoder_impl::generic_work(const void* inbuffer, void* outbuffer)
{
    std::cout << "turbo_encoder_impl::generic_work" << std::endl;
    const int* in = (const int*)inbuffer;
    int* out = (int*)outbuffer;

    std::cout << "Address out: " << static_cast<const void*>(out) << std::endl;

    try {
        std::cout << "calling d_encoder->tail_length() " << d_encoder->tail_length() << std::endl;
        d_encoder->encode(in, out);
        std::cout << "Address out: " << static_cast<const void*>(out) << std::endl;
    }
    catch (const std::exception &e) {
        std::cerr << "Exception during encode: " << e.what() << std::endl;
    }
    std::cout << "end of turbo_encoder_impl::generic_work" << std::endl;
}

} /* namespace fec_dev */
} /* namespace gr */
