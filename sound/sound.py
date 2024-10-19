# site:https://nerdparadise.com/programming/pythonwave
def push_int(byte_list, value, byte_length):
    while byte_length > 0:
        byte_list.append(chr(value & 255))
        value = value >> 8
        byte_length -= 1


def push_string(byte_list, value):
    length = len(value)
    i = 0
    while i < length:
        byte_list.append(value[i])
        i += 1


class ByteStream:
    def __init__(self, file):
        self.i = 0
        c = open(file, 'rb')
        self.data = c.read()
        c.close()
        self.length = len(self.data)

    def has_next(self):
        return self.i < self.length

    def next_byte(self):
        output = ord(self.data[self.i])
        self.i += 1
        return output

    def next_string(self, length):
        output = ''
        while length > 0:
            output = self.data[self.i]
            self.i += 1
            length -= 1
        return output

    def next_int(self, byte_length):
        if byte_length == 1:
            output = ord(self.data[self.i])
            self.i += 1
        elif byte_length == 2:
            output = (ord(self.data[self.i]) +
                      (ord(self.data[self.i + 1]) << 8))
            self.i += 2
        elif byte_length == 4:
            output = (ord(self.data[self.i]) +
                      (ord(self.data[self.i + 1]) << 8) +
                      (ord(self.data[self.i + 2]) << 16) +
                      (ord(self.data[self.i + 3]) << 24))
            self.i += 4
        else:
            # how did this happen?
            pass
        return output


def create_sound_from_file(filename):
    bs = ByteStream(filename)

    ignore = bs.next_string(4)  # "RIFF"
    ignore = bs.next_int(4)  # file size
    ignore = bs.next_string(4)  # "WAVE"
    ignore = bs.next_string(4)  # "fmt "
    excess = bs.next_int(4) - 16  # file header size
    ignore = bs.next_int(2)  # 1 for PCM

    channels = bs.next_int(2)  # num channels

    sps = bs.next_int(4)  # samples per second (e.g. 44100)

    ignore = bs.next_int(4)  # bytes per second

    ignore = bs.next_int(2)  # bytes per sample

    bps = bs.next_int(2)  # bits per sample

    while excess > 0:
        ignore = bs.next_char()
        excess -= 1

    ignore = bs.next_string(4)  # "data"
    ignore = bs.next_int(4)  # length of data

    bytes_per_sample = bps // 8

    samples = []
    for channel in range(channels):
        samples.append([])

    while bs.has_next():
        channel_i = 0
        while channel_i < channels:
            samples[channel_i].append(bs.next_int(bytes_per_sample))
            channel_i += 1

    s = Sound(len(samples[0]), sps, channels, bps)
    s.samples = samples
    return s


class Sound:

    def __init__(self, sample_count, samples_per_second, channels, bits_per_sample):
        self.sps = samples_per_second
        self.bps = bits_per_sample
        self.samples = []
        for i in range(channels):
            self.samples.append([0] * sample_count)

    def save_to_file(self, filename):
        output = []

        push_string(output, "RIFF")

        header = self.generate_header()
        data = self.generate_data()

        push_int(output, len(data) + 36, 4)

        output += header
        output += data

        c = open(filename, 'wb')
        c.write(''.join(output))
        c.close()

    def generate_header(self):
        output = []

        push_string(output, "WAVE")

        push_string(output, "fmt ")

        # Header size (16 bytes follow)
        push_int(output, 16, 4)

        # 1 (to indicate PCM. Not sure what other valid values are)
        push_int(output, 1, 2)

        # number of channels (stereo = 2, mono = 1)
        push_int(output, len(self.samples), 2)

        # samples per second
        push_int(output, self.sps, 4)

        # bytes per second (across all channels)
        push_int(output, self.bps / 8 * len(self.samples) * self.sps, 4)

        # bytes per sample across all channels
        push_int(output, self.bps / 8 * len(self.samples), 2)

        # bits per sample
        push_int(output, self.bps, 2)

        return output

    def generate_data(self):
        output = []

        samples = self.samples
        sample_i = 0
        samples_length = len(self.samples[0])
        num_channels = len(self.samples)
        bps_total = self.bps / 8
        while sample_i < samples_length:

            channels_i = 0
            while channels_i < num_channels:
                push_int(output, self.samples[channels_i][sample_i], bps_total)

                channels_i += 1

            sample_i += 1

        prefix = []
        push_string(prefix, 'data')

        # length of the rest of the data
        push_int(prefix, len(output), 4)

        return prefix + output


if __name__ == '__main__':
    snd = create_sound_from_file('bolomotnguoi.wav')
    snd.samples[0] = snd.samples[0][::-1]  # reverse left channel
    snd.samples[1] = snd.samples[1][::-1]  # reverse right channel

    snd.save_to_file('foo2.wav')
