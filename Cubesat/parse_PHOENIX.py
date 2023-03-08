#!/usr/bin/env python
import binascii
import pprint
import sys
import json


def app_info(help_flag):
    """ Display information """

    VER = "0.0.4"
    USAGE = f"Usage: python {sys.argv[0]} [-h | -v] | file_name]"
    CONTACT = "questions/feedback -> ognyan@endurosat.com"
    HELP = """
    =============================
    Parse PHOENIX Mode UHF Beacon
    =============================
    Parses PHOENIX Mode [RAW HEX] AX25 packets. 

        -h      Help, shows this text
        -v      Version, shows the version

        file_name   The .bin/.txt file name of beacon data in the same dir.

        {}
        
    NOTE: Output is a dict.
        
    -----------------------------
    {}

    """.format(USAGE, CONTACT)

    if help_flag == True:
        return HELP
    else:
        return VER


def format_temp(temp_val):
    """ Format temperature values depending on sign. """
    if temp_val < 32768:
        formatted_temp_val = temp_val * 0.00390625
    else:
        formatted_temp_val = (((temp_val >> 4) - 1) ^ 0xFFF) * (-0.0625)

    return formatted_temp_val


def impl_struct(frame):
    """ Implement beacon structure"""

    payload = frame[2]
    head = [int((payload[2] + payload[1]), 16)]
    v_batt = [int((payload[4] + payload[3]), 16)]
    i_batt = [int((payload[6] + payload[5]), 16)]
    v_bcr = [int((payload[8] + payload[7]), 16)]
    i_bcr = [int((payload[10] + payload[9]), 16)]
    v_x = [int((payload[12] + payload[11]), 16)]
    i_xm = [int((payload[14] + payload[13]), 16)]
    i_xp = [int((payload[16] + payload[15]), 16)]
    v_y = [int((payload[18] + payload[17]), 16)]
    i_ym = [int((payload[20] + payload[19]), 16)]
    i_yp = [int((payload[22] + payload[21]), 16)]
    v_z = [int((payload[24] + payload[23]), 16)]
    i_zm = [int((payload[26] + payload[25]), 16)]
    i_zp = [int((payload[28] + payload[27]), 16)]
    i_3V3 = [int((payload[30] + payload[29]), 16)]
    i_5V = [int((payload[32] + payload[31]), 16)]
    t_mcu = [int((payload[34] + payload[33]), 16)]
    t_batt1 = [int((payload[36] + payload[35]), 16)]
    t_batt2 = [int((payload[38] + payload[37]), 16)]
    t_batt3 = [int((payload[40] + payload[39]), 16)]
    t_batt4 = [int((payload[42] + payload[41]), 16)]
    cnd_input = [int((payload[44] + payload[43]), 16)]
    cnd_output1 = [int((payload[46] + payload[45]), 16)]
    cnd_output2 = [int((payload[48] + payload[47]), 16)]
    por_cycles = [int((payload[50] + payload[49]), 16)]
    v_under = [int((payload[52] + payload[51]), 16)]
    v_short = [int((payload[54] + payload[53]), 16)]
    v_overtemp = [int((payload[56] + payload[55]), 16)]
    t_max1 = [int((payload[58] + payload[57]), 16)]
    t_min1 = [int((payload[60] + payload[59]), 16)]
    def1 = [int((payload[62] + payload[61]), 16)]
    def2 = [int((payload[64] + payload[63]), 16)]
    r_batt = [int((payload[66] + payload[65]), 16)]
    v_ideal_batt = [int((payload[68] + payload[67]), 16)]
    UHFAnt = [(payload[72] + payload[71] + payload[70] + payload[69])]
    scw = [int((payload[74] + payload[73]), 16)]

    # Identifiers
    CONOPS_MODE_PHOENIX = int("0xa1c9", 16)  # CONOPS
    print(f'CONOPS_MODE_PHOENIX   ==> {CONOPS_MODE_PHOENIX}')
    CONOPS_MODE_OTHER = int("0xe7a9", 16)  # CONOPS
    ANTENNA_REGISTERS_OFF = "deafbeef"  # ANTENNA

    # Units
    units = {
        "miliV": "[mV]",
        "volt": "[V]",
        "amp": "[A]",
        "miliamp": "[mA]",
        "centigrade": "[°C]",
        "ohm": "[Ω]",
    }

    frame_struct = {
        "ConOps magic num ID": [CONOPS_MODE_PHOENIX if head[0] == CONOPS_MODE_PHOENIX else "Other"],
        "EPS I Battery Voltage": [float(v_batt[0] * 0.0023394775), units["volt"]],
        "EPS I Battery Current": [float(i_batt[0] * 3.0517578), units["miliamp"]],
        "BCR Voltage": [float(v_bcr[0] * 0.0023394775), units["volt"]],
        "BCR Current": [float(i_bcr[0] * 1.5258789), units["miliamp"]],
        "SOL PAN X V": [float(v_x[0] * 0.0024414063), units["volt"]],
        "SOL PAN X- Current": [float(i_xm[0] * 0.6103516), units["miliamp"]],
        "SOL PAN X+ Current": [float(i_xp[0] * 0.6103516), units["miliamp"]],
        "SOL PAN Y V": [float(v_y[0] * 0.0024414063), units["volt"]],
        "SOL PAN Y- Current": [float(i_ym[0] * 0.6103516), units["miliamp"]],
        "SOL PAN Y+ Current": [float(i_yp[0] * 0.6103516), units["miliamp"]],
        "SOL PAN Z V": [float(v_z[0] * 0.0024414063), units["volt"]],
        "SOL PAN Z- Current": [float(i_zm[0] * 0.6103516), units["miliamp"]],
        "SOL PAN Z+ Current": [float(i_zp[0] * 0.6103516), units["miliamp"]],
        "3.3V Bus Current": [float(i_3V3[0] * 2.0345052), units["miliamp"]],
        "5V   Bus Current": [float(i_5V[0] * 2.0345052), units["miliamp"]],
        "MCU Temperature": [(float(((t_mcu[0] * 0.0006103516) - 0.986) / 0.00355))/10, units["centigrade"]],
        "Battery Cell 1 Temp": [(float(format_temp(t_batt1[0])))/10, units["centigrade"]],
        "Battery Cell 2 Temp": [(float(format_temp(t_batt2[0])))/10, units["centigrade"]],
        "Battery Cell 3 Temp": ['{:010.5f}'.format(round((float(format_temp(t_batt3[0])))/10, 5)), units["centigrade"]],
        "Battery Cell 4 Temp": ['{:010.5f}'.format(round((float(format_temp(t_batt4[0])))/10, 5)), units["centigrade"]],
        "Input Condition": [hex(cnd_input[0])],
        "Output Conditions 1": [hex(cnd_output1[0])],
        "Output Conditions 2": [hex(cnd_output2[0])],
        "Power ON Cycle Counter": [por_cycles[0]],
        "Under Voltage Cond Counter": [hex(v_under[0])],
        "Short Circuit Cond Counter": [hex(v_short[0])],
        "Over Temp Cond Counter": [hex(v_overtemp[0])],
        "Battpack1 temp sensor 1 max temp": [(float(format_temp(t_max1[0])))/10, units["centigrade"]],
        "Battpack1 temp sensor 1 min temp": [(float(format_temp(t_min1[0])))/10, units["centigrade"]],
        "Default Vals LUPs & fastcharge": [hex(def1[0])],
        "Default Vals OUTs 1:6": [hex(def2[0])],
        "Battery Internal Resistance": [float(r_batt[0] * 1.4972656), units["ohm"]],
        "Battery Ideal Voltage": [float(v_ideal_batt[0] * 0.0023394775), units["volt"]],
        "UHF Antenna Registers": [
            ("0x{}".format(str(UHFAnt[0]).upper())) if UHFAnt[0] == ANTENNA_REGISTERS_OFF else ("ANTENNA: {CONNECTED - DEPLOYED} - 0x" + str(UHFAnt[0]))],
        "UHF Status Control Word": [hex(scw[0])],
    }
    return frame_struct


def format_frame(input_file):
    """ Preliminary formatting of beacon frame """
    frame_string = input_file
    frame_array = []
    header_bytes = []
    size_bytes = []
    payload_bytes = []

    for i, j in zip(frame_string[::2], frame_string[1::2]):
        frame_array.append(i + j)

    # Header Bytes
    header_bytes = frame_array[0]

    # Size Bytes
    size_bytes = frame_array[1]

    # Payload Bytes
    payload_bytes = frame_array[1:len(frame_array)]

    payload_bytes_string = ('').join(payload_bytes)

    if len(frame_array) > 106:
        bytestream = separate_frames(frame_array)
        for packet in bytestream:
            start_frame_bytes_index = packet.find("f0c9")
            payload_bytes_cut = []
            for i, j in zip(packet[::2], packet[1::2]):
                payload_bytes_cut.append(i + j)

            payload_bytes_cut = payload_bytes_cut[start_frame_bytes_index // 2:]
            frame_parts = [header_bytes, size_bytes, payload_bytes_cut]
            impl_struct(frame_parts)
    else:
        start_frame_bytes_index = payload_bytes_string.find("f0c9")

        payload_bytes_cut = payload_bytes[start_frame_bytes_index // 2:]

        frame_parts = [header_bytes, size_bytes, payload_bytes_cut]
        return impl_struct(frame_parts)


def separate_frames(frames):
    """ Separates telemetry frames in the case of more than 1 frame in a file """

    frames_input = frames
    conjoined_data = ('').join(frames_input)
    n_packets = conjoined_data.count('efbeafde')

    frames_list = []

    for i in range(n_packets):
        conjoined_data_deafbeef_index = conjoined_data.find("efbeafde")
        frame = conjoined_data[:conjoined_data_deafbeef_index + 18]
        frames_list.append(frame)
        conjoined_data = conjoined_data[conjoined_data_deafbeef_index + 18:]
    return frames_list


def main(beacon):
    frame = format_frame(beacon)
    return process_dic(frame)

def process_dic(dic):
    dic1 = {}
    for key,value in dic.items():
        dic1[key] = value[0]
    #print(dic1)
    return dic1


if __name__ == '__main__':
    main(
        '8AA68EA66062E0A29AA496AEA8E103F0C9A1FA052400040002000300030003000200030003000200030002000E0006004E062006A0060180018001001B3CAB000800773400000000102210F203005B008B000406EFBEAFDE4333000000'.lower())
