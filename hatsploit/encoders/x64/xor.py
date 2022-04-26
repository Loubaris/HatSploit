#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.encoder import Encoder

from pex.string import StringTools
from pex.assembler import AssemblerTools


class HatSploitEncoder(Encoder, StringTools, AssemblerTools):
    details = {
        'Name': "x64 XOR Encoder",
        'Encoder': "x64/xor",
        'Authors': [
            'Ivan Nikolsky (enty8080) - encoder developer'
        ],
        'Description': "Simple XOR encoder for x64.",
        'Architecture': "x64"
    }

    options = {
        'KEY': {
            'Description': "8-byte key to encode.",
            'Value': "P@ssW0rd",
            'Type': None,
            'Required': True
        }
    }

    def run(self):
        key = self.parse_options(self.options)
        count = - int((len(self.payload) - 1 / len(key)) + 1)

        decoder = (
            b"\x48\x31\xc9"
            b"\x48\x81\xe9" + self.pack_integer(count) +
            b"\x48\x8d\x05\xef\xff\xff\xff"
            b"\x48\xbb" + key.encode() +
            b"\x48\x31\x58\x27"
            b"\x48\x2d\xf8\xff\xff\xff"
            b"\xe2\xf4"
        )

        return decoder + self.xor_key_bytes(self.payload, key)
