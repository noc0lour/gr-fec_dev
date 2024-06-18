#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Fecapi Decoders
# GNU Radio version: gac2244fa1

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
from gnuradio import digital
from gnuradio import fec
from gnuradio import fec_dev
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class fecapi_decoders(gr.top_block, Qt.QWidget):

    def __init__(self, frame_size=30, puncpat='11'):
        gr.top_block.__init__(self, "Fecapi Decoders", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fecapi Decoders")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fecapi_decoders")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Parameters
        ##################################################
        self.frame_size = frame_size
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.k = k = 7
        self.variable_cc_encoder_def_0 = variable_cc_encoder_def_0 = fec.cc_encoder_make(2048,7, 2, [79,109], 0, fec.CC_STREAMING, False)
        self.samp_rate = samp_rate = 50000
        self.enc_turbo = enc_turbo = fec_dev.turbo_encoder_make(272)
        self.enc_rep = enc_rep = fec.repetition_encoder_make((frame_size*8), 3)
        self.enc_dummy = enc_dummy = fec.dummy_encoder_make((frame_size*8))
        self.enc_ccsds = enc_ccsds = fec.ccsds_encoder_make((frame_size*8),0, fec.CC_TAILBITING)
        self.dec_turbo = dec_turbo = fec_dev.turbo_decoder.make(2048)
        self.dec_rep = dec_rep = fec.repetition_decoder.make((frame_size*8),3, 0.5)
        self.dec_dummy = dec_dummy = fec.dummy_decoder.make((frame_size*8))
        self.dec_cc = dec_cc = fec.cc_decoder.make((frame_size*8),k, rate, polys, 0, (-1), fec.CC_TAILBITING, False)
        self.constellation = constellation = digital.constellation_bpsk().base()
        self.constellation.set_npwr(1.0)

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            2048, #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0.set_y_axis(-0.5, 1.5)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Input', 'Dummy', 'Rep. (Rate=3)', 'CC (K=7, Rate=2)', 'CCSDS',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 0.6, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.fec_extended_encoder_1_0_0 = fec.extended_encoder(encoder_obj_list=enc_turbo, threading='ordinary', puncpat=puncpat)
        self.fec_extended_decoder_0_1_0 = fec.extended_decoder(decoder_obj_list=dec_turbo, threading= None, ann=None, puncpat=puncpat, integration_period=10000)
        self.digital_constellation_encoder_bc_0 = digital.constellation_encoder_bc(constellation)
        self.blocks_vector_source_x_0_1_0 = blocks.vector_source_b((frame_size//15)*[0, 0, 1, 0, 3, 0, 7, 0, 15, 0, 31, 0, 63, 0, 127], True, 1, [])
        self.blocks_unpack_k_bits_bb_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_char_to_float_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_0_0 = blocks.char_to_float(1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0_0_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_char_to_float_0_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.fec_extended_decoder_0_1_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_char_to_float_0_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.fec_extended_encoder_1_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0, 0), (self.blocks_char_to_float_0_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.digital_constellation_encoder_bc_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.fec_extended_decoder_0_1_0, 0), (self.blocks_unpack_k_bits_bb_0_0, 0))
        self.connect((self.fec_extended_encoder_1_0_0, 0), (self.digital_constellation_encoder_bc_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fecapi_decoders")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_frame_size(self):
        return self.frame_size

    def set_frame_size(self, frame_size):
        self.frame_size = frame_size
        self.blocks_vector_source_x_0_1_0.set_data((self.frame_size//15)*[0, 0, 1, 0, 3, 0, 7, 0, 15, 0, 31, 0, 63, 0, 127], [])

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_variable_cc_encoder_def_0(self):
        return self.variable_cc_encoder_def_0

    def set_variable_cc_encoder_def_0(self, variable_cc_encoder_def_0):
        self.variable_cc_encoder_def_0 = variable_cc_encoder_def_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_enc_turbo(self):
        return self.enc_turbo

    def set_enc_turbo(self, enc_turbo):
        self.enc_turbo = enc_turbo

    def get_enc_rep(self):
        return self.enc_rep

    def set_enc_rep(self, enc_rep):
        self.enc_rep = enc_rep

    def get_enc_dummy(self):
        return self.enc_dummy

    def set_enc_dummy(self, enc_dummy):
        self.enc_dummy = enc_dummy

    def get_enc_ccsds(self):
        return self.enc_ccsds

    def set_enc_ccsds(self, enc_ccsds):
        self.enc_ccsds = enc_ccsds

    def get_dec_turbo(self):
        return self.dec_turbo

    def set_dec_turbo(self, dec_turbo):
        self.dec_turbo = dec_turbo

    def get_dec_rep(self):
        return self.dec_rep

    def set_dec_rep(self, dec_rep):
        self.dec_rep = dec_rep

    def get_dec_dummy(self):
        return self.dec_dummy

    def set_dec_dummy(self, dec_dummy):
        self.dec_dummy = dec_dummy

    def get_dec_cc(self):
        return self.dec_cc

    def set_dec_cc(self, dec_cc):
        self.dec_cc = dec_cc

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation
        self.digital_constellation_encoder_bc_0.set_constellation(self.constellation)



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--frame-size", dest="frame_size", type=intx, default=30,
        help="Set Frame Size [default=%(default)r]")
    return parser


def main(top_block_cls=fecapi_decoders, options=None):
    if options is None:
        options = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(frame_size=options.frame_size)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
