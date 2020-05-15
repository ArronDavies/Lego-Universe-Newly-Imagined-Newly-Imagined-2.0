from uuid import uuid3, uuid4, NAMESPACE_DNS
from pyraknet.transports.abc import *
import Packets.Outgoing
from bitstream import *
from Enums import *

def LOAD_STATIC_ZONE(stream, conn, server):
	address = (str(conn.get_address()[0]), int(conn.get_address()[1]))
	uid = str(uuid3(NAMESPACE_DNS, str(address)))
	session = server.get_session(uid)

	response = WriteStream()
	Packets.Outgoing.CONSTRUCT_PACKET_HEADER.CONSTRUCT_PACKET_HEADER(0x53, 0x05, 0x02, response=response)

	for character in session.characters:
		if character.id == session.current_character_id:
			session.current_character = character
			break

	current_character = session.current_character

	response.write(c_ushort(int(current_character.last_zone)))
	response.write(c_ushort(0))
	response.write(c_ulong(0))

	if int(current_character.last_zone) == 0:
		zone_name = ZONE_IDS(1000).name
	else:
		zone_name = ZONE_IDS(int(current_character.last_zone)).name

	checksum = ZONE_CHECKSUMS[zone_name].value

	response.write(c_ulong(checksum)) # checksum
	response.write(c_ushort(0))  # ???

	response.write(c_float(ZONE_SPAWNPOINTS[int(current_character.last_zone)].x))  # x
	response.write(c_float(ZONE_SPAWNPOINTS[int(current_character.last_zone)].y))  # y
	response.write(c_float(ZONE_SPAWNPOINTS[int(current_character.last_zone)].z))  # z
	response.write(c_ulong(0))  # if activity world 4 else 0

	conn.send(response, reliability=Reliability.Reliable)