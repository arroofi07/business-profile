<script lang="ts">
	import { onMount } from 'svelte';

	// ── Product data ──────────────────────────────────────────────
	const allProducts = [
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

	const categories = [
		{ key: 'semua', label: 'Semua' },
		{ key: 'spanduk', label: 'Spanduk' },
		{ key: 'baliho', label: 'Baliho' },
		{ key: 'stiker', label: 'Stiker' },
		{ key: 'kartu-nama', label: 'Kartu Nama' },
		{ key: 'banner', label: 'Banner' },
		{ key: 'lainnya', label: 'Lainnya' }
	];

	// ── Reactive state ────────────────────────────────────────────
	let searchQuery = $state('');
	let activeCategory = $state('semua');
	let sortOrder = $state('populer');
	let mobileNavOpen = $state(false);
	let openFaq = $state<number | null>(null);

	// ── Derived: filtered + sorted products ──────────────────────
	const filteredProducts = $derived(() => {
		let list = allProducts.filter((p) => {
			const matchCat = activeCategory === 'semua' || p.category === activeCategory;
			const matchSearch =
				p.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
				p.desc.toLowerCase().includes(searchQuery.toLowerCase());
			return matchCat && matchSearch;
		});
		if (sortOrder === 'populer') {
			list = [...list].sort(
				(a, b) => (b.tags.includes('Populer') ? 1 : 0) - (a.tags.includes('Populer') ? 1 : 0)
			);
		} else if (sortOrder === 'baru') {
			list = [...list].sort(
				(a, b) => (b.tags.includes('Baru') ? 1 : 0) - (a.tags.includes('Baru') ? 1 : 0)
			);
		}
		return list;
	});

	// ── Animated counters ─────────────────────────────────────────
	let statCounter = $state({ products: 0, clients: 0, years: 0, quality: 0 });
	const statTargets = { products: 100, clients: 1000, years: 7, quality: 100 };

	function animateCounters() {
		const duration = 2000;
		const step = 16;
		const steps = duration / step;
		let frame = 0;
		const timer = setInterval(() => {
			frame++;
			const progress = Math.min(frame / steps, 1);
			const ease = 1 - Math.pow(1 - progress, 3);
			statCounter = {
				products: Math.round(statTargets.products * ease),
				clients: Math.round(statTargets.clients * ease),
				years: Math.round(statTargets.years * ease),
				quality: Math.round(statTargets.quality * ease)
			};
			if (frame >= steps) clearInterval(timer);
		}, step);
	}

	// ── WhatsApp link helper ─────────────────────────────────────
	const WA_NUMBER = '6282170716039';
	function waLink(msg = '') {
		return `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(msg)}`;
	}

	function waProduct(name: string) {
		return waLink(
			`Halo DRV Digital Printing, saya ingin memesan *${name}*. Bisa info lebih lanjut?`
		);
	}

	const waGeneral = waLink(
		'Halo DRV Digital Printing, saya ingin berkonsultasi mengenai produk cetak. Bisa bantu?'
	);

	// ── FAQ data ─────────────────────────────────────────────────
	const faqs = [
		{
			q: 'Berapa lama proses cetak?',
			a: 'Umumnya 1–3 hari kerja tergantung jenis & ukuran produk. Untuk order urgent bisa kami usahakan lebih cepat — hubungi kami langsung.'
		},
		{
			q: 'Apakah bisa custom ukuran?',
			a: 'Tentu! Kami melayani cetak dengan ukuran custom sesuai kebutuhan Anda. Cukup informasikan ukuran yang diinginkan saat order.'
		},
		{
			q: 'Format file apa yang diterima?',
			a: 'Kami menerima file CDR (CorelDRAW), AI (Illustrator), PDF, dan JPG/PNG dengan resolusi minimal 150 dpi. Format vektor sangat direkomendasikan.'
		},
		{
			q: 'Apakah ada layanan antar ke rumah?',
			a: 'Ada! Kami melayani pengiriman ke seluruh wilayah Kota Padang & sekitarnya. Ongkos kirim menyesuaikan jarak & berat produk.'
		},
		{
			q: 'Bagaimana cara pembayaran?',
			a: 'Kami menerima pembayaran via transfer bank (BCA, BRI, Mandiri), QRIS, dan cash. DP 50% untuk order custom, pelunasan sebelum pengambilan.'
		},
		{
			q: 'Apakah ada harga grosir?',
			a: 'Ya, tersedia harga spesial untuk order dalam jumlah besar. Silakan hubungi kami via WhatsApp untuk negosiasi harga grosir.'
		}
	];

	// ── Testimonials ─────────────────────────────────────────────
	const testimonials = [
		{
			name: 'Budi Santoso',
			role: 'Pemilik Toko Baju',
			text: 'Spanduk dari DRV kualitasnya bagus banget, warnanya tajam dan tahan lama. Udah langganan dari 2022!',
			stars: 5
		},
		{
			name: 'Rina Marlina',
			role: 'Event Organizer',
			text: 'Backdrop photobooth-nya memuaskan, bahan tebal dan gambar HD. Proses cepat, tim DRV juga responsif.',
			stars: 5
		},
		{
			name: 'Agus Firmansyah',
			role: 'UMKM Kuliner',
			text: 'Label produk saya dicetak di sini, hasilnya profesional dan rapih. Harga juga bersaing untuk kualitas segini.',
			stars: 5
		},
		{
			name: 'Sari Dewi',
			role: 'Mahasiswi',
			text: 'Pesan kartu nama wisuda di DRV, hasilnya beyond expectation! Kertasnya tebal, warnanya cantik.',
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
			text: 'Cetak banner acara sekolah di DRV, komunikatif dan hasilnya rapi. Harga ramah di kantong.',
			stars: 5
		}
	];

	// ── Intersection Observer for counter ────────────────────────
	onMount(() => {
		const el = document.getElementById('stats-section');
		if (!el) return;
		const obs = new IntersectionObserver(
			(entries) => {
				if (entries[0].isIntersecting) {
					animateCounters();
					obs.disconnect();
				}
			},
			{ threshold: 0.4 }
		);
		obs.observe(el);
	});
</script>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  NAVBAR                                                      -->
<!-- ════════════════════════════════════════════════════════════ -->
<header
	class="glass-dark fixed top-0 right-0 left-0 z-50 overflow-hidden"
	style="border-bottom:1px solid rgba(190,24,93,0.18);"
>
	<nav
		class="mx-auto flex max-w-7xl items-center justify-between px-6"
		style="height:var(--nav-height);"
	>
		<!-- Logo -->
		<a href="#hero" class="group flex items-center gap-3">
			<div
				class="flex h-10 w-10 items-center justify-center rounded-lg text-xl"
				style="background:var(--drv-gradient-blue); box-shadow:var(--drv-glow-blue);"
			>
				🖨️
			</div>
			<div>
				<div class="font-display font-700 text-lg leading-tight" style="color:var(--drv-white);">
					DRV <span style="color:var(--drv-blue)">Digital</span>
				</div>
				<div class="font-mono text-xs tracking-widest" style="color:var(--drv-gray);">
					PRINTING PADANG
				</div>
			</div>
		</a>

		<!-- Desktop nav -->
		<div class="hidden items-center gap-8 md:flex">
			{#each [['#produk', 'Produk'], ['#harga', 'Harga'], ['#cara-pesan', 'Cara Pesan'], ['#tentang', 'Tentang'], ['#kontak', 'Kontak']] as [href, label]}
				<a
					{href}
					class="font-500 text-sm transition-colors duration-200 hover:text-sky-400"
					style="color:var(--drv-gray-light);">{label}</a
				>
			{/each}
		</div>

		<!-- CTA + Open badge -->
		<div class="hidden items-center gap-4 md:flex">
			<div
				class="flex items-center gap-2 rounded-full px-3 py-1.5 font-mono text-xs"
				style="background:rgba(34,197,94,0.1); border:1px solid rgba(34,197,94,0.3); color:#4ade80;"
			>
				<span class="animate-ping-blue inline-block h-2 w-2 rounded-full bg-green-400"></span>
				BUKA
			</div>
			<a href={waGeneral} target="_blank" class="btn-primary-drv text-sm">Order Sekarang →</a>
		</div>

		<!-- Mobile hamburger -->
		<button
			class="p-2 md:hidden"
			onclick={() => (mobileNavOpen = !mobileNavOpen)}
			aria-label="Toggle nav"
		>
			<div class="mb-1.5 h-0.5 w-6 transition-all" style="background:var(--drv-blue);"></div>
			<div class="mb-1.5 h-0.5 w-4" style="background:var(--drv-blue);"></div>
			<div class="h-0.5 w-6" style="background:var(--drv-blue);"></div>
		</button>
	</nav>

	<!-- Mobile menu -->
	{#if mobileNavOpen}
		<div class="glass-dark animate-slide-down flex flex-col gap-4 px-6 py-4 md:hidden">
			{#each [['#produk', 'Produk'], ['#harga', 'Harga'], ['#cara-pesan', 'Cara Pesan'], ['#tentang', 'Tentang'], ['#kontak', 'Kontak']] as [href, label]}
				<a
					{href}
					class="font-500 border-b py-2 text-sm"
					onclick={() => (mobileNavOpen = false)}
					style="color:var(--drv-gray-light); border-color:rgba(14,165,233,0.1);">{label}</a
				>
			{/each}
			<a href={waGeneral} target="_blank" class="btn-primary-drv mt-2 text-center text-sm"
				>Order Sekarang →</a
			>
		</div>
	{/if}
</header>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  HERO                                                        -->
<!-- ════════════════════════════════════════════════════════════ -->
<section
	id="hero"
	class="circuit-pattern relative flex min-h-screen items-center overflow-hidden"
	style="background:var(--drv-bg-deep); padding-top:var(--nav-height);"
>
	<!-- Scan-line overlay -->
	<div class="pointer-events-none absolute inset-0 overflow-hidden">
		<div
			class="animate-scan-line absolute right-0 left-0 h-px opacity-30"
			style="background:linear-gradient(90deg,transparent,var(--drv-blue),transparent); top:0;"
		></div>
	</div>

	<!-- Glowing orbs background -->
	<div
		class="pointer-events-none absolute top-1/4 left-1/4 h-96 w-96 rounded-full"
		style="background:radial-gradient(circle, rgba(14,165,233,0.12) 0%, transparent 70%); filter:blur(40px);"
	></div>
	<div
		class="pointer-events-none absolute right-1/4 bottom-1/4 h-80 w-80 rounded-full"
		style="background:radial-gradient(circle, rgba(249,115,22,0.10) 0%, transparent 70%); filter:blur(40px);"
	></div>

	<div
		class="relative z-10 mx-auto grid w-full max-w-7xl items-center gap-16 px-6 py-20 lg:grid-cols-2"
	>
		<!-- Left: copy -->
		<div>
			<div
				class="font-600 animate-slide-up mb-6 inline-flex items-center gap-2 rounded-full px-4 py-2 font-mono text-xs"
				style="background:rgba(14,165,233,0.1); border:1px solid rgba(14,165,233,0.3); color:var(--drv-blue);"
			>
				<span>●</span> JASA CETAK DIGITAL PROFESIONAL — PADANG
			</div>
			<h1
				class="font-display font-700 animate-slide-up mb-6 leading-tight delay-100"
				style="font-size:clamp(2.5rem,6vw,4rem); color:var(--drv-white);"
			>
				Cetak Impian Anda,<br />
				Dengan <span class="gradient-text-shimmer">Presisi</span><br />
				<span style="color:var(--drv-orange);">Digital</span>
			</h1>
			<p
				class="animate-slide-up mb-8 max-w-lg text-lg delay-200"
				style="color:var(--drv-gray-light); line-height:1.75;"
			>
				Spanduk, Baliho, Stiker, Kartu Nama & lebih dari 100 produk cetak berkualitas tinggi. Harga
				terjangkau, hasil profesional, tepat waktu.
			</p>
			<div class="animate-slide-up flex flex-col gap-3 delay-300 sm:flex-row sm:flex-wrap sm:gap-4">
				<a href="#produk" class="btn-primary-drv w-full text-center sm:w-auto">Lihat Produk ↓</a>
				<a href={waGeneral} target="_blank" class="btn-whatsapp flex w-full items-center justify-center gap-2 sm:w-auto">
					<span>💬</span> Hubungi via WhatsApp
				</a>
			</div>

			<!-- Floating stats -->
			<div class="animate-slide-up mt-10 flex gap-6 delay-500 sm:mt-12 sm:gap-8">
				<div>
					<div class="font-display font-700 text-2xl sm:text-3xl" style="color:var(--drv-blue);">100+</div>
					<div class="text-xs" style="color:var(--drv-gray);">Produk Cetak</div>
				</div>
				<div style="width:1px; background:rgba(190,24,93,0.2);"></div>
				<div>
					<div class="font-display font-700 text-2xl sm:text-3xl" style="color:var(--drv-cyan);">1K+</div>
					<div class="text-xs" style="color:var(--drv-gray);">Pelanggan Puas</div>
				</div>
				<div style="width:1px; background:rgba(190,24,93,0.2);"></div>
				<div>
					<div class="font-display font-700 text-2xl sm:text-3xl" style="color:var(--drv-orange);">⭐ 5.0</div>
					<div class="text-xs" style="color:var(--drv-gray);">Rating Pelanggan</div>
				</div>
			</div>
		</div>

		<!-- Right: visual card -->
		<div class="animate-scale-reveal hidden justify-center delay-300 lg:flex">
			<div class="relative w-full max-w-md">
				<div class="neon-border-blue glass-card animate-float-tech rounded-2xl p-8">
					<div class="mb-4 text-center text-6xl">🖨️</div>
					<div
						class="font-display font-700 mb-2 text-center text-2xl"
						style="color:var(--drv-white);"
					>
						DRV Digital Printing
					</div>
					<div class="mb-6 text-center text-sm" style="color:var(--drv-gray);">
						Jl. Raya Ampang, depan Es Teh Indonesia, Kota Padang
					</div>
					<div class="grid grid-cols-2 gap-3">
						{#each ['Spanduk', 'Baliho', 'Stiker Label', 'Kartu Nama', 'Roll Banner', 'ID Card'] as p}
							<div
								class="rounded-lg px-3 py-2 text-center font-mono text-xs"
								style="background:rgba(14,165,233,0.08); border:1px solid rgba(14,165,233,0.15); color:var(--drv-blue-glow);"
							>
								{p}
							</div>
						{/each}
					</div>
					<div
						class="font-600 mt-4 flex items-center justify-center gap-2 text-sm"
						style="color:#4ade80;"
					>
						<span class="h-2 w-2 rounded-full bg-green-400"></span>
						Senin – Sabtu • 09:00 – 17:30
					</div>
				</div>
				<!-- Decorative rings -->
				<div
					class="animate-spin-slow absolute -top-4 -right-4 h-16 w-16 rounded-full border opacity-30"
					style="border-color:var(--drv-blue);"
				></div>
				<div
					class="animate-spin-slow absolute -bottom-4 -left-4 h-10 w-10 rounded-full border opacity-20 delay-300"
					style="border-color:var(--drv-orange); animation-direction:reverse;"
				></div>
			</div>
		</div>
	</div>
</section>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  STATS BAR                                                   -->
<!-- ════════════════════════════════════════════════════════════ -->
<section
	id="stats-section"
	class="py-12"
	style="background:var(--drv-bg-mid); border-top:1px solid rgba(14,165,233,0.1); border-bottom:1px solid rgba(14,165,233,0.1);"
>
	<div class="mx-auto grid max-w-5xl grid-cols-2 gap-8 px-6 md:grid-cols-4">
		{#each [{ label: 'Jenis Produk', val: statCounter.products, suffix: '+', color: 'var(--drv-blue)' }, { label: 'Pelanggan Puas', val: statCounter.clients, suffix: '+', color: 'var(--drv-cyan)' }, { label: 'Tahun Pengalaman', val: statCounter.years, suffix: '', color: 'var(--drv-orange)' }, { label: 'Kualitas Terjamin', val: statCounter.quality, suffix: '%', color: 'var(--drv-yellow)' }] as s}
			<div class="text-center">
				<div class="font-display font-700 mb-1" style="font-size:2.5rem; color:{s.color};">
					{s.val}{s.suffix}
				</div>
				<div class="font-500 text-sm" style="color:var(--drv-gray);">{s.label}</div>
			</div>
		{/each}
	</div>
</section>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  PRODUCT CATALOG                                             -->
<!-- ════════════════════════════════════════════════════════════ -->
<section id="produk" class="py-24" style="background:var(--drv-bg-deep);">
	<div class="mx-auto max-w-7xl px-6">
		<!-- Section heading -->
		<div class="mb-14 text-center">
			<div
				class="font-600 mb-4 inline-block rounded-full px-4 py-1.5 font-mono text-xs"
				style="background:rgba(14,165,233,0.1); border:1px solid rgba(14,165,233,0.2); color:var(--drv-blue);"
			>
				KATALOG PRODUK
			</div>
			<h2
				class="font-display font-700 mb-4"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--drv-white);"
			>
				Semua Solusi Cetak <span class="gradient-text-blue">Anda</span>
			</h2>
			<p class="mx-auto max-w-xl" style="color:var(--drv-gray);">
				Temukan produk yang Anda butuhkan. Kualitas premium, harga bersaing, dikerjakan oleh tim
				berpengalaman.
			</p>
		</div>

		<!-- Search + Sort row -->
		<div class="mb-6 flex flex-col gap-4 md:flex-row">
			<!-- Search -->
			<div class="relative flex-1">
				<span class="absolute top-1/2 left-4 -translate-y-1/2 text-lg">🔍</span>
				<input
					type="text"
					bind:value={searchQuery}
					placeholder="Cari produk cetak..."
					class="font-500 w-full rounded-xl py-3.5 pr-4 pl-12 text-sm transition-all duration-300 outline-none"
					style="background:var(--drv-bg-card); border:1px solid rgba(14,165,233,0.2); color:var(--drv-white); font-family:'Inter',sans-serif;"
					onfocus={(e) => { e.currentTarget.style.borderColor='rgba(14,165,233,0.6)'; e.currentTarget.style.boxShadow='0 0 0 3px rgba(14,165,233,0.1)'; }}
					onblur={(e)  => { e.currentTarget.style.borderColor='rgba(14,165,233,0.2)'; e.currentTarget.style.boxShadow='none'; }}
				/>
			</div>
			<!-- Sort -->
			<select
				bind:value={sortOrder}
				class="font-500 cursor-pointer rounded-xl px-4 py-3.5 text-sm outline-none"
				style="background:var(--drv-bg-card); border:1px solid rgba(14,165,233,0.2); color:var(--drv-white); font-family:'Inter',sans-serif; min-width:160px;"
			>
				<option value="populer">⭐ Terpopuler</option>
				<option value="baru">🆕 Terbaru</option>
				<option value="default">🔤 Default</option>
			</select>
		</div>

		<!-- Category filter tabs - horizontal scroll on mobile -->
		<div class="mb-10 -mx-6 px-6 overflow-x-auto sm:mx-0 sm:px-0">
			<div class="flex gap-2 pb-2 sm:flex-wrap sm:pb-0" style="min-width:max-content;">
			{#each categories as cat}
				<button
					onclick={() => (activeCategory = cat.key)}
					class="font-600 font-display cursor-pointer rounded-full px-5 py-2 text-sm transition-all duration-250 shrink-0"
					style={activeCategory === cat.key
						? 'background:var(--drv-gradient-blue); color:#fff; box-shadow:var(--drv-glow-blue);'
						: 'background:var(--drv-bg-card); color:var(--drv-gray-light); border:1px solid rgba(190,24,93,0.2);'}
					>{cat.label}</button
				>
			{/each}
			</div>
		</div>

		<!-- Product grid -->
		{#if filteredProducts().length === 0}
			<div class="py-20 text-center">
				<div class="mb-4 text-5xl">🔍</div>
				<div class="font-display font-600 mb-2 text-xl" style="color:var(--drv-white);">
					Produk tidak ditemukan
				</div>
				<div style="color:var(--drv-gray);">Coba kata kunci atau kategori lain</div>
			</div>
		{:else}
			<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
				{#each filteredProducts() as product (product.id)}
					<div class="card-tech flex flex-col gap-4 rounded-2xl p-6">
						<!-- Icon + badges -->
						<div class="flex items-start justify-between">
							<div
								class="flex h-14 w-14 items-center justify-center rounded-xl text-3xl"
								style="background:rgba(14,165,233,0.08); border:1px solid rgba(14,165,233,0.15);"
							>
								{product.emoji}
							</div>
							<div class="flex flex-col items-end gap-1">
								{#each product.tags as tag}
									{#if tag === 'Populer'}
										<span class="badge-popular">{tag}</span>
									{:else if tag === 'Baru'}
										<span class="badge-new">{tag}</span>
									{/if}
								{/each}
							</div>
						</div>
						<!-- Info -->
						<div class="flex-1">
							<h3 class="font-display font-700 mb-1 text-base" style="color:var(--drv-white);">
								{product.name}
							</h3>
							<p class="text-xs leading-relaxed" style="color:var(--drv-gray);">{product.desc}</p>
						</div>
						<!-- Price + CTA -->
						<div>
							<div class="font-600 mb-3 font-mono text-sm" style="color:var(--drv-blue-glow);">
								{product.price}
							</div>
							<a
								href={waProduct(product.name)}
								target="_blank"
								class="font-600 font-display block w-full rounded-xl py-2.5 text-center text-sm transition-all duration-250 hover:-translate-y-0.5"
								style="background:rgba(14,165,233,0.1); border:1px solid rgba(14,165,233,0.3); color:var(--drv-blue);"
								onmouseenter={(e) => { e.currentTarget.style.background='rgba(14,165,233,0.2)'; e.currentTarget.style.boxShadow='0 0 12px rgba(14,165,233,0.3)'; }}
								onmouseleave={(e) => { e.currentTarget.style.background='rgba(14,165,233,0.1)'; e.currentTarget.style.boxShadow='none'; }}
								>💬 Pesan Sekarang</a
							>
						</div>
					</div>
				{/each}
			</div>
		{/if}

		<!-- Result count -->
		{#if filteredProducts().length > 0}
			<p class="mt-8 text-center font-mono text-sm" style="color:var(--drv-gray);">
				Menampilkan <span style="color:var(--drv-blue);">{filteredProducts().length}</span> dari {allProducts.length}
				produk
			</p>
		{/if}
	</div>
</section>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  HOW IT WORKS                                               -->
<!-- ════════════════════════════════════════════════════════════ -->
<section id="cara-pesan" class="py-24" style="background:var(--drv-bg-mid);">
	<div class="mx-auto max-w-6xl px-6">
		<div class="mb-16 text-center">
			<div
				class="font-600 mb-4 inline-block rounded-full px-4 py-1.5 font-mono text-xs"
				style="background:rgba(249,115,22,0.1); border:1px solid rgba(249,115,22,0.25); color:var(--drv-orange);"
			>
				CARA PESAN
			</div>
			<h2
				class="font-display font-700 mb-4"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--drv-white);"
			>
				4 Langkah <span class="gradient-text-orange">Mudah</span>
			</h2>
			<p style="color:var(--drv-gray);">
				Pesan cetakan Anda dengan proses yang simpel dan transparan.
			</p>
		</div>

		<div class="relative grid grid-cols-1 gap-8 md:grid-cols-4">
			<!-- Connector line desktop only -->
			<div
				class="absolute right-[12%] left-[12%] hidden h-px md:block"
				style="background:linear-gradient(90deg, transparent, var(--drv-blue), var(--drv-cyan), var(--drv-blue), transparent); top:36px;"
			></div>

			{#each [{ step: '01', emoji: '💬', title: 'Konsultasi', desc: 'Hubungi kami via WhatsApp, ceritakan kebutuhan cetak Anda.', color: 'var(--drv-blue)' }, { step: '02', emoji: '🎨', title: 'Desain & File', desc: 'Kirim file desain Anda, atau minta tim kami untuk membantu.', color: 'var(--drv-cyan)' }, { step: '03', emoji: '✅', title: 'Konfirmasi Order', desc: 'Setujui harga, spesifikasi, dan estimasi waktu produksi.', color: 'var(--drv-orange)' }, { step: '04', emoji: '📦', title: 'Ambil / Dikirim', desc: 'Produk siap diambil di toko atau kami antar ke lokasi Anda.', color: 'var(--drv-yellow)' }] as step, i}
				<div
					class="animate-slide-up relative flex flex-col items-center text-center"
					style="animation-delay:{i * 0.15}s;"
				>
					<div
						class="relative z-10 mb-4 flex h-20 w-20 items-center justify-center rounded-full text-3xl"
						style="background:var(--drv-bg-card); border:2px solid {step.color}; box-shadow:0 0 16px {step.color}3a;"
					>
						{step.emoji}
					</div>
					<div class="font-600 mb-2 font-mono text-xs" style="color:{step.color};">
						LANGKAH {step.step}
					</div>
					<h3 class="font-display font-700 mb-2 text-lg" style="color:var(--drv-white);">
						{step.title}
					</h3>
					<p class="text-sm leading-relaxed" style="color:var(--drv-gray);">{step.desc}</p>
				</div>
			{/each}
		</div>

		<div class="mt-12 text-center">
			<a href={waGeneral} target="_blank" class="btn-primary-drv inline-block"
				>Mulai Order Sekarang →</a
			>
		</div>
	</div>
</section>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  PRICING                                                     -->
<!-- ════════════════════════════════════════════════════════════ -->
<section id="harga" class="py-24" style="background:var(--drv-bg-deep);">
	<div class="mx-auto max-w-5xl px-6">
		<div class="mb-16 text-center">
			<div
				class="font-600 mb-4 inline-block rounded-full px-4 py-1.5 font-mono text-xs"
				style="background:rgba(14,165,233,0.1); border:1px solid rgba(14,165,233,0.2); color:var(--drv-blue);"
			>
				ESTIMASI HARGA
			</div>
			<h2
				class="font-display font-700 mb-4"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--drv-white);"
			>
				Harga <span class="gradient-text-blue">Transparan</span>
			</h2>
			<p style="color:var(--drv-gray);">
				Kami memberikan harga terbaik tanpa biaya tersembunyi. Harga bisa menyesuaikan spesifikasi &
				kuantitas.
			</p>
		</div>

		<div class="grid gap-8 md:grid-cols-3">
			{#each [{ tier: 'Basic', icon: '🏷️', color: 'var(--drv-cyan)', desc: 'Cocok untuk kebutuhan cetak kecil & personal', items: ['Kartu Nama (100pcs) mulai Rp 30rb', 'Stiker Cutting mulai Rp 15rb', 'Poster A3 mulai Rp 5rb/lembar', 'ID Card mulai Rp 10rb/pcs'], cta: 'Tanya Harga Basic', featured: false }, { tier: 'Standard', icon: '⭐', color: 'var(--drv-blue)', desc: 'Pilihan terbaik untuk promosi bisnis Anda', items: ['Spanduk PVC mulai Rp 25rb/m²', 'Roll Banner mulai Rp 150rb', 'X-Banner mulai Rp 85rb', 'Backdrop mulai Rp 80rb/m²'], cta: 'Tanya Harga Standard', featured: true }, { tier: 'Premium', icon: '💎', color: 'var(--drv-orange)', desc: 'Untuk event besar, proyek & order massal', items: ['Baliho Outdoor mulai Rp 45rb/m²', 'Custom ukuran besar', 'Nota / Bon custom Rp 45rb/buku', 'Harga grosir (diskusi)'], cta: 'Tanya Harga Premium', featured: false }] as plan}
				<div
					class="relative flex flex-col gap-5 rounded-2xl p-7 transition-all duration-300 hover:-translate-y-2"
					style={plan.featured
						? 'background:linear-gradient(145deg,#0F1E38,#111827); border:1px solid ' +
							plan.color +
							'; box-shadow:0 0 30px rgba(14,165,233,0.2);'
						: 'background:var(--drv-bg-card); border:1px solid rgba(14,165,233,0.1);'}
				>
					{#if plan.featured}
						<div
							class="font-700 absolute -top-3 left-1/2 -translate-x-1/2 rounded-full px-4 py-1 font-mono text-xs"
							style="background:var(--drv-gradient-blue); color:#fff;"
						>
							PALING POPULER
						</div>
					{/if}
					<div class="text-4xl">{plan.icon}</div>
					<div>
						<h3 class="font-display font-700 mb-1 text-2xl" style="color:{plan.color};">
							{plan.tier}
						</h3>
						<p class="text-sm" style="color:var(--drv-gray);">{plan.desc}</p>
					</div>
					<ul class="flex flex-1 flex-col gap-2">
						{#each plan.items as item}
							<li class="flex items-start gap-2 text-sm" style="color:var(--drv-gray-light);">
								<span style="color:{plan.color}; flex-shrink:0; margin-top:1px;">✓</span>
								{item}
							</li>
						{/each}
					</ul>
					<a
						href={waLink(`Halo DRV, saya mau tanya harga paket *${plan.tier}*`)}
						target="_blank"
						class="font-700 font-display block w-full rounded-xl py-3 text-center text-sm transition-all duration-250"
						style={plan.featured
							? 'background:var(--drv-gradient-blue); color:#fff;'
							: 'background:transparent; border:1px solid ' +
								plan.color +
								'; color:' +
								plan.color +
								';'}
						onmouseenter={(e) => { e.currentTarget.style.opacity='0.85'; }}
						onmouseleave={(e) => { e.currentTarget.style.opacity='1'; }}>{plan.cta}</a
					>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  ABOUT                                                       -->
<!-- ════════════════════════════════════════════════════════════ -->
<section id="tentang" class="circuit-pattern py-24" style="background:var(--drv-bg-mid);">
	<div class="mx-auto grid max-w-6xl items-center gap-16 px-6 lg:grid-cols-2">
		<!-- Visual -->
		<div class="flex flex-col gap-4">
			<div class="glass-card neon-border-blue animate-float-tech rounded-2xl p-8 text-center">
				<div class="mb-4 text-7xl">🖨️</div>
				<div class="font-display font-700 mb-1 text-xl" style="color:var(--drv-white);">
					DRV Digital Printing
				</div>
				<div class="font-mono text-sm" style="color:var(--drv-blue);">Padang, Sumatera Barat</div>
			</div>
			<div class="grid grid-cols-2 gap-4">
				{#each [{ icon: '🔵', label: 'Kualitas Tinggi', color: 'var(--drv-blue)' }, { icon: '⚡', label: 'Proses Cepat', color: 'var(--drv-cyan)' }, { icon: '💰', label: 'Harga Terjangkau', color: 'var(--drv-orange)' }, { icon: '🤝', label: 'Pelayanan Ramah', color: 'var(--drv-yellow)' }] as v}
					<div class="card-tech flex items-center gap-3 rounded-xl p-4">
						<span class="text-2xl">{v.icon}</span>
						<span class="font-600 text-sm" style="color:var(--drv-white);">{v.label}</span>
					</div>
				{/each}
			</div>
		</div>

		<!-- Copy -->
		<div>
			<div
				class="font-600 mb-4 inline-block rounded-full px-4 py-1.5 font-mono text-xs"
				style="background:rgba(14,165,233,0.1); border:1px solid rgba(14,165,233,0.2); color:var(--drv-blue);"
			>
				TENTANG KAMI
			</div>
			<h2
				class="font-display font-700 mb-6"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--drv-white);"
			>
				Mitra Cetak <span class="gradient-text-blue">Terpercaya</span><br />Kota Padang
			</h2>
			<div class="mb-8 flex flex-col gap-4">
				<p style="color:var(--drv-gray-light); line-height:1.8;">
					DRV Digital Printing hadir sebagai solusi cetak profesional untuk bisnis, UMKM, instansi,
					dan perorangan di Kota Padang dan sekitarnya.
				</p>
				<p style="color:var(--drv-gray-light); line-height:1.8;">
					Dengan pengalaman bertahun-tahun dan mesin cetak modern, kami berkomitmen menghadirkan
					produk berkualitas tinggi dengan harga yang bersaing dan ketepatan waktu yang dapat
					diandalkan.
				</p>
			</div>
			<div
				class="flex flex-col gap-3 rounded-xl p-5"
				style="background:var(--drv-bg-card); border:1px solid rgba(14,165,233,0.1);"
			>
				{#each [{ icon: '📍', label: 'Alamat', val: 'Jl. Raya Ampang, depan Es Teh Indonesia, Kota Padang' }, { icon: '📞', label: 'Telepon / WA', val: '082170716039' }, { icon: '🕐', label: 'Jam Operasional', val: 'Senin – Sabtu, 09:00 – 17:30 WIB' }, { icon: '📸', label: 'Instagram', val: '@drv.digitalprinting_padang' }] as info}
					<div class="flex items-start gap-3 text-sm">
						<span class="flex-shrink-0 text-lg">{info.icon}</span>
						<div>
							<div class="font-600 mb-0.5" style="color:var(--drv-blue);">{info.label}</div>
							<div style="color:var(--drv-gray-light);">{info.val}</div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  TESTIMONIALS                                                -->
<!-- ════════════════════════════════════════════════════════════ -->
<section class="py-24" style="background:var(--drv-bg-deep);">
	<div class="mx-auto max-w-7xl px-6">
		<div class="mb-14 text-center">
			<div
				class="font-600 mb-4 inline-block rounded-full px-4 py-1.5 font-mono text-xs"
				style="background:rgba(234,179,8,0.1); border:1px solid rgba(234,179,8,0.25); color:var(--drv-yellow);"
			>
				TESTIMONI
			</div>
			<h2
				class="font-display font-700 mb-4"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--drv-white);"
			>
				Kata Pelanggan <span class="gradient-text-orange">Kami</span>
			</h2>
		</div>
		<div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
			{#each testimonials as t, i}
				<div
					class="card-tech animate-slide-up flex flex-col gap-4 rounded-2xl p-6"
					style="animation-delay:{i * 0.1}s;"
				>
					<div class="flex gap-1">
						{#each Array(t.stars) as _}
							<span style="color:var(--drv-yellow);">★</span>
						{/each}
					</div>
					<p class="flex-1 text-sm leading-relaxed" style="color:var(--drv-gray-light);">
						"{t.text}"
					</p>
					<div
						class="flex items-center gap-3 pt-2"
						style="border-top:1px solid rgba(14,165,233,0.1);"
					>
						<div
							class="font-display font-700 flex h-10 w-10 items-center justify-center rounded-full text-sm"
							style="background:var(--drv-gradient-blue); color:#fff;"
						>
							{t.name[0]}
						</div>
						<div>
							<div class="font-600 text-sm" style="color:var(--drv-white);">{t.name}</div>
							<div class="text-xs" style="color:var(--drv-gray);">{t.role}</div>
						</div>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  FAQ                                                         -->
<!-- ════════════════════════════════════════════════════════════ -->
<section class="py-24" style="background:var(--drv-bg-mid);">
	<div class="mx-auto max-w-3xl px-6">
		<div class="mb-14 text-center">
			<div
				class="font-600 mb-4 inline-block rounded-full px-4 py-1.5 font-mono text-xs"
				style="background:rgba(14,165,233,0.1); border:1px solid rgba(14,165,233,0.2); color:var(--drv-blue);"
			>
				FAQ
			</div>
			<h2
				class="font-display font-700 mb-4"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--drv-white);"
			>
				Pertanyaan yang <span class="gradient-text-blue">Sering Ditanya</span>
			</h2>
		</div>
		<div class="flex flex-col gap-3">
			{#each faqs as faq, i}
				<div
					class="overflow-hidden rounded-2xl transition-all duration-300"
					style="background:var(--drv-bg-card); border:1px solid {openFaq === i
						? 'rgba(14,165,233,0.4)'
						: 'rgba(14,165,233,0.1)'};"
				>
					<button
						class="flex w-full cursor-pointer items-center justify-between gap-4 px-6 py-5 text-left"
						onclick={() => (openFaq = openFaq === i ? null : i)}
					>
						<span class="font-display font-600 text-base" style="color:var(--drv-white);"
							>{faq.q}</span
						>
						<span
							class="flex-shrink-0 text-xl transition-transform duration-300"
							style="color:var(--drv-blue); transform:{openFaq === i
								? 'rotate(45deg)'
								: 'rotate(0deg)'};">+</span
						>
					</button>
					{#if openFaq === i}
						<div class="animate-slide-down px-6 pb-5">
							<p class="text-sm leading-relaxed" style="color:var(--drv-gray-light);">{faq.a}</p>
						</div>
					{/if}
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  CONTACT                                                     -->
<!-- ════════════════════════════════════════════════════════════ -->
<section id="kontak" class="py-24" style="background:var(--drv-bg-deep);">
	<div class="mx-auto max-w-6xl px-6">
		<div class="mb-14 text-center">
			<div
				class="font-600 mb-4 inline-block rounded-full px-4 py-1.5 font-mono text-xs"
				style="background:rgba(14,165,233,0.1); border:1px solid rgba(14,165,233,0.2); color:var(--drv-blue);"
			>
				KONTAK
			</div>
			<h2
				class="font-display font-700 mb-4"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--drv-white);"
			>
				Hubungi <span class="gradient-text-blue">Kami</span>
			</h2>
			<p style="color:var(--drv-gray);">
				Kami siap membantu kebutuhan cetak Anda. Konsultasi gratis!
			</p>
		</div>

		<div class="grid items-start gap-10 lg:grid-cols-2">
			<!-- Contact cards -->
			<div class="flex flex-col gap-5">
				{#each [{ icon: '📱', title: 'WhatsApp', val: '082170716039', sub: 'Chat langsung dengan tim kami', href: waGeneral, btnLabel: 'Chat Sekarang', btnStyle: 'background:linear-gradient(135deg,#25D366,#128C7E); color:#fff;' }, { icon: '📍', title: 'Alamat', val: 'Jl. Raya Ampang', sub: 'Depan Es Teh Indonesia, Kota Padang', href: 'https://maps.google.com/?q=Jl.+Raya+Ampang,+Padang', btnLabel: 'Lihat di Maps', btnStyle: 'background:rgba(190,24,93,0.1); border:1px solid rgba(190,24,93,0.3); color:var(--drv-blue);' }, { icon: '📸', title: 'Instagram', val: '@drv.digitalprinting_padang', sub: 'Follow untuk update terbaru', href: 'https://www.instagram.com/drv.digitalprinting_padang/', btnLabel: 'Kunjungi IG', btnStyle: 'background:linear-gradient(135deg,#833AB4,#FD1D1D,#F77737); color:#fff;' }] as c}
					<div class="card-tech flex flex-col gap-4 rounded-2xl p-5 sm:flex-row sm:items-center sm:gap-5 sm:p-6">
						<div
							class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl text-2xl sm:h-14 sm:w-14 sm:text-3xl"
							style="background:var(--drv-bg-mid); border:1px solid rgba(190,24,93,0.15);"
						>
							{c.icon}
						</div>
						<div class="min-w-0 flex-1">
							<div class="mb-0.5 text-sm font-600" style="color:var(--drv-gray);">{c.title}</div>
							<div class="truncate font-display font-700" style="color:var(--drv-white);">{c.val}</div>
							<div class="mt-0.5 text-xs" style="color:var(--drv-gray);">{c.sub}</div>
						</div>
						<a
							href={c.href}
							target="_blank"
							class="shrink-0 rounded-xl px-4 py-2 text-center text-xs font-700 transition-all hover:-translate-y-0.5 sm:text-left"
							style={c.btnStyle}>{c.btnLabel}</a
						>
					</div>
				{/each}
				<!-- Hours -->
				<div class="card-tech rounded-2xl p-6">
					<div class="font-display font-700 mb-4 text-lg" style="color:var(--drv-white);">
						🕐 Jam Operasional
					</div>
					<div class="flex flex-col gap-2">
						{#each [{ day: 'Senin – Sabtu', hours: '09:00 – 17:30 WIB', open: true }, { day: 'Minggu', hours: 'Libur', open: false }] as row}
							<div
								class="flex items-center justify-between py-2 text-sm"
								style="border-bottom:1px solid rgba(14,165,233,0.08);"
							>
								<span style="color:var(--drv-gray-light);">{row.day}</span>
								<span
									class="font-600 font-mono"
									style="color:{row.open ? '#4ade80' : 'var(--drv-gray)'};">{row.hours}</span
								>
							</div>
						{/each}
					</div>
				</div>
			</div>

			<!-- Map embed -->
			<div class="neon-border-blue w-full overflow-hidden rounded-2xl" style="height:300px; min-height:300px;">
				<iframe
					src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3989.3!2d100.377!3d-0.903!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMMKwNTQnMTAuOCJTIDEwMMKwMjInMzcuMiJF!5e0!3m2!1sen!2sid!4v1!5m2!1sen!2sid"
					width="100%"
					height="100%"
					style="border:0; filter:invert(90%) hue-rotate(180deg); display:block;"
					allowfullscreen
					loading="lazy"
					title="Lokasi DRV Digital Printing Padang"
				></iframe>
			</div>
		</div>
	</div>
</section>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  FOOTER                                                      -->
<!-- ════════════════════════════════════════════════════════════ -->
<footer style="background:#060A14; border-top:1px solid rgba(14,165,233,0.15);">
	<div class="mx-auto max-w-7xl px-6 py-16">
		<div class="mb-12 grid grid-cols-1 gap-10 md:grid-cols-4">
			<!-- Brand -->
			<div class="md:col-span-2">
				<div class="mb-4 flex items-center gap-3">
					<div
						class="flex h-10 w-10 items-center justify-center rounded-lg text-xl"
						style="background:var(--drv-gradient-blue);"
					>
						🖨️
					</div>
					<div>
						<div class="font-display font-700 text-lg" style="color:var(--drv-white);">
							DRV <span style="color:var(--drv-blue);">Digital</span> Printing
						</div>
						<div class="font-mono text-xs tracking-widest" style="color:var(--drv-gray);">
							PADANG
						</div>
					</div>
				</div>
				<p class="mb-5 max-w-xs text-sm leading-relaxed" style="color:var(--drv-gray);">
					Cetak profesional, hasil berkualitas. Solusi cetak terpercaya untuk bisnis dan personal
					Anda di Kota Padang.
				</p>
				<div class="flex gap-3">
					<a
						href="https://www.instagram.com/drv.digitalprinting_padang/"
						target="_blank"
						class="flex h-10 w-10 items-center justify-center rounded-lg text-xl transition-all hover:-translate-y-1"
						style="background:linear-gradient(135deg,#833AB4,#FD1D1D,#F77737);">📸</a
					>
					<a
						href={waGeneral}
						target="_blank"
						class="flex h-10 w-10 items-center justify-center rounded-lg text-xl transition-all hover:-translate-y-1"
						style="background:linear-gradient(135deg,#25D366,#128C7E);">💬</a
					>
				</div>
			</div>

			<!-- Quick links -->
			<div>
				<div class="font-display font-700 mb-4" style="color:var(--drv-white);">Navigasi</div>
				<div class="flex flex-col gap-2">
					{#each [['#produk', 'Katalog Produk'], ['#harga', 'Estimasi Harga'], ['#cara-pesan', 'Cara Pesan'], ['#tentang', 'Tentang Kami'], ['#kontak', 'Kontak']] as [href, label]}
						<a
							{href}
							class="text-sm transition-colors hover:text-sky-400"
							style="color:var(--drv-gray);">{label}</a
						>
					{/each}
				</div>
			</div>

			<!-- Produk -->
			<div>
				<div class="font-display font-700 mb-4" style="color:var(--drv-white);">
					Produk Unggulan
				</div>
				<div class="flex flex-col gap-2">
					{#each ['Spanduk PVC', 'Baliho Outdoor', 'Stiker Label', 'Kartu Nama', 'Roll Banner', 'ID Card'] as p}
						<span class="text-sm" style="color:var(--drv-gray);">{p}</span>
					{/each}
				</div>
			</div>
		</div>

		<div class="section-divider mb-6"></div>

		<div
			class="flex flex-col items-center justify-between gap-4 text-sm md:flex-row"
			style="color:var(--drv-gray-dark);"
		>
			<span>© 2025 DRV Digital Printing Padang. All rights reserved.</span>
			<span class="font-mono text-xs">Jl. Raya Ampang, Kota Padang · 082170716039</span>
		</div>
	</div>
</footer>

<!-- ════════════════════════════════════════════════════════════ -->
<!--  FLOATING WhatsApp BUTTON                                    -->
<!-- ════════════════════════════════════════════════════════════ -->
<a
	href={waGeneral}
	target="_blank"
	class="animate-glow-pulse fixed right-6 bottom-6 z-50 flex h-14 w-14 items-center justify-center rounded-full text-2xl shadow-2xl transition-transform hover:scale-110"
	style="background:linear-gradient(135deg,#25D366,#128C7E); box-shadow:0 4px 20px rgba(37,211,102,0.5);"
	aria-label="Chat WhatsApp"
>
	💬
</a>
