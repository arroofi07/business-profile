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

// ── Categories ──
export const categories = [
	{ key: 'semua',    label: 'Semua',                    icon: '🗂️' },
	{ key: 'signage',  label: 'Signage & Banner',         icon: '🪧' },
	{ key: 'promosi',  label: 'Kebutuhan Promosi',        icon: '📢' },
	{ key: 'office',   label: 'Office Supplies',          icon: '🗂️' },
	{ key: 'buku',     label: 'Buku',                     icon: '📚' },
	{ key: 'souvenir', label: 'Souvenir',                 icon: '🎁' },
	{ key: 'textile',  label: 'Textile',                  icon: '👕' },
	{ key: 'industri', label: 'Industri',                 icon: '🏭' },
];

// ── All Products ──
export const allProducts = [
	// ─── 🪧 SIGNAGE & BANNER DISPLAY ───
	{ id: 1,  name: 'X Banner',             category: 'signage',  emoji: '🪧', tags: ['Populer'], desc: 'Banner portabel berbentuk X, cocok untuk acara, pameran, dan promosi indoor/outdoor.' },
	{ id: 2,  name: 'Y Banner',             category: 'signage',  emoji: '🚩', tags: [],          desc: 'Banner dengan penyangga berbentuk Y, lebih stabil untuk penggunaan outdoor.' },
	{ id: 3,  name: 'Roll Up Banner',       category: 'signage',  emoji: '📜', tags: ['Populer'], desc: 'Banner gulung praktis yang mudah dipasang dan disimpan, tampilan elegan.' },
	{ id: 4,  name: 'Mini X Banner',        category: 'signage',  emoji: '🔖', tags: [],          desc: 'Versi kecil X Banner, biasa diletakkan di atas meja restoran atau counter.' },
	{ id: 5,  name: 'Giant Banner',         category: 'signage',  emoji: '🏟️', tags: [],          desc: 'Banner ukuran sangat besar, ideal untuk stadion, konser, dan area luas.' },
	{ id: 6,  name: 'Tripod Banner',        category: 'signage',  emoji: '📷', tags: [],          desc: 'Banner dengan tiga kaki penyangga, sangat fleksibel dan mudah disesuaikan.' },
	{ id: 7,  name: 'Flag Banner',          category: 'signage',  emoji: '🎌', tags: [],          desc: 'Banner berbentuk bendera, bahan lentur dan tidak transparan, dinamis di luar ruangan.' },
	{ id: 8,  name: 'Spanduk',              category: 'signage',  emoji: '🖼️', tags: ['Populer'], desc: 'Banner persegi panjang tahan lama, tersedia berbagai ukuran untuk indoor/outdoor.' },
	{ id: 9,  name: 'Flag Chain',           category: 'signage',  emoji: '🎏', tags: [],          desc: 'Rangkaian bendera kecil berwarna-warni untuk dekorasi acara dan toko.' },
	{ id: 10, name: 'Signage',              category: 'signage',  emoji: '🪧', tags: [],          desc: 'Papan tanda informatif dan menarik untuk navigasi, branding, atau promosi.' },
	{ id: 11, name: 'Neon Box',             category: 'signage',  emoji: '💡', tags: ['Populer'], desc: 'Kotak cahaya cerah dan terang, sangat mencolok siang maupun malam hari.' },
	{ id: 12, name: 'Magnetic Backdrop',    category: 'signage',  emoji: '🧲', tags: ['Baru'],    desc: 'Latar belakang display berbasis magnet, mudah ganti grafik sesuai kebutuhan.' },
	{ id: 13, name: 'Event Desk',           category: 'signage',  emoji: '🏢', tags: [],          desc: 'Meja atau counter portabel berbranding, ideal untuk stan pameran dan acara.' },
	{ id: 14, name: 'Kanvas',               category: 'signage',  emoji: '🖌️', tags: [],          desc: 'Cetak di atas kanvas bertekstur, cocok untuk seni, foto, dan dekorasi ruangan.' },
	{ id: 15, name: 'Wallpaper',            category: 'signage',  emoji: '🧱', tags: ['Baru'],    desc: 'Pelapis dinding dekoratif dengan berbagai motif dan desain custom.' },
	{ id: 16, name: 'Balon Joged',          category: 'signage',  emoji: '🎈', tags: [],          desc: 'Balon bergerak warna cerah untuk menarik perhatian di acara outdoor.' },
	{ id: 17, name: 'Balon Promosi',        category: 'signage',  emoji: '🎉', tags: [],          desc: 'Balon besar berlogo untuk meningkatkan visibilitas di area penjualan.' },

	// ─── 📢 KEBUTUHAN PROMOSI ───
	{ id: 18, name: 'Tent Card',            category: 'promosi',  emoji: '📋', tags: [],          desc: 'Kartu lipat yang bisa berdiri sendiri, untuk promosi di meja restoran atau counter.' },
	{ id: 19, name: 'Hang Tag',             category: 'promosi',  emoji: '🏷️', tags: [],          desc: 'Label gantung untuk detail produk seperti harga, ukuran, dan informasi brand.' },
	{ id: 20, name: 'Poster',               category: 'promosi',  emoji: '🖨️', tags: ['Populer'], desc: 'Cetakan besar informatif untuk promosi, iklan, atau pengumuman acara.' },
	{ id: 21, name: 'Bendera Sedotan',      category: 'promosi',  emoji: '🚩', tags: [],          desc: 'Bendera mini di atas sedotan, cocok untuk lomba dan pesta anak-anak.' },
	{ id: 22, name: 'Triangle Pop Display', category: 'promosi',  emoji: '🔺', tags: ['Baru'],    desc: 'Display segitiga unik untuk menyajikan informasi perusahaan atau produk.' },
	{ id: 23, name: 'ID Card',              category: 'promosi',  emoji: '🪪', tags: ['Populer'], desc: 'Kartu identitas cetak untuk karyawan, peserta acara, atau anggota komunitas.' },
	{ id: 24, name: 'Wobbler',              category: 'promosi',  emoji: '🪁', tags: [],          desc: 'Materi promosi kecil yang bergoyang, dipasang di rak toko untuk menarik perhatian.' },
	{ id: 25, name: 'Undangan',             category: 'promosi',  emoji: '💌', tags: ['Populer'], desc: 'Cetakan undangan elegan untuk pernikahan, ulang tahun, dan acara korporasi.' },
	{ id: 26, name: 'Kalender',             category: 'promosi',  emoji: '📅', tags: [],          desc: 'Kalender dinding atau meja custom, bisa dijadikan media promosi perusahaan.' },
	{ id: 27, name: 'Postcard',             category: 'promosi',  emoji: '📮', tags: [],          desc: 'Kartu pos bergambar, populer untuk koleksi, suvenir, atau kirim salam.' },
	{ id: 28, name: 'Voucher Belanja',      category: 'promosi',  emoji: '🎟️', tags: [],          desc: 'Kartu voucher berisi detail promo atau diskon untuk meningkatkan penjualan.' },
	{ id: 29, name: 'Spunbond',             category: 'promosi',  emoji: '🛍️', tags: [],          desc: 'Bahan kain serat kuat untuk tas belanja dan barang promosi tahan lama.' },
	{ id: 30, name: 'Paper Bag',            category: 'promosi',  emoji: '🛍️', tags: ['Populer'], desc: 'Tas kertas ramah lingkungan dengan opsi cetak logo atau pesan promosi.' },
	{ id: 31, name: 'Cutting Sticker',      category: 'promosi',  emoji: '✂️', tags: ['Populer'], desc: 'Stiker vinil potong custom untuk dekorasi kendaraan, barang, atau ruangan.' },
	{ id: 32, name: 'Lanyard',              category: 'promosi',  emoji: '🔗', tags: [],          desc: 'Tali leher untuk menampung ID card atau kunci, bisa dicetak nama/logo.' },
	{ id: 33, name: 'Akrilik Printing',     category: 'promosi',  emoji: '💎', tags: ['Baru'],    desc: 'Cetak penuh warna di atas akrilik transparan, tampilan mewah dan tahan lama.' },
	{ id: 34, name: 'Brosur',               category: 'promosi',  emoji: '📄', tags: ['Populer'], desc: 'Cetakan terlipat berkualitas untuk membagikan info produk atau promosi.' },
	{ id: 35, name: 'Bangku Promosi',       category: 'promosi',  emoji: '🪑', tags: [],          desc: 'Tempat duduk portabel dengan permukaan berbranding untuk acara dan pameran.' },
	{ id: 36, name: 'E-Money',              category: 'promosi',  emoji: '💳', tags: ['Baru'],    desc: 'Kartu pembayaran elektronik custom berlogo, efektif untuk loyalitas pelanggan.' },

	// ─── 🗂️ OFFICE SUPPLIES ───
	{ id: 37, name: 'Kartu Nama',           category: 'office',   emoji: '💼', tags: ['Populer'], desc: 'Kartu identitas profesional berisi nama, kontak, dan logo perusahaan.' },
	{ id: 38, name: 'Kop Surat',            category: 'office',   emoji: '📝', tags: [],          desc: 'Kertas surat resmi berlogo perusahaan untuk komunikasi dan dokumen bisnis.' },
	{ id: 39, name: 'Amplop',               category: 'office',   emoji: '✉️', tags: [],          desc: 'Amplop berwarna dan berdesain unik, cocok untuk undangan atau pengiriman promosi.' },
	{ id: 40, name: 'Map Folder',           category: 'office',   emoji: '🗂️', tags: [],          desc: 'Folder dokumen tahan lama untuk menyimpan berkas dan material penting kantor.' },
	{ id: 41, name: 'Ordner',               category: 'office',   emoji: '📁', tags: [],          desc: 'Tempat penyimpanan dokumen berlubang dengan klip, cocok untuk pengarsipan kantor.' },

	// ─── 📚 BUKU ───
	{ id: 42, name: 'Buku Agenda',          category: 'buku',     emoji: '📓', tags: ['Populer'], desc: 'Buku jadwal harian portabel untuk merencanakan dan memantau aktivitas.' },
	{ id: 43, name: 'Buku Manual',          category: 'buku',     emoji: '📗', tags: [],          desc: 'Panduan produk atau perangkat dengan tampilan modern dan informatif.' },
	{ id: 44, name: 'Booklet',              category: 'buku',     emoji: '📔', tags: [],          desc: 'Buku kecil multi-halaman untuk promosi produk atau informasi layanan secara detail.' },
	{ id: 45, name: 'Company Profile',      category: 'buku',     emoji: '🏢', tags: ['Populer'], desc: 'Dokumen cetak profesional yang menggambarkan identitas dan profil perusahaan.' },
	{ id: 46, name: 'Katalog',              category: 'buku',     emoji: '📋', tags: [],          desc: 'Dokumen produk lengkap berisi gambar, deskripsi, dan harga untuk calon pelanggan.' },
	{ id: 47, name: 'Buku Menu',            category: 'buku',     emoji: '🍽️', tags: ['Populer'], desc: 'Daftar makanan dan minuman restoran dalam format cetak menarik dan profesional.' },
	{ id: 48, name: 'Annual Book',          category: 'buku',     emoji: '📆', tags: [],          desc: 'Buku catatan kegiatan tahunan, cocok untuk organisasi atau perencanaan bisnis.' },
	{ id: 49, name: 'Majalah',              category: 'buku',     emoji: '📰', tags: [],          desc: 'Publikasi cetak berkala untuk hiburan, informasi, atau promosi brand.' },
	{ id: 50, name: 'Buku Notes',           category: 'buku',     emoji: '📒', tags: [],          desc: 'Buku catatan portabel untuk pelajar, mahasiswa, dan profesional.' },
	{ id: 51, name: 'Buku Tamu',            category: 'buku',     emoji: '📖', tags: [],          desc: 'Buku pencatat kehadiran tamu untuk hotel, acara, atau instansi resmi.' },

	// ─── 🎁 SOUVENIR ───
	{ id: 52, name: 'Payung',               category: 'souvenir', emoji: '☂️', tags: ['Populer'], desc: 'Payung full-color custom, fungsional sekaligus efektif sebagai media promosi.' },
	{ id: 53, name: 'Mug',                  category: 'souvenir', emoji: '☕', tags: ['Populer'], desc: 'Gelas minum dengan cetak desain pribadi atau logo perusahaan.' },
	{ id: 54, name: 'USB',                  category: 'souvenir', emoji: '💾', tags: [],          desc: 'Flashdisk custom berbentuk unik dengan logo atau pesan brand.' },
	{ id: 55, name: 'Power Bank',           category: 'souvenir', emoji: '🔋', tags: ['Baru'],    desc: 'Charger portabel berdesain custom, cocok untuk hadiah atau doorprize.' },
	{ id: 56, name: 'Pen',                  category: 'souvenir', emoji: '🖊️', tags: ['Populer'], desc: 'Pulpen eksklusif berkualitas tinggi, cocok untuk hadiah profesional.' },
	{ id: 57, name: 'Pin',                  category: 'souvenir', emoji: '📌', tags: [],          desc: 'Aksesori kecil custom sesuai desain, populer untuk komunitas dan promosi.' },
	{ id: 58, name: 'Casing Handphone',     category: 'souvenir', emoji: '📱', tags: ['Populer'], desc: 'Pelindung ponsel dengan desain unik atau logo brand pilihan sendiri.' },
	{ id: 59, name: 'Gantungan Kunci',      category: 'souvenir', emoji: '🔑', tags: [],          desc: 'Aksesori kunci atau tas custom, diminati semua kalangan untuk merchandise.' },
	{ id: 60, name: 'Tumbler',              category: 'souvenir', emoji: '🧃', tags: ['Populer'], desc: 'Botol minum stylish dan ramah lingkungan, bisa dicetak nama atau logo.' },
	{ id: 61, name: 'Kipas Promosi',        category: 'souvenir', emoji: '🌀', tags: [],          desc: 'Kipas custom berlogo, praktis untuk disebar di acara outdoor berskala besar.' },
	{ id: 62, name: 'Travel Bag',           category: 'souvenir', emoji: '🧳', tags: [],          desc: 'Tas perjalanan tahan lama dengan desain stylish, cocok untuk merchandise.' },

	// ─── 👕 TEXTILE ───
	{ id: 63, name: 'Jersey',               category: 'textile',  emoji: '🥋', tags: ['Populer'], desc: 'Seragam olahraga custom full-color, paling banyak diminati di kategori tekstil.' },
	{ id: 64, name: 'Kaos',                 category: 'textile',  emoji: '👕', tags: ['Populer'], desc: 'Pakaian kasual dengan berbagai pilihan desain dan gambar custom.' },
	{ id: 65, name: 'Hijab',                category: 'textile',  emoji: '🧕', tags: [],          desc: 'Kerudung custom dari berbagai bahan, memadukan fungsi dan tren fashion.' },
	{ id: 66, name: 'Bantal',               category: 'textile',  emoji: '🛋️', tags: [],          desc: 'Bantal empuk dengan cetak gambar atau desain custom, cocok sebagai hadiah.' },
	{ id: 67, name: 'Sarung Bantal & Sprei',category: 'textile',  emoji: '🛏️', tags: [],          desc: 'Perlengkapan tidur bermotif cantik hasil cetak digital berkualitas.' },
	{ id: 68, name: 'Tote Bag',             category: 'textile',  emoji: '👜', tags: ['Populer'], desc: 'Tas serbaguna bahan kuat dengan desain custom, ramah lingkungan.' },
	{ id: 69, name: 'Masker',               category: 'textile',  emoji: '😷', tags: [],          desc: 'Masker kain berdesain cute atau keren, tetap diminati sebagai aksesori gaya.' },
	{ id: 70, name: 'Topi',                 category: 'textile',  emoji: '🧢', tags: ['Populer'], desc: 'Topi custom dengan nama atau gambar pilihan, bisa jadi hadiah personal.' },
	{ id: 71, name: 'Batik Printing',       category: 'textile',  emoji: '🎨', tags: ['Baru'],    desc: 'Kain bermotif batik hasil cetak digital, cepat dan berkualitas tinggi.' },
	{ id: 72, name: 'Sepatu Printing',      category: 'textile',  emoji: '👟', tags: ['Baru'],    desc: 'Sepatu dengan desain cetak variatif dan unik, cocok untuk merchandise.' },

	// ─── 🏭 INDUSTRI ───
	{ id: 73, name: 'Kemasan Produk',       category: 'industri', emoji: '📦', tags: ['Populer'], desc: 'Packaging custom untuk berbagai jenis produk, fungsi perlindungan sekaligus branding.' },
	{ id: 74, name: 'Paper Cup',            category: 'industri', emoji: '☕', tags: [],          desc: 'Gelas kertas custom berlogo, cocok untuk acara komunitas dan minuman takeaway.' },
	{ id: 75, name: 'Box Makanan',          category: 'industri', emoji: '🍱', tags: ['Populer'], desc: 'Kemasan makanan tahan lama untuk katering, restoran, atau pesanan massal.' },
	{ id: 76, name: 'Label',                category: 'industri', emoji: '🏷️', tags: ['Populer'], desc: 'Stiker informasi produk berdesain menarik untuk meningkatkan daya tarik konsumen.' },
	{ id: 77, name: 'Rigid Box',            category: 'industri', emoji: '🎁', tags: ['Baru'],    desc: 'Kotak premium kokoh dengan finishing mewah untuk produk high-end atau hampers.' },
	{ id: 78, name: 'Botol Plastik Printing',category: 'industri',emoji: '🍶', tags: [],          desc: 'Botol minum berdesain trendi dan unik, cocok untuk merchandise atau promosi.' },
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
