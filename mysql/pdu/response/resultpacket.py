import struct

from mysql.pdu.base import Packet
from mysql.pdu.response.okpacket import OkPacket
from mysql.pdu.response.errorpacket import ErrorPacket


class ResultPacket(Packet):
    
    def from_data(self, data):
        self.data = data
        first_byte = ord(data[0])

        if first_byte == 0x00:
            return OkPacket().from_data(data)
        elif first_byte == 0xff:
            return ErrorPacket().from_data(data)
        
        return self