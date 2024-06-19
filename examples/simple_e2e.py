#!/usr/bin/env python3

import gnuradio
from gnuradio import gr
from gnuradio import blocks
from gnuradio import fec
from gnuradio import fec_dev
from gnuradio import digital
import numpy as np

import sys
import time


class simple_fg(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "Add two vectors")

        samp_rate = 32e3
        frame_size = 272
        puncpat = '11'

        self.source = blocks.vector_source_b((frame_size//15)*[0, 0, 1, 0, 3, 0, 7, 0, 15, 0, 31, 0, 63, 0, 127], False, 1, [])
        self.unpack = blocks.unpack_k_bits_bb(8)
        constellation = digital.constellation_bpsk()
        self.mapper = digital.constellation_encoder_bc(constellation)
        self.enc_turbo = enc_turbo = fec_dev.turbo_encoder.make(frame_size * 8)
        self.fec_encoder = fec.encoder(enc_turbo, input_item_size=gr.sizeof_char, output_item_size=gr.sizeof_char)
        self.dec_turbo = dec_turbo = fec_dev.turbo_decoder.make(frame_size * 8)
        self.fec_decoder = fec.decoder(dec_turbo, input_item_size=gr.sizeof_float, output_item_size=gr.sizeof_char)
        self.char_to_float = blocks.char_to_float(1,1)
        self.complex_to_real = blocks.complex_to_real(1)
        self.throttle = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )

        self.src_b = blocks.vector_sink_b()
        self.enc_b = blocks.vector_sink_b()
        self.dec_b = blocks.vector_sink_b()


        self.connect((self.source, 0),(self.throttle,0))
        self.connect((self.throttle, 0),(self.unpack, 0))
        self.connect((self.unpack, 0), (self.fec_encoder, 0)),
        self.connect((self.fec_encoder), (self.mapper, 0))
        self.connect((self.mapper,0), (self.complex_to_real,0))
        self.connect((self.complex_to_real, 0), (self.fec_decoder, 0))

        self.connect((self.source, 0),(self.src_b, 0))
        self.connect((self.fec_encoder, 0),(self.enc_b, 0))
        self.connect((self.fec_decoder, 0),(self.dec_b, 0))

def main():
    fg = simple_fg()
    fg.start()
    fg.wait()
    print(fg.src_b.data())
    print(fg.enc_b.data())
    print(fg.dec_b.data())

    return True

if __name__ == "__main__":
    sys.exit(not main())


