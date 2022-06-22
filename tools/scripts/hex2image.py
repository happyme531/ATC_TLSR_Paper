from tools.utils import hex2image

if __name__ == '__main__':
    s = '0000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007ffffffe07ffffffffc00000000000007ffffffc03ffffffffc00000000000007ffffff803ffffffffc00000000000007ffffff803ffffffffc00000000000007ffffff807ffffffffc00000000000007ffffff83fffffffffc00000000000007ffffff83fffffffffc00000000000007ffffffc1fffffffffc00000000000007ffffffc0fffffffffc00000000000007ffffffe07ffffffffc00000000000007ffffffc0001ffffffc00000000000007ffffff80000ffffffc00000000000007ffffff80000ffffffc00000000000007ffffff80000ffffffc00000000000007ffffffc0001ffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffff87ffffffc00000000000007fffffff0f83ffffffc00000000000007ffffffe0781ffffffc00000000000007ffffffc03c1ffffffc000000001bc007ffffffc03c1ffffffc0000000033e007ffffff801e0ffffffc00000000376007ffffff821e0ffffffc00000000366007ffffff820e0ffffffc000000003e6007ffffff830e0ffffffc000000001ce007ffffff830e0ffffffc00000000000007ffffff83860ffffffc00000000000007ffffff81860ffffffc00000001bfe007ffffffc0401ffffffc00000001bfe007ffffffc0001ffffffc00000001bfe007ffffffe0003ffffffc00000000000007fffffff0003ffffffc00000000000007fffffffc007ffffffc00000000000007ffffffff01fffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffc03fffffffc000000001ec007fffffff0007ffffffc000000003ee007ffffffe0003ffffffc00000000366007ffffffc0001ffffffc00000000366007ffffff80001ffffffc00000000366007ffffff81f80ffffffc000000003ee007ffffff83fe0ffffffc000000001fc007ffffff83fe0ffffffc000000000fc007ffffff83fe0ffffffc00000000000007ffffffc1fe0ffffffc00000000000007ffffffc1fe0ffffffc000000001fe007ffffff8000000ffffc000000003fe007ffffff00000007fffc00000000380007ffffff00000007fffc00000000300007ffffff00000007fffc00000000300007ffffff0000000ffffc000000001fe007ffffffc1fffffffffc000000003fe007fffffffffffffffffc000000003fe007fffffffffffffffffc00000000300007fffffffffffffffffc00000000300007ffffffffff1ffffffc000000001fe007ffffffe0000ffffffc000000003fe007ffffffc0000ffffffc000000003fe007ffffffc0001ffffffc00000000000007ffffff80001ffffffc00000000000007ffffff80001ffffffc000000001fe007ffffff83fc0ffffffc000000003fe007ffffff83fe0ffffffc000000003ee007ffffff83fe0ffffffc00000000366007ffffff81fe0ffffffc00000000366007ffffffc07c0ffffffc0000000037e007ffffffc0000ffffffc000000001bc007ffffffe0001ffffffc00000000000007fffffff0003ffffffc00000000000007fffffffc007ffffffc000000001fe007ffffffff01fffffffc000000003fe007fffffffffffffffffc00000000380007fffffffffffffffffc00000000300007fffff81ffffffffffc00000000300007fffff007fffffffffc000000001fe007ffffe003fffffffffc000000003fe007ffffc001fffffffffc000000003fe007ffff8001fffffffffc00000000000007ffff81c0fffffffffc00000000000007ffff83e0fffffffffc00000000000007ffff03e07ffffffffc00000000000007ffff07f07ffffffffc00000000000007ffff07f07ffffffffc00000000300007ffff07f07ffffffffc000000003e0007ffff07f07ffffffffc000000003fc007ffff0000001ffffffc0000000007f807ffff0000000ffffffc0000000001fc07ffff0000000ffffffc0000000007fc07ffff8000000ffffffc000000003f8407ffffc000001ffffffc000000003c0007fffffffffffffffffc00000000300007fffffffffffffffffc00000000000007fffffffffffffffffc000000001fe007fffffffffffffffffc000000003fe007ffffffffdffffffffc00000000380007ffffffff8ffffffffc00000000300007ffffffff8ffffffffc00000000300007ffffffff8ffffffffc000000001fe007ffffffff8ffffffffc000000003fe007ffffffff8ffffffffc000000003fe007ffffffff8ffffffffc00000000300007ffffffff8ffffffffc00000000300007ffffffff8ffffffffc000000001fe007ffffffff8ffffffffc000000003fe007ffffffff8ffffffffc000000003fe007ffffffff8ffffffffc00000000000007ffffffff8ffffffffc00000000000007ffffffffdffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc000000001fc007fffffffffffffffffc000000003fc007ffff8ffffffffffffc0000000038e007ffff07f8ff8ffffffc00000000306007ffff07f07f07fffffc00000000306007ffff07f07f07fffffc0000000038e007ffff07f07f07fffffc000000001fe007ffff07f07f07fffffc000000001fc007ffff07f07f07fffffc00000000000007ffff07f07f07fffffc00000000000007ffff07f07f07fffffc00000003ffe007ffff07f07f07fffffc00000003ffe007ffff07f07f07fffffc00000003ffe007ffff07f07f07fffffc00000000000007ffff07f07f07fffffc00000000000007ffff07f07f07fffffc00000003ffe007ffff00000007fffffc00000003ffe007ffff0000000ffffffc00000003ffe007ffff0000000ffffffc00000000000007ffff0000001ffffffc00000000000007ffff8000007ffffffc000000001ec007fffffffffffffffffc000000003ee007fffffffffffffffffc00000000366007fffffffffc7ffffffc00000000366007fffffffff83ffffffc00000000366007fffffffff83ffffffc000000003ee007fffffffff81ffffffc000000001fc007fffffffffc1ffffffc000000000fc007fffffffffc1ffffffc00000000000007fffffffffc1ffffffc00000000000007fffffffffc1ffffffc00000001ffe007fffffffffe0ffffffc00000001ffe007fffffffffe0ffffffc00000001ffe007fffffffffe0ffffffc000000000c0007fffffffffe0ffffffc000000000c0007ffff8000000ffffffc000000000c0007ffff0000000ffffffc000000000c0007ffff0000000ffffffc00000001ffe007ffff0000001ffffffc00000001ffe007ffff8000003ffffffc00000001ffe007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007ffffffffc3fffffffc00000000000007ffffffff80fffffffc00000000000007fffffc1f00fffffffc00000000000007fffff006007ffffffc00000000000007ffffe000003ffffffc00000000000007ffffc000183ffffffc00000000000007ffff8000381ffffffc00000000000007ffff81c03c1ffffffc00000000000007ffff83e07c1ffffffc00000000000007ffff07f07c1ffffffc00000000000007ffff07f07e0ffffffc00000000000007ffff07f07e0ffffffc00000000000007ffff07f07e0ffffffc00000000000007ffff07f07e0ffffffc00000000000007ffff0000000ffffffc00000000000007ffff0000000ffffffc00000000000007ffff0000000ffffffc00000000000007ffff8000000ffffffc00000000000007ffff8000001ffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc00000000000007fffffffffffffffffc0000'
    hex2image(s, 200, 213)
