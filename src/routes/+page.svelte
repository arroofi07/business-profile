<script lang="ts">
	import { Separator } from '$lib/components/ui/separator';
	import {
		Star,
		Phone,
		Clock,
		MapPin,
		Menu,
		X,
		ChevronRight,
		Sparkles,
		Shield,
		Heart,
		Zap,
		Award,
		Instagram,
		MessageCircle,
		CheckCircle2,
		ArrowRight,
		Droplets,
		Eye,
		Flower2,
		Gem,
		Stethoscope,
		Sun,
		Activity,
		Syringe,
		Microscope,
		Target
	} from 'lucide-svelte';

	let menuOpen = $state(false);

	const navLinks = [
		{ href: '#home', label: 'Beranda' },
		{ href: '#about', label: 'Tentang' },
		{ href: '#services', label: 'Layanan' },
		{ href: '#hours', label: 'Jadwal' },
		{ href: '#reviews', label: 'Ulasan' },
		{ href: '#contact', label: 'Kontak' }
	];

	const services = [
		{
			icon: Stethoscope,
			tag: 'Medical Skincare',
			title: 'Konsultasi Dokter Kulit',
			desc: 'Konsultasi langsung bersama dr. Wahyu Triasmara, spesialis skincare berpengalaman. Dapatkan diagnosis dan rencana perawatan yang tepat untuk kulit Anda.'
		},
		{
			icon: Sun,
			tag: 'Brightening',
			title: 'Skin Brightening',
			desc: 'Perawatan pemutihan dan pencerahan kulit menggunakan teknologi terkini dan bahan aktif medis yang aman dan efektif untuk kulit lebih cerah merata.'
		},
		{
			icon: Activity,
			tag: 'Anti-Aging',
			title: 'Anti-Aging Treatment',
			desc: 'Teknologi anti-penuaan modern yang membantu meremajakan kulit, mengurangi kerutan, dan meningkatkan elastisitas kulit secara signifikan.'
		},
		{
			icon: Droplets,
			tag: 'Hydration',
			title: 'Deep Hydration',
			desc: 'Perawatan hidrasi mendalam dengan serum & treatment premium untuk kulit yang lembap, kenyal, dan bercahaya tahan lama sepanjang hari.'
		},
		{
			icon: Target,
			tag: 'Problem Solving',
			title: 'Acne & Scar Treatment',
			desc: 'Penanganan jerawat aktif dan bekas luka secara medis dan estetik, dengan pendekatan terapi yang personal sesuai kondisi kulit Anda.'
		},
		{
			icon: Gem,
			tag: 'Premium',
			title: 'Perawatan Eksklusif',
			desc: 'Paket perawatan lengkap yang dikombinasikan secara khusus untuk hasil maksimal. Investasi terbaik untuk kecantikan dan kesehatan kulit Anda.'
		}
	];

	const stats = [
		{ value: 'dr.', label: 'Wahyu Triasmara', sub: 'Founder & Dokter' },
		{ value: '7×', label: 'Hari Buka', sub: 'Termasuk 24 jam Minggu' },
		{ value: '6+', label: 'Tahun Berdiri', sub: 'Melayani Padang' },
		{ value: '100%', label: 'Berlisensi', sub: 'Klinik resmi & terdaftar' }
	];

	const hours = [
		{ day: 'Senin', time: '07.00 – 21.00', open: true },
		{ day: 'Selasa', time: '07.00 – 21.00', open: true },
		{ day: 'Rabu', time: '07.00 – 21.00', open: true },
		{ day: 'Kamis', time: '07.00 – 21.00', open: true },
		{ day: 'Jumat', time: '07.00 – 21.00', open: true },
		{ day: 'Sabtu', time: '07.00 – 21.00', open: true },
		{ day: 'Minggu', time: 'Buka 24 Jam', open: true, special: true }
	];

	const reviews = [
		{
			name: 'Rina Marlina',
			initial: 'RM',
			count: '3 ulasan',
			time: '2 bulan lalu',
			stars: 5,
			text: 'Pelayanan luar biasa di Drw Skincare! Dr. Wahyu sangat ramah dan profesional. Kulit saya jauh lebih bersih dan cerah setelah rutin treatment di sini. Tempatnya bersih dan nyaman 🌸'
		},
		{
			name: 'Budi Santoso',
			initial: 'BS',
			count: '1 ulasan',
			time: '4 bulan lalu',
			stars: 5,
			text: 'Awalnya ragu karena masalah jerawat sudah lama tidak sembuh. Setelah konsultasi dengan dr. Wahyu dan treatment selama 2 bulan, hasilnya sungguh luar biasa! Sangat direkomendasikan!'
		},
		{
			name: 'Sari Dewi P.',
			initial: 'SD',
			count: '2 ulasan · 12 foto',
			time: '1 tahun lalu',
			stars: 5,
			text: 'Klinik terbaik di Padang untuk skincare! Produknya berkualitas, dokternya berpengalaman, dan harganya sangat terjangkau. Tidak pernah menyesal pilih Drw Skincare.',
			isGuide: true
		}
	];

	const whyUs = [
		{ icon: Shield, title: 'Dokter Berlisensi', desc: 'Ditangani langsung dr. Wahyu Triasmara, founder & ahli skincare' },
		{ icon: Award, title: 'Klinik Resmi', desc: 'Terdaftar resmi & beroperasi sesuai standar medis nasional' },
		{ icon: Heart, title: 'Pendekatan Personal', desc: 'Setiap pasien mendapat rencana perawatan yang disesuaikan' },
		{ icon: Clock, title: 'Jadwal Fleksibel', desc: 'Buka 7 hari seminggu, Minggu buka 24 jam untuk Anda' }
	];
</script>

<svelte:head>
	<title>Drw Skincare Padang – Klinik Kecantikan & Kesehatan Kulit dr. Wahyu Triasmara</title>
	<meta
		name="description"
		content="Drw Skincare Padang – klinik kecantikan & kesehatan kulit by dr. Wahyu Triasmara. Residence Tahap 1 Blok i6, Aie Pacah, Koto Tangah. Buka Senin–Sabtu 07.00-21.00, Minggu 24 jam. Hubungi: 0823-8143-2222"
	/>
</svelte:head>

<!-- ═══════ NAVBAR ═══════ -->
<header class="fixed inset-x-0 top-0 z-50">
	<nav
		class="border-b backdrop-blur-2xl"
		style="background:rgba(13,27,42,0.96);border-color:rgba(200,116,138,0.15);box-shadow:0 1px 40px rgba(0,0,0,0.3)"
	>
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-20 items-center justify-between">
				<!-- Logo -->
				<a href="#home" class="group flex items-center gap-3">
					<!-- Rose circle logo -->
					<div class="relative flex h-11 w-11 items-center justify-center rounded-2xl transition-all group-hover:scale-110 group-hover:rotate-3"
						style="background:var(--brand-gradient-rose);box-shadow:var(--brand-shadow-rose)"
					>
						<span class="text-white font-bold text-lg" style="font-family:'Playfair Display',serif">D</span>
						<!-- small dot -->
						<span class="absolute -top-0.5 -right-0.5 h-2.5 w-2.5 rounded-full bg-white border-2 border-[#1a2e45]"></span>
					</div>
					<div class="leading-tight">
						<div
							class="text-[17px] font-bold text-white tracking-wide"
							style="font-family:'Playfair Display',serif;"
						>
							Drw<span style="color:#e8a0b4"> Skincare</span>
						</div>
						<div class="text-[9px] font-semibold tracking-[0.2em] uppercase" style="color:rgba(200,116,138,0.6)">
							Klinik Kecantikan · Padang
						</div>
					</div>
				</a>

				<!-- Desktop Nav -->
				<div class="hidden items-center gap-1 md:flex">
					{#each navLinks as link}
						<a
							href={link.href}
							class="relative rounded-xl px-4 py-2 text-sm font-medium transition-all duration-200 hover:text-white"
							style="color:rgba(255,255,255,0.6)"
						>
							{link.label}
							<span class="absolute bottom-1 left-1/2 h-0.5 w-0 -translate-x-1/2 rounded-full transition-all duration-200 group-hover:w-4" style="background:var(--drw-rose)"></span>
						</a>
					{/each}
				</div>

				<!-- CTA -->
				<div class="hidden items-center gap-3 md:flex">
					<a href="tel:+6282381432222">
						<button
							class="flex h-10 items-center gap-2 rounded-xl border px-4 text-sm font-medium text-white/70 transition-all hover:bg-white/10 hover:text-white"
							style="border-color:rgba(255,255,255,0.12)"
						>
							<Phone class="h-4 w-4" style="color:#e8a0b4" />
							0823-8143-2222
						</button>
					</a>
					<a href="https://wa.me/6282381432222" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-10 items-center gap-2 rounded-xl px-5 text-sm font-semibold text-white shadow-lg transition-all hover:scale-105 hover:shadow-xl"
							style="background:var(--brand-gradient-rose);box-shadow:var(--brand-shadow-rose)"
						>
							<MessageCircle class="h-4 w-4" />
							WhatsApp
						</button>
					</a>
				</div>

				<!-- Mobile Toggle -->
				<button
					onclick={() => (menuOpen = !menuOpen)}
					class="rounded-xl p-2 text-white/70 transition hover:bg-white/10 hover:text-white md:hidden"
					aria-label="Toggle menu"
				>
					{#if menuOpen}<X class="h-6 w-6" />{:else}<Menu class="h-6 w-6" />{/if}
				</button>
			</div>
		</div>

		<!-- Mobile Menu -->
		{#if menuOpen}
			<div class="border-t px-4 pt-3 pb-6 md:hidden" style="background:rgba(13,27,42,0.98);border-color:rgba(200,116,138,0.12)">
				{#each navLinks as link}
					<a
						href={link.href}
						onclick={() => (menuOpen = false)}
						class="flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium transition hover:bg-white/8 hover:text-white"
						style="color:rgba(255,255,255,0.65)"
					>
						<ChevronRight class="h-4 w-4" style="color:#c8748a" />
						{link.label}
					</a>
				{/each}
				<div class="mt-4 grid grid-cols-2 gap-2 border-t pt-4" style="border-color:rgba(200,116,138,0.12)">
					<a href="tel:+6282381432222" class="block">
						<button
							class="flex h-11 w-full items-center justify-center gap-2 rounded-xl border text-sm font-medium text-white/80 transition"
							style="border-color:rgba(200,116,138,0.3)"
						>
							<Phone class="h-4 w-4" style="color:#e8a0b4" /> Telepon
						</button>
					</a>
					<a href="https://wa.me/6282381432222" target="_blank" rel="noopener noreferrer" class="block">
						<button
							class="flex h-11 w-full items-center justify-center gap-2 rounded-xl text-sm font-semibold text-white"
							style="background:var(--brand-gradient-rose)"
						>
							<MessageCircle class="h-4 w-4" /> WhatsApp
						</button>
					</a>
				</div>
			</div>
		{/if}
	</nav>
</header>

<main class="pt-20">

	<!-- ═══════ HERO ═══════ -->
	<section
		id="home"
		class="relative min-h-screen overflow-hidden flex items-center"
		style="background:var(--brand-gradient-hero)"
	>
		<!-- Grid pattern overlay -->
		<div class="pointer-events-none absolute inset-0 grid-pattern opacity-60"></div>

		<!-- Large decorative circle -->
		<div
			class="pointer-events-none absolute -top-40 -right-40 h-[700px] w-[700px] rounded-full opacity-[0.06]"
			style="background:radial-gradient(circle, #c8748a 0%, transparent 65%); filter:blur(1px);"
		></div>
		<div
			class="pointer-events-none absolute bottom-0 -left-20 h-[450px] w-[450px] rounded-full opacity-[0.05]"
			style="background:radial-gradient(circle, #c8748a 0%, transparent 65%); filter:blur(1px);"
		></div>

		<!-- Diagonal accent line -->
		<div
			class="pointer-events-none absolute top-0 right-0 bottom-0 w-px opacity-20"
			style="background:linear-gradient(to bottom, transparent, #c8748a 30%, #c8748a 70%, transparent);left:55%"
		></div>

		<div class="relative mx-auto max-w-7xl px-4 pb-20 pt-24 sm:px-6 lg:grid lg:grid-cols-12 lg:gap-0 lg:px-8 lg:pt-32">

			<!-- Left content – 6 cols -->
			<div class="animate-slide-up lg:col-span-6 flex flex-col justify-center space-y-8">

				<!-- Tag pill -->
				<div class="inline-flex items-center gap-2.5 self-start rounded-full border px-4 py-2"
					style="border-color:rgba(200,116,138,0.35);background:rgba(200,116,138,0.1)"
				>
					<span class="h-2 w-2 animate-pulse rounded-full" style="background:#e8a0b4"></span>
					<span class="text-sm font-semibold" style="color:#e8a0b4">Klinik Kecantikan Medis · Aie Pacah, Padang</span>
				</div>

				<!-- Heading -->
				<div class="animate-slide-up delay-100">
					<h1
						class="text-5xl leading-[1.08] text-white sm:text-6xl lg:text-[70px]"
						style="font-family:'Playfair Display',serif;font-weight:400"
					>
						Kulit <em style="color:#e8a0b4">Sehat</em><br />
						<span style="font-weight:700">& Bercahaya</span><br />
						<span class="text-white/50 text-4xl lg:text-5xl" style="font-weight:300">bersama dr. Wahyu</span>
					</h1>
				</div>

				<p class="animate-slide-up max-w-md text-base leading-relaxed text-white/55 delay-200" style="font-size:1.05rem">
					Drw Skincare hadir di Padang dengan pendekatan perawatan skin medis yang personal dan profesional. Ditangani langsung oleh <strong style="color:rgba(232,160,180,0.9)">dr. Wahyu Triasmara</strong> — founder & dokter kulit berpengalaman.
				</p>

				<!-- CTA Buttons -->
				<div class="animate-slide-up flex flex-wrap gap-4 delay-300">
					<a href="https://wa.me/6282381432222" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-14 items-center gap-2.5 rounded-2xl px-8 text-sm font-bold text-white transition-all hover:scale-105 hover:shadow-2xl"
							style="background:var(--brand-gradient-rose);box-shadow:var(--brand-shadow-rose)"
						>
							<MessageCircle class="h-5 w-5" />
							Konsultasi via WhatsApp
						</button>
					</a>
					<a href="#services">
						<button
							class="flex h-14 items-center gap-2.5 rounded-2xl border px-8 text-sm font-semibold text-white/80 transition-all hover:bg-white/8 hover:text-white"
							style="border-color:rgba(255,255,255,0.18)"
						>
							Lihat Layanan <ArrowRight class="h-4 w-4" />
						</button>
					</a>
				</div>

				<!-- Trust badges row -->
				<div class="animate-slide-up flex flex-wrap items-center gap-6 border-t pt-6 delay-400" style="border-color:rgba(255,255,255,0.08)">
					{#each [['🩺', 'Dokter Resmi'], ['📍', 'Aie Pacah, Padang'], ['📞', '0823-8143-2222']] as [icon, label]}
						<div class="flex items-center gap-2">
							<span class="text-lg">{icon}</span>
							<span class="text-sm font-medium text-white/60">{label}</span>
						</div>
					{/each}
				</div>
			</div>

			<!-- Right – image area: 6 cols -->
			<div class="animate-slide-left relative mt-16 lg:col-span-6 lg:mt-0 delay-200">
				<!-- Main image container with geometric clip -->
				<div class="relative pl-8 lg:pl-16">
					<!-- Background shape -->
					<div
						class="absolute inset-6 rounded-3xl"
						style="background:rgba(200,116,138,0.08);border:1px solid rgba(200,116,138,0.15)"
					></div>

					<!-- Image with unique shape -->
					<div
						class="relative overflow-hidden shadow-2xl"
						style="border-radius:24px 80px 24px 80px;box-shadow:0 40px 80px -20px rgba(0,0,0,0.6)"
					>
						<img
							src="https://images.unsplash.com/photo-1629909613654-28e377c37b09?q=80&w=700&auto=format&fit=crop"
							alt="Drw Skincare professional skincare treatment"
							class="w-full object-cover transition-transform duration-700 hover:scale-105"
							style="aspect-ratio:3/4"
						/>
						<!-- Overlay gradient -->
						<div
							class="absolute inset-0"
							style="background:linear-gradient(to top, rgba(13,27,42,0.5) 0%, transparent 50%)"
						></div>
					</div>

					<!-- Floating doctor badge -->
					<div
						class="glass-navy animate-float-gentle absolute -left-2 top-12 rounded-2xl px-5 py-4 shadow-2xl lg:-left-8"
					>
						<div class="flex items-center gap-3">
							<div
								class="flex h-10 w-10 items-center justify-center rounded-xl text-white font-bold"
								style="background:var(--brand-gradient-rose)"
							>
								👨‍⚕️
							</div>
							<div>
								<div class="text-xs font-bold text-white">dr. Wahyu Triasmara</div>
								<div class="text-[10px]" style="color:rgba(232,160,180,0.8)">Founder & Dokter Skincare</div>
							</div>
						</div>
					</div>

					<!-- Floating hours badge -->
					<div
						class="glass-navy animate-float-gentle absolute -bottom-4 right-4 rounded-2xl px-5 py-4 shadow-2xl lg:right-0"
						style="animation-delay:1.5s"
					>
						<div class="text-center">
							<div class="text-xs font-bold text-white">Buka Setiap Hari</div>
							<div class="mt-1 text-[11px]" style="color:rgba(232,160,180,0.8)">Senin–Sabtu 07.00–21.00</div>
							<div class="mt-0.5 text-[10px]" style="color:rgba(232,160,180,0.6)">Minggu: 24 Jam 🌙</div>
						</div>
					</div>

					<!-- Geometric decorative ring -->
					<div
						class="animate-spin-slow pointer-events-none absolute -right-6 top-1/2 h-28 w-28 -translate-y-1/2 rounded-full border-2 border-dashed opacity-25"
						style="border-color:#c8748a"
					></div>
				</div>
			</div>
		</div>

		<!-- Bottom diagonal cut -->
		<div class="pointer-events-none absolute inset-x-0 bottom-0">
			<svg viewBox="0 0 1440 80" fill="none" preserveAspectRatio="none" class="w-full" style="height:70px">
				<path d="M0 80L1440 80L1440 0L0 60Z" fill="#fefaf8" />
			</svg>
		</div>
	</section>

	<!-- ═══════ STATS STRIP ═══════ -->
	<section class="py-0" style="background:#fefaf8">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-2 gap-px md:grid-cols-4" style="background:rgba(200,116,138,0.1)">
				{#each stats as s}
					<div class="flex flex-col items-center py-10 text-center" style="background:#fefaf8">
						<div class="text-4xl font-bold" style="font-family:'Playfair Display',serif;color:#0d1b2a">
							{s.value}
						</div>
						<div class="mt-1.5 text-sm font-bold tracking-wide" style="color:#c8748a">{s.label}</div>
						<div class="mt-0.5 text-xs" style="color:#6b7f93">{s.sub}</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ ABOUT ═══════ -->
	<section id="about" class="py-28 relative overflow-hidden" style="background:#fefaf8">
		<!-- Dot pattern bg -->
		<div class="pointer-events-none absolute inset-0 dot-pattern opacity-50"></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-1 items-center gap-16 lg:grid-cols-2">

				<!-- Content side -->
				<div class="space-y-8">
					<!-- Label -->
					<div class="flex items-center gap-3">
						<div class="h-px w-10 rounded" style="background:var(--brand-gradient-rose)"></div>
						<span class="text-sm font-bold tracking-widest uppercase" style="color:#c8748a">Tentang Kami</span>
					</div>

					<div>
						<h2
							class="text-4xl leading-tight lg:text-5xl"
							style="font-family:'Playfair Display',serif;color:#0d1b2a;font-weight:400"
						>
							Klinik Skincare<br />
							<em style="color:#c8748a;font-weight:600">Tepercaya</em> di Padang
						</h2>
					</div>

					<p class="text-base leading-relaxed" style="color:#3d4f60">
						<strong style="color:#0d1b2a">Drw Skincare</strong> adalah klinik kecantikan dan kesehatan kulit yang berfokus pada perawatan medis yang personal dan profesional. Berlokasi di <strong style="color:#0d1b2a">Residence Tahap 1 Blok i6, Aie Pacah, Koto Tangah, Kota Padang</strong>, kami siap memberikan layanan terbaik untuk kulit Anda.
					</p>
					<p class="text-sm leading-relaxed" style="color:#6b7f93">
						Didirikan dan dikelola langsung oleh <strong>dr. Wahyu Triasmara</strong>, setiap pasien mendapatkan perhatian penuh dan rencana perawatan yang disesuaikan dengan kebutuhan spesifik kulit mereka.
					</p>

					<!-- Feature list -->
					<div class="grid grid-cols-1 gap-3 sm:grid-cols-2">
						{#each [
							'Ditangani dokter berpengalaman',
							'Diagnosa & konsultasi personal',
							'Klinik resmi & berlisensi',
							'Bahan perawatan medis berkualitas',
							'Harga transparan & terjangkau',
							'Buka 7 hari + Minggu 24 jam'
						] as item}
							<div
								class="flex items-center gap-3 rounded-xl border px-4 py-3 transition-all card-hover"
								style="border-color:rgba(200,116,138,0.15);background:rgba(200,116,138,0.03)"
							>
								<div class="flex h-5 w-5 shrink-0 items-center justify-center rounded-full" style="background:var(--brand-gradient-rose)">
									<CheckCircle2 class="h-3 w-3 text-white" />
								</div>
								<span class="text-sm font-medium" style="color:#0d1b2a">{item}</span>
							</div>
						{/each}
					</div>

					<a href="#contact">
						<button
							class="flex h-12 items-center gap-2.5 rounded-2xl px-8 text-sm font-bold text-white transition-all hover:scale-105 hover:shadow-lg"
							style="background:var(--brand-gradient)"
						>
							Hubungi Kami <ArrowRight class="h-4 w-4" />
						</button>
					</a>
				</div>

				<!-- Image collage -->
				<div class="relative">
					<!-- Main large image -->
					<div
						class="overflow-hidden rounded-3xl shadow-2xl"
						style="border-radius:40px 12px 40px 12px"
					>
						<img
							src="https://images.unsplash.com/photo-1614159689907-42a5ab3d5803?q=80&w=600&auto=format&fit=crop"
							alt="Drw Skincare klinik interior"
							class="w-full object-cover transition-transform duration-500 hover:scale-105"
							style="aspect-ratio:4/5"
						/>
					</div>

					<!-- Small overlapping image -->
					<div
						class="absolute -bottom-6 -left-6 overflow-hidden rounded-2xl border-4 shadow-xl"
						style="border-color:#fefaf8;width:48%"
					>
						<img
							src="https://images.unsplash.com/photo-1556228578-8c89e6adf883?q=80&w=350&auto=format&fit=crop"
							alt="Skincare products"
							class="w-full object-cover"
							style="aspect-ratio:4/3"
						/>
					</div>

					<!-- Accent card -->
					<div
						class="absolute -top-5 -right-5 rounded-2xl px-6 py-5 shadow-2xl text-center"
						style="background:var(--brand-gradient-rose);min-width:130px"
					>
						<div class="text-3xl font-bold text-white" style="font-family:'Playfair Display',serif">
							0823
						</div>
						<div class="mt-1 text-[10px] font-bold tracking-widest uppercase text-white/70">
							Hubungi Kami
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ WHY US ═══════ -->
	<section class="py-20" style="background:#fdf0f0">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mb-14 text-center">
				<div class="mb-3 inline-flex items-center gap-3">
					<div class="h-px w-8 rounded" style="background:var(--brand-gradient-rose)"></div>
					<span class="text-sm font-bold tracking-widest uppercase" style="color:#c8748a">Mengapa Drw Skincare</span>
					<div class="h-px w-8 rounded" style="background:var(--brand-gradient-rose)"></div>
				</div>
				<h2 class="text-3xl lg:text-4xl" style="font-family:'Playfair Display',serif;color:#0d1b2a;font-weight:400">
					Kepercayaan Anda, <em style="color:#c8748a;font-weight:600">Prioritas Kami</em>
				</h2>
			</div>

			<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
				{#each whyUs as w}
					<div
						class="group rounded-2xl border bg-white p-7 transition-all card-hover"
						style="border-color:rgba(200,116,138,0.15);box-shadow:var(--brand-shadow-card)"
					>
						<div
							class="mb-5 flex h-14 w-14 items-center justify-center rounded-2xl transition-transform duration-300 group-hover:scale-110"
							style="background:var(--brand-gradient-rose)"
						>
							<svelte:component this={w.icon} class="h-6 w-6 text-white" />
						</div>
						<h3 class="mb-2 text-base font-bold" style="color:#0d1b2a">{w.title}</h3>
						<p class="text-sm leading-relaxed" style="color:#6b7f93">{w.desc}</p>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ SERVICES ═══════ -->
	<section id="services" class="relative overflow-hidden py-28" style="background:var(--drw-navy)">
		<!-- Pattern -->
		<div class="pointer-events-none absolute inset-0 dot-pattern-navy"></div>

		<!-- Accent glow -->
		<div
			class="pointer-events-none absolute -top-20 right-1/4 h-[400px] w-[400px] rounded-full opacity-[0.08]"
			style="background:radial-gradient(circle, #c8748a 0%, transparent 65%); filter:blur(40px);"
		></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<!-- Header -->
			<div class="mb-16 max-w-2xl">
				<div class="mb-3 flex items-center gap-3">
					<div class="h-px w-10 rounded" style="background:var(--brand-gradient-rose)"></div>
					<span class="text-sm font-bold tracking-widest uppercase" style="color:#e8a0b4">Layanan Kami</span>
				</div>
				<h2
					class="text-4xl font-light text-white lg:text-5xl"
					style="font-family:'Playfair Display',serif"
				>
					Perawatan <em class="font-semibold" style="color:#e8a0b4">Profesional</em><br />
					untuk Kulit Terbaik Anda
				</h2>
				<p class="mt-5 text-sm leading-relaxed" style="color:rgba(255,255,255,0.45)">
					Setiap layanan di Drw Skincare dirancang dengan standar medis tinggi, ditangani langsung oleh dr. Wahyu Triasmara untuk hasil yang optimal.
				</p>
			</div>

			<!-- Services grid – 3 col, asymmetric sizes -->
			<div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
				{#each services as svc, i}
					<div
						class="group relative overflow-hidden rounded-2xl border p-7 transition-all duration-350 hover:-translate-y-2 hover:border-pink-400/30"
						style="border-color:rgba(200,116,138,0.12);background:rgba(255,255,255,0.03)"
						class:lg:col-span-1={true}
					>
						<!-- Corner accent -->
						<div
							class="absolute top-0 right-0 h-16 w-16 opacity-0 transition-opacity duration-300 group-hover:opacity-100"
							style="background:linear-gradient(135deg, transparent 50%, rgba(200,116,138,0.08) 50%)"
						></div>

						<!-- Tag -->
						<div class="mb-5 inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-[10px] font-bold tracking-widest uppercase"
							style="background:rgba(200,116,138,0.12);color:#e8a0b4"
						>
							{svc.tag}
						</div>

						<!-- Icon -->
						<div
							class="mb-4 flex h-12 w-12 items-center justify-center rounded-xl border transition-all duration-300 group-hover:scale-110 group-hover:border-pink-400/40"
							style="border-color:rgba(200,116,138,0.2);background:rgba(200,116,138,0.08)"
						>
							<svelte:component this={svc.icon} class="h-6 w-6" style="color:#e8a0b4" />
						</div>

						<h3 class="mb-3 text-xl font-semibold text-white" style="font-family:'Playfair Display',serif">
							{svc.title}
						</h3>
						<p class="text-sm leading-relaxed" style="color:rgba(255,255,255,0.45)">{svc.desc}</p>

						<!-- Hover CTA -->
						<div
							class="mt-6 flex items-center gap-1.5 text-xs font-bold opacity-0 transition-opacity duration-300 group-hover:opacity-100"
							style="color:#e8a0b4"
						>
							Tanya dokter <ArrowRight class="h-3.5 w-3.5" />
						</div>

						<!-- Bottom line accent -->
						<div
							class="absolute bottom-0 left-0 h-0.5 w-0 rounded-full transition-all duration-500 group-hover:w-full"
							style="background:var(--brand-gradient-rose)"
						></div>
					</div>
				{/each}
			</div>

			<!-- CTA -->
			<div class="mt-14 text-center">
				<a href="https://wa.me/6282381432222" target="_blank" rel="noopener noreferrer">
					<button
						class="inline-flex h-14 items-center gap-3 rounded-2xl px-10 text-sm font-bold text-white transition-all hover:scale-105 hover:shadow-2xl"
						style="background:var(--brand-gradient-rose);box-shadow:var(--brand-shadow-rose)"
					>
						<MessageCircle class="h-5 w-5" />
						Konsultasikan Kebutuhan Kulit Anda
					</button>
				</a>
			</div>
		</div>
	</section>

	<!-- ═══════ HOURS ═══════ -->
	<section id="hours" class="py-24" style="background:#fefaf8">
		<div class="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-1 gap-16 lg:grid-cols-2 items-center">

				<!-- Left: heading & info -->
				<div class="space-y-6">
					<div class="flex items-center gap-3">
						<div class="h-px w-10 rounded" style="background:var(--brand-gradient-rose)"></div>
						<span class="text-sm font-bold tracking-widest uppercase" style="color:#c8748a">Jam Operasional</span>
					</div>
					<h2 class="text-4xl lg:text-5xl" style="font-family:'Playfair Display',serif;color:#0d1b2a;font-weight:400">
						Kami <em style="color:#c8748a;font-weight:600">Selalu</em><br />Ada untuk Anda
					</h2>
					<p class="text-base leading-relaxed" style="color:#6b7f93">
						Drw Skincare buka 7 hari seminggu dengan jam operasional yang panjang agar Anda dapat berkunjung kapan saja sesuai jadwal. Bahkan di hari Minggu, kami buka <strong style="color:#c8748a">24 jam penuh</strong> melayani Anda!
					</p>

					<!-- Call to action -->
					<a href="tel:+6282381432222">
						<button
							class="flex h-12 items-center gap-3 rounded-2xl border-2 px-7 text-sm font-bold transition-all hover:shadow-lg"
							style="border-color:#c8748a;color:#c8748a;background:transparent"
						>
							<Phone class="h-4 w-4" />
							0823-8143-2222
						</button>
					</a>
				</div>

				<!-- Right: hours card -->
				<div class="overflow-hidden rounded-3xl border shadow-2xl" style="border-color:rgba(200,116,138,0.2)">
					<!-- Card header -->
					<div
						class="px-7 py-5"
						style="background:var(--brand-gradient)"
					>
						<div class="flex items-center gap-3">
							<Clock class="h-5 w-5" style="color:#e8a0b4" />
							<div>
								<div class="text-sm font-bold text-white">Jadwal Buka</div>
								<div class="text-[11px]" style="color:rgba(232,160,180,0.6)">Drw Skincare – Aie Pacah, Padang</div>
							</div>
						</div>
					</div>

					<!-- Hours list -->
					<div style="background:#fefaf8">
						{#each hours as h, i}
							<div
								class="flex items-center justify-between px-7 py-4 transition-colors hover:bg-pink-50"
								class:border-t={i !== 0}
								style="border-color:rgba(200,116,138,0.1)"
							>
								<div class="flex items-center gap-3">
									<!-- Day indicator dot -->
									<div
										class="h-2 w-2 rounded-full"
										style="background:{h.special ? 'linear-gradient(135deg,#c8748a,#e8a0b4)' : '#0d1b2a'}"
									></div>
									<span class="font-semibold text-sm" style="color:#0d1b2a">{h.day}</span>
									{#if h.special}
										<span
											class="rounded-full px-2 py-0.5 text-[9px] font-bold uppercase"
											style="background:linear-gradient(135deg,#c8748a,#e8a0b4);color:white"
										>Special</span>
									{/if}
								</div>
								<div class="flex items-center gap-2">
									<span class="text-sm font-bold" style="color:{h.special ? '#c8748a' : '#3d4f60'}">{h.time}</span>
									<span
										class="rounded-full px-2.5 py-0.5 text-[10px] font-bold uppercase"
										style="background:rgba(13,27,42,0.07);color:#0d1b2a"
									>Buka</span>
								</div>
							</div>
						{/each}
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ REVIEWS ═══════ -->
	<section id="reviews" class="py-24 relative" style="background:#fdf0f0">
		<div class="pointer-events-none absolute inset-0 dot-pattern opacity-40"></div>
		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">

			<div class="mb-16 text-center">
				<div class="mb-3 inline-flex items-center gap-3">
					<div class="h-px w-8 rounded" style="background:var(--brand-gradient-rose)"></div>
					<span class="text-sm font-bold tracking-widest uppercase" style="color:#c8748a">Ulasan Pelanggan</span>
					<div class="h-px w-8 rounded" style="background:var(--brand-gradient-rose)"></div>
				</div>
				<h2
					class="text-4xl lg:text-5xl"
					style="font-family:'Playfair Display',serif;color:#0d1b2a;font-weight:400"
				>
					Suara Mereka yang <em style="color:#c8748a;font-weight:600">Telah Percaya</em>
				</h2>

				<!-- Rating pill -->
				<div
					class="mt-6 inline-flex items-center gap-4 rounded-2xl border bg-white px-7 py-4 shadow-sm"
					style="border-color:rgba(200,116,138,0.2)"
				>
					<div>
						<div class="text-4xl font-bold" style="font-family:'Playfair Display',serif;color:#0d1b2a">★★★★★</div>
					</div>
					<Separator orientation="vertical" class="h-8" />
					<div class="text-left">
						<div class="text-sm font-bold" style="color:#0d1b2a">Rating Bintang 5</div>
						<div class="text-xs" style="color:#6b7f93">Google Maps · Drw Skincare</div>
					</div>
				</div>
			</div>

			<div class="grid grid-cols-1 gap-6 md:grid-cols-3">
				{#each reviews as rv, i}
					<div
						class="group relative flex flex-col rounded-3xl bg-white p-8 shadow-sm transition-all card-hover"
						style="border:1px solid rgba(200,116,138,0.12);box-shadow:var(--brand-shadow-card)"
					>
						<!-- Quote mark -->
						<div
							class="mb-3 text-6xl font-bold leading-none select-none"
							style="color:rgba(200,116,138,0.15);font-family:'Playfair Display',serif"
						>
							"
						</div>

						<p class="mb-6 flex-1 text-sm leading-relaxed" style="color:#3d4f60">{rv.text}</p>

						<!-- Stars -->
						<div class="mb-4 flex gap-1">
							{#each Array(rv.stars) as _}
								<Star class="h-4 w-4 fill-current" style="color:#c8748a" />
							{/each}
						</div>

						<Separator style="background:rgba(200,116,138,0.12)" />

						<div class="mt-4 flex items-center gap-3">
							<div
								class="flex h-11 w-11 items-center justify-center rounded-full text-sm font-bold text-white"
								style="background:var(--brand-gradient-rose)"
							>
								{rv.initial}
							</div>
							<div>
								<div class="text-sm font-bold" style="color:#0d1b2a">{rv.name}</div>
								<div class="mt-0.5 flex items-center gap-1.5 text-xs" style="color:#9ab0c4">
									{#if rv.isGuide}
										<span
											class="rounded-full px-1.5 py-0.5 text-[10px] font-bold"
											style="background:rgba(200,116,138,0.1);color:#c8748a"
										>Local Guide</span>
									{/if}
									<span>{rv.count}</span> · <span>{rv.time}</span>
								</div>
							</div>
						</div>

						<!-- Bottom accent line on hover -->
						<div
							class="absolute bottom-0 left-0 right-0 h-1 rounded-b-3xl opacity-0 transition-opacity duration-300 group-hover:opacity-100"
							style="background:var(--brand-gradient-rose)"
						></div>
					</div>
				{/each}
			</div>

			<div class="mt-10 text-center">
				<a
					href="https://maps.google.com/?q=Drw+Skincare+Aie+Pacah+Padang"
					target="_blank"
					rel="noopener noreferrer"
				>
					<button
						class="inline-flex h-12 items-center gap-2 rounded-2xl border-2 px-8 text-sm font-bold transition-all hover:bg-pink-50"
						style="border-color:rgba(200,116,138,0.4);color:#c8748a"
					>
						Lihat di Google Maps <ArrowRight class="h-4 w-4" />
					</button>
				</a>
			</div>
		</div>
	</section>

	<!-- ═══════ CONTACT / CTA ═══════ -->
	<section id="contact" class="relative overflow-hidden py-28" style="background:var(--drw-navy)">
		<div class="pointer-events-none absolute inset-0 dot-pattern-navy"></div>

		<!-- Rose glow -->
		<div
			class="pointer-events-none absolute top-0 left-1/2 h-[500px] w-[500px] -translate-x-1/2 -translate-y-1/2 rounded-full opacity-[0.07]"
			style="background:radial-gradient(circle, #c8748a 0%, transparent 65%)"
		></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<!-- Header -->
			<div class="mb-16 text-center">
				<div class="mb-3 inline-flex items-center gap-3">
					<div class="h-px w-8 rounded" style="background:var(--brand-gradient-rose)"></div>
					<span class="text-sm font-bold tracking-widest uppercase" style="color:#e8a0b4">Hubungi & Kunjungi</span>
					<div class="h-px w-8 rounded" style="background:var(--brand-gradient-rose)"></div>
				</div>
				<h2
					class="text-4xl font-light text-white lg:text-5xl"
					style="font-family:'Playfair Display',serif"
				>
					Kunjungi Kami di <em class="font-semibold" style="color:#e8a0b4">Aie Pacah,</em><br />Kota Padang
				</h2>
			</div>

			<div class="grid grid-cols-1 gap-8 lg:grid-cols-3">
				<!-- Info cards -->
				<div class="space-y-5 lg:col-span-1">
					<!-- Address card -->
					<div
						class="rounded-2xl border p-6 transition-all hover:border-pink-400/30"
						style="border-color:rgba(200,116,138,0.15);background:rgba(255,255,255,0.04)"
					>
						<div class="mb-4 flex items-center gap-3">
							<div
								class="flex h-11 w-11 items-center justify-center rounded-xl"
								style="background:var(--brand-gradient-rose)"
							>
								<MapPin class="h-5 w-5 text-white" />
							</div>
							<div class="text-xs font-bold tracking-wider uppercase" style="color:#e8a0b4">Alamat</div>
						</div>
						<p class="text-sm leading-relaxed text-white/65">
							Residence Tahap 1 Blok i6,<br />
							Aie Pacah, Kec. Koto Tangah,<br />
							Kota Padang, Sumatera Barat 25176<br />
							<span class="mt-1 block text-xs" style="color:rgba(232,160,180,0.6)">Kode: 49JG+9H Aie Pacah</span>
						</p>
					</div>

					<!-- Phone card -->
					<a
						href="tel:+6282381432222"
						class="flex items-start gap-4 rounded-2xl border p-6 transition-all hover:border-pink-400/30"
						style="border-color:rgba(200,116,138,0.15);background:rgba(255,255,255,0.04)"
					>
						<div
							class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl"
							style="background:var(--brand-gradient-rose)"
						>
							<Phone class="h-5 w-5 text-white" />
						</div>
						<div>
							<div class="mb-1 text-xs font-bold tracking-wider uppercase" style="color:#e8a0b4">Telepon</div>
							<div class="text-sm font-semibold text-white/80">0823-8143-2222</div>
						</div>
					</a>

					<!-- Hours mini card -->
					<div
						class="rounded-2xl border p-6"
						style="border-color:rgba(200,116,138,0.15);background:rgba(255,255,255,0.04)"
					>
						<div class="mb-4 flex items-center gap-3">
							<div
								class="flex h-11 w-11 items-center justify-center rounded-xl"
								style="background:var(--brand-gradient-rose)"
							>
								<Clock class="h-5 w-5 text-white" />
							</div>
							<div class="text-xs font-bold tracking-wider uppercase" style="color:#e8a0b4">Jam Buka</div>
						</div>
						<div class="space-y-1.5 text-sm text-white/65">
							<div class="flex justify-between"><span>Senin – Sabtu</span><span class="font-semibold text-white/80">07.00 – 21.00</span></div>
							<div class="flex justify-between"><span style="color:#e8a0b4">Minggu</span><span class="font-bold" style="color:#e8a0b4">Buka 24 Jam ✨</span></div>
						</div>
					</div>
				</div>

				<!-- Map embed – 2 cols -->
				<div class="overflow-hidden rounded-3xl shadow-2xl lg:col-span-2" style="border:2px solid rgba(200,116,138,0.15)">
					<iframe
						title="Lokasi Drw Skincare Padang"
						src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.5!2d100.37!3d-0.87!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMDDCsDUyJzEyLjAiUyAxMDDCsDIyJzEyLjAiRQ!5e0!3m2!1sid!2sid!4v1000000000000!5m2!1sid!2sid"
						width="100%"
						height="100%"
						style="border:0;min-height:420px;filter:grayscale(15%) contrast(1.05)"
						allowfullscreen
						loading="lazy"
						referrerpolicy="no-referrer-when-downgrade"
					></iframe>
				</div>
			</div>

			<!-- Bottom CTA banner -->
			<div
				class="mt-12 flex flex-col items-center justify-between gap-6 overflow-hidden rounded-3xl p-8 text-center sm:flex-row sm:text-left"
				style="background:var(--brand-gradient-rose);box-shadow:var(--brand-shadow-rose)"
			>
				<div>
					<div class="text-xl font-bold text-white" style="font-family:'Playfair Display',serif">
						Siap Merawat Kulit Anda Hari Ini?
					</div>
					<p class="mt-1 text-sm text-white/75">
						Hubungi Drw Skincare sekarang dan dapatkan konsultasi dengan dr. Wahyu.
					</p>
				</div>
				<div class="flex shrink-0 flex-col gap-3 sm:flex-row">
					<a href="https://wa.me/6282381432222" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-12 items-center gap-2 rounded-2xl bg-white px-7 text-sm font-bold transition-all hover:scale-105"
							style="color:#c8748a"
						>
							<MessageCircle class="h-4 w-4" /> WhatsApp Sekarang
						</button>
					</a>
					<a href="tel:+6282381432222">
						<button
							class="flex h-12 items-center gap-2 rounded-2xl border-2 border-white/40 px-7 text-sm font-semibold text-white transition-all hover:bg-white/15"
						>
							<Phone class="h-4 w-4" /> Telepon
						</button>
					</a>
				</div>
			</div>
		</div>
	</section>

</main>

<!-- ═══════ FOOTER ═══════ -->
<footer style="background:#080e18;border-top:1px solid rgba(200,116,138,0.1)">
	<div class="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
		<div class="flex flex-col items-center justify-between gap-6 md:flex-row">
			<!-- Brand -->
			<div class="flex items-center gap-3">
				<div
					class="flex h-9 w-9 items-center justify-center rounded-xl"
					style="background:var(--brand-gradient-rose)"
				>
					<span class="text-sm font-bold text-white" style="font-family:'Playfair Display',serif">D</span>
				</div>
				<div>
					<div class="text-sm font-bold text-white" style="font-family:'Playfair Display',serif">
						Drw Skincare
					</div>
					<div class="text-[10px]" style="color:rgba(200,116,138,0.5)">Klinik Kecantikan Padang</div>
				</div>
			</div>

			<!-- Center info -->
			<div class="text-center text-xs" style="color:rgba(255,255,255,0.35)">
				<p>Residence Tahap 1 Blok i6, Aie Pacah, Kec. Koto Tangah, Kota Padang, Sumatera Barat 25176</p>
				<p class="mt-1">
					<a href="tel:+6282381432222" class="hover:text-white/60 transition-colors">0823-8143-2222</a>
					· Founded by dr. Wahyu Triasmara
				</p>
			</div>

			<!-- Right: WA link -->
			<a href="https://wa.me/6282381432222" target="_blank" rel="noopener noreferrer">
				<button
					class="flex h-9 items-center gap-2 rounded-xl px-5 text-xs font-bold text-white transition-all hover:scale-105"
					style="background:var(--brand-gradient-rose)"
				>
					<MessageCircle class="h-3.5 w-3.5" /> WhatsApp
				</button>
			</a>
		</div>

		<div class="mt-8 border-t pt-6 text-center text-[11px]" style="border-color:rgba(255,255,255,0.06);color:rgba(255,255,255,0.2)">
			© 2025 Drw Skincare. All rights reserved.
		</div>
	</div>
</footer>
