"""getar.py - Getar 1.0.0, tahap 1: suara dari matematika frekuensi (belum pakai AI).

Pakai:
  python getar.py        -> membuat 4 suara demo di folder suara/
"""
import os
import wave

import numpy as np

VERSI = "1.0.0"
SR = 16000  # sampel per detik (kecil supaya file ringan)


def waktu(detik):
    return np.arange(int(SR * detik)) / SR


def nada(f, detik=1.5, harmonik=(1.0,), vibrato=0.0, peluruhan=3.0):
    """Satu nada: jumlah gelombang sinus pada kelipatan frekuensi f.

    harmonik : kekuatan tiap kelipatan frekuensi (1x, 2x, 3x, ...)
    vibrato  : seberapa besar frekuensi bergetar (0.01 = 1 persen)
    peluruhan: makin besar, makin cepat suara memudar
    """
    t = waktu(detik)
    frek = f * (1 + vibrato * np.sin(2 * np.pi * 5 * t))
    fase = 2 * np.pi * np.cumsum(frek) / SR
    x = sum(a * np.sin((k + 1) * fase) for k, a in enumerate(harmonik))
    amplop = np.exp(-peluruhan * t) * np.minimum(1.0, t / 0.02)
    return x * amplop


def simpan(nama, x):
    os.makedirs("suara", exist_ok=True)
    x = x / (np.abs(x).max() + 1e-9) * 0.8
    data = (x * 32767).astype(np.int16)
    with wave.open(f"suara/{nama}.wav", "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())
    print(f"tersimpan: suara/{nama}.wav")


if __name__ == "__main__":
    print(f"Getar {VERSI}")
    simpan("1_sinus_murni", nada(440))
    simpan("2_harmonik", nada(220, harmonik=(1, .5, .33, .25, .2, .17)))
    simpan("3_akor", nada(261.63) + nada(329.63) + nada(392.00))
    simpan("4_bergetar", nada(330, detik=2.5, harmonik=(1, .4, .2),
                              vibrato=0.01, peluruhan=0.8))
