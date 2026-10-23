# AGENTS.md - panduan untuk AI yang membantu proyek Getar

Baca file ini dan PROGRESS.md sebelum menulis apa pun.

## Konteks
- Getar adalah model AI kecil buatan pemilik repo, penghasil suara dari matematika
  frekuensi (sintesis aditif: jumlah gelombang sinus), bukan teks jadi suara.
- Pemilik bekerja sepenuhnya dari ponsel: Termux + GitHub, tanpa PC. Semua kode harus
  bisa jalan di Termux.
- Bahasa pemrograman: Python + NumPy saja. Hindari library berat (misalnya PyTorch).
- Komunikasi dengan pemilik memakai bahasa Indonesia.

## Aturan kerja
1. Kerjakan bertahap dan kecil. Satu tahap, lalu uji, lalu latih, lalu uji.
2. Setelah setiap perubahan, perbarui PROGRESS.md (apa yang dilakukan, hasil uji).
3. Jangan pernah menaruh token, kata sandi, atau data pribadi di repo.
4. Jangan menyimpan percakapan pribadi pengguna di repo.
5. Otak AI disimpan sebagai .npz (bukan pickle). Catatan nilai di .csv.
6. Jujur soal batas: jangan menjanjikan kualitas melebihi kemampuan model kecil.

## Rencana tahap
1. Suara dari matematika murni -> .wav (getar.py)
2. Representasi suara sebagai frame (kekuatan frekuensi per waktu)
3. Otak kecil (NumPy) yang menebak frame berikutnya, lalu dirender jadi suara
4. Penilaian pengguna (suka atau tidak) dipakai untuk melatih ulang
5. Ujian "IQ": skor penilaian rata-rata dan kesamaan spektrum, dicatat berkala
