---
name: ux-writing-microcopy
description: "Write crisp, human-centered UX microcopy and seed domain-realistic UI data (eliminating AI clichés, 'Lorem ipsum', 'John Doe', and 'Submit' buttons). Use whenever populating text layers in FigCraft or writing copy, labels, empty states, error messages, and mock datasets in UI code."
---

# UX Writing, Microcopy & Domain-Realistic Data Seeding

Even a visually strong layout looks like an AI template when filled with `"Supercharge Your Workflow"`, `"Seamless Integration"`, `"John Doe"`, `"$12,345"`, or `"Submit"`. Apply this skill to every text node in FigCraft and every string in frontend/mobile code.

## 1. Banned AI Copy Clichés vs. Studio Replacements

| Context | Banned AI Slop Copy | Industrial-Grade Replacement |
| :--- | :--- | :--- |
| **SaaS Hero Headline** | *"Revolutionize / Supercharge / Elevate Your Workflow with AI"* | State the concrete mechanism or outcome: *"Tutup buku kas bulanan dalam 4 menit, bukan 4 hari."* / *"Issue tracking built for speed."* |
| **Hero Subheadline** | *"Experience seamless integration and empower your team to achieve more with our cutting-edge platform."* | Name who it is for and what it replaces in $\le 20$ words: *"Rekonsiliasi mutasi bank, faktur pajak, dan payroll otomatis dalam satu buku besar real-time."* |
| **Primary CTA Button** | *"Submit"*, *"Click Here"*, *"Learn More"*, *"Get Started Now"* | Verb + specific object: *"Transfer Rp 1.250.000"*, *"Buat Workspace"*, *"Unduh Laporan PDF"*, *"Coba Gratis 14 Hari"* |
| **Destructive Confirmation** | *"Are you sure you want to delete this item? Yes / No"* | Title: *"Hapus proyek 'Q4 Redesign'?"* Body: *"14 file desain dan riwayat versi akan dihapus permanen."* CTAs: *"Batal"* + *"Hapus Proyek"* (red) |
| **Empty State** | *"No data available"* / *"Nothing to see here!"* | *"Belum ada tagihan jatuh tempo"* + *"Tagihan yang Anda buat untuk klien akan muncul otomatis di sini."* + *"+ Buat Tagihan"* |
| **Form Error** | *"Invalid input"* / *"Error occurred"* | State the exact rule: *"Masukkan minimal 8 karakter termasuk satu angka."* / *"Nomor VA harus 16 digit angka."* |

## 2. Domain-Realistic Data Seeding (Zero Placeholder Rule)

Never use `Lorem ipsum`, `User 1 / User 2`, `John Doe`, `test@example.com`, `Product A / Product B`, or sequential numbers (`10, 20, 30`). Seed every table, card, and list with **contextual, domain-accurate data**:

### Indonesian / Regional Product Context (when prompt or product is Indonesian)
- **Names**: *Nadia Kusuma*, *Rizky Pratama*, *Budi Santoso*, *Ayu Lestari*, *PT Sinar Niaga Nusantara*, *CV Karya Mandiri*.
- **Currency & Amounts**: Proper thousand separators and realistic pricing/balances (`Rp 4.850.000`, `Rp 128.400`, `Rp 19.750.000` — avoid fake round `Rp 1.000.000` on every row).
- **Banks / Payment Channels**: *BCA Virtual Account*, *Mandiri QRIS*, *GoPay*, *Bank Jago*, *SeaBank*, *Transfer BI-FAST*.
- **Timestamps**: Relative for recent activity (*"2 menit lalu"*, *"Hari ini, 14:32 WIB"*), formatted date for history (*"04 Nov 2026"*).

### Global / B2B SaaS Product Context
- **Names & Roles**: *Elena Rostova (Staff Engineer)*, *Marcus Vance (VP Finance)*, *Kenji Takahashi (Design Lead)*.
- **Identifiers**: Realistic short hashes/IDs (`INV-2026-0842`, `PR #1429`, `us-east-1a`, `v2.14.0`).
- **Metrics**: Plausible non-uniform distributions (`99.94% uptime`, `142 ms p95`, `$48,920 MRR`, `+8.4% vs last month`).

## 3. Microcopy Discipline Rules

1. **Verb-Noun Symmetry**: Keep vocabulary identical across trigger and feedback. If the button says **"Terbitkan"**, the toast says **"Berhasil diterbitkan"** (never button *"Publish"* $\rightarrow$ toast *"Saved"*).
2. **Sentence Case by Default**: Use Sentence case for headings, buttons, navigation links, and table headers (`"Pengaturan akun"`, `"Tambah anggota"`). Reserve `ALL CAPS` strictly for short `10–11px` status badges (`LUNAS`, `DRAFT`, `BETA`).
3. **Cut Label Redundancy**: Inside a section already titled **"Anggota Tim"**, the button is **"+ Tambah"** or **"+ Undang"** (not *"+ Tambah Anggota Tim Baru"*).
