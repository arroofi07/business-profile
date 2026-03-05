<script lang="ts">
	import { onMount } from 'svelte';

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

	let searchQuery = $state('');
	let activeCategory = $state('semua');
	let sortOrder = $state('populer');
	let mobileNavOpen = $state(false);
	let openFaq = $state<number | null>(null);
	let navScrolled = $state(false);

	// Typewriter
	const typeWords = ['Profesional', 'Berkualitas', 'Terpercaya', 'Terjangkau'];
	let typeText = $state(typeWords[0]);
	let typeFading = $state(false);

	// Particles
	let particles = $state<{ x: number; y: number; r: number; dx: number; dy: number; o: number }[]>(
		[]
	);
	let canvasEl = $state<HTMLCanvasElement | null>(null);

	const filteredProducts = $derived(() => {
		let list = allProducts.filter((p) => {
			const matchCat = activeCategory === 'semua' || p.category === activeCategory;
			const matchSearch =
				p.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
				p.desc.toLowerCase().includes(searchQuery.toLowerCase());
			return matchCat && matchSearch;
		});
		if (sortOrder === 'populer')
			list = [...list].sort(
				(a, b) => (b.tags.includes('Populer') ? 1 : 0) - (a.tags.includes('Populer') ? 1 : 0)
			);
		else if (sortOrder === 'baru')
			list = [...list].sort(
				(a, b) => (b.tags.includes('Baru') ? 1 : 0) - (a.tags.includes('Baru') ? 1 : 0)
			);
		return list;
	});

	let statCounter = $state({ products: 0, clients: 0, years: 0, followers: 0 });
	const statTargets = { products: 100, clients: 1149, years: 7, followers: 1149 };

	function animateCounters() {
		const duration = 2000,
			step = 16,
			steps = duration / step;
		let frame = 0;
		const timer = setInterval(() => {
			frame++;
			const ease = 1 - Math.pow(1 - Math.min(frame / steps, 1), 3);
			statCounter = {
				products: Math.round(statTargets.products * ease),
				clients: Math.round(statTargets.clients * ease),
				years: Math.round(statTargets.years * ease),
				followers: Math.round(statTargets.followers * ease)
			};
			if (frame >= steps) clearInterval(timer);
		}, step);
	}

	const WA_NUMBER = '6281166352 8'.replace(/\s/g, '');
	function waLink(msg = '') {
		return `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(msg)}`;
	}
	function waProduct(name: string) {
		return waLink(`Halo Smartprint Padang, saya ingin memesan *${name}*. Bisa info lebih lanjut?`);
	}
	const waGeneral = waLink(
		'Halo Smartprint Padang, saya ingin berkonsultasi mengenai produk cetak. Bisa bantu?'
	);

	const faqs = [
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

	const testimonials = [
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

	onMount(() => {
		// ── Animated counters ──
		const statsEl = document.getElementById('stats-section');
		if (statsEl) {
			const obs = new IntersectionObserver(
				(entries) => {
					if (entries[0].isIntersecting) {
						animateCounters();
						obs.disconnect();
					}
				},
				{ threshold: 0.4 }
			);
			obs.observe(statsEl);
		}

		// ── Scroll-reveal: add .sp-visible when element enters viewport ──
		const revealEls = document.querySelectorAll('.sp-reveal');
		const revealObs = new IntersectionObserver(
			(entries) => {
				entries.forEach((e) => {
					if (e.isIntersecting) {
						e.target.classList.add('sp-visible');
						revealObs.unobserve(e.target);
					}
				});
			},
			{ threshold: 0.12 }
		);
		revealEls.forEach((el) => revealObs.observe(el));

		// ── Nav shadow on scroll ──
		const onScroll = () => {
			navScrolled = window.scrollY > 30;
		};
		window.addEventListener('scroll', onScroll, { passive: true });

		// ── Typewriter loop ──
		let wordIdx = 0;
		const typeTimer = setInterval(() => {
			typeFading = true;
			setTimeout(() => {
				wordIdx = (wordIdx + 1) % typeWords.length;
				typeText = typeWords[wordIdx];
				typeFading = false;
			}, 400);
		}, 2800);

		// ── Canvas floating particles ──
		const canvas = canvasEl;
		if (canvas) {
			const ctx = canvas.getContext('2d')!;
			const resize = () => {
				canvas.width = canvas.offsetWidth;
				canvas.height = canvas.offsetHeight;
			};
			resize();
			window.addEventListener('resize', resize);
			const NUM = 38;
			let pts = Array.from({ length: NUM }, () => ({
				x: Math.random() * canvas.width,
				y: Math.random() * canvas.height,
				r: 1.5 + Math.random() * 3,
				dx: (Math.random() - 0.5) * 0.35,
				dy: (Math.random() - 0.5) * 0.35,
				o: 0.2 + Math.random() * 0.55
			}));
			let raf: number;
			const draw = () => {
				ctx.clearRect(0, 0, canvas.width, canvas.height);
				for (const p of pts) {
					p.x += p.dx;
					p.y += p.dy;
					if (p.x < 0) p.x = canvas.width;
					if (p.x > canvas.width) p.x = 0;
					if (p.y < 0) p.y = canvas.height;
					if (p.y > canvas.height) p.y = 0;
					ctx.beginPath();
					ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
					ctx.fillStyle = `rgba(59,130,246,${p.o})`;
					ctx.fill();
				}
				// draw connections
				for (let i = 0; i < pts.length; i++) {
					for (let j = i + 1; j < pts.length; j++) {
						const dist = Math.hypot(pts[i].x - pts[j].x, pts[i].y - pts[j].y);
						if (dist < 120) {
							ctx.beginPath();
							ctx.strokeStyle = `rgba(59,130,246,${0.12 * (1 - dist / 120)})`;
							ctx.lineWidth = 0.7;
							ctx.moveTo(pts[i].x, pts[i].y);
							ctx.lineTo(pts[j].x, pts[j].y);
							ctx.stroke();
						}
					}
				}
				raf = requestAnimationFrame(draw);
			};
			draw();
			return () => {
				cancelAnimationFrame(raf);
				window.removeEventListener('resize', resize);
			};
		}

		return () => {
			window.removeEventListener('scroll', onScroll);
			clearInterval(typeTimer);
		};
	});
</script>

<!-- ═══════════════════════════════════════════ -->
<!--  NAVBAR                                     -->
<!-- ═══════════════════════════════════════════ -->
<header
	class="glass-light fixed top-0 right-0 left-0 z-50 transition-all duration-300 {navScrolled
		? 'nav-scroll'
		: ''}"
	style="border-bottom: {navScrolled ? 'none' : '1px solid rgba(29,78,216,0.12)'};"
>
	<nav
		class="mx-auto flex max-w-7xl items-center justify-between px-6"
		style="height:var(--nav-height);"
	>
		<!-- Logo -->
		<a href="#hero" class="group flex items-center gap-3">
			<div
				class="flex h-11 w-11 items-center justify-center rounded-xl text-2xl shadow-md"
				style="background:var(--sp-gradient-blue);"
			>
				🖨️
			</div>
			<div>
				<div class="font-display text-lg leading-tight font-bold" style="color:var(--sp-navy);">
					Smart<span style="color:var(--sp-blue-mid);">print</span>
				</div>
				<div
					class="text-xs font-semibold tracking-widest"
					style="color:var(--sp-gray); font-family:'Plus Jakarta Sans',sans-serif;"
				>
					DIGITAL PRINTING PADANG
				</div>
			</div>
		</a>

		<!-- Desktop nav -->
		<div class="hidden items-center gap-7 md:flex">
			{#each [['#layanan', 'Layanan'], ['#produk', 'Katalog'], ['#harga', 'Harga'], ['#cara-pesan', 'Cara Order'], ['#tentang', 'Tentang'], ['#kontak', 'Kontak']] as [href, label]}
				<a
					{href}
					class="text-sm font-semibold transition-colors duration-200"
					style="color:var(--sp-gray);"
					onmouseenter={(e) => (e.currentTarget.style.color = 'var(--sp-blue)')}
					onmouseleave={(e) => (e.currentTarget.style.color = 'var(--sp-gray)')}>{label}</a
				>
			{/each}
		</div>

		<!-- CTA -->
		<div class="hidden items-center gap-3 md:flex">
			<div
				class="flex items-center gap-2 rounded-full px-3 py-1.5 text-xs font-bold"
				style="background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.3); color:#10B981; font-family:'Outfit',sans-serif;"
			>
				<span class="animate-ping-dot inline-block h-2 w-2 rounded-full" style="background:#10B981;"
				></span>BUKA
			</div>
			<a href={waGeneral} target="_blank" class="btn-primary-sp text-sm">Order Sekarang →</a>
		</div>

		<!-- Mobile hamburger -->
		<button
			class="p-2 md:hidden"
			onclick={() => (mobileNavOpen = !mobileNavOpen)}
			aria-label="Toggle nav"
		>
			{#each [6, 4, 6] as w}<div
					class="mb-1.5 h-0.5 rounded-full transition-all last:mb-0"
					style="width:{w * 4}px; background:var(--sp-blue);"
				></div>{/each}
		</button>
	</nav>

	<!-- Mobile menu -->
	{#if mobileNavOpen}
		<div
			class="animate-slide-down flex flex-col gap-3 px-6 py-5 md:hidden"
			style="background:rgba(255,255,255,0.97); border-top:1px solid var(--sp-gray-border);"
		>
			{#each [['#layanan', 'Layanan'], ['#produk', 'Katalog'], ['#harga', 'Harga'], ['#cara-pesan', 'Cara Order'], ['#tentang', 'Tentang'], ['#kontak', 'Kontak']] as [href, label]}
				<a
					{href}
					class="border-b py-2 text-sm font-semibold"
					style="color:var(--sp-text-mid); border-color:var(--sp-gray-border);"
					onclick={() => (mobileNavOpen = false)}>{label}</a
				>
			{/each}
			<a href={waGeneral} target="_blank" class="btn-primary-sp mt-2 text-center text-sm"
				>Order Sekarang →</a
			>
		</div>
	{/if}
</header>

<!-- ═══════════════════════════════════════════ -->
<!--  HERO                                       -->
<!-- ═══════════════════════════════════════════ -->
<section
	id="hero"
	class="dot-pattern-light relative flex min-h-screen items-center overflow-hidden"
	style="background:var(--sp-gradient-hero); padding-top:var(--nav-height);"
>
	<!-- Canvas Particles -->
	<canvas bind:this={canvasEl} class="absolute inset-0 z-0 h-full w-full"></canvas>

	<!-- Decorative blobs -->
	<div
		class="pointer-events-none absolute top-20 -left-20 h-96 w-96 rounded-full opacity-40"
		style="background:radial-gradient(circle, rgba(59,130,246,0.25) 0%, transparent 70%); filter:blur(60px);"
	></div>
	<div
		class="pointer-events-none absolute -right-20 bottom-20 h-80 w-80 rounded-full opacity-30"
		style="background:radial-gradient(circle, rgba(14,165,233,0.2) 0%, transparent 70%); filter:blur(60px);"
	></div>

	<div
		class="relative z-10 mx-auto grid w-full max-w-7xl items-center gap-16 px-6 py-20 lg:grid-cols-2"
	>
		<!-- Left copy -->
		<div>
			<div class="animate-slide-up section-chip mb-6 inline-flex items-center gap-2">
				<span>✦</span> CREATIVE AGENCY · PADANG
			</div>
			<h1
				class="font-display animate-slide-up mb-6 leading-tight font-extrabold delay-100"
				style="font-size:clamp(2.4rem,5.5vw,3.8rem); color:var(--sp-navy);"
			>
				Solusi Cetak<br />
				<span
					class="gradient-text-shimmer inline-block min-w-[300px] transition-opacity duration-300"
					style="opacity: {typeFading ? 0 : 1};">{typeText}</span
				><br />
				<span style="color:var(--sp-orange);">Untuk Bisnis Anda</span>
			</h1>
			<p
				class="animate-slide-up mb-8 max-w-lg text-lg delay-200"
				style="color:var(--sp-gray); line-height:1.8;"
			>
				Digital Printing · Advertising · Percetakan. Lebih dari 100 produk cetak berkualitas tinggi
				— harga terjangkau, hasil profesional, pengerjaan cepat.
			</p>
			<div class="animate-slide-up flex flex-col gap-3 delay-300 sm:flex-row sm:gap-4">
				<a href="#produk" class="btn-primary-sp w-full text-center sm:w-auto">Lihat Katalog ↓</a>
				<a
					href={waGeneral}
					target="_blank"
					class="btn-whatsapp flex w-full items-center justify-center gap-2 sm:w-auto"
					>💬 Chat WhatsApp</a
				>
			</div>

			<!-- Mini stats -->
			<div class="animate-slide-up mt-10 flex gap-8 delay-500">
				{#each [['1.149+', 'Followers IG', 'var(--sp-blue)'], ['100+', 'Jenis Produk', 'var(--sp-orange)'], ['⭐ 5.0', 'Rating', 'var(--sp-cyan)']] as [val, lbl, col]}
					<div>
						<div class="font-display text-2xl font-bold" style="color:{col};">{val}</div>
						<div class="text-xs font-medium" style="color:var(--sp-gray);">{lbl}</div>
					</div>
				{/each}
			</div>
		</div>

		<!-- Right floating card -->
		<div class="animate-scale-reveal hidden justify-center delay-300 lg:flex">
			<div class="relative w-full max-w-md">
				<div
					class="animate-float-soft rounded-2xl p-8 shadow-2xl"
					style="background:white; border:1.5px solid rgba(59,130,246,0.25);"
				>
					<div class="mb-4 flex items-center gap-3">
						<div
							class="flex h-14 w-14 items-center justify-center rounded-xl text-3xl"
							style="background:var(--sp-gradient-blue);"
						>
							🖨️
						</div>
						<div>
							<div class="font-display text-lg font-bold" style="color:var(--sp-navy);">
								Smartprint Padang
							</div>
							<div class="text-xs font-semibold" style="color:var(--sp-blue-mid);">
								@smartprint_padang
							</div>
						</div>
					</div>
					<div
						class="mb-5 grid grid-cols-3 gap-2 text-center text-xs font-bold"
						style="color:var(--sp-gray);"
					>
						{#each [['417', 'Posts'], ['1.149', 'Followers'], ['770', 'Following']] as [n, l]}
							<div class="rounded-lg py-2" style="background:var(--sp-bg-off);">
								<div class="font-display text-base font-extrabold" style="color:var(--sp-navy);">
									{n}
								</div>
								<div>{l}</div>
							</div>
						{/each}
					</div>
					<div class="grid grid-cols-2 gap-2">
						{#each ['Spanduk', 'Baliho', 'Stiker Label', 'Kartu Nama', 'Roll Banner', 'ID Card'] as p}
							<div
								class="rounded-lg px-3 py-2 text-center text-xs font-semibold"
								style="background:var(--sp-bg-light); color:var(--sp-blue);"
							>
								{p}
							</div>
						{/each}
					</div>
					<div
						class="mt-5 flex items-center justify-center gap-2 text-sm font-semibold"
						style="color:var(--sp-green);"
					>
						<span class="h-2 w-2 rounded-full" style="background:var(--sp-green);"></span>Senin –
						Sabtu · 09:00 – 17:30
					</div>
					<div
						class="mt-3 rounded-lg p-3 text-center text-xs"
						style="background:var(--sp-bg-off); color:var(--sp-gray);"
					>
						Part of <strong style="color:var(--sp-blue);">@redline_comunication</strong> &
						<strong style="color:var(--sp-blue);">@redline_production_</strong>
					</div>
				</div>
				<!-- Decorative ring -->
				<div
					class="animate-spin-slow absolute -top-5 -right-5 h-16 w-16 rounded-full border-2 opacity-25"
					style="border-color:var(--sp-blue-mid);"
				></div>
				<div
					class="animate-spin-slow absolute -bottom-4 -left-4 h-10 w-10 rounded-full border-2 opacity-20"
					style="border-color:var(--sp-orange); animation-direction:reverse;"
				></div>
			</div>
		</div>
	</div>
</section>

<!-- Stats Bar -->
<section
	id="stats-section"
	class="py-14"
	style="background:var(--sp-bg-dark); border-top:4px solid var(--sp-blue);"
>
	<div class="mx-auto grid max-w-5xl grid-cols-2 gap-8 px-6 md:grid-cols-4">
		{#each [{ label: 'Jenis Produk', val: statCounter.products, suffix: '+', color: '#93C5FD' }, { label: 'Pelanggan Puas', val: statCounter.clients, suffix: '+', color: '#6EE7B7' }, { label: 'Tahun Pengalaman', val: statCounter.years, suffix: '', color: '#FBD38D' }, { label: 'Instagram Followers', val: statCounter.followers, suffix: '', color: '#C4B5FD' }] as s}
			<div class="text-center">
				<div class="font-display mb-1 font-extrabold" style="font-size:2.5rem; color:{s.color};">
					{s.val}{s.suffix}
				</div>
				<div class="text-sm font-medium" style="color:rgba(255,255,255,0.6);">{s.label}</div>
			</div>
		{/each}
	</div>
</section>

<!-- ═══════════════════════════════════════════ -->
<!--  LAYANAN (Services)                         -->
<!-- ═══════════════════════════════════════════ -->
<section id="layanan" class="py-24" style="background:var(--sp-bg-section);">
	<div class="mx-auto max-w-7xl px-6">
		<div class="sp-reveal mb-16 text-center">
			<div class="section-chip mb-4">LAYANAN KAMI</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Apa yang Bisa Kami <span class="gradient-text-blue">Lakukan</span>
			</h2>
			<p class="mx-auto max-w-xl" style="color:var(--sp-gray);">
				Kami hadir sebagai mitra kreatif untuk kebutuhan cetak dan advertising bisnis Anda.
			</p>
		</div>
		<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
			{#each [{ icon: '🖨️', title: 'Digital Printing', desc: 'Cetak berkualitas tinggi dengan teknologi digital terkini. Warna akurat, detail tajam, hasil memuaskan.', color: 'var(--sp-blue)' }, { icon: '📢', title: 'Advertising', desc: 'Solusi periklanan kreatif untuk promosi brand dan produk Anda — spanduk, baliho, banner outdoor.', color: 'var(--sp-orange)' }, { icon: '📄', title: 'Percetakan', desc: 'Dari kartu nama, nota, brosur, poster hingga undangan. Semua dikerjakan dengan presisi tinggi.', color: 'var(--sp-cyan)' }, { icon: '🎨', title: 'Desain Grafis', desc: 'Tim desainer siap membantu membuat desain menarik sesuai identitas brand Anda.', color: 'var(--sp-blue-mid)' }, { icon: '🚚', title: 'Pengiriman', desc: 'Layanan antar ke seluruh wilayah Kota Padang dan sekitarnya dengan aman dan tepat waktu.', color: 'var(--sp-green)' }, { icon: '💼', title: 'Corporate Branding', desc: 'Paket branding lengkap untuk perusahaan — seragam, ID card, media promosi, & lebih banyak lagi.', color: 'var(--sp-orange)' }] as s, i}
				<div class="card-sp sp-reveal p-7" style="transition-delay: {i * 50}ms;">
					<div
						class="mb-4 flex h-14 w-14 items-center justify-center rounded-xl text-3xl"
						style="background:color-mix(in srgb, {s.color} 12%, transparent);"
					>
						{s.icon}
					</div>
					<h3 class="font-display mb-2 text-lg font-bold" style="color:var(--sp-navy);">
						{s.title}
					</h3>
					<p class="text-sm leading-relaxed" style="color:var(--sp-gray);">{s.desc}</p>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ═══════════════════════════════════════════ -->
<!--  PRODUCT CATALOG                            -->
<!-- ═══════════════════════════════════════════ -->
<section id="produk" class="py-24" style="background:var(--sp-bg-white);">
	<div class="mx-auto max-w-7xl px-6">
		<div class="sp-reveal mb-12 text-center">
			<div class="section-chip mb-4">KATALOG PRODUK</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Semua Solusi Cetak <span class="gradient-text-blue">Anda</span>
			</h2>
			<p class="mx-auto max-w-xl" style="color:var(--sp-gray);">
				Temukan produk yang Anda butuhkan. Kualitas premium, harga bersaing.
			</p>
		</div>

		<!-- Search + Sort -->
		<div class="mb-6 flex flex-col gap-4 md:flex-row">
			<div class="relative flex-1">
				<span class="absolute top-1/2 left-4 -translate-y-1/2 text-lg">🔍</span>
				<input
					type="text"
					bind:value={searchQuery}
					placeholder="Cari produk cetak..."
					class="w-full rounded-xl py-3.5 pr-4 pl-12 text-sm font-medium transition-all duration-300 outline-none"
					style="background:var(--sp-bg-off); border:1.5px solid var(--sp-gray-border); color:var(--sp-text-dark); font-family:'Plus Jakarta Sans',sans-serif;"
					onfocus={(e) => {
						e.currentTarget.style.borderColor = 'var(--sp-blue-mid)';
						e.currentTarget.style.boxShadow = '0 0 0 3px rgba(59,130,246,0.12)';
					}}
					onblur={(e) => {
						e.currentTarget.style.borderColor = 'var(--sp-gray-border)';
						e.currentTarget.style.boxShadow = 'none';
					}}
				/>
			</div>
			<select
				bind:value={sortOrder}
				class="cursor-pointer rounded-xl px-4 py-3.5 text-sm font-medium outline-none"
				style="background:var(--sp-bg-off); border:1.5px solid var(--sp-gray-border); color:var(--sp-text-dark); min-width:160px; font-family:'Plus Jakarta Sans',sans-serif;"
			>
				<option value="populer">⭐ Terpopuler</option>
				<option value="baru">🆕 Terbaru</option>
				<option value="default">🔤 Default</option>
			</select>
		</div>

		<!-- Category filter -->
		<div class="-mx-6 mb-10 overflow-x-auto px-6 sm:mx-0 sm:px-0">
			<div class="flex gap-2 pb-2 sm:flex-wrap sm:pb-0" style="min-width:max-content;">
				{#each categories as cat}
					<button
						onclick={() => (activeCategory = cat.key)}
						class="font-display shrink-0 cursor-pointer rounded-full px-5 py-2 text-sm font-semibold transition-all duration-200"
						style={activeCategory === cat.key
							? 'background:var(--sp-gradient-blue); color:#fff; box-shadow:var(--sp-shadow-blue);'
							: 'background:var(--sp-bg-off); color:var(--sp-gray); border:1.5px solid var(--sp-gray-border);'}
					>
						{cat.label}
					</button>
				{/each}
			</div>
		</div>

		<!-- Grid -->
		{#if filteredProducts().length === 0}
			<div class="py-20 text-center">
				<div class="mb-4 text-5xl">🔍</div>
				<div class="font-display mb-2 text-xl font-bold" style="color:var(--sp-navy);">
					Produk tidak ditemukan
				</div>
				<div style="color:var(--sp-gray);">Coba kata kunci atau kategori lain</div>
			</div>
		{:else}
			<div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
				{#each filteredProducts() as product, i (product.id)}
					<div
						class="card-sp sp-reveal flex flex-col gap-4 p-6"
						style="transition-delay: {(i % 4) * 50}ms;"
					>
						<div class="flex items-start justify-between">
							<div
								class="flex h-14 w-14 items-center justify-center rounded-xl text-3xl"
								style="background:var(--sp-bg-light);"
							>
								{product.emoji}
							</div>
							<div class="flex flex-col items-end gap-1">
								{#each product.tags as tag}
									{#if tag === 'Populer'}<span class="badge-popular">{tag}</span>
									{:else if tag === 'Baru'}<span class="badge-new">{tag}</span>
									{/if}
								{/each}
							</div>
						</div>
						<div class="flex-1">
							<h3 class="font-display mb-1 text-base font-bold" style="color:var(--sp-navy);">
								{product.name}
							</h3>
							<p class="text-xs leading-relaxed" style="color:var(--sp-gray);">{product.desc}</p>
						</div>
						<div>
							<div
								class="mb-3 text-sm font-bold"
								style="color:var(--sp-blue); font-family:'Outfit',sans-serif;"
							>
								{product.price}
							</div>
							<a
								href={waProduct(product.name)}
								target="_blank"
								class="font-display block w-full rounded-xl py-2.5 text-center text-sm font-semibold transition-all duration-200 hover:-translate-y-0.5"
								style="background:var(--sp-bg-light); border:1.5px solid rgba(59,130,246,0.3); color:var(--sp-blue);"
								onmouseenter={(e) => {
									e.currentTarget.style.background = 'var(--sp-gradient-blue)';
									e.currentTarget.style.color = '#fff';
								}}
								onmouseleave={(e) => {
									e.currentTarget.style.background = 'var(--sp-bg-light)';
									e.currentTarget.style.color = 'var(--sp-blue)';
								}}
							>
								💬 Pesan Sekarang
							</a>
						</div>
					</div>
				{/each}
			</div>
			<p class="mt-8 text-center text-sm" style="color:var(--sp-gray);">
				Menampilkan <span style="color:var(--sp-blue); font-weight:700;"
					>{filteredProducts().length}</span
				>
				dari {allProducts.length} produk
			</p>
		{/if}
	</div>
</section>

<!-- ═══════════════════════════════════════════ -->
<!--  HOW TO ORDER                               -->
<!-- ═══════════════════════════════════════════ -->
<section id="cara-pesan" class="py-24" style="background:var(--sp-gradient-dark);">
	<div class="mx-auto max-w-6xl px-6">
		<div class="sp-reveal mb-16 text-center">
			<div
				class="mb-4 inline-block rounded-full px-4 py-1.5 text-xs font-bold tracking-widest uppercase"
				style="background:rgba(255,255,255,0.15); color:#fff; font-family:'Outfit',sans-serif;"
			>
				CARA ORDER
			</div>
			<h2 class="font-display mb-4 font-bold text-white" style="font-size:clamp(2rem,5vw,3rem);">
				4 Langkah <span style="color:#93C5FD;">Mudah</span>
			</h2>
			<p style="color:rgba(255,255,255,0.7);">
				Pesan cetakan Anda dengan proses yang simpel dan transparan.
			</p>
		</div>
		<div class="relative grid grid-cols-1 gap-8 md:grid-cols-4">
			<div
				class="absolute right-[12%] left-[12%] hidden h-px md:block"
				style="background:linear-gradient(90deg,transparent,rgba(255,255,255,0.3),transparent); top:40px;"
			></div>
			{#each [{ step: '01', emoji: '💬', title: 'Konsultasi', desc: 'Hubungi kami via WhatsApp, ceritakan kebutuhan cetak Anda.', color: '#93C5FD' }, { step: '02', emoji: '🎨', title: 'Desain & File', desc: 'Kirim file desain, atau minta tim kami untuk membantu.', color: '#6EE7B7' }, { step: '03', emoji: '✅', title: 'Konfirmasi', desc: 'Setujui harga, spesifikasi, dan estimasi waktu produksi.', color: '#FBD38D' }, { step: '04', emoji: '📦', title: 'Terima Produk', desc: 'Ambil di toko atau kami antar ke lokasi Anda.', color: '#C4B5FD' }] as step, i}
				<div
					class="sp-reveal relative flex flex-col items-center text-center"
					style="transition-delay:{i * 150}ms;"
				>
					<div
						class="relative z-10 mb-5 flex h-20 w-20 items-center justify-center rounded-2xl text-3xl shadow-lg"
						style="background:rgba(255,255,255,0.12); border:2px solid {step.color}; backdrop-filter:blur(8px);"
					>
						{step.emoji}
					</div>
					<div
						class="mb-2 text-xs font-bold tracking-widest"
						style="color:{step.color}; font-family:'Outfit',sans-serif;"
					>
						LANGKAH {step.step}
					</div>
					<h3 class="font-display mb-2 text-lg font-bold text-white">{step.title}</h3>
					<p class="text-sm leading-relaxed" style="color:rgba(255,255,255,0.65);">{step.desc}</p>
				</div>
			{/each}
		</div>
		<div class="mt-14 text-center">
			<a href={waGeneral} target="_blank" class="btn-whatsapp inline-flex items-center gap-2"
				>💬 Mulai Order Sekarang →</a
			>
		</div>
	</div>
</section>

<!-- ═══════════════════════════════════════════ -->
<!--  PRICING                                    -->
<!-- ═══════════════════════════════════════════ -->
<section id="harga" class="py-24" style="background:var(--sp-bg-section);">
	<div class="mx-auto max-w-5xl px-6">
		<div class="sp-reveal mb-16 text-center">
			<div class="section-chip mb-4">ESTIMASI HARGA</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Harga <span class="gradient-text-blue">Transparan</span>
			</h2>
			<p style="color:var(--sp-gray);">Kami memberikan harga terbaik tanpa biaya tersembunyi.</p>
		</div>
		<div class="grid gap-8 md:grid-cols-3">
			{#each [{ tier: 'Basic', icon: '🏷️', color: 'var(--sp-cyan)', desc: 'Cocok untuk kebutuhan cetak kecil & personal', featured: false, items: ['Kartu Nama (100pcs) mulai Rp 30rb', 'Stiker Cutting mulai Rp 15rb', 'Poster A3 mulai Rp 5rb/lembar', 'ID Card mulai Rp 10rb/pcs'] }, { tier: 'Standard', icon: '⭐', color: 'var(--sp-blue)', desc: 'Pilihan terbaik untuk promosi bisnis Anda', featured: true, items: ['Spanduk PVC mulai Rp 25rb/m²', 'Roll Banner mulai Rp 150rb', 'X-Banner mulai Rp 85rb', 'Backdrop mulai Rp 80rb/m²'] }, { tier: 'Premium', icon: '💎', color: 'var(--sp-orange)', desc: 'Untuk event besar, proyek & order massal', featured: false, items: ['Baliho Outdoor mulai Rp 45rb/m²', 'Custom ukuran besar', 'Nota / Bon custom Rp 45rb/buku', 'Harga grosir (diskusi)'] }] as plan, i}
				<div
					class="sp-reveal relative flex flex-col gap-5 rounded-2xl p-7 transition-all duration-300 hover:-translate-y-2"
					style="{plan.featured
						? 'background:var(--sp-gradient-blue); box-shadow:var(--sp-shadow-xl);'
						: 'background:white; border:1.5px solid var(--sp-gray-border); box-shadow:var(--sp-shadow-sm);'} transition-delay:{i *
						100}ms;"
				>
					{#if plan.featured}
						<div
							class="absolute -top-3 left-1/2 -translate-x-1/2 rounded-full px-4 py-1 text-xs font-bold"
							style="background:var(--sp-orange); color:#fff; font-family:'Outfit',sans-serif; white-space:nowrap;"
						>
							PALING POPULER
						</div>
					{/if}
					<div class="text-4xl">{plan.icon}</div>
					<div>
						<h3
							class="font-display mb-1 text-2xl font-bold"
							style="color:{plan.featured ? '#fff' : plan.color};"
						>
							{plan.tier}
						</h3>
						<p
							class="text-sm"
							style="color:{plan.featured ? 'rgba(255,255,255,0.75)' : 'var(--sp-gray)'};"
						>
							{plan.desc}
						</p>
					</div>
					<ul class="flex flex-1 flex-col gap-2">
						{#each plan.items as item}
							<li
								class="flex items-start gap-2 text-sm"
								style="color:{plan.featured ? 'rgba(255,255,255,0.88)' : 'var(--sp-text-mid)'};"
							>
								<span
									style="color:{plan.featured
										? '#93C5FD'
										: plan.color}; flex-shrink:0; margin-top:1px;">✓</span
								>{item}
							</li>
						{/each}
					</ul>
					<a
						href={waLink(`Halo Smartprint, saya mau tanya harga paket *${plan.tier}*`)}
						target="_blank"
						class="font-display block w-full rounded-xl py-3 text-center text-sm font-bold transition-all duration-200"
						style={plan.featured
							? 'background:white; color:var(--sp-blue);'
							: `background:transparent; border:2px solid ${plan.color}; color:${plan.color};`}
					>
						Tanya Harga {plan.tier}
					</a>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ═══════════════════════════════════════════ -->
<!--  ABOUT                                      -->
<!-- ═══════════════════════════════════════════ -->
<section id="tentang" class="dot-pattern-light py-24" style="background:var(--sp-bg-white);">
	<div class="mx-auto grid max-w-6xl items-center gap-16 px-6 lg:grid-cols-2">
		<!-- Left copy -->
		<div class="sp-reveal">
			<div class="section-chip mb-4">TENTANG KAMI</div>
			<h2
				class="font-display mb-6 font-bold"
				style="font-size:clamp(1.8rem,4vw,2.8rem); color:var(--sp-navy);"
			>
				Mengapa Pilih <span class="gradient-text-blue">Smartprint?</span>
			</h2>
			<p class="mb-6 text-base leading-relaxed" style="color:var(--sp-gray);">
				Smartprint Padang adalah creative agency yang bergerak di bidang digital printing,
				advertising, dan percetakan. Bagian dari ekosistem <strong style="color:var(--sp-blue);"
					>Redline Communication</strong
				> — kami hadir untuk membantu bisnis Anda tampil profesional.
			</p>
			<p class="mb-8 text-base leading-relaxed" style="color:var(--sp-gray);">
				Dengan pengalaman lebih dari 7 tahun, kami telah melayani ribuan pelanggan di Padang dan
				sekitarnya — dari UMKM, event organizer, sekolah, hingga perusahaan besar.
			</p>
			<div class="grid grid-cols-2 gap-4">
				{#each [{ icon: '🎯', label: 'Kualitas Tinggi', color: 'var(--sp-blue)' }, { icon: '⚡', label: 'Proses Cepat', color: 'var(--sp-cyan)' }, { icon: '💰', label: 'Harga Terjangkau', color: 'var(--sp-orange)' }, { icon: '🤝', label: 'Pelayanan Ramah', color: 'var(--sp-green)' }] as v}
					<div
						class="flex items-center gap-3 rounded-xl p-4"
						style="background:var(--sp-bg-off); border:1px solid var(--sp-gray-border);"
					>
						<span class="text-2xl">{v.icon}</span>
						<span class="text-sm font-semibold" style="color:var(--sp-navy);">{v.label}</span>
					</div>
				{/each}
			</div>
		</div>

		<!-- Right visual -->
		<div class="sp-reveal flex flex-col gap-4" style="transition-delay: 200ms;">
			<div
				class="animate-float-soft rounded-2xl p-8 text-center shadow-xl"
				style="background:var(--sp-gradient-dark);"
			>
				<div class="mb-4 text-7xl">🖨️</div>
				<div class="font-display mb-1 text-xl font-bold text-white">Smartprint Padang</div>
				<div class="mb-3 text-sm" style="color:#93C5FD;">
					Digital Printing · Advertising · Percetakan
				</div>
				<div
					class="rounded-lg p-3 text-xs"
					style="background:rgba(255,255,255,0.1); color:rgba(255,255,255,0.75);"
				>
					Part of <strong style="color:#93C5FD;">@redline_comunication</strong> &
					<strong style="color:#93C5FD;">@redline_production_</strong>
				</div>
			</div>
			<div
				class="rounded-xl p-5 shadow-sm"
				style="background:var(--sp-bg-off); border:1px solid var(--sp-gray-border);"
			>
				<div class="font-display mb-3 text-base font-bold" style="color:var(--sp-navy);">
					📍 Jam Operasional
				</div>
				{#each [['Senin – Jumat', '09:00 – 17:30'], ['Sabtu', '09:00 – 15:00'], ['Minggu', 'Tutup']] as [hari, jam]}
					<div
						class="flex justify-between border-b py-1.5 text-sm last:border-0"
						style="border-color:var(--sp-gray-border); color:var(--sp-text-mid);"
					>
						<span>{hari}</span><span class="font-semibold" style="color:var(--sp-blue);">{jam}</span
						>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>

<!-- ═══════════════════════════════════════════ -->
<!--  TESTIMONIALS                               -->
<!-- ═══════════════════════════════════════════ -->
<section class="py-24" style="background:var(--sp-bg-light);">
	<div class="mx-auto max-w-6xl px-6">
		<div class="sp-reveal mb-14 text-center">
			<div class="section-chip mb-4">TESTIMONI</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Kata Pelanggan <span class="gradient-text-blue">Kami</span>
			</h2>
		</div>
		<div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
			{#each testimonials as t, i}
				<div class="card-sp sp-reveal p-6" style="transition-delay: {(i % 3) * 100}ms;">
					<div class="mb-3 flex gap-0.5">
						{#each Array(t.stars) as _}<span style="color:#FBBF24;">★</span>{/each}
					</div>
					<p class="mb-4 text-sm leading-relaxed" style="color:var(--sp-text-mid);">"{t.text}"</p>
					<div class="flex items-center gap-3">
						<div
							class="flex h-10 w-10 items-center justify-center rounded-full text-sm font-bold text-white"
							style="background:var(--sp-gradient-blue);"
						>
							{t.name[0]}
						</div>
						<div>
							<div class="text-sm font-semibold" style="color:var(--sp-navy);">{t.name}</div>
							<div class="text-xs" style="color:var(--sp-gray);">{t.role}</div>
						</div>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ═══════════════════════════════════════════ -->
<!--  FAQ                                        -->
<!-- ═══════════════════════════════════════════ -->
<section class="py-24" style="background:var(--sp-bg-white);">
	<div class="mx-auto max-w-3xl px-6">
		<div class="sp-reveal mb-14 text-center">
			<div class="section-chip mb-4">FAQ</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(1.8rem,4vw,2.5rem); color:var(--sp-navy);"
			>
				Pertanyaan <span class="gradient-text-blue">Umum</span>
			</h2>
		</div>
		<div class="flex flex-col gap-3">
			{#each faqs as faq, i}
				<div
					class="sp-reveal overflow-hidden rounded-xl transition-all duration-200"
					style="{openFaq === i
						? 'border:2px solid var(--sp-blue); box-shadow:var(--sp-shadow-md);'
						: 'border:1.5px solid var(--sp-gray-border);'} transition-delay:{i * 50}ms;"
				>
					<button
						class="flex w-full items-center justify-between p-5 text-left"
						onclick={() => (openFaq = openFaq === i ? null : i)}
					>
						<span class="font-display text-base font-semibold" style="color:var(--sp-navy);"
							>{faq.q}</span
						>
						<span
							class="text-xl font-bold transition-transform duration-200"
							style="color:var(--sp-blue); transform:{openFaq === i
								? 'rotate(45deg)'
								: 'rotate(0deg)'};">+</span
						>
					</button>
					{#if openFaq === i}
						<div
							class="animate-slide-down px-5 pb-5 text-sm leading-relaxed"
							style="color:var(--sp-gray);"
						>
							{faq.a}
						</div>
					{/if}
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ═══════════════════════════════════════════ -->
<!--  CONTACT / CTA                              -->
<!-- ═══════════════════════════════════════════ -->
<section id="kontak" class="py-24" style="background:var(--sp-gradient-dark);">
	<div class="mx-auto max-w-4xl px-6 text-center">
		<div class="sp-reveal">
			<div
				class="mb-4 inline-block rounded-full px-4 py-1.5 text-xs font-bold tracking-widest uppercase"
				style="background:rgba(255,255,255,0.15); color:#fff; font-family:'Outfit',sans-serif;"
			>
				HUBUNGI KAMI
			</div>
			<h2 class="font-display mb-4 font-bold text-white" style="font-size:clamp(2rem,5vw,3rem);">
				Siap Mencetak <span style="color:#93C5FD;">Bersama Kami?</span>
			</h2>
			<p class="mx-auto mb-10 max-w-xl" style="color:rgba(255,255,255,0.7);">
				Hubungi Smartprint Padang sekarang dan dapatkan konsultasi gratis untuk kebutuhan cetak
				Anda.
			</p>
			<div class="flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
				<a
					href={waGeneral}
					target="_blank"
					class="btn-whatsapp flex items-center gap-2 px-8 py-4 text-base"
					>💬 Chat WhatsApp Sekarang</a
				>
				<a
					href="https://www.instagram.com/smartprint_padang/"
					target="_blank"
					class="flex items-center gap-2 rounded-xl px-8 py-4 text-base font-bold transition-all duration-200 hover:opacity-80"
					style="background:linear-gradient(135deg,#E1306C,#833AB4); color:white; font-family:'Outfit',sans-serif;"
					>📷 Follow Instagram</a
				>
			</div>
		</div>
		<div class="mt-10 grid grid-cols-1 gap-4 sm:grid-cols-3">
			{#each [{ icon: '📞', label: 'Telepon / WhatsApp', val: '0811 663 528' }, { icon: '📸', label: 'Instagram', val: '@smartprint_padang' }, { icon: '🏙️', label: 'Kota', val: 'Padang, Sumatera Barat' }] as c, i}
				<div
					class="sp-reveal rounded-xl p-5"
					style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); transition-delay:{i *
						100}ms;"
				>
					<div class="mb-2 text-2xl">{c.icon}</div>
					<div
						class="mb-1 text-xs"
						style="color:rgba(255,255,255,0.55); font-family:'Outfit',sans-serif;"
					>
						{c.label}
					</div>
					<div class="text-sm font-semibold text-white">{c.val}</div>
				</div>
			{/each}
		</div>
	</div>
</section>

<!-- ═══════════════════════════════════════════ -->
<!--  FOOTER                                     -->
<!-- ═══════════════════════════════════════════ -->
<footer style="background:#0F172A; border-top:3px solid var(--sp-blue);">
	<div class="mx-auto max-w-7xl px-6 py-16">
		<div class="grid grid-cols-1 gap-10 md:grid-cols-4">
			<!-- Brand -->
			<div class="md:col-span-2">
				<div class="mb-4 flex items-center gap-3">
					<div
						class="flex h-11 w-11 items-center justify-center rounded-xl text-2xl"
						style="background:var(--sp-gradient-blue);"
					>
						🖨️
					</div>
					<div>
						<div class="font-display text-lg font-bold text-white">Smartprint Padang</div>
						<div
							class="text-xs"
							style="color:rgba(255,255,255,0.45); font-family:'Plus Jakarta Sans',sans-serif;"
						>
							DIGITAL PRINTING PADANG
						</div>
					</div>
				</div>
				<p class="mb-4 max-w-xs text-sm" style="color:rgba(255,255,255,0.55);">
					Creative Agency · Digital Printing · Advertising · Percetakan. Bagian dari ekosistem
					Redline Communication.
				</p>
				<div class="flex gap-3">
					<a
						href="https://www.instagram.com/smartprint_padang/"
						target="_blank"
						class="flex h-9 w-9 items-center justify-center rounded-lg text-lg transition-opacity hover:opacity-75"
						style="background:linear-gradient(135deg,#E1306C,#833AB4);">📷</a
					>
					<a
						href={waGeneral}
						target="_blank"
						class="flex h-9 w-9 items-center justify-center rounded-lg text-lg transition-opacity hover:opacity-75"
						style="background:linear-gradient(135deg,#25D366,#128C7E);">💬</a
					>
				</div>
			</div>

			<!-- Links -->
			<div>
				<div
					class="font-display mb-4 text-sm font-bold tracking-wider uppercase"
					style="color:rgba(255,255,255,0.4);"
				>
					Layanan
				</div>
				{#each ['Digital Printing', 'Advertising', 'Percetakan', 'Desain Grafis', 'Corporate Branding'] as l}
					<div class="py-1.5 text-sm" style="color:rgba(255,255,255,0.6);">{l}</div>
				{/each}
			</div>

			<!-- Contact -->
			<div>
				<div
					class="font-display mb-4 text-sm font-bold tracking-wider uppercase"
					style="color:rgba(255,255,255,0.4);"
				>
					Kontak
				</div>
				{#each [['📞', '0811 663 528'], ['📸', '@smartprint_padang'], ['🏙️', 'Padang, Sumatera Barat'], ['🔗', 'Part of @redline_comunication']] as [ico, val]}
					<div class="flex items-start gap-2 py-1.5 text-sm" style="color:rgba(255,255,255,0.6);">
						<span>{ico}</span><span>{val}</span>
					</div>
				{/each}
			</div>
		</div>

		<div class="section-divider my-8"></div>
		<div
			class="flex flex-col items-center justify-between gap-3 text-xs sm:flex-row"
			style="color:rgba(255,255,255,0.35);"
		>
			<span>© 2025 Smartprint Padang. All rights reserved.</span>
			<span
				>Part of <a
					href="https://www.instagram.com/redline_comunication/"
					target="_blank"
					style="color:var(--sp-blue-light);">Redline Communication</a
				></span
			>
		</div>
	</div>
</footer>
