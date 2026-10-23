# Getar 1.0.0

AI kecil yang menciptakan suara dari matematika frekuensi, dan belajar dari seleramu.

## Fungsi
Menghasilkan suara dan tekstur nada baru. Bukan musik tiruan, bukan teks jadi suara,
dan bukan peniru suara orang.

## Cara belajar
Getar membuat suara, kamu menilainya (suka atau tidak), lalu Getar menyesuaikan diri.
Skor penilaian rata-rata dipakai sebagai "IQ" Getar dari waktu ke waktu.

## Bisa dipakai untuk
Musik latar, efek suara, atau bereksperimen dengan bunyi.

## Bukan untuk
Teks jadi suara bicara, atau meniru suara orang.

## Cara menjalankan (Termux)
```
pkg install python python-numpy git
python getar.py
```
Hasilnya ada di folder `suara/` (file .wav).

## Struktur
```
getar.py      kode (tahap 1: suara dari matematika murni)
suara/        hasil suara (.wav)
brain/        otak AI (.npz) dan catatan latihan (nanti)
README.md     perkenalan
AGENTS.md     panduan untuk AI lain yang membantu
PROGRESS.md   catatan kemajuan
```

## Status
Tahap awal. Lihat PROGRESS.md.
