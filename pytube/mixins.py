# -*- coding: utf-8 -*-
"""
pytube.mixins
~~~~~~~~~~~~~

"""
from urllib.parse import parse_qsl
from urllib.parse import unquote

from pytube import cipher


def apply(dct, key, fn):
    dct[key] = fn(dct[key])


def apply_cipher(video_info, fmt, js):
    stream_map = video_info[fmt]
    for i, stream in enumerate(stream_map):
        url = stream['url']
        if 'signature=' in url:
            continue
        signature = cipher.get_signature(js, stream['s'])
        stream_map[i]['url'] = url + '&signature=' + signature


def apply_fmt_decoder(video_info, fmt):
    video_info[fmt] = [
        {k: unquote(v) for k, v in parse_qsl(i)} for i
        in video_info[fmt].split(',')
    ]
