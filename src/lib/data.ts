export const WA_NUMBER = '6281166352 8'.replace(/\s/g, '');

export function waLink(msg = '') {
	return `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(msg)}`;
}

export function waProduct(name: string) {
	return waLink(`Halo Smartprint Padang, saya ingin memesan *${name}*. Bisa info lebih lanjut?`);
}

export const waGeneral = waLink(
	'Halo Smartprint Padang, saya ingin berkonsultasi mengenai produk cetak. Bisa bantu?'
);

export const allProducts = [
	{
		id: 1,
		name: 'Spanduk PVC',
		category: 'spanduk',
		emoji: '🖼️',
		price: 'Mulai Rp 25.000/m²',
		tags: ['Populer'],
		desc: 'Spanduk outdoor berkualitas tinggi, tahan cuaca & sinar UV.'
	},
	{
		id: 2,
		name: 'Baliho Outdoor',
		category: 'baliho',
		emoji: '📋',
		price: 'Mulai Rp 45.000/m²',
		tags: ['Populer'],
		desc: 'Baliho ukuran besar untuk promosi jalan & event outdoor.'
	},
	{
		id: 3,
		name: 'Stiker Cutting',
		category: 'stiker',
		emoji: '✂️',
		price: 'Mulai Rp 15.000',
		tags: ['Populer'],
		desc: 'Stiker cutting presisi tinggi untuk kaca, motor, & properti.'
	},
	{
		id: 4,
		name: 'Stiker Label Produk',
		category: 'stiker',
		emoji: '🏷️',
		price: 'Mulai Rp 200/pcs',
		tags: ['Baru'],
		desc: 'Label produk UMKM dengan berbagai ukuran & finishing.'
	},
	{
		id: 5,
		name: 'Kartu Nama Premium',
		category: 'kartu-nama',
		emoji: '💼',
		price: 'Mulai Rp 30.000/100pcs',
		tags: ['Populer'],
		desc: 'Kartu nama profesional, art carton 260gsm, full color.'
	},
	{
		id: 6,
		name: 'Roll Banner',
		category: 'banner',
		emoji: '🎯',
		price: 'Mulai Rp 150.000',
		tags: [],
		desc: 'Banner roll-up portabel untuk pameran & promosi indoor.'
	},
	{
		id: 7,
		name: 'Backdrop Photobooth',
		category: 'banner',
		emoji: '📸',
		price: 'Mulai Rp 80.000/m²',
		tags: [],
		desc: 'Backdrop custom untuk acara pernikahan, wisuda, & event.'
	},
	{
		id: 8,
		name: 'X-Banner',
		category: 'banner',
		emoji: '📌',
		price: 'Mulai Rp 85.000',
		tags: [],
		desc: 'X-banner lengkap dengan stand, cocok untuk toko & kantor.'
	},
	{
		id: 9,
		name: 'Nota / Bon Custom',
		category: 'lainnya',
		emoji: '🧾',
		price: 'Mulai Rp 45.000/buku',
		tags: [],
		desc: 'Nota 2 rangkap custom dengan logo usaha Anda.'
	},
	{
		id: 10,
		name: 'Poster A3 / A2',
		category: 'lainnya',
		emoji: '🖨️',
		price: 'Mulai Rp 5.000/lembar',
		tags: [],
		desc: 'Poster full color glossy/matte untuk promosi & informasi.'
	},
	{
		id: 11,
		name: 'ID Card / Name Tag',
		category: 'kartu-nama',
		emoji: '🪪',
		price: 'Mulai Rp 10.000/pcs',
		tags: ['Baru'],
		desc: 'ID card PVC atau kertas laminasi untuk perusahaan & sekolah.'
	},
	{
		id: 12,
		name: 'Undangan Digital Print',
		category: 'lainnya',
		emoji: '💌',
		price: 'Mulai Rp 25.000/pcs',
		tags: ['Baru'],
		desc: 'Undangan cetak elegan untuk pernikahan, khitanan, & acara.'
	}
];

export const categories = [
	{ key: 'semua', label: 'Semua' },
	{ key: 'spanduk', label: 'Spanduk' },
	{ key: 'baliho', label: 'Baliho' },
	{ key: 'stiker', label: 'Stiker' },
	{ key: 'kartu-nama', label: 'Kartu Nama' },
	{ key: 'banner', label: 'Banner' },
	{ key: 'lainnya', label: 'Lainnya' }
];

export const statTargets = { products: 100, clients: 1149, years: 7, followers: 1149 };

export const faqs = [
	{
		q: 'Berapa lama proses cetak?',
		a: 'Umumnya 1–3 hari kerja tergantung jenis & ukuran produk. Untuk order urgent bisa lebih cepat — hubungi kami langsung.'
	},
	{
		q: 'Apakah bisa custom ukuran?',
		a: 'Tentu! Kami melayani cetak dengan ukuran custom sesuai kebutuhan Anda.'
	},
	{
		q: 'Format file apa yang diterima?',
		a: 'Kami menerima CDR, AI, PDF, JPG/PNG (min. 150 dpi). Format vektor sangat direkomendasikan.'
	},
	{
		q: 'Apakah ada layanan antar?',
		a: 'Ada! Kami melayani pengiriman ke seluruh wilayah Kota Padang & sekitarnya.'
	},
	{
		q: 'Bagaimana cara pembayaran?',
		a: 'Transfer bank (BCA, BRI, Mandiri), QRIS, dan cash. DP 50% untuk order custom.'
	},
	{
		q: 'Apakah ada harga grosir?',
		a: 'Ya, tersedia harga spesial untuk order dalam jumlah besar. Hubungi kami via WhatsApp.'
	}
];

export const testimonials = [
	{
		name: 'Budi Santoso',
		role: 'Pemilik Toko Baju',
		text: 'Spanduk dari Smartprint kualitasnya bagus, warnanya tajam dan tahan lama. Udah langganan dari 2022!',
		stars: 5
	},
	{
		name: 'Rina Marlina',
		role: 'Event Organizer',
		text: 'Backdrop photobooth-nya memuaskan, bahan tebal dan gambar HD. Proses cepat, tim juga responsif.',
		stars: 5
	},
	{
		name: 'Agus Firmansyah',
		role: 'UMKM Kuliner',
		text: 'Label produk saya dicetak di sini, hasilnya profesional. Harga juga bersaing untuk kualitas segini.',
		stars: 5
	},
	{
		name: 'Sari Dewi',
		role: 'Mahasiswi',
		text: 'Pesan kartu nama wisuda, hasilnya beyond expectation! Kertasnya tebal, warnanya cantik.',
		stars: 5
	},
	{
		name: 'Rizky Pratama',
		role: 'Kontraktor',
		text: 'Sering pesan baliho proyek di sini, selalu on time dan kualitas terjamin. Rekomended!',
		stars: 5
	},
	{
		name: 'Lita Permata',
		role: 'Guru SD',
		text: 'Cetak banner acara sekolah, komunikatif dan hasilnya rapi. Harga ramah di kantong.',
		stars: 5
	}
];
