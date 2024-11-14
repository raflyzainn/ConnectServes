-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 14 Nov 2024 pada 05.39
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `connectserve`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `daftarjasa_merch`
--

CREATE TABLE `daftarjasa_merch` (
  `id_jasa` varchar(10) NOT NULL,
  `id_merch` varchar(10) NOT NULL,
  `nama` varchar(30) DEFAULT NULL,
  `kategori` varchar(50) DEFAULT NULL,
  `harga` int(10) DEFAULT NULL,
  `lokasi` varchar(300) DEFAULT NULL,
  `foto_jasa` blob DEFAULT NULL,
  `deskripsi` varchar(500) DEFAULT NULL,
  `id_review` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `jasaselesai_merch`
--

CREATE TABLE `jasaselesai_merch` (
  `id_pesanan` varchar(10) NOT NULL,
  `id_jasa` varchar(10) NOT NULL,
  `id_merch` varchar(10) NOT NULL,
  `bukti_foto` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `lastseenjasa_cust`
--

CREATE TABLE `lastseenjasa_cust` (
  `id_cust` varchar(10) NOT NULL,
  `id_jasa` varchar(10) NOT NULL,
  `urutan_last` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `listjasa_merch`
--

CREATE TABLE `listjasa_merch` (
  `id_jasa` varchar(10) NOT NULL,
  `id_merch` varchar(10) NOT NULL,
  `id_pesanan` varchar(10) NOT NULL,
  `status_pesanan` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `paymentjasa_cust`
--

CREATE TABLE `paymentjasa_cust` (
  `id_payment` varchar(10) NOT NULL,
  `id_pesanan` varchar(10) NOT NULL,
  `id_jasa` varchar(10) NOT NULL,
  `id_merch` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengguna`
--

CREATE TABLE `pengguna` (
  `email` varchar(30) NOT NULL,
  `no_hp` bigint(13) NOT NULL,
  `nama` varchar(30) DEFAULT NULL,
  `kata_sandi` varchar(30) DEFAULT NULL,
  `peran_pengguna` varchar(15) DEFAULT NULL,
  `ava_pengguna` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `pesanjasa_cust`
--

CREATE TABLE `pesanjasa_cust` (
  `id_pesanan` varchar(10) NOT NULL,
  `id_jasa` varchar(10) NOT NULL,
  `id_cust` varchar(10) NOT NULL,
  `harga` int(10) DEFAULT NULL,
  `alamat` varchar(300) DEFAULT NULL,
  `id_merch` varchar(10) NOT NULL,
  `tanggal_pemesanan` date DEFAULT NULL,
  `metode_pembayaran` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `reviewjasa_cust`
--

CREATE TABLE `reviewjasa_cust` (
  `id_review` varchar(10) NOT NULL,
  `id_cust` varchar(10) NOT NULL,
  `id_jasa` varchar(10) NOT NULL,
  `rating_jasa` int(1) DEFAULT NULL,
  `deskripsirating_jasa` varchar(10) DEFAULT NULL,
  `uploadFoto_jasa` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `user_cust`
--

CREATE TABLE `user_cust` (
  `id_cust` varchar(10) NOT NULL,
  `email_cust` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `user_merch`
--

CREATE TABLE `user_merch` (
  `id_merch` varchar(10) NOT NULL,
  `email_merch` varchar(30) NOT NULL,
  `foto_ktp` blob DEFAULT NULL,
  `nama_ktp` varchar(30) DEFAULT NULL,
  `nik` bigint(16) DEFAULT NULL,
  `lokasi` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `daftarjasa_merch`
--
ALTER TABLE `daftarjasa_merch`
  ADD PRIMARY KEY (`id_jasa`),
  ADD KEY `fk_id_merch_daftar` (`id_merch`);

--
-- Indeks untuk tabel `jasaselesai_merch`
--
ALTER TABLE `jasaselesai_merch`
  ADD KEY `fk_id_pesanan_selesai` (`id_pesanan`),
  ADD KEY `fk_id_jasa_selesai` (`id_jasa`),
  ADD KEY `fk_id_merch_selesai` (`id_merch`);

--
-- Indeks untuk tabel `lastseenjasa_cust`
--
ALTER TABLE `lastseenjasa_cust`
  ADD KEY `fk_id_cust_lastseen` (`id_cust`),
  ADD KEY `fk_id_jasa_lastseen` (`id_jasa`);

--
-- Indeks untuk tabel `listjasa_merch`
--
ALTER TABLE `listjasa_merch`
  ADD KEY `fk_id_jasa_list` (`id_jasa`),
  ADD KEY `fk_id_merch_list` (`id_merch`),
  ADD KEY `fk_id_pesanan_list` (`id_pesanan`);

--
-- Indeks untuk tabel `paymentjasa_cust`
--
ALTER TABLE `paymentjasa_cust`
  ADD PRIMARY KEY (`id_payment`),
  ADD KEY `fk_id_pesanan_payment` (`id_pesanan`),
  ADD KEY `fk_id_jasa_payment` (`id_jasa`),
  ADD KEY `fk_id_merch_payment` (`id_merch`);

--
-- Indeks untuk tabel `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`email`,`no_hp`);

--
-- Indeks untuk tabel `pesanjasa_cust`
--
ALTER TABLE `pesanjasa_cust`
  ADD PRIMARY KEY (`id_pesanan`),
  ADD KEY `fk_id_jasa` (`id_jasa`),
  ADD KEY `fk_id_cust` (`id_cust`),
  ADD KEY `fk_id_merch` (`id_merch`);

--
-- Indeks untuk tabel `reviewjasa_cust`
--
ALTER TABLE `reviewjasa_cust`
  ADD PRIMARY KEY (`id_review`),
  ADD KEY `fk_id_cust_review` (`id_cust`),
  ADD KEY `fk_id_jasa_review` (`id_jasa`);

--
-- Indeks untuk tabel `user_cust`
--
ALTER TABLE `user_cust`
  ADD PRIMARY KEY (`id_cust`),
  ADD KEY `fk_email_cust` (`email_cust`);

--
-- Indeks untuk tabel `user_merch`
--
ALTER TABLE `user_merch`
  ADD PRIMARY KEY (`id_merch`),
  ADD KEY `fk_email_merch` (`email_merch`);

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `daftarjasa_merch`
--
ALTER TABLE `daftarjasa_merch`
  ADD CONSTRAINT `fk_id_merch_daftar` FOREIGN KEY (`id_merch`) REFERENCES `user_merch` (`id_merch`);

--
-- Ketidakleluasaan untuk tabel `jasaselesai_merch`
--
ALTER TABLE `jasaselesai_merch`
  ADD CONSTRAINT `fk_id_jasa_selesai` FOREIGN KEY (`id_jasa`) REFERENCES `daftarjasa_merch` (`id_jasa`),
  ADD CONSTRAINT `fk_id_merch_selesai` FOREIGN KEY (`id_merch`) REFERENCES `user_merch` (`id_merch`),
  ADD CONSTRAINT `fk_id_pesanan_selesai` FOREIGN KEY (`id_pesanan`) REFERENCES `pesanjasa_cust` (`id_pesanan`);

--
-- Ketidakleluasaan untuk tabel `lastseenjasa_cust`
--
ALTER TABLE `lastseenjasa_cust`
  ADD CONSTRAINT `fk_id_cust_lastseen` FOREIGN KEY (`id_cust`) REFERENCES `user_cust` (`id_cust`),
  ADD CONSTRAINT `fk_id_jasa_lastseen` FOREIGN KEY (`id_jasa`) REFERENCES `daftarjasa_merch` (`id_jasa`);

--
-- Ketidakleluasaan untuk tabel `listjasa_merch`
--
ALTER TABLE `listjasa_merch`
  ADD CONSTRAINT `fk_id_jasa_list` FOREIGN KEY (`id_jasa`) REFERENCES `daftarjasa_merch` (`id_jasa`),
  ADD CONSTRAINT `fk_id_merch_list` FOREIGN KEY (`id_merch`) REFERENCES `user_merch` (`id_merch`),
  ADD CONSTRAINT `fk_id_pesanan_list` FOREIGN KEY (`id_pesanan`) REFERENCES `pesanjasa_cust` (`id_pesanan`);

--
-- Ketidakleluasaan untuk tabel `paymentjasa_cust`
--
ALTER TABLE `paymentjasa_cust`
  ADD CONSTRAINT `fk_id_jasa_payment` FOREIGN KEY (`id_jasa`) REFERENCES `daftarjasa_merch` (`id_jasa`),
  ADD CONSTRAINT `fk_id_merch_payment` FOREIGN KEY (`id_merch`) REFERENCES `user_merch` (`id_merch`),
  ADD CONSTRAINT `fk_id_pesanan_payment` FOREIGN KEY (`id_pesanan`) REFERENCES `pesanjasa_cust` (`id_pesanan`);

--
-- Ketidakleluasaan untuk tabel `pesanjasa_cust`
--
ALTER TABLE `pesanjasa_cust`
  ADD CONSTRAINT `fk_id_cust` FOREIGN KEY (`id_cust`) REFERENCES `user_cust` (`id_cust`),
  ADD CONSTRAINT `fk_id_jasa` FOREIGN KEY (`id_jasa`) REFERENCES `daftarjasa_merch` (`id_jasa`),
  ADD CONSTRAINT `fk_id_merch` FOREIGN KEY (`id_merch`) REFERENCES `user_merch` (`id_merch`);

--
-- Ketidakleluasaan untuk tabel `reviewjasa_cust`
--
ALTER TABLE `reviewjasa_cust`
  ADD CONSTRAINT `fk_id_cust_review` FOREIGN KEY (`id_cust`) REFERENCES `user_cust` (`id_cust`),
  ADD CONSTRAINT `fk_id_jasa_review` FOREIGN KEY (`id_jasa`) REFERENCES `daftarjasa_merch` (`id_jasa`);

--
-- Ketidakleluasaan untuk tabel `user_cust`
--
ALTER TABLE `user_cust`
  ADD CONSTRAINT `fk_email_cust` FOREIGN KEY (`email_cust`) REFERENCES `pengguna` (`email`);

--
-- Ketidakleluasaan untuk tabel `user_merch`
--
ALTER TABLE `user_merch`
  ADD CONSTRAINT `fk_email_merch` FOREIGN KEY (`email_merch`) REFERENCES `pengguna` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
