<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { Badge } from '$lib/components/ui/badge';
	import { Separator } from '$lib/components/ui/separator';
	import { Avatar, AvatarFallback } from '$lib/components/ui/avatar';
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
		Leaf,
		Zap,
		Award,
		Instagram,
		MessageCircle,
		CheckCircle2,
		ArrowRight,
		Droplets,
		Eye,
		Flower2,
		Gem
	} from 'lucide-svelte';

	let menuOpen = $state(false);

	const navLinks = [
		{ href: '#home', label: 'Beranda' },
		{ href: '#about', label: 'Tentang' },
		{ href: '#services', label: 'Layanan' },
		{ href: '#reviews', label: 'Ulasan' },
		{ href: '#contact', label: 'Kontak' }
	];

	const services = [
		{
			icon: Flower2,
			title: 'Facial Treatment',
			desc: 'Perawatan wajah premium menggunakan bahan natural terpilih untuk kulit cerah, sehat, dan bercahaya secara alami.'
		},
		{
			icon: Droplets,
			title: 'Skin Hydration',
			desc: 'Hidrasi mendalam untuk kulit kering dan kusam. Formula eksklusif berbasis bahan botanis menjaga kelembapan sepanjang hari.'
		},
		{
			icon: Leaf,
			title: 'Natural Body Care',
			desc: 'Rangkaian perawatan tubuh holistik menggunakan ekstrak herbal pilihan yang memperbarui dan melembutkan kulit.'
		},
		{
			icon: Eye,
			title: 'Eye & Lip Treatment',
			desc: 'Perawatan khusus area sensitif mata dan bibir agar tampak lebih segar, kenyal, dan bebas kerutan dini.'
		},
		{
			icon: Shield,
			title: 'Skin Consultation',
			desc: 'Konsultasi personal bersama ahli skincare kami untuk solusi perawatan yang tepat sesuai jenis kulit Anda.'
		},
		{
			icon: Gem,
			title: 'Paket Eksklusif',
			desc: 'Nikmati rangkaian lengkap treatment premium dalam satu paket eksklusif dengan hasil optimal dan menyeluruh.'
		}
	];

	const stats = [
		{ value: '5.0', label: 'Rating Google', sub: 'Sempurna' },
		{ value: '174', label: 'Ulasan', sub: 'Pelanggan puas' },
		{ value: '100%', label: 'Natural', sub: 'Bahan alami' },
		{ value: '7', label: 'Hari Buka', sub: 'Setiap minggu' }
	];

	const hours = [
		{ day: 'Senin', time: '09.00 – 20.00', open: true },
		{ day: 'Selasa', time: '09.00 – 20.00', open: true },
		{ day: 'Rabu', time: '09.00 – 20.00', open: true },
		{ day: 'Kamis', time: '09.00 – 20.00', open: true },
		{ day: 'Jumat', time: '09.00 – 20.00', open: true },
		{ day: 'Sabtu', time: '09.00 – 20.00', open: true },
		{ day: 'Minggu', time: '09.00 – 17.00', open: true }
	];

	const reviews = [
		{
			name: 'Indah Yosefa',
			initial: 'IY',
			count: '2 ulasan',
			time: '5 bulan lalu',
			stars: 5,
			text: 'Perawatan wajah terbaik dan alami 🥰 Kulit saya terasa jauh lebih lembut dan cerah setelah rutin treatment di sini. Karyawannya ramah dan tempatnya bersih. Sangat direkomendasikan!'
		},
		{
			name: 'SYUHAIBI',
			initial: 'SH',
			count: '1 ulasan',
			time: '8 tahun lalu',
			stars: 5,
			text: 'Karena banyak yang datang untuk perawatan tubuh serta lokasinya aman dan dekat rumah saya. Pelayanan memuaskan dan hasilnya benar-benar terasa. Sudah jadi pelanggan setia dari dulu!'
		},
		{
			name: 'Dicky NPS',
			initial: 'DN',
			count: '1 ulasan · 44 foto',
			time: '5 tahun lalu',
			stars: 5,
			text: 'Layanannya Ok ✅ Tempatnya nyaman, produknya berkualitas, dan hasilnya memuaskan. Cocok untuk yang ingin perawatan premium dengan harga terjangkau di Kota Padang.',
			isGuide: true
		}
	];

	const values = [
		'Formulasi 100% bahan alami & aman',
		'Tenaga ahli berpengalaman & terlatih',
		'Konsultasi kulit personal setiap sesi',
		'Lingkungan bersih, nyaman & steril',
		'Harga transparan & terjangkau',
		'Buka 7 hari – Senin hingga Minggu'
	];
</script>

<svelte:head>
	<title>Naavagreen Natural Skincare Padang – Klinik Kecantikan Alami Terbaik</title>
	<meta
		name="description"
		content="Naavagreen Natural Skincare Padang – klinik kesehatan dan kecantikan alami terpercaya di Padang. Rating 5.0 ⭐ dari 174 pelanggan. Jl. S. Parman 153 B, Padang Utara."
	/>
</svelte:head>

<!-- ═══════ NAVBAR ═══════ -->
<header class="fixed inset-x-0 top-0 z-50">
	<nav class="border-b border-white/10 bg-[#16312a]/95 shadow-lg backdrop-blur-xl">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-[76px] items-center justify-between">
				<!-- Logo -->
				<a href="#home" class="group flex items-center gap-3">
					<div
						class="flex h-10 w-10 items-center justify-center rounded-full shadow-lg transition-transform group-hover:scale-110"
						style="background: var(--brand-gradient-gold)"
					>
						<Leaf class="h-5 w-5 text-white" />
					</div>
					<div class="leading-tight">
						<div
							class="text-base font-bold tracking-wide text-white"
							style="font-family:'Cormorant Garamond',serif;letter-spacing:0.08em;"
						>
							NAAVAGREEN
						</div>
						<div class="text-[9px] font-medium tracking-widest text-white/50 uppercase">
							Natural Skincare · Padang
						</div>
					</div>
				</a>

				<!-- Desktop Nav -->
				<div class="hidden items-center gap-1 md:flex">
					{#each navLinks as link}
						<a
							href={link.href}
							class="rounded-full px-4 py-2 text-sm font-medium text-white/70 transition-all duration-200 hover:bg-white/10 hover:text-white"
						>
							{link.label}
						</a>
					{/each}
				</div>

				<!-- CTA -->
				<div class="hidden items-center gap-3 md:flex">
					<a href="https://wa.me/6281128002556" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-10 items-center gap-2 rounded-full px-5 text-sm font-semibold text-[#16312a] shadow-lg transition-all hover:scale-105 hover:shadow-xl"
							style="background: var(--brand-gradient-gold); box-shadow: var(--brand-shadow-gold)"
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
			<div class="border-t border-white/10 bg-[#16312a] px-4 pt-2 pb-5 md:hidden">
				{#each navLinks as link}
					<a
						href={link.href}
						onclick={() => (menuOpen = false)}
						class="flex items-center gap-2 rounded-xl px-3 py-3 text-sm font-medium text-white/70 transition hover:bg-white/10 hover:text-white"
					>
						<ChevronRight class="h-4 w-4" />
						{link.label}
					</a>
				{/each}
				<div class="mt-4 border-t border-white/10 pt-4">
					<a
						href="https://wa.me/6281128002556"
						target="_blank"
						rel="noopener noreferrer"
						class="block"
					>
						<button
							class="flex h-11 w-full items-center justify-center gap-2 rounded-full text-sm font-semibold text-[#16312a]"
							style="background: var(--brand-gradient-gold)"
						>
							<MessageCircle class="h-4 w-4" /> Chat WhatsApp
						</button>
					</a>
				</div>
			</div>
		{/if}
	</nav>
</header>

<main class="pt-[76px]">
	<!-- ═══════ HERO ═══════ -->
	<section
		id="home"
		class="relative min-h-screen overflow-hidden"
		style="background:var(--ng-green-deep)"
	>
		<!-- Decorative blobs -->
		<div
			class="pointer-events-none absolute -top-32 -left-32 h-[500px] w-[500px] rounded-full opacity-10"
			style="background:radial-gradient(circle, #2d6a4f 0%, transparent 70%); filter:blur(60px);"
		></div>
		<div
			class="pointer-events-none absolute top-1/3 -right-20 h-[350px] w-[350px] rounded-full opacity-10"
			style="background:radial-gradient(circle, #c9a25a 0%, transparent 70%); filter:blur(70px);"
		></div>
		<div
			class="pointer-events-none absolute bottom-0 left-1/3 h-[300px] w-[300px] rounded-full opacity-8"
			style="background:radial-gradient(circle, #1f4a3a 0%, transparent 70%); filter:blur(50px);"
		></div>

		<!-- Dot grid -->
		<div
			class="pointer-events-none absolute inset-0"
			style="background-image:radial-gradient(circle,rgba(201,162,90,0.07) 1px,transparent 1px);background-size:32px 32px;"
		></div>

		<div
			class="relative mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-4 py-24 sm:px-6 lg:grid-cols-2 lg:gap-20 lg:px-8"
		>
			<!-- Left content -->
			<div class="space-y-8">
				<!-- Badge -->
				<div
					class="animate-reveal-up inline-flex items-center gap-3 rounded-full border px-5 py-2.5"
					style="border-color:rgba(201,162,90,0.3);background:rgba(201,162,90,0.08)"
				>
					<span class="h-2 w-2 animate-pulse rounded-full" style="background:#c9a25a"></span>
					<span class="text-sm font-medium" style="color:#e8c98a"
						>⭐ Rating 5.0 · 174 Ulasan Google</span
					>
				</div>

				<!-- Heading -->
				<div class="animate-reveal-up delay-100">
					<h1
						class="text-5xl leading-[1.05] font-light text-white sm:text-6xl lg:text-7xl"
						style="font-family:'Cormorant Garamond',serif"
					>
						<em>Kulit Sehat,</em><br />
						<span class="font-semibold" style="color:#c9a25a">Cantik Alami</span><br />
						<span class="text-white/80">dari Alam</span>
					</h1>
				</div>

				<p
					class="animate-reveal-up max-w-md text-base leading-relaxed text-white/60 delay-200"
					style="font-size:1.05rem"
				>
					Naavagreen Natural Skincare hadir di Padang menghadirkan perawatan kulit premium berbasis
					bahan alami. Dipercaya oleh ratusan pelanggan sejak bertahun-tahun.
				</p>

				<div class="animate-reveal-up flex flex-wrap gap-4 delay-300">
					<a href="#services">
						<button
							class="flex h-13 items-center gap-2 rounded-full px-8 text-[0.95rem] font-semibold text-[#16312a] shadow-xl transition-all hover:scale-105 hover:shadow-2xl"
							style="background:var(--brand-gradient-gold);box-shadow:var(--brand-shadow-gold)"
						>
							Lihat Layanan <ArrowRight class="h-4 w-4" />
						</button>
					</a>
					<a href="#contact">
						<button
							class="flex h-13 items-center gap-2 rounded-full border px-8 text-[0.95rem] font-semibold text-white/80 transition-all hover:bg-white/10 hover:text-white"
							style="border-color:rgba(255,255,255,0.2)"
						>
							Temukan Kami <MapPin class="h-4 w-4" />
						</button>
					</a>
				</div>

				<!-- Trust badges -->
				<div class="animate-reveal-up flex flex-wrap gap-5 pt-2 delay-400">
					{#each [['🌿', 'Bahan Alami'], ['✨', 'Tenaga Ahli'], ['📍', 'Padang, Sumbar']] as [icon, label]}
						<div class="flex items-center gap-2 text-sm text-white/50">
							<span>{icon}</span>
							<span class="font-medium text-white/70">{label}</span>
						</div>
					{/each}
				</div>
			</div>

			<!-- Right: image -->
			<div
				class="animate-scale-in relative flex items-center justify-center delay-200 lg:justify-end"
			>
				<div class="relative w-full max-w-sm">
					<!-- Main image -->
					<div
						class="overflow-hidden shadow-2xl"
						style="border-radius:60% 40% 55% 45% / 45% 55% 40% 60%;box-shadow:0 30px 80px -15px rgba(0,0,0,0.5)"
					>
						<img
							src="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?q=80&w=700&auto=format&fit=crop"
							alt="Naavagreen Natural Skincare treatment"
							class="h-full w-full object-cover transition-transform duration-700 hover:scale-105"
							style="aspect-ratio:4/5"
						/>
						<div
							class="absolute inset-0"
							style="background:linear-gradient(to top, rgba(22,49,42,0.4) 0%, transparent 60%)"
						></div>
					</div>

					<!-- Floating rating card -->
					<div
						class="glass-dark animate-float absolute -bottom-6 -left-8 rounded-2xl px-5 py-4 shadow-2xl"
					>
						<div class="flex items-center gap-3">
							<div class="flex gap-0.5" style="color:#c9a25a">
								{#each Array(5) as _}<Star class="h-3.5 w-3.5 fill-current" />{/each}
							</div>
							<div>
								<div class="text-sm font-bold text-white">5.0 / 5.0</div>
								<div class="text-xs text-white/50">174 Ulasan</div>
							</div>
						</div>
					</div>

					<!-- Floating "Open" badge -->
					<div
						class="glass-dark animate-float absolute -top-4 -right-6 rounded-2xl px-5 py-3 shadow-xl"
						style="animation-delay:1.2s"
					>
						<div class="flex items-center gap-2">
							<div class="h-2.5 w-2.5 animate-pulse rounded-full bg-emerald-400"></div>
							<div>
								<div class="text-xs font-bold text-white">Buka Sekarang</div>
								<div class="text-[10px] text-white/50">09.00 – 20.00</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Bottom wave -->
		<div class="pointer-events-none absolute inset-x-0 bottom-0">
			<svg
				viewBox="0 0 1440 70"
				fill="none"
				preserveAspectRatio="none"
				class="w-full"
				style="height:60px"
			>
				<path
					d="M0 70L1440 70L1440 35C1200 70 960 0 720 20C480 40 240 70 0 35L0 70Z"
					fill="#fdf8f0"
				/>
			</svg>
		</div>
	</section>

	<!-- ═══════ STATS STRIP ═══════ -->
	<section class="py-0" style="background:#fdf8f0">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div
				class="grid grid-cols-2 gap-px overflow-hidden rounded-none border-y md:grid-cols-4"
				style="border-color:rgba(201,162,90,0.2);background:rgba(201,162,90,0.15)"
			>
				{#each stats as s}
					<div class="flex flex-col items-center py-8 text-center" style="background:#fdf8f0">
						<div
							class="text-4xl font-semibold"
							style="font-family:'Cormorant Garamond',serif;color:#16312a"
						>
							{s.value}
						</div>
						<div class="mt-1 text-xs font-semibold tracking-widest uppercase" style="color:#c9a25a">
							{s.label}
						</div>
						<div class="mt-0.5 text-xs" style="color:#3a5a48">{s.sub}</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ ABOUT ═══════ -->
	<section id="about" class="py-24" style="background:#fdf8f0">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-1 items-center gap-16 lg:grid-cols-2">
				<!-- Images -->
				<div class="relative grid grid-cols-2 gap-4">
					<div class="space-y-4">
						<div class="aspect-[2/3] overflow-hidden rounded-3xl shadow-xl">
							<img
								src="https://images.unsplash.com/photo-1596755389378-c31d21fd1273?q=80&w=500&auto=format&fit=crop"
								alt="Skincare products"
								class="h-full w-full object-cover transition-transform duration-500 hover:scale-105"
							/>
						</div>
					</div>
					<div class="mt-10 space-y-4">
						<div class="aspect-square overflow-hidden rounded-3xl shadow-xl">
							<img
								src="https://images.unsplash.com/photo-1515377905703-c4788e51af15?q=80&w=500&auto=format&fit=crop"
								alt="Beauty products"
								class="h-full w-full object-cover transition-transform duration-500 hover:scale-105"
							/>
						</div>
						<div class="aspect-video overflow-hidden rounded-3xl shadow-xl">
							<img
								src="https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?q=80&w=500&auto=format&fit=crop"
								alt="Clinic interior"
								class="h-full w-full object-cover transition-transform duration-500 hover:scale-105"
							/>
						</div>
					</div>
					<!-- Badge -->
					<div
						class="absolute -bottom-5 left-1/2 -translate-x-1/2 rounded-2xl px-7 py-4 text-center shadow-2xl"
						style="background:var(--brand-gradient);min-width:150px"
					>
						<div
							class="text-3xl font-semibold text-white"
							style="font-family:'Cormorant Garamond',serif"
						>
							5.0
						</div>
						<div
							class="mt-0.5 text-[10px] font-bold tracking-widest uppercase"
							style="color:#e8c98a"
						>
							Rating Sempurna
						</div>
					</div>
				</div>

				<!-- Content -->
				<div class="space-y-7">
					<div>
						<span
							class="mb-3 inline-flex items-center gap-2 text-sm font-semibold tracking-widest uppercase"
							style="color:#c9a25a"
						>
							<span class="h-px w-8 rounded" style="background:#c9a25a"></span>Tentang Kami
						</span>
						<h2
							class="text-4xl leading-tight font-light lg:text-5xl"
							style="font-family:'Cormorant Garamond',serif;color:#16312a"
						>
							Klinik Kecantikan<br /><em class="font-medium" style="color:#2d6a4f">Berbasis Alam</em
							><br />di Kota Padang
						</h2>
					</div>

					<p class="text-base leading-relaxed" style="color:#3a5a48">
						<strong style="color:#16312a">Naavagreen Natural Skincare</strong> adalah klinik kesehatan
						dan kecantikan terpercaya yang berlokasi di Jl. S. Parman 153 B, Padang Utara. Kami menghadirkan
						perawatan kulit premium berbasis bahan-bahan alami pilihan yang aman dan efektif.
					</p>
					<p class="text-sm leading-relaxed" style="color:#5a7a68">
						Dengan rating Google sempurna 5.0 dari 174 ulasan, kepercayaan pelanggan adalah bukti
						nyata komitmen kami dalam menghadirkan pengalaman perawatan kulit terbaik di Kota
						Padang, Sumatera Barat.
					</p>

					<div class="grid grid-cols-1 gap-3 sm:grid-cols-2">
						{#each values as v}
							<div
								class="flex items-center gap-3 rounded-2xl border px-4 py-3 transition-all duration-200 hover:shadow-md"
								style="border-color:rgba(201,162,90,0.2);background:rgba(201,162,90,0.05)"
							>
								<CheckCircle2 class="h-4 w-4 shrink-0" style="color:#2d6a4f" />
								<span class="text-sm font-medium" style="color:#16312a">{v}</span>
							</div>
						{/each}
					</div>

					<a href="#contact">
						<button
							class="mt-2 flex h-12 items-center gap-2 rounded-full px-8 text-sm font-semibold text-white transition-all hover:scale-105 hover:shadow-lg"
							style="background:var(--brand-gradient)"
						>
							Hubungi Kami <ArrowRight class="h-4 w-4" />
						</button>
					</a>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ SERVICES ═══════ -->
	<section id="services" class="py-24" style="background:var(--ng-green-deep)">
		<!-- Dot overlay -->
		<div
			class="pointer-events-none absolute inset-0"
			style="background-image:radial-gradient(circle,rgba(201,162,90,0.05) 1px,transparent 1px);background-size:28px 28px;"
		></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<!-- Header -->
			<div class="mb-16 text-center">
				<span
					class="mb-3 inline-flex items-center gap-2 text-sm font-semibold tracking-widest uppercase"
					style="color:#c9a25a"
				>
					<span class="h-px w-8" style="background:#c9a25a"></span>Layanan Kami<span
						class="h-px w-8"
						style="background:#c9a25a"
					></span>
				</span>
				<h2
					class="text-4xl font-light text-white lg:text-5xl"
					style="font-family:'Cormorant Garamond',serif"
				>
					Perawatan <em class="font-semibold" style="color:#c9a25a">Natural</em> Terbaik
				</h2>
				<p
					class="mx-auto mt-4 max-w-xl text-sm leading-relaxed"
					style="color:rgba(255,255,255,0.5)"
				>
					Setiap layanan kami dirancang khusus untuk mengoptimalkan kesehatan dan kecantikan kulit
					Anda menggunakan kekuatan bahan-bahan alam terbaik.
				</p>
			</div>

			<!-- Services grid -->
			<div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
				{#each services as svc, i}
					<div
						class="group relative overflow-hidden rounded-3xl border p-7 transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl"
						style="border-color:rgba(201,162,90,0.15);background:rgba(255,255,255,0.04);backdrop-filter:blur(8px)"
					>
						<!-- Gold glow -->
						<div
							class="pointer-events-none absolute -right-8 -bottom-8 h-40 w-40 rounded-full opacity-0 transition-opacity duration-300 group-hover:opacity-20"
							style="background:var(--brand-gradient-gold);filter:blur(40px)"
						></div>
						<!-- Icon -->
						<div
							class="mb-5 flex h-14 w-14 items-center justify-center rounded-2xl border transition-transform duration-300 group-hover:scale-110"
							style="border-color:rgba(201,162,90,0.3);background:rgba(201,162,90,0.1)"
						>
							<svelte:component this={svc.icon} class="h-7 w-7" style="color:#c9a25a" />
						</div>
						<h3
							class="mb-3 text-xl font-medium text-white"
							style="font-family:'Cormorant Garamond',serif"
						>
							{svc.title}
						</h3>
						<p class="text-sm leading-relaxed" style="color:rgba(255,255,255,0.5)">{svc.desc}</p>
						<div
							class="mt-6 flex items-center gap-1 text-xs font-semibold opacity-0 transition-opacity duration-300 group-hover:opacity-100"
							style="color:#c9a25a"
						>
							Pelajari <ArrowRight class="h-3.5 w-3.5" />
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ HOURS ═══════ -->
	<section class="py-20" style="background:var(--ng-cream-warm)">
		<div class="mx-auto max-w-3xl px-4 text-center sm:px-6">
			<span
				class="mb-3 inline-flex items-center gap-2 text-sm font-semibold tracking-widest uppercase"
				style="color:#c9a25a"
			>
				<span class="h-px w-8" style="background:#c9a25a"></span>Jam Operasional<span
					class="h-px w-8"
					style="background:#c9a25a"
				></span>
			</span>
			<h2
				class="mb-10 text-3xl font-light"
				style="font-family:'Cormorant Garamond',serif;color:#16312a"
			>
				Kapan Saja Anda <em class="font-medium">Bisa Mengunjungi</em> Kami
			</h2>

			<div
				class="overflow-hidden rounded-3xl border shadow-xl"
				style="border-color:rgba(201,162,90,0.2);background:#fdf8f0"
			>
				<div
					class="px-6 py-4 text-center text-xs font-bold tracking-widest uppercase"
					style="background:var(--brand-gradient);color:rgba(255,255,255,0.8)"
				>
					Naavagreen Natural Skincare – Jadwal Buka
				</div>
				{#each hours as h, i}
					<div
						class="flex items-center justify-between px-8 py-4 transition-colors hover:bg-amber-50/50"
						class:border-t={i !== 0}
						style="border-color:rgba(201,162,90,0.12)"
					>
						<span class="font-medium" style="color:#16312a">{h.day}</span>
						<div class="flex items-center gap-3">
							<span class="text-sm font-semibold" style="color:#2d6a4f">{h.time}</span>
							<span
								class="rounded-full px-2.5 py-0.5 text-[10px] font-bold uppercase"
								style="background:rgba(45,106,79,0.12);color:#2d6a4f">Buka</span
							>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ REVIEWS ═══════ -->
	<section id="reviews" class="py-24" style="background:#fdf8f0">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mb-16 text-center">
				<span
					class="mb-3 inline-flex items-center gap-2 text-sm font-semibold tracking-widest uppercase"
					style="color:#c9a25a"
				>
					<span class="h-px w-8" style="background:#c9a25a"></span>Ulasan Pelanggan<span
						class="h-px w-8"
						style="background:#c9a25a"
					></span>
				</span>
				<h2
					class="text-4xl font-light lg:text-5xl"
					style="font-family:'Cormorant Garamond',serif;color:#16312a"
				>
					Apa Kata <em class="font-medium" style="color:#2d6a4f">Mereka?</em>
				</h2>
				<!-- Overall rating badge -->
				<div
					class="mt-6 inline-flex items-center gap-3 rounded-2xl border px-7 py-3 shadow-sm"
					style="border-color:rgba(201,162,90,0.25);background:#fff"
				>
					<span
						class="text-4xl font-semibold"
						style="font-family:'Cormorant Garamond',serif;color:#16312a">5.0</span
					>
					<div class="text-left">
						<div class="flex gap-0.5" style="color:#c9a25a">
							{#each Array(5) as _}<Star class="h-4 w-4 fill-current" />{/each}
						</div>
						<div class="mt-0.5 text-xs" style="color:#5a7a68">
							174 ulasan Google · Rating Sempurna
						</div>
					</div>
				</div>
			</div>

			<div class="grid grid-cols-1 gap-6 md:grid-cols-3">
				{#each reviews as rv}
					<div
						class="group flex flex-col rounded-3xl border bg-white p-7 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
						style="border-color:rgba(201,162,90,0.15)"
					>
						<div
							class="mb-3 font-sans text-5xl leading-none select-none"
							style="color:rgba(201,162,90,0.25)"
						>
							"
						</div>
						<p class="mb-6 flex-1 text-sm leading-relaxed" style="color:#3a5a48">{rv.text}</p>
						<div class="mb-4 flex gap-0.5" style="color:#c9a25a">
							{#each Array(rv.stars) as _}<Star class="h-4 w-4 fill-current" />{/each}
						</div>
						<Separator class="mb-4" style="background:rgba(201,162,90,0.15)" />
						<div class="flex items-center gap-3">
							<div
								class="flex h-11 w-11 items-center justify-center rounded-full text-sm font-bold text-white shadow"
								style="background:var(--brand-gradient)"
							>
								{rv.initial}
							</div>
							<div>
								<div class="text-sm font-semibold" style="color:#16312a">{rv.name}</div>
								<div class="mt-0.5 flex items-center gap-1.5 text-xs" style="color:#8aaa98">
									{#if rv.isGuide}
										<span
											class="rounded-full px-1.5 py-0.5 text-[10px] font-bold"
											style="background:rgba(201,162,90,0.1);color:#c9a25a">Local Guide</span
										>
									{/if}
									<span>{rv.count}</span> · <span>{rv.time}</span>
								</div>
							</div>
						</div>
					</div>
				{/each}
			</div>

			<div class="mt-10 text-center">
				<a
					href="https://maps.google.com/?cid=naavagreen+padang"
					target="_blank"
					rel="noopener noreferrer"
				>
					<button
						class="mx-auto flex h-12 items-center gap-2 rounded-full border px-8 text-sm font-semibold transition-all hover:shadow-lg"
						style="border-color:rgba(22,49,42,0.25);color:#16312a;background:#fff"
					>
						Lihat Semua 174 Ulasan <ArrowRight class="h-4 w-4" />
					</button>
				</a>
			</div>
		</div>
	</section>

	<!-- ═══════ CONTACT ═══════ -->
	<section id="contact" class="py-24" style="background:var(--ng-green-deep)">
		<div
			class="pointer-events-none absolute inset-0"
			style="background-image:radial-gradient(circle,rgba(201,162,90,0.04) 1px,transparent 1px);background-size:30px 30px;"
		></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mb-14 text-center">
				<span
					class="mb-3 inline-flex items-center gap-2 text-sm font-semibold tracking-widest uppercase"
					style="color:#c9a25a"
				>
					<span class="h-px w-8" style="background:#c9a25a"></span>Temukan Kami<span
						class="h-px w-8"
						style="background:#c9a25a"
					></span>
				</span>
				<h2
					class="text-4xl font-light text-white lg:text-5xl"
					style="font-family:'Cormorant Garamond',serif"
				>
					Kunjungi <em class="font-medium" style="color:#c9a25a">Naavagreen</em><br />di Padang
				</h2>
			</div>

			<div class="grid grid-cols-1 gap-8 lg:grid-cols-5">
				<!-- Info -->
				<div class="space-y-4 lg:col-span-2">
					<!-- Address -->
					<div
						class="flex items-start gap-4 rounded-2xl border p-5 transition-all hover:border-amber-400/30"
						style="border-color:rgba(201,162,90,0.15);background:rgba(255,255,255,0.04)"
					>
						<div
							class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl"
							style="background:var(--brand-gradient-gold)"
						>
							<MapPin class="h-5 w-5 text-white" />
						</div>
						<div>
							<div class="mb-1 text-xs font-bold tracking-wider uppercase" style="color:#c9a25a">
								Alamat
							</div>
							<p class="text-sm leading-relaxed text-white/70">
								Jl. S. Parman 153 B, South Ulak Karang,<br />
								Padang Utara, Padang City,<br />
								West Sumatra 25133
							</p>
						</div>
					</div>

					<!-- Phone -->
					<a
						href="tel:+6281128002556"
						class="flex items-center gap-4 rounded-2xl border p-5 transition-all hover:border-emerald-400/30"
						style="border-color:rgba(201,162,90,0.15);background:rgba(255,255,255,0.04)"
					>
						<div
							class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl"
							style="background:#2d6a4f"
						>
							<Phone class="h-5 w-5 text-white" />
						</div>
						<div>
							<div class="mb-1 text-xs font-bold tracking-wider uppercase" style="color:#c9a25a">
								Telepon / WhatsApp
							</div>
							<div class="text-base font-semibold text-white">0811-2800-2556</div>
						</div>
					</a>

					<!-- Hours summary -->
					<div
						class="flex items-start gap-4 rounded-2xl border p-5"
						style="border-color:rgba(201,162,90,0.15);background:rgba(255,255,255,0.04)"
					>
						<div
							class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl"
							style="background:#1f4a3a"
						>
							<Clock class="h-5 w-5 text-white" />
						</div>
						<div class="w-full">
							<div class="mb-2 text-xs font-bold tracking-wider uppercase" style="color:#c9a25a">
								Jam Buka
							</div>
							<div class="space-y-1 text-sm">
								<div class="flex justify-between">
									<span class="text-white/60">Senin – Sabtu</span><span
										class="font-semibold text-white">09.00 – 20.00</span
									>
								</div>
								<div class="flex justify-between">
									<span class="text-white/60">Minggu</span><span class="font-semibold text-white"
										>09.00 – 17.00</span
									>
								</div>
							</div>
						</div>
					</div>

					<!-- Social -->
					<div class="flex items-center gap-3 pt-1">
						<span class="text-xs font-semibold text-white/40">Ikuti Kami:</span>
						<a
							href="https://instagram.com/naavagreen"
							target="_blank"
							rel="noopener noreferrer"
							class="flex h-9 w-9 items-center justify-center rounded-xl border transition-all hover:scale-110"
							style="border-color:rgba(201,162,90,0.2);background:rgba(255,255,255,0.05);color:#c9a25a"
						>
							<Instagram class="h-4 w-4" />
						</a>
						<a
							href="https://wa.me/6281128002556"
							target="_blank"
							rel="noopener noreferrer"
							class="flex h-9 w-9 items-center justify-center rounded-xl border transition-all hover:scale-110"
							style="border-color:rgba(45,106,79,0.3);background:rgba(45,106,79,0.15);color:#4ade80"
						>
							<MessageCircle class="h-4 w-4" />
						</a>
					</div>
				</div>

				<!-- Map -->
				<div class="lg:col-span-3">
					<div
						class="relative h-full min-h-[420px] overflow-hidden rounded-3xl border shadow-2xl"
						style="border-color:rgba(201,162,90,0.2)"
					>
						<iframe
							title="Lokasi Naavagreen Natural Skincare di Google Maps"
							src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3989.2!2d100.3531!3d-0.9125!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sJl.+S.+Parman+153+B%2C+South+Ulak+Karang%2C+Padang+Utara!5e0!3m2!1sid!2sid!4v1700000000000!5m2!1sid!2sid"
							class="absolute inset-0 h-full w-full"
							style="border:0;filter:saturate(1.1) hue-rotate(-10deg)"
							allowfullscreen
							loading="lazy"
							referrerpolicy="no-referrer-when-downgrade"
						>
						</iframe>
						<div class="absolute inset-x-0 bottom-0 p-4">
							<a
								href="https://maps.google.com/?q=Jl.+S.+Parman+153+B+Padang+Utara+Padang"
								target="_blank"
								rel="noopener noreferrer"
							>
								<button
									class="flex h-11 w-full items-center justify-center gap-2 rounded-2xl text-sm font-semibold text-[#16312a] shadow-xl"
									style="background:var(--brand-gradient-gold)"
								>
									<MapPin class="h-4 w-4" /> Buka di Google Maps
								</button>
							</a>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ CTA BANNER ═══════ -->
	<section class="relative overflow-hidden py-20" style="background:var(--ng-cream-warm)">
		<div
			class="pointer-events-none absolute -top-24 -right-24 h-64 w-64 rounded-full opacity-30"
			style="background:radial-gradient(circle, #c9a25a 0%, transparent 70%);filter:blur(60px)"
		></div>
		<div class="relative mx-auto max-w-3xl space-y-7 px-4 text-center sm:px-6">
			<span class="text-xs font-bold tracking-widest uppercase" style="color:#c9a25a"
				>✦ Jadwalkan Kunjungan Anda ✦</span
			>
			<h2
				class="text-4xl leading-tight font-light lg:text-5xl"
				style="font-family:'Cormorant Garamond',serif;color:#16312a"
			>
				Mulai Perjalanan<br /><em class="font-semibold" style="color:#2d6a4f">Kulit Sehat</em> Anda Hari
				Ini
			</h2>
			<p class="mx-auto max-w-lg text-sm leading-relaxed" style="color:#5a7a68">
				Hubungi Naavagreen Natural Skincare Padang sekarang untuk konsultasi gratis. Tim ahli kami
				siap menemukan solusi perawatan terbaik sesuai kebutuhan kulit Anda.
			</p>
			<div class="flex flex-wrap justify-center gap-4">
				<a
					href="https://wa.me/6281128002556?text=Halo%20Naavagreen%2C%20saya%20ingin%20konsultasi%20perawatan%20kulit"
					target="_blank"
					rel="noopener noreferrer"
				>
					<button
						class="flex h-14 items-center gap-2 rounded-full px-10 text-sm font-semibold text-[#16312a] shadow-xl transition-all hover:scale-105"
						style="background:var(--brand-gradient-gold);box-shadow:var(--brand-shadow-gold)"
					>
						<MessageCircle class="h-5 w-5" /> Chat via WhatsApp
					</button>
				</a>
				<a href="tel:+6281128002556">
					<button
						class="flex h-14 items-center gap-2 rounded-full border px-10 text-sm font-semibold transition-all hover:shadow-md"
						style="border-color:rgba(22,49,42,0.3);color:#16312a"
					>
						<Phone class="h-5 w-5" /> Telepon Sekarang
					</button>
				</a>
			</div>
		</div>
	</section>

	<!-- ═══════ FOOTER ═══════ -->
	<footer class="pt-16 pb-8" style="background:var(--ng-green-deep);color:rgba(255,255,255,0.5)">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mb-12 grid grid-cols-1 gap-10 md:grid-cols-2 lg:grid-cols-4">
				<!-- Brand -->
				<div class="space-y-5 lg:col-span-2">
					<div class="flex items-center gap-3">
						<div
							class="flex h-10 w-10 items-center justify-center rounded-full"
							style="background:var(--brand-gradient-gold)"
						>
							<Leaf class="h-5 w-5 text-white" />
						</div>
						<div>
							<div
								class="font-semibold text-white"
								style="font-family:'Cormorant Garamond',serif;letter-spacing:0.08em"
							>
								NAAVAGREEN
							</div>
							<div class="text-[10px] tracking-widest uppercase" style="color:#c9a25a">
								Natural Skincare · Padang
							</div>
						</div>
					</div>
					<p class="max-w-xs text-sm leading-relaxed">
						Klinik kecantikan alami terpercaya di Kota Padang dengan rating Google 5.0 dari 174
						pelanggan setia.
					</p>
					<div class="flex gap-3">
						<a
							href="https://instagram.com/naavagreen"
							target="_blank"
							rel="noopener noreferrer"
							class="flex h-9 w-9 items-center justify-center rounded-lg transition-all duration-200 hover:scale-110"
							style="background:rgba(255,255,255,0.07);color:rgba(255,255,255,0.5)"
						>
							<Instagram class="h-4 w-4" />
						</a>
						<a
							href="https://wa.me/6281128002556"
							target="_blank"
							rel="noopener noreferrer"
							class="flex h-9 w-9 items-center justify-center rounded-lg transition-all duration-200 hover:scale-110"
							style="background:rgba(255,255,255,0.07);color:rgba(255,255,255,0.5)"
						>
							<MessageCircle class="h-4 w-4" />
						</a>
					</div>
				</div>

				<!-- Nav -->
				<div>
					<h4 class="mb-4 text-xs font-bold tracking-widest text-white uppercase">Navigasi</h4>
					<ul class="space-y-2.5 text-sm">
						{#each navLinks as link}
							<li>
								<a href={link.href} class="transition-colors hover:text-white">{link.label}</a>
							</li>
						{/each}
					</ul>
				</div>

				<!-- Contact -->
				<div>
					<h4 class="mb-4 text-xs font-bold tracking-widest text-white uppercase">Kontak</h4>
					<div class="space-y-3 text-sm">
						<div class="flex items-start gap-2">
							<MapPin class="mt-0.5 h-4 w-4 shrink-0" style="color:#c9a25a" />
							<span>Jl. S. Parman 153 B, Padang Utara, Padang 25133</span>
						</div>
						<div class="flex items-center gap-2">
							<Phone class="h-4 w-4 shrink-0" style="color:#c9a25a" />
							<a href="tel:+6281128002556" class="transition-colors hover:text-white"
								>0811-2800-2556</a
							>
						</div>
						<div class="flex items-center gap-2">
							<Instagram class="h-4 w-4 shrink-0" style="color:#c9a25a" />
							<a
								href="https://instagram.com/naavagreen"
								target="_blank"
								rel="noopener noreferrer"
								class="transition-colors hover:text-white">instagram.com/naavagreen</a
							>
						</div>
						<div class="flex items-start gap-2">
							<Clock class="mt-0.5 h-4 w-4 shrink-0" style="color:#c9a25a" />
							<span>Buka setiap hari mulai 09.00</span>
						</div>
					</div>
				</div>
			</div>

			<Separator style="background:rgba(255,255,255,0.08);margin-bottom:2rem" />

			<div class="flex flex-col items-center justify-between gap-4 text-xs sm:flex-row">
				<span>© 2025 Naavagreen Natural Skincare Padang. Hak cipta dilindungi.</span>
				<span style="color:rgba(255,255,255,0.25)"
					>38PX+7V Ulak Karang Sel., Kota Padang, Sumatera Barat</span
				>
			</div>
		</div>
	</footer>
</main>
