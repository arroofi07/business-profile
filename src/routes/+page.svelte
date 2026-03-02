<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { Badge } from '$lib/components/ui/badge';
	import { Separator } from '$lib/components/ui/separator';
	import { Avatar, AvatarFallback } from '$lib/components/ui/avatar';

	import {
		Star,
		Navigation,
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
		Users,
		Award,
		Instagram,
		Facebook,
		MessageCircle,
		CheckCircle2,
		ArrowRight
	} from 'lucide-svelte';

	let menuOpen = $state(false);

	const navLinks = [
		{ href: '#home', label: 'Beranda' },
		{ href: '#about', label: 'Tentang' },
		{ href: '#services', label: 'Layanan' },
		{ href: '#why-us', label: 'Mengapa Kami' },
		{ href: '#reviews', label: 'Ulasan' },
		{ href: '#contact', label: 'Kontak' }
	];

	const services = [
		{
			icon: Sparkles,
			title: 'Perawatan Wajah',
			desc: 'Facial treatment premium menggunakan bahan-bahan alami pilihan untuk kulit yang lebih cerah, sehat, dan glowing.',
			color: 'blue',
			bg: 'bg-blue-50',
			iconBg: 'bg-blue-100',
			iconColor: 'text-blue-600'
		},
		{
			icon: Shield,
			title: 'Perawatan Tubuh',
			desc: 'Rangkaian treatment tubuh holistik yang membantu relaksasi mendalam, meremajakan kulit, dan meningkatkan vitalitas.',
			color: 'pink',
			bg: 'bg-pink-50',
			iconBg: 'bg-pink-100',
			iconColor: 'text-pink-500'
		},
		{
			icon: Leaf,
			title: 'Perawatan Alami',
			desc: 'Menggunakan bahan-bahan herbal dan organik pilihan yang aman, gentle, dan terbukti efektif secara ilmiah.',
			color: 'teal',
			bg: 'bg-teal-50',
			iconBg: 'bg-teal-100',
			iconColor: 'text-teal-500'
		},
		{
			icon: Heart,
			title: 'Konsultasi Kulit',
			desc: 'Konsultasi mendalam bersama tenaga ahli berpengalaman untuk solusi terbaik sesuai jenis dan kondisi kulit Anda.',
			color: 'violet',
			bg: 'bg-violet-50',
			iconBg: 'bg-violet-100',
			iconColor: 'text-violet-500'
		},
		{
			icon: Zap,
			title: 'Treatment Ekspress',
			desc: 'Perawatan cepat namun efektif untuk Anda yang memiliki keterbatasan waktu. Hasil maksimal dalam waktu singkat.',
			color: 'amber',
			bg: 'bg-amber-50',
			iconBg: 'bg-amber-100',
			iconColor: 'text-amber-500'
		},
		{
			icon: Award,
			title: 'Paket Premium',
			desc: 'Nikmati serangkaian treatment lengkap dalam satu paket eksklusif yang dirancang untuk hasil perawatan optimal.',
			color: 'indigo',
			bg: 'bg-indigo-50',
			iconBg: 'bg-indigo-100',
			iconColor: 'text-indigo-500'
		}
	];

	const whyUs = [
		{
			stat: '8+',
			label: 'Tahun Pengalaman',
			desc: 'Sudah lebih dari 8 tahun melayani kepercayaan pelanggan setia kami'
		},
		{
			stat: '500+',
			label: 'Pelanggan Puas',
			desc: 'Ribuan pelanggan telah merasakan manfaat nyata dari perawatan kami'
		},
		{
			stat: '4.8',
			label: 'Rating Google',
			desc: 'Penilaian bintang lima dari pelanggan yang puas dengan layanan kami'
		},
		{
			stat: '100%',
			label: 'Bahan Alami',
			desc: 'Semua produk menggunakan bahan pilihan yang aman dan telah teruji klinis'
		}
	];

	const reviews = [
		{
			name: 'Indah Yosefa',
			initial: 'IY',
			count: '2 ulasan',
			time: '5 bulan lalu',
			stars: 5,
			text: 'Perawatan wajah terbaik dan alami 🥰🥰🥰🥰 Kulit saya terasa jauh lebih lembut dan cerah setelah rutin treatment di sini. Karyawannya ramah dan tempatnya bersih. Sangat direkomendasikan!',
			gradient: 'from-blue-100 to-indigo-100',
			textColor: 'text-blue-700'
		},
		{
			name: 'SYUHAIBI',
			initial: 'SY',
			count: '1 ulasan',
			time: '8 tahun lalu',
			stars: 5,
			text: 'Karena banyak yg datang untuk perawatan tubuh serta lokasinya aman dan dekat rumah saya. Pelayanan memuaskan dan hasilnya benar-benar terasa. Sudah jadi pelanggan setia dari dulu!',
			gradient: 'from-teal-100 to-emerald-100',
			textColor: 'text-teal-700'
		},
		{
			name: 'Dicky NPS',
			initial: 'DN',
			count: '1 ulasan · 44 foto',
			time: '5 tahun lalu',
			stars: 5,
			text: 'Layanan nya Ok ✅ Tempatnya nyaman, produknya berkualitas, dan hasilnya memuaskan. Cocok untuk yang ingin perawatan premium dengan harga yang terjangkau di Kota Padang.',
			isGuide: true,
			gradient: 'from-violet-100 to-purple-100',
			textColor: 'text-violet-700'
		}
	];

	const teamValues = [
		'Menggunakan produk alami & aman',
		'Tenaga ahli berpengalaman',
		'Konsultasi personal setiap sesi',
		'Lingkungan bersih & steril',
		'Harga terjangkau & transparan',
		'Jadwal fleksibel & mudah diakses'
	];
</script>

<svelte:head>
	<title>Aa Skin Care – Klinik Perawatan Kulit Terbaik di Padang</title>
	<meta
		name="description"
		content="Aa Skin Care adalah klinik kesehatan dan perawatan kulit profesional di Padang, Sumatera Barat. Perawatan wajah & tubuh alami dengan tenaga ahli berpengalaman."
	/>
</svelte:head>

<!-- ═══════════════════════════════════ NAVBAR ═══════════════════════════════════ -->
<header class="fixed inset-x-0 top-0 z-50 transition-all duration-300">
	<nav class="glass border-b border-white/30 shadow-sm">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-18 items-center justify-between py-3">
				<!-- Logo -->
				<a href="#home" class="group flex items-center gap-3">
					<div
						class="flex h-10 w-10 items-center justify-center rounded-xl text-lg font-black text-white shadow-lg transition-transform group-hover:scale-110"
						style="background: var(--brand-gradient)"
					>
						A
					</div>
					<div class="leading-tight">
						<div class="text-base font-extrabold tracking-tight text-slate-900">Aa Skin Care</div>
						<div class="text-[10px] font-semibold tracking-widest text-slate-400 uppercase">
							Klinik Kesehatan
						</div>
					</div>
				</a>

				<!-- Desktop Nav -->
				<div class="hidden items-center gap-1 md:flex">
					{#each navLinks as link}
						<a
							href={link.href}
							class="rounded-lg px-4 py-2 text-sm font-semibold text-slate-600 transition-all duration-200 hover:bg-blue-50 hover:text-blue-600"
						>
							{link.label}
						</a>
					{/each}
				</div>

				<!-- CTA -->
				<div class="hidden items-center gap-3 md:flex">
					<a href="tel:+6281363336257">
						<Button
							class="h-10 rounded-full border-0 px-5 font-bold text-white shadow-lg"
							style="background: var(--brand-gradient)"
						>
							<Phone class="mr-2 h-4 w-4" />
							Hubungi Kami
						</Button>
					</a>
				</div>

				<!-- Mobile Menu Toggle -->
				<button
					onclick={() => (menuOpen = !menuOpen)}
					class="rounded-xl p-2 text-slate-700 transition-colors hover:bg-slate-100 md:hidden"
					aria-label="Toggle menu"
				>
					{#if menuOpen}
						<X class="h-6 w-6" />
					{:else}
						<Menu class="h-6 w-6" />
					{/if}
				</button>
			</div>
		</div>

		<!-- Mobile Nav Dropdown -->
		{#if menuOpen}
			<div
				class="animate-fade-up border-t border-white/30 bg-white/95 px-4 pt-2 pb-4 backdrop-blur-xl md:hidden"
			>
				{#each navLinks as link}
					<a
						href={link.href}
						onclick={() => (menuOpen = false)}
						class="flex items-center gap-2 rounded-xl px-3 py-3 text-sm font-semibold text-slate-700 transition-all hover:bg-blue-50 hover:text-blue-600"
					>
						<ChevronRight class="h-4 w-4" />
						{link.label}
					</a>
				{/each}
				<div class="mt-3 border-t border-slate-100 pt-3">
					<a href="tel:+6281363336257" class="block">
						<Button
							class="h-11 w-full rounded-full border-0 font-bold text-white"
							style="background: var(--brand-gradient)"
						>
							<Phone class="mr-2 h-4 w-4" /> Hubungi Kami
						</Button>
					</a>
				</div>
			</div>
		{/if}
	</nav>
</header>

<main class="pt-[72px]">
	<!-- ═══════════════════════════════════ HERO ═══════════════════════════════════ -->
	<section id="home" class="relative flex min-h-screen items-center overflow-hidden bg-white">
		<!-- Background blobs -->
		<div class="hero-blob pointer-events-none absolute -top-20 -left-20 h-[500px] w-[500px]"></div>
		<div
			class="hero-blob pointer-events-none absolute -right-20 -bottom-20 h-[400px] w-[400px]"
			style="opacity:0.12"
		></div>
		<!-- Dot grid pattern -->
		<div
			class="pointer-events-none absolute inset-0"
			style="background-image:radial-gradient(circle,#2563eb1a 1px,transparent 1px);background-size:30px 30px;"
		></div>

		<div
			class="relative mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-4 py-20 sm:px-6 lg:grid-cols-2 lg:gap-20 lg:px-8"
		>
			<!-- Left: Text content -->
			<div class="space-y-8">
				<div
					class="glass animate-fade-up inline-flex items-center gap-2 rounded-full px-4 py-2 text-sm font-semibold shadow-sm"
				>
					<span class="h-2 w-2 animate-pulse rounded-full bg-emerald-400"></span>
					<span class="text-slate-600">⭐ Rating 4.8 · Terpercaya di Padang</span>
				</div>

				<div class="animate-fade-up delay-100">
					<h1
						class="text-5xl leading-[1.05] font-extrabold tracking-tight text-slate-900 sm:text-6xl lg:text-7xl"
					>
						Cantik Alami,<br />
						<span class="gradient-text">Kulit Sehat</span><br />
						Bersama Kami
					</h1>
				</div>

				<p class="animate-fade-up max-w-lg text-lg leading-relaxed text-slate-500 delay-200">
					Aa Skin Care hadir sebagai klinik kesehatan kulit terpercaya di Kota Padang. Perawatan
					wajah & tubuh menggunakan bahan alami pilihan oleh tenaga ahli profesional.
				</p>

				<div class="animate-fade-up flex flex-wrap gap-4 delay-300">
					<a href="#services">
						<Button
							class="h-13 rounded-full border-0 px-8 text-base font-bold text-white shadow-xl transition-transform hover:scale-105 hover:shadow-2xl"
							style="background: var(--brand-gradient); box-shadow: var(--brand-shadow)"
						>
							Lihat Layanan Kami
							<ArrowRight class="ml-2 h-5 w-5" />
						</Button>
					</a>
					<a href="#contact">
						<Button
							variant="outline"
							class="h-13 rounded-full border-2 border-blue-200 px-8 text-base font-bold text-blue-600 transition-all hover:border-blue-300 hover:bg-blue-50"
						>
							Buat Janji
						</Button>
					</a>
				</div>

				<!-- Trust badges -->
				<div class="animate-fade-up flex flex-wrap gap-6 pt-4 delay-400">
					<div class="flex items-center gap-2 text-sm text-slate-500">
						<div
							class="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-emerald-100"
						>
							<CheckCircle2 class="h-4 w-4 text-emerald-600" />
						</div>
						<span class="font-semibold">Bahan 100% Alami</span>
					</div>
					<div class="flex items-center gap-2 text-sm text-slate-500">
						<div
							class="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-blue-100"
						>
							<Users class="h-4 w-4 text-blue-600" />
						</div>
						<span class="font-semibold">500+ Pelanggan Puas</span>
					</div>
					<div class="flex items-center gap-2 text-sm text-slate-500">
						<div
							class="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-amber-100"
						>
							<Award class="h-4 w-4 text-amber-600" />
						</div>
						<span class="font-semibold">8+ Tahun Pengalaman</span>
					</div>
				</div>
			</div>

			<!-- Right: Floating visual card -->
			<div
				class="animate-scale-in relative flex items-center justify-center delay-200 lg:justify-end"
			>
				<div class="relative w-full max-w-md">
					<!-- Main image card -->
					<div
						class="aspect-[4/5] overflow-hidden rounded-3xl shadow-2xl"
						style="box-shadow: var(--brand-shadow)"
					>
						<img
							src="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?q=80&w=800&auto=format&fit=crop"
							alt="Professional skin care treatment"
							class="h-full w-full scale-105 object-cover transition-transform duration-700 hover:scale-100"
						/>
						<div
							class="absolute inset-0 bg-gradient-to-t from-black/30 via-transparent to-transparent"
						></div>
					</div>

					<!-- Floating rating badge -->
					<div class="glass animate-float absolute -bottom-5 -left-5 rounded-2xl p-4 shadow-xl">
						<div class="flex items-center gap-3">
							<div class="flex gap-0.5 text-amber-400">
								{#each Array(5) as _}
									<Star class="h-4 w-4 fill-current" />
								{/each}
							</div>
							<div>
								<div class="text-sm font-extrabold text-slate-800">4.8 / 5.0</div>
								<div class="text-xs text-slate-500">34 Ulasan Google</div>
							</div>
						</div>
					</div>

					<!-- Floating clients badge -->
					<div
						class="glass animate-float absolute -top-5 -right-5 rounded-2xl p-4 shadow-xl"
						style="animation-delay: 1s"
					>
						<div class="flex items-center gap-3">
							<div
								class="flex h-10 w-10 items-center justify-center rounded-xl"
								style="background: var(--brand-gradient)"
							>
								<Users class="h-5 w-5 text-white" />
							</div>
							<div>
								<div class="text-sm font-extrabold text-slate-800">500+</div>
								<div class="text-xs text-slate-500">Pelanggan Puas</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Bottom wave -->
		<div class="pointer-events-none absolute inset-x-0 bottom-0">
			<svg
				viewBox="0 0 1440 80"
				fill="none"
				xmlns="http://www.w3.org/2000/svg"
				preserveAspectRatio="none"
				class="h-16 w-full text-slate-50"
			>
				<path
					d="M0 80L1440 80L1440 40C1200 80 960 0 720 20C480 40 240 80 0 40L0 80Z"
					fill="currentColor"
				/>
			</svg>
		</div>
	</section>

	<!-- ═══════════════════════════════════ ABOUT ═══════════════════════════════════ -->
	<section id="about" class="bg-slate-50 py-24">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-1 items-center gap-16 lg:grid-cols-2">
				<!-- Left: Images collage -->
				<div class="relative grid grid-cols-2 gap-4">
					<div class="space-y-4">
						<div
							class="aspect-[3/4] overflow-hidden rounded-2xl shadow-lg transition-shadow hover:shadow-xl"
						>
							<img
								src="https://images.unsplash.com/photo-1596755389378-c31d21fd1273?q=80&w=600&auto=format&fit=crop"
								alt="Skincare consultation"
								class="h-full w-full object-cover transition-transform duration-500 hover:scale-105"
							/>
						</div>
					</div>
					<div class="mt-8 space-y-4">
						<div
							class="aspect-square overflow-hidden rounded-2xl shadow-lg transition-shadow hover:shadow-xl"
						>
							<img
								src="https://images.unsplash.com/photo-1515377905703-c4788e51af15?q=80&w=600&auto=format&fit=crop"
								alt="Beauty treatment products"
								class="h-full w-full object-cover transition-transform duration-500 hover:scale-105"
							/>
						</div>
						<div
							class="aspect-square overflow-hidden rounded-2xl shadow-lg transition-shadow hover:shadow-xl"
						>
							<img
								src="https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?q=80&w=600&auto=format&fit=crop"
								alt="Clinic interior"
								class="h-full w-full object-cover transition-transform duration-500 hover:scale-105"
							/>
						</div>
					</div>

					<!-- Experience badge -->
					<div
						class="glass absolute bottom-4 left-1/2 min-w-[160px] -translate-x-1/2 rounded-2xl px-6 py-4 text-center shadow-xl"
					>
						<div class="gradient-text text-3xl font-black">8+</div>
						<div class="mt-0.5 text-xs font-bold tracking-wider text-slate-600 uppercase">
							Tahun Pengalaman
						</div>
					</div>
				</div>

				<!-- Right: Content -->
				<div class="space-y-7">
					<div>
						<span
							class="mb-3 inline-flex items-center gap-2 text-sm font-bold tracking-widest text-rose-500 uppercase"
						>
							<span class="h-0.5 w-8 rounded bg-rose-400"></span>
							Tentang Kami
						</span>
						<h2 class="text-4xl leading-tight font-extrabold text-slate-900 lg:text-5xl">
							Klinik Perawatan Kulit<br />
							<span class="gradient-text">Terpercaya di Padang</span>
						</h2>
					</div>

					<p class="text-lg leading-relaxed text-slate-500">
						<strong class="text-slate-700">Aa Skin Care</strong> adalah klinik kesehatan dan kecantikan
						yang telah berdiri selama lebih dari 8 tahun di Kota Padang, Sumatera Barat. Kami berkomitmen
						menghadirkan layanan perawatan kulit terbaik dengan pendekatan alami dan holistik.
					</p>
					<p class="leading-relaxed text-slate-500">
						Dengan tim tenaga ahli yang berpengalaman dan berdedikasi, kami selalu mengutamakan
						hasil yang optimal dan keamanan setiap klien kami menggunakan produk-produk pilihan
						berkualitas tinggi.
					</p>

					<div class="grid grid-cols-1 gap-3 sm:grid-cols-2">
						{#each teamValues as val}
							<div
								class="flex items-center gap-3 rounded-xl border border-slate-100 bg-white px-4 py-3 shadow-sm transition-all duration-200 hover:border-blue-200 hover:shadow"
							>
								<CheckCircle2 class="h-4 w-4 shrink-0 text-blue-600" />
								<span class="text-sm font-semibold text-slate-700">{val}</span>
							</div>
						{/each}
					</div>

					<a href="#contact">
						<Button
							class="mt-2 h-12 rounded-full border-0 px-8 text-base font-bold text-white transition-transform hover:scale-105"
							style="background: var(--brand-gradient)"
						>
							Pelajari Lebih Lanjut <ArrowRight class="ml-2 h-4 w-4" />
						</Button>
					</a>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════════════════════════════════ SERVICES ═══════════════════════════════════ -->
	<section id="services" class="bg-white py-24">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<!-- Header -->
			<div class="mb-16 space-y-4 text-center">
				<span
					class="inline-flex items-center gap-2 text-sm font-bold tracking-widest text-blue-600 uppercase"
				>
					<span class="h-0.5 w-8 rounded bg-blue-400"></span>
					Layanan Kami
					<span class="h-0.5 w-8 rounded bg-blue-400"></span>
				</span>
				<h2 class="text-4xl font-extrabold text-slate-900 lg:text-5xl">
					Perawatan <span class="gradient-text">Terbaik</span> Untuk Anda
				</h2>
				<p class="mx-auto max-w-2xl text-lg text-slate-500">
					Kami menawarkan berbagai layanan perawatan kulit premium yang disesuaikan dengan kebutuhan
					unik setiap pelanggan.
				</p>
			</div>

			<!-- Services Grid -->
			<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
				{#each services as svc, i}
					<div
						class="group relative {svc.bg} overflow-hidden rounded-3xl border border-white p-7 shadow-sm transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl"
					>
						<!-- bg decoration -->
						<div
							class="absolute -right-6 -bottom-6 h-32 w-32 rounded-full opacity-30 blur-2xl {svc.iconBg}"
						></div>

						<div
							class="{svc.iconBg} mb-5 flex h-14 w-14 items-center justify-center rounded-2xl shadow-sm transition-transform duration-300 group-hover:scale-110"
						>
							<svelte:component this={svc.icon} class="h-7 w-7 {svc.iconColor}" />
						</div>
						<h3 class="mb-3 text-xl font-extrabold text-slate-900">{svc.title}</h3>
						<p class="text-sm leading-relaxed text-slate-500">{svc.desc}</p>

						<div
							class="mt-6 flex items-center gap-2 text-sm font-bold {svc.iconColor} opacity-0 transition-opacity duration-300 group-hover:opacity-100"
						>
							Selengkapnya <ArrowRight class="h-4 w-4" />
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════════════════════════════════ WHY US / STATS ═══════════════════════════════════ -->
	<section
		id="why-us"
		class="relative overflow-hidden py-24"
		style="background: var(--brand-gradient)"
	>
		<!-- Pattern overlay -->
		<div
			class="pointer-events-none absolute inset-0"
			style="background-image:radial-gradient(circle,rgba(255,255,255,0.08) 1px,transparent 1px);background-size:24px 24px;"
		></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<!-- Header -->
			<div class="mb-16 space-y-4 text-center">
				<span
					class="inline-flex items-center gap-2 text-sm font-bold tracking-widest text-white/70 uppercase"
				>
					<span class="h-0.5 w-8 rounded bg-white/50"></span>
					Pencapaian Kami
					<span class="h-0.5 w-8 rounded bg-white/50"></span>
				</span>
				<h2 class="text-4xl leading-tight font-extrabold text-white lg:text-5xl">
					Mengapa Memilih<br />Aa Skin Care?
				</h2>
				<p class="mx-auto max-w-xl text-lg text-white/70">
					Dipercaya oleh ratusan pelanggan di Kota Padang karena kualitas dan konsistensi layanan
					kami.
				</p>
			</div>

			<!-- Stats Grid -->
			<div class="mb-16 grid grid-cols-2 gap-6 lg:grid-cols-4">
				{#each whyUs as item}
					<div
						class="glass rounded-3xl border border-white/40 p-7 text-center shadow-lg transition-all duration-300 hover:-translate-y-1 hover:border-white/60"
					>
						<div class="mb-2 text-5xl font-black text-white">{item.stat}</div>
						<div class="mb-2 text-sm font-extrabold text-white/90">{item.label}</div>
						<p class="text-xs leading-relaxed text-white/65">{item.desc}</p>
					</div>
				{/each}
			</div>

			<!-- Feature highlights row -->
			<div class="grid grid-cols-1 gap-6 md:grid-cols-3">
				{#each [{ icon: Shield, title: 'Aman & Terpercaya', desc: 'Semua produk telah melalui seleksi ketat dan uji keamanan untuk memberikan perawatan terbaik.' }, { icon: Heart, title: 'Penuh Dedikasi', desc: 'Tim kami selalu siap memberikan pelayanan yang hangat, personal, dan profesional.' }, { icon: Sparkles, title: 'Hasil Nyata', desc: 'Formulasi dan metode perawatan kami terbukti efektif menghasilkan kulit sehat dan bercahaya.' }] as feat}
					<div
						class="glass flex items-start gap-5 rounded-2xl border border-white/30 p-6 transition-all duration-200 hover:border-white/50"
					>
						<div
							class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl bg-white/20"
						>
							<svelte:component this={feat.icon} class="h-6 w-6 text-white" />
						</div>
						<div>
							<h3 class="mb-1 text-base font-extrabold text-white">{feat.title}</h3>
							<p class="text-sm leading-relaxed text-white/70">{feat.desc}</p>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════════════════════════════════ REVIEWS ═══════════════════════════════════ -->
	<section id="reviews" class="bg-slate-50 py-24">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<!-- Header -->
			<div class="mb-16 space-y-4 text-center">
				<span
					class="inline-flex items-center gap-2 text-sm font-bold tracking-widest text-blue-600 uppercase"
				>
					<span class="h-0.5 w-8 rounded bg-blue-400"></span>
					Ulasan Pelanggan
					<span class="h-0.5 w-8 rounded bg-blue-400"></span>
				</span>
				<h2 class="text-4xl font-extrabold text-slate-900 lg:text-5xl">Apa Kata Mereka?</h2>
				<!-- Overall rating -->
				<div class="glass inline-flex items-center gap-3 rounded-2xl px-6 py-3 shadow-sm">
					<span class="gradient-text text-4xl font-black">4.8</span>
					<div>
						<div class="flex gap-0.5 text-amber-400">
							{#each Array(5) as _}
								<Star class="h-4 w-4 fill-current" />
							{/each}
						</div>
						<div class="mt-0.5 text-xs font-semibold text-slate-500">
							Berdasarkan 34 ulasan Google
						</div>
					</div>
				</div>
			</div>

			<!-- Review Cards -->
			<div class="grid grid-cols-1 gap-6 md:grid-cols-3">
				{#each reviews as review}
					<div
						class="group flex flex-col rounded-3xl border border-slate-100 bg-white p-7 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-blue-100 hover:shadow-xl"
					>
						<!-- Quote mark -->
						<div class="mb-2 font-serif text-6xl leading-none text-slate-100 select-none">"</div>

						<p class="mb-6 flex-1 text-sm leading-relaxed text-slate-600">{review.text}</p>

						<!-- Stars -->
						<div class="mb-5 flex gap-0.5 text-amber-400">
							{#each Array(review.stars) as _}
								<Star class="h-4 w-4 fill-current" />
							{/each}
						</div>

						<Separator class="mb-5 bg-slate-100" />

						<!-- Reviewer info -->
						<div class="flex items-center gap-4">
							<Avatar class="h-12 w-12 border-2 border-white shadow ring-2 ring-slate-50">
								<AvatarFallback
									class="bg-gradient-to-br {review.gradient} {review.textColor} text-sm font-black"
								>
									{review.initial}
								</AvatarFallback>
							</Avatar>
							<div class="min-w-0 flex-1">
								<div class="truncate text-sm font-extrabold text-slate-900">{review.name}</div>
								<div
									class="mt-0.5 flex flex-wrap items-center gap-1.5 text-xs font-medium text-slate-400"
								>
									{#if review.isGuide}
										<Badge
											class="pointer-events-none h-4 border-0 bg-amber-50 px-1.5 py-0 text-[10px] font-bold text-amber-600"
											>Local Guide</Badge
										>
									{/if}
									<span>{review.count}</span>
									<span>·</span>
									<span>{review.time}</span>
								</div>
							</div>
						</div>
					</div>
				{/each}
			</div>

			<div class="mt-10 text-center">
				<a href="https://maps.google.com" target="_blank" rel="noopener noreferrer">
					<Button
						variant="outline"
						class="h-12 rounded-full border-2 border-blue-200 px-8 font-bold text-blue-600 transition-all hover:border-blue-300 hover:bg-blue-50"
					>
						Lihat Semua Ulasan (34)
						<ArrowRight class="ml-2 h-4 w-4" />
					</Button>
				</a>
			</div>
		</div>
	</section>

	<!-- ═══════════════════════════════════ CONTACT ═══════════════════════════════════ -->
	<section id="contact" class="bg-white py-24">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<!-- Header -->
			<div class="mb-16 space-y-4 text-center">
				<span
					class="inline-flex items-center gap-2 text-sm font-bold tracking-widest text-blue-600 uppercase"
				>
					<span class="h-0.5 w-8 rounded bg-blue-400"></span>
					Hubungi Kami
					<span class="h-0.5 w-8 rounded bg-blue-400"></span>
				</span>
				<h2 class="text-4xl font-extrabold text-slate-900 lg:text-5xl">
					Temukan & Hubungi<br />
					<span class="gradient-text">Aa Skin Care</span>
				</h2>
			</div>

			<div class="grid grid-cols-1 gap-8 lg:grid-cols-5">
				<!-- Contact Info Cards (left 2 cols) -->
				<div class="space-y-4 lg:col-span-2">
					<div
						class="group flex cursor-pointer items-start gap-5 rounded-2xl border border-slate-100 bg-slate-50 p-6 transition-all duration-300 hover:border-blue-200 hover:bg-blue-50/40 hover:shadow-md"
					>
						<div
							class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl"
							style="background: var(--brand-gradient)"
						>
							<MapPin class="h-6 w-6 text-white" />
						</div>
						<div>
							<div class="mb-1 text-sm font-extrabold tracking-wide text-slate-800 uppercase">
								Alamat
							</div>
							<p class="text-sm leading-relaxed text-slate-600">
								Jl. Angkasa Puri No.26, Parupuk Tabing,<br />
								Kec. Koto Tangah, Kota Padang,<br />
								Sumatera Barat 25173
							</p>
						</div>
					</div>

					<a
						href="tel:+6281363336257"
						class="group flex items-center gap-5 rounded-2xl border border-slate-100 bg-slate-50 p-6 transition-all duration-300 hover:border-emerald-200 hover:bg-emerald-50/40 hover:shadow-md"
					>
						<div
							class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl bg-emerald-500 transition-transform group-hover:scale-110"
						>
							<Phone class="h-6 w-6 text-white" />
						</div>
						<div>
							<div class="mb-1 text-sm font-extrabold tracking-wide text-slate-800 uppercase">
								Telepon / WhatsApp
							</div>
							<div
								class="text-lg font-bold text-slate-700 transition-colors group-hover:text-emerald-600"
							>
								0813-6333-6257
							</div>
						</div>
					</a>

					<div
						class="group flex cursor-pointer items-start gap-5 rounded-2xl border border-slate-100 bg-slate-50 p-6 transition-all duration-300 hover:border-amber-200 hover:bg-amber-50/40 hover:shadow-md"
					>
						<div
							class="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl bg-amber-500 transition-transform group-hover:scale-110"
						>
							<Clock class="h-6 w-6 text-white" />
						</div>
						<div>
							<div class="mb-2 text-sm font-extrabold tracking-wide text-slate-800 uppercase">
								Jam Operasional
							</div>
							<div class="space-y-1.5 text-sm text-slate-600">
								<div class="flex justify-between gap-6">
									<span>Senin – Jumat</span>
									<span class="font-bold text-slate-800">10.00 – 20.00</span>
								</div>
								<div class="flex justify-between gap-6">
									<span>Sabtu – Minggu</span>
									<span class="font-bold text-slate-800">10.00 – 18.00</span>
								</div>
							</div>
						</div>
					</div>

					<!-- Social media -->
					<div class="flex items-center gap-3 pt-2">
						<span class="text-sm font-bold text-slate-500">Ikuti Kami:</span>
						<a
							href="https://wa.me/6281363336257"
							target="_blank"
							rel="noopener noreferrer"
							class="flex h-10 w-10 items-center justify-center rounded-xl bg-green-100 text-green-600 shadow-sm transition-all duration-200 hover:scale-110 hover:bg-green-500 hover:text-white"
						>
							<MessageCircle class="h-5 w-5" />
						</a>
						<a
							href="#"
							class="flex h-10 w-10 items-center justify-center rounded-xl bg-pink-100 text-pink-600 shadow-sm transition-all duration-200 hover:scale-110 hover:bg-pink-500 hover:text-white"
						>
							<Instagram class="h-5 w-5" />
						</a>
						<a
							href="#"
							class="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-100 text-blue-600 shadow-sm transition-all duration-200 hover:scale-110 hover:bg-blue-500 hover:text-white"
						>
							<Facebook class="h-5 w-5" />
						</a>
					</div>
				</div>

				<!-- Google Maps embed (right 3 cols) -->
				<div class="lg:col-span-3">
					<div
						class="relative h-full min-h-[420px] overflow-hidden rounded-3xl border-4 border-white shadow-xl"
					>
						<iframe
							title="Lokasi Aa Skin Care di Google Maps"
							src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3989.049!2d100.3544!3d-0.8683!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2fd4b8b4b4b4b4b4%3A0x0!2sJl.+Angkasa+Puri+No.26%2C+Parupuk+Tabing%2C+Kota+Padang!5e0!3m2!1sid!2sid!4v1700000000000!5m2!1sid!2sid"
							class="absolute inset-0 h-full w-full"
							style="border:0;filter:saturate(1.1)"
							allowfullscreen
							loading="lazy"
							referrerpolicy="no-referrer-when-downgrade"
						></iframe>
						<!-- Map overlay CTA -->
						<div class="absolute inset-x-0 bottom-0 p-4">
							<a
								href="https://maps.google.com/?q=Jl.+Angkasa+Puri+No.26+Parupuk+Tabing+Padang"
								target="_blank"
								rel="noopener noreferrer"
							>
								<Button
									class="h-12 w-full rounded-2xl border-0 text-sm font-bold text-white shadow-xl"
									style="background: var(--brand-gradient)"
								>
									<Navigation class="mr-2 h-4 w-4" />
									Dapatkan Rute ke Klinik
								</Button>
							</a>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════════════════════════════════ CTA BANNER ═══════════════════════════════════ -->
	<section class="relative overflow-hidden py-20" style="background: var(--brand-gradient-soft)">
		<div
			class="hero-blob pointer-events-none absolute top-0 left-0 h-96 w-96"
			style="opacity:0.12"
		></div>
		<div class="relative mx-auto max-w-4xl space-y-7 px-4 text-center sm:px-6">
			<h2 class="text-4xl leading-tight font-extrabold text-slate-900 lg:text-5xl">
				Siap Untuk Kulit<br />
				<span class="gradient-text">Lebih Sehat & Cantik?</span>
			</h2>
			<p class="mx-auto max-w-xl text-lg text-slate-500">
				Hubungi kami sekarang untuk jadwal konsultasi gratis. Tim ahli kami siap membantu Anda
				menemukan perawatan yang paling tepat.
			</p>
			<div class="flex flex-wrap justify-center gap-4">
				<a
					href="https://wa.me/6281363336257?text=Halo%20Aa%20Skin%20Care%2C%20saya%20ingin%20membuat%20janji%20perawatan"
					target="_blank"
					rel="noopener noreferrer"
				>
					<Button
						class="h-14 rounded-full border-0 px-10 text-base font-bold text-white shadow-2xl transition-transform hover:scale-105"
						style="background: var(--brand-gradient); box-shadow: var(--brand-shadow)"
					>
						<MessageCircle class="mr-2 h-5 w-5" />
						Chat via WhatsApp
					</Button>
				</a>
				<a href="tel:+6281363336257">
					<Button
						variant="outline"
						class="h-14 rounded-full border-2 border-blue-300 px-10 text-base font-bold text-blue-600 transition-all hover:border-blue-400 hover:bg-blue-50"
					>
						<Phone class="mr-2 h-5 w-5" />
						Telepon Sekarang
					</Button>
				</a>
			</div>
		</div>
	</section>

	<!-- ═══════════════════════════════════ FOOTER ═══════════════════════════════════ -->
	<footer class="bg-slate-900 pt-16 pb-8 text-slate-400">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mb-12 grid grid-cols-1 gap-10 md:grid-cols-2 lg:grid-cols-4">
				<!-- Brand -->
				<div class="space-y-5 lg:col-span-2">
					<div class="flex items-center gap-3">
						<div
							class="flex h-11 w-11 items-center justify-center rounded-xl text-xl font-black text-white shadow-lg"
							style="background: var(--brand-gradient)"
						>
							A
						</div>
						<div>
							<div class="text-lg font-extrabold text-white">Aa Skin Care</div>
							<div class="text-xs tracking-widest text-slate-500 uppercase">Klinik Kesehatan</div>
						</div>
					</div>
					<p class="max-w-xs text-sm leading-relaxed">
						Klinik perawatan kulit terpercaya di Kota Padang dengan pengalaman lebih dari 8 tahun
						melayani pelanggan setia kami.
					</p>
					<div class="flex gap-3">
						<a
							href="https://wa.me/6281363336257"
							target="_blank"
							rel="noopener noreferrer"
							class="flex h-9 w-9 items-center justify-center rounded-lg bg-slate-800 text-slate-400 transition-all duration-200 hover:bg-green-600 hover:text-white"
						>
							<MessageCircle class="h-4 w-4" />
						</a>
						<a
							href="#"
							class="flex h-9 w-9 items-center justify-center rounded-lg bg-slate-800 text-slate-400 transition-all duration-200 hover:bg-pink-600 hover:text-white"
						>
							<Instagram class="h-4 w-4" />
						</a>
						<a
							href="#"
							class="flex h-9 w-9 items-center justify-center rounded-lg bg-slate-800 text-slate-400 transition-all duration-200 hover:bg-blue-700 hover:text-white"
						>
							<Facebook class="h-4 w-4" />
						</a>
					</div>
				</div>

				<!-- Links -->
				<div>
					<h4 class="mb-4 text-sm font-bold tracking-wider text-white uppercase">Navigasi</h4>
					<ul class="space-y-2.5">
						{#each navLinks as link}
							<li>
								<a
									href={link.href}
									class="inline-block text-sm transition-colors duration-200 hover:translate-x-1 hover:text-blue-400"
									>{link.label}</a
								>
							</li>
						{/each}
					</ul>
				</div>

				<!-- Address -->
				<div>
					<h4 class="mb-4 text-sm font-bold tracking-wider text-white uppercase">Kontak</h4>
					<div class="space-y-3 text-sm">
						<div class="flex items-start gap-3">
							<MapPin class="mt-0.5 h-4 w-4 shrink-0 text-blue-400" />
							<span>Jl. Angkasa Puri No.26, Parupuk Tabing, Kota Padang, Sumbar 25173</span>
						</div>
						<div class="flex items-center gap-3">
							<Phone class="h-4 w-4 shrink-0 text-blue-400" />
							<a href="tel:+6281363336257" class="transition-colors hover:text-blue-400"
								>0813-6333-6257</a
							>
						</div>
						<div class="flex items-start gap-3">
							<Clock class="mt-0.5 h-4 w-4 shrink-0 text-blue-400" />
							<span>Buka pukul 10.00</span>
						</div>
					</div>
				</div>
			</div>

			<Separator class="mb-8 bg-slate-800" />

			<div class="flex flex-col items-center justify-between gap-4 text-xs sm:flex-row">
				<span>© 2025 Aa Skin Care. Hak cipta dilindungi.</span>
				<div class="flex items-center gap-1">
					<span>4965+XM Parupuk Tabing, Kota Padang, Sumatera Barat</span>
				</div>
			</div>
		</div>
	</footer>
</main>
