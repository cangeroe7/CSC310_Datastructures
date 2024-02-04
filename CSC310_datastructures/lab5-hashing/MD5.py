# For MD5: https://www.comparitech.com/blog/information-security/md5-algorithm-with-examples/

from sys import byteorder
from io import BytesIO
from typing import BinaryIO
import numpy as np

md5_block_size = 64
md5_digest_size = 16

# Shifts used for when the value of a is left-shifted
shift = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
         5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
         4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
         6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

# Creating the sines for that are used to create 32 bit integers for K
sines = np.abs(np.sin(np.arange(64) + 1))
K = [int(x) for x in np.floor(2 ** 32 * sines)]

# Creating the rounds of 16 that decide which msg_int gets used in the hashing round
round_1 = [i for i in range(16)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
round_2 = [(5 * i + 1) % 16 for i in range(16)] # [1, 6, 11, 0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12]
round_3 = [(3 * i + 5) % 16 for i in range(16)] # [5, 8, 11, 14, 1, 4, 7, 10, 13, 0, 3, 6, 9, 12, 15, 2]
round_4 = [(7 * i) % 16 for i in range(16)] # [0, 7, 14, 5, 12, 3, 10, 1, 8, 15, 6, 13, 4, 11, 2, 9]

# Putting all the rounds in a row. 4 rounds of 16
msg_idx_for_step = round_1 + round_2 + round_3 + round_4

# bit not for 32 bit integer
def bit_not(x: int) -> int:
    return 4294967295 - x

# The bit mixer functions
# These are used to reassign the value of a
# All functions use bit manipulation on the values of b, c, and d

def F(b: int, c: int, d: int) -> int:
    return d ^ (b & (c ^ d))

def G(b: int, c: int, d: int) -> int:
    return c ^ (d & (b ^ c))

def H(b: int, c: int, d: int) -> int:
    return b ^ c ^ d

def I(b: int, c: int, d: int) -> int:
    return c ^ (b | bit_not(d))

# There are 4 rounds of 16 the first round uses F, the second G, etc
mixer_for_step = [F for _ in range(16)] + [G for _ in range(16)] + [H for _ in range(16)] + [I for _ in range(16)]

# shifts the x int by y places to the left
def left_shift(x: int, y: int) -> int:
    return ((x << (y & 31)) | ((x & 0xffffffff) >> (32 - (y & 31)))) & 0xffffffff

class MD5State:
    def __init__(self):
        self.length: int = 0
        # initial values for a, b, c, and d
        self.state: tuple[int, int, int, int] = (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)
        self.n_filled_bytes: int = 0
        self.buf: bytearray = bytearray(md5_block_size)
    
    # Converts a, b, c, d into 128 bit hashed value
    def digest(self):
        return b''.join(x.to_bytes(length=4, byteorder='little') for x in self.state)
    
    def hex_digest(self):
        return self.digest().hex()

    
    def process(self, stream: BinaryIO) -> None:
        assert self.n_filled_bytes < len(self.buf)

        # Create a memory view for the buffer
        view = memoryview(self.buf)

        # While loop will run until the stream runs out of bytes
        while bytes_read := stream.read(md5_block_size - self.n_filled_bytes): # assign bytes to bytes_read
            # Bytes from the stream are added to the buffer
            view[self.n_filled_bytes:self.n_filled_bytes + len(bytes_read)] = bytes_read

            # If there are no filled bytes and the bytes_read is 64 bytes the buffer gets compressed
            if self.n_filled_bytes == 0 and len(bytes_read) == md5_block_size:
                self.compress(self.buf)
                self.length += md5_block_size
            # else the extra bytes count gets added to n_filled_bytes and it 
            # again checks if there are 512 bits to be compressed,
            # and it adjusts the length and resets the n_filled_bytes to 0
            else:
                self.n_filled_bytes += len(bytes_read)
                if self.n_filled_bytes == md5_block_size:
                    self.compress(self.buf)
                    self.length += md5_block_size
                    self.n_filled_bytes = 0

    # The finalize function does one last compress, and makes sure that the length fits
    def finalize(self) -> None:
        assert self.n_filled_bytes < md5_block_size

        self.length += self.n_filled_bytes
        self.buf[self.n_filled_bytes] = 0b10000000
        self.n_filled_bytes += 1

        n_bytes_needed_for_len = 8

        if self.n_filled_bytes + n_bytes_needed_for_len > md5_block_size:
            self.buf[self.n_filled_bytes:] = bytes(md5_block_size - self.n_filled_bytes)
            self.compress(self.buf)
            self.n_filled_bytes = 0

        self.buf[self.n_filled_bytes:] = bytes(md5_block_size - self.n_filled_bytes)
        bit_len_64 = (self.length * 8) % (2 ** 64)
        self.buf[-n_bytes_needed_for_len:] = bit_len_64.to_bytes(length=n_bytes_needed_for_len,
                                                                 byteorder='little')
        self.compress(self.buf)

    # The compress function uses 512 bits at a time to hash the values of a, b, c, and d
    def compress(self, msg_chunk: bytearray) -> None:
        # Making sure that we have 64 bytes
        assert len(msg_chunk) == md5_block_size
        # Turning bytes into 32-int
        msg_ints = [int.from_bytes(msg_chunk[i:i + 4], byteorder="little") for i in range(0, md5_block_size, 4)]
        # Making sure there are 16 msg_ints
        assert len(msg_ints) == md5_digest_size

        # Assign a, b, c, d to the current state
        a, b, c, d = self.state

        # Running the hashing 64 times
        for i in range(md5_block_size):
            # Assigning the mixer function (F, G, H, or I), and the index for the msg_int
            bit_mixer = mixer_for_step[i]
            msg_idx = msg_idx_for_step[i]

            # The actual hashing of the MD5 algorithm
            # a is reassigned to a + the mixer function + the integer + the sine number, 
            # then it is resized to a 32 bit integer if it got bigger than that
            a = (a + bit_mixer(b, c, d) + msg_ints[msg_idx] + K[i]) % (2 ** 32)
            # A left shift is performed on a 
            a = left_shift(a, shift[i])
            a = (a + b) % (2 ** 32)
            # a, b, c, d is rotated to the right 
            a, b, c, d = d, a, b, c

        # a, b, c, d are reassigned the state of the object, to be used by the next 512 bits
        self.state = (
            (self.state[0] + a) % (2 ** 32),
            (self.state[1] + b) % (2 ** 32),
            (self.state[2] + c) % (2 ** 32),
            (self.state[3] + d) % (2 ** 32)
        )

# Usually MD5 would return a 128 bit hash, 
# but because it needs to be between 0 - 9999 we convert it to an int and take the mod 10000
def test_md5(s: bytes):
    state = MD5State()
    state.process(BytesIO(s))
    state.finalize()
    return int.from_bytes(state.digest(), byteorder=byteorder) % 10000