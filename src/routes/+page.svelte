<script lang="ts">
	import { Separator } from '$lib/components/ui/separator';

	// Assets moved to static/assets for local serving
	const heroImg = '/assets/hero.png';
	const pempekImg = '/assets/pempek.png';
	const kerupukImg = '/assets/kerupuk.png';

	import {
		Phone,
		MessageCircle,
		Menu,
		X,
		ArrowRight,
		ShieldCheck,
		CheckCircle2,
		ShoppingBag,
		Award,
		Star,
		Instagram,
		Check,
		Clock,
		Heart,
		Gift,
		Sparkles,
		MapPin,
		Utensils
	} from 'lucide-svelte';

	let menuOpen = $state(false);

	const navLinks = [
		{ href: '#home', label: 'Beranda' },
		{ href: '#about', label: 'Tentang Kami' },
		{ href: '#menu', label: 'Menu Unggulan' },
		{ href: '#order', label: 'Cara Pesan' },
		{ href: '#reviews', label: 'Review' }
	];

	const stats = [
		{ value: '700+', label: 'Instagram Followers' },
		{ value: '62', label: 'Postingan Terkini' },
		{ value: 'MUI', label: 'Halal Certified' },
		{ value: 'Premium', label: 'Authentic Taste' }
	];

	const features = [
		{
			icon: Utensils,
			title: 'Authentic Minang',
			desc: 'Resep warisan turun temurun dengan bumbu rempah pilihan.'
		},
		{
			icon: ShieldCheck,
			title: 'MUI Halal Certified',
			desc: 'Terjamin kehalalan dan kebersihannya untuk semua produk.'
		},
		{
			icon: Award,
			title: 'Kualitas Ekspor',
			desc: 'Olahan Minang yang sudah merambah selera dunia.'
		},
		{
			icon: Gift,
			title: 'Packing Aman',
			desc: 'Packaging eksklusif, aman dikirim ke luar kota maupun luar negeri.'
		}
	];

	const products = [
		{
			category: 'Signature',
			title: 'Aneka Rendang',
			desc: 'Rendang daging sapi pilihan dengan bumbu meresap sempurna, tekstur lembut dan tahan lama.',
			image: heroImg
		},
		{
			category: 'Best Seller',
			title: 'Pempek Cik Unik',
			desc: 'Pempek khas dengan cuko kental pedas-asam-manis yang pas, dibuat dari ikan segar berkualitas.',
			image: pempekImg
		},
		{
			category: 'Camilan Sehat',
			title: 'Kerupuk Tulang Tuna',
			desc: 'Camilan inovatif bergizi tinggi, renyah, gurih, dan bebas pengawet.',
			image: kerupukImg
		}
	];

	const reviews = [
		{
			name: 'Budi Santoso',
			initial: 'BS',
			time: '2 hari lalu',
			stars: 5,
			text: 'Rendangnya juara! Dagingnya empuk banget dan bumbunya bener-bener meresap. Pas banget buat stok di rumah atau oleh-oleh.'
		},
		{
			name: 'Siti Aminah',
			initial: 'SA',
			time: '1 minggu lalu',
			stars: 5,
			text: 'Pempek Cik Unik beneran unik rasanya, ikannya kerasa banget dan cukonya mantap. Gak kalah sama pempek langsung dari Palembang.'
		},
		{
			name: 'Hendra Wijaya',
			initial: 'HW',
			time: '2 minggu lalu',
			stars: 5,
			text: 'Kerupuk tulang tunanya nagih banget buat camilan sehat. Baru kali ini nemu kerupuk dari tulang ikan yang seenak ini. Recommended!'
		}
	];
</script>

<svelte:head>
	<title>Dapur Yonica | Olahan Minang Jadi Selera Dunia ✨</title>
	<meta
		name="description"
		content="Dapur Yonica – Aneka Rendang, Pempek Cik Unik, dan Kerupuk Tulang Tuna. Cita rasa otentik Minang yang merambah dunia. MUI Halal Certified."
	/>
	<link
		href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<!-- ═══════ NAVBAR ═══════ -->
<header class="fixed inset-x-0 top-0 z-50">
	<nav
		class="border-b backdrop-blur-md transition-all"
		style="background:rgba(18,18,18,0.95);border-color:rgba(255,193,7,0.15);box-shadow:0 4px 20px rgba(0,0,0,0.5)"
	>
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-20 items-center justify-between">
				<!-- Logo -->
				<a href="#home" class="group flex items-center gap-3">
					<div
						class="flex h-12 w-12 items-center justify-center rounded-xl bg-linear-to-br from-[#D32F2F] to-[#8c1c1c] shadow-lg transition-transform duration-300 group-hover:scale-110"
					>
						<Utensils class="h-7 w-7 text-[#FFC107]" />
					</div>
					<div class="leading-tight">
						<div
							style="font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:800;color:#fff"
						>
							Dapur<span style="color:#FFC107">.Yonica</span>
						</div>
						<div
							style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.65rem;font-weight:800;letter-spacing:0.2em;text-transform:uppercase;color:#D32F2F"
						>
							Padang, West Sumatra
						</div>
					</div>
				</a>

				<!-- Desktop Nav -->
				<div class="hidden items-center gap-2 md:flex">
					{#each navLinks as link}
						<a
							href={link.href}
							class="group relative rounded-full px-5 py-2 text-[0.9rem] font-bold transition-all duration-200"
							style="font-family:'Plus Jakarta Sans',sans-serif;color:#eee"
						>
							{link.label}
							<span
								class="absolute bottom-1.5 left-1/2 h-0.5 w-0 -translate-x-1/2 rounded-full opacity-80 transition-all duration-300 group-hover:w-5"
								style="background:#FFC107"
							></span>
						</a>
					{/each}
				</div>

				<!-- CTA -->
				<div class="hidden items-center gap-4 md:flex">
					<div
						class="flex items-center gap-2 rounded-full border px-3 py-1.5"
						style="border-color:rgba(255,193,7,0.3);color:#FFC107;font-size:0.75rem;font-weight:800;font-family:'Plus Jakarta Sans',sans-serif"
					>
						<ShieldCheck class="h-4 w-4" /> Halal Certified
					</div>
					<a href="https://wa.me/628123456789" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-11 items-center gap-2 rounded-full px-6 text-[0.95rem] font-bold text-white transition-all hover:-translate-y-1 hover:shadow-xl"
							style="font-family:'Plus Jakarta Sans',sans-serif;background:linear-gradient(135deg,#D32F2F,#8c1c1c);box-shadow:0 6px 20px rgba(211,47,47,0.35);color:#fff"
						>
							<MessageCircle class="h-4.5 w-4.5" /> Order via WA
						</button>
					</a>
				</div>

				<!-- Mobile Toggle -->
				<button
					onclick={() => (menuOpen = !menuOpen)}
					class="rounded-xl p-2 transition hover:bg-white/5 md:hidden"
					style="color:#fff"
					aria-label="Toggle menu"
				>
					{#if menuOpen}<X class="h-7 w-7" />{:else}<Menu class="h-7 w-7" />{/if}
				</button>
			</div>
		</div>

		<!-- Mobile Menu -->
		{#if menuOpen}
			<div
				class="border-t px-4 pt-3 pb-6 md:hidden"
				style="background:#121212;border-color:rgba(255,193,7,0.15)"
			>
				{#each navLinks as link}
					<a
						href={link.href}
						onclick={() => (menuOpen = false)}
						class="flex items-center gap-3 rounded-2xl px-5 py-3.5 text-base font-bold transition hover:bg-white/5"
						style="font-family:'Plus Jakarta Sans',sans-serif;color:#eee"
					>
						{link.label}
					</a>
				{/each}
				<div class="mt-4 border-t pt-5" style="border-color:rgba(211,47,47,0.15)">
					<a href="https://wa.me/628123456789" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-12 w-full items-center justify-center gap-2 rounded-2xl text-base font-bold shadow-lg"
							style="font-family:'Plus Jakarta Sans',sans-serif;background:linear-gradient(135deg,#D32F2F,#8c1c1c);color:#fff"
						>
							<MessageCircle class="h-5 w-5" /> Chat via WhatsApp
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
		class="relative flex min-h-[95vh] items-center overflow-hidden"
		style="background:#121212"
	>
		<!-- Sophisticated background pattern -->
		<div
			class="absolute inset-0 opacity-10"
			style="background-image: radial-gradient(#FFC107 1px, transparent 1px); background-size: 40px 40px;"
		></div>

		<!-- Decorative blobs -->
		<div
			class="pointer-events-none absolute -top-40 -left-40 h-[800px] w-[800px] opacity-20"
			style="background:radial-gradient(circle,#D32F2F 0%,transparent 70%);filter:blur(100px)"
		></div>
		<div
			class="pointer-events-none absolute right-0 bottom-0 h-[600px] w-[600px] opacity-10"
			style="background:radial-gradient(circle,#FFC107 0%,transparent 65%);filter:blur(80px)"
		></div>

		<div
			class="relative mx-auto w-full max-w-7xl px-4 pt-16 pb-20 sm:px-6 lg:grid lg:grid-cols-12 lg:gap-10 lg:px-8 lg:pt-24 lg:pb-32"
		>
			<!-- Left text -->
			<div class="animate-slide-up z-10 flex flex-col justify-center space-y-8 lg:col-span-6">
				<!-- Tag pill -->
				<div
					class="inline-flex items-center gap-2.5 self-start rounded-full border px-4 py-2"
					style="border-color:rgba(255,193,7,0.3);background:rgba(255,255,255,0.05);backdrop-filter:blur(8px)"
				>
					<MapPin class="h-4 w-4 text-[#FFC107]" />
					<span
						style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.75rem;font-weight:800;letter-spacing:0.15em;text-transform:uppercase;color:#eee"
					>
						Authentic Padang, Indonesia
					</span>
				</div>

				<!-- Heading -->
				<div class="animate-slide-up delay-100">
					<h1
						style="font-family:'Playfair Display',serif;font-size:clamp(3.5rem,7vw,6rem);line-height:1;color:#fff"
					>
						Cita Rasa<br />
						<span class="relative inline-block">
							<span class="relative z-10" style="color:#FFC107">Minang</span>
							<span
								class="absolute -bottom-2 left-0 -z-10 h-4 w-full rounded-full opacity-40"
								style="background:#D32F2F"
							></span>
						</span><br />
						<span
							style="font-size:0.5em;color:#D32F2F;letter-spacing:0.1em;text-transform:uppercase;font-weight:900;font-family:'Plus Jakarta Sans'"
							>Selera Dunia 🌏</span
						>
					</h1>
				</div>

				<p
					class="animate-slide-up max-w-lg text-[1.15rem] leading-relaxed delay-200"
					style="font-family:'Plus Jakarta Sans',sans-serif;color:#ccc"
				>
					Menyajikan kelezatan otentik Minang dalam <strong style="color:#FFC107"
						>Aneka Rendang</strong
					>,
					<strong style="color:#FFC107">Pempek Cik Unik</strong>, dan camilan sehat
					<strong style="color:#FFC107">Kerupuk Tulang Tuna</strong>. Dibuat dengan rempah asli &
					cinta.
				</p>

				<!-- CTA -->
				<div class="animate-slide-up flex flex-wrap gap-5 pt-4 delay-300">
					<a href="#menu">
						<button
							class="group flex h-16 items-center gap-3 rounded-xl px-10 text-lg font-bold transition-all hover:scale-105"
							style="font-family:'Plus Jakarta Sans',sans-serif;background:#D32F2F;color:white;box-shadow:0 15px 35px rgba(211,47,47,0.3)"
						>
							<ShoppingBag class="h-6 w-6 transition-transform group-hover:scale-110" /> Jelajahi Menu
						</button>
					</a>
					<a href="#about">
						<button
							class="flex h-16 items-center gap-3 rounded-xl border border-white/20 px-10 text-lg font-bold transition-all hover:border-white/40 hover:bg-white/5"
							style="font-family:'Plus Jakarta Sans',sans-serif;color:#fff"
						>
							Tentang Kami
						</button>
					</a>
				</div>
			</div>

			<!-- Right image -->
			<div class="animate-slide-left relative mt-20 delay-200 lg:col-span-6 lg:mt-0">
				<div class="relative flex justify-center lg:justify-end">
					<!-- Gold Frame -->
					<div
						class="absolute -inset-4 rounded-[2.5rem] border border-[#FFC107]/20 lg:-right-4 lg:left-12"
					></div>

					<!-- Main Image -->
					<div class="relative z-10 w-full max-w-[550px]">
						<div
							class="relative overflow-hidden shadow-[0_40px_80px_-15px_rgba(0,0,0,0.8)]"
							style="border-radius:2rem; border:8px solid #1e1e1e"
						>
							<img
								src={heroImg}
								alt="Dapur Yonica Rendang"
								class="w-full object-cover transition-transform duration-[2s] hover:scale-110"
								style="aspect-ratio:4/5"
							/>
							<!-- Badge Overlay -->
							<div
								class="absolute bottom-6 left-6 rounded-2xl border border-white/10 bg-black/60 p-4 backdrop-blur-md"
							>
								<div class="flex items-center gap-3">
									<div class="flex h-10 w-10 items-center justify-center rounded-full bg-[#FFC107]">
										<Award class="h-6 w-6 text-black" />
									</div>
									<div>
										<div class="text-sm font-bold text-white">Best Minang Product</div>
										<div class="text-xs font-bold tracking-widest text-[#FFC107] uppercase">
											Premium Quality
										</div>
									</div>
								</div>
							</div>
						</div>

						<!-- Floating Decor -->
						<div class="animate-spin-slow absolute -top-10 -right-10 opacity-20">
							<svg width="200" height="200" viewBox="0 0 100 100">
								<path
									d="M50 0 L61 35 L97 35 L68 57 L79 92 L50 70 L21 92 L32 57 L3 35 L39 35 Z"
									fill="#FFC107"
								/>
							</svg>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<style>
		@keyframes float {
			0%,
			100% {
				transform: translateY(0px) rotate(0deg);
			}
			50% {
				transform: translateY(-20px) rotate(2deg);
			}
		}
		.animate-spin-slow {
			animation: spin 20s linear infinite;
		}
	</style>

	<!-- ═══════ STATS ═══════ -->
	<section
		class="relative z-20 py-16"
		style="background:#1e1e1e; border-y: 1px solid rgba(255,193,7,0.1)"
	>
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-2 gap-6 md:grid-cols-4 lg:gap-12">
				{#each stats as s}
					<div class="group flex flex-col items-center justify-center text-center">
						<div
							class="transition-transform duration-300 group-hover:scale-110"
							style="font-family:'Playfair Display',serif;font-size:2.8rem;font-weight:800;color:#FFC107"
						>
							{s.value}
						</div>
						<div
							class="mt-2 text-xs font-black tracking-[0.2em] uppercase"
							style="font-family:'Plus Jakarta Sans',sans-serif;color:#eee"
						>
							{s.label}
						</div>
						<div
							class="mt-4 h-1 w-8 rounded-full bg-[#D32F2F] opacity-0 transition-opacity group-hover:opacity-100"
						></div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ ABOUT / TENTANG ═══════ -->
	<section id="about" class="relative overflow-hidden py-24" style="background:#F9F5F0">
		<!-- Decorative elements -->
		<div
			class="absolute top-1/4 right-0 h-96 w-96 translate-x-1/2 -translate-y-1/2 rounded-full opacity-5"
			style="background:#D32F2F; filter:blur(100px)"
		></div>
		<div
			class="absolute bottom-1/4 left-0 h-80 w-80 -translate-x-1/2 translate-y-1/2 rounded-full opacity-5"
			style="background:#FFC107; filter:blur(80px)"
		></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-1 items-center gap-20 lg:grid-cols-2">
				<!-- Image side -->
				<div class="relative order-2 lg:order-1">
					<div class="relative z-10 mx-auto w-full max-w-lg">
						<!-- Main Image with Gold Border -->
						<div
							class="relative overflow-hidden shadow-2xl"
							style="border-radius:2.5rem; border:10px solid #fff; box-shadow:0 30px 60px rgba(0,0,0,0.2)"
						>
							<img
								src={heroImg}
								alt="Dapur Yonica Culinary"
								class="w-full object-cover transition-transform duration-700 hover:scale-110"
								style="aspect-ratio:1/1"
							/>
							<div class="absolute inset-0 bg-linear-to-t from-black/60 to-transparent"></div>
						</div>

						<!-- Small overlay Image (Pempek) -->
						<div
							class="absolute -right-12 -bottom-10 z-20 hidden overflow-hidden rounded-4xl border-8 border-white shadow-[0_20px_50px_rgba(0,0,0,0.3)] md:block"
							style="width:240px; height:240px;"
						>
							<img src={pempekImg} alt="Pempek Cik Unik" class="h-full w-full object-cover" />
						</div>

						<!-- Heritage Badge -->
						<div
							class="absolute -top-10 -left-10 z-20 flex h-32 w-32 flex-col items-center justify-center rounded-full shadow-2xl"
							style="background:linear-gradient(135deg,#FFC107,#FFB300); color:#121212; border:6px solid #121212; transform: rotate(-12deg)"
						>
							<Utensils class="mb-1 h-8 w-8" />
							<span
								style="font-family:'Playfair Display',serif;font-size:1rem;font-weight:900;line-height:1"
								>EST.</span
							>
							<span
								style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.65rem;font-weight:900;letter-spacing:0.1em"
								>PADANG</span
							>
						</div>
					</div>
				</div>

				<!-- Text side -->
				<div class="order-1 flex flex-col justify-center lg:order-2">
					<div class="mb-6 inline-flex items-center gap-4">
						<span class="h-1 w-12 rounded-full bg-[#D32F2F]"></span>
						<span
							style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.85rem;font-weight:900;letter-spacing:0.2em;text-transform:uppercase;color:#D32F2F"
							>Warisan Kuliner Minang</span
						>
					</div>

					<h2
						class="mb-8"
						style="font-family:'Playfair Display',serif;font-size:clamp(2.5rem,5vw,4rem);line-height:1.1;color:#121212"
					>
						Olahan <span style="color:#D32F2F">Otentik</span> Berkelas
						<span class="text-[#FFC107] italic">Dunia</span>
					</h2>

					<p
						class="mb-10 text-lg leading-relaxed"
						style="font-family:'Plus Jakarta Sans',sans-serif;color:#4a4a4a"
					>
						<strong class="text-[#121212]">Dapur Yonica</strong> adalah wujud cinta kami terhadap kekayaan
						rasa Minang. Setiap produk kami—mulai dari Rendang yang legendaris hingga Pempek Cik Unik
						yang spesial—dibuat menggunakan rempah pilihan dan standar kualitas premium untuk menghadirkan
						kebahagiaan di setiap meja makan.
					</p>

					<div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
						{#each features as { icon: Icon, title, desc }}
							<div
								class="group flex items-start gap-5 rounded-2xl p-5 transition-all hover:bg-white hover:shadow-xl"
								style="border: 1px solid rgba(0,0,0,0.05)"
							>
								<div
									class="mt-1 flex h-14 w-14 shrink-0 items-center justify-center rounded-xl bg-[#121212] text-[#FFC107] transition-colors group-hover:bg-[#D32F2F] group-hover:text-white"
								>
									<Icon class="h-7 w-7" />
								</div>
								<div>
									<h4
										class="mb-1 text-[1.1rem] font-bold"
										style="font-family:'Playfair Display',serif;color:#121212"
									>
										{title}
									</h4>
									<p
										class="text-xs leading-relaxed"
										style="font-family:'Plus Jakarta Sans',sans-serif;color:#666"
									>
										{desc}
									</p>
								</div>
							</div>
						{/each}
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ MENU PUDING ═══════ -->
	<section id="menu" class="relative py-28" style="background:#121212">
		<!-- Background pattern -->
		<div
			class="absolute inset-0 opacity-[0.05]"
			style="background-image: radial-gradient(#FFC107 2px, transparent 2px); background-size: 40px 40px;"
		></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<!-- Header -->
			<div class="mb-20 flex flex-col items-center text-center">
				<div class="mb-4 inline-flex items-center gap-4">
					<span class="h-1 w-10 bg-[#FFC107]"></span>
					<span
						style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.85rem;font-weight:900;letter-spacing:0.25em;text-transform:uppercase;color:#FFC107"
						>Menu Unggulan Kami</span
					>
					<span class="h-1 w-10 bg-[#FFC107]"></span>
				</div>
				<h2
					class="mx-auto max-w-3xl"
					style="font-family:'Playfair Display',serif;font-size:clamp(2.5rem,5vw,4.5rem);line-height:1.1;color:#fff"
				>
					Karya <span style="color:#D32F2F">Kuliner</span> Terbaik Pelipur
					<em class="text-[#FFC107] not-italic">Lara</em>
				</h2>
			</div>

			<!-- Product Grid -->
			<div class="grid grid-cols-1 gap-10 sm:grid-cols-2 lg:grid-cols-3">
				{#each products as prod}
					<div
						class="group flex flex-col overflow-hidden rounded-[2.5rem] border border-white/5 bg-[#1e1e1e] transition-all duration-500 hover:-translate-y-3 hover:shadow-[0_40px_80px_-15px_rgba(0,0,0,0.6)]"
					>
						<div class="relative aspect-[4/3] overflow-hidden">
							<img
								src={prod.image}
								alt={prod.title}
								class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-110"
							/>
							<!-- Category Tag -->
							<div
								class="absolute top-6 right-6 z-10 rounded-xl border border-white/10 px-4 py-2 shadow-lg backdrop-blur-md"
								style="background:rgba(211,47,47,0.8)"
							>
								<span
									style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.75rem;font-weight:900;letter-spacing:0.1em;color:#fff;text-transform:uppercase"
									>{prod.category}</span
								>
							</div>
						</div>
						<div class="relative flex flex-1 flex-col p-10">
							<!-- Floating Icon -->
							<div
								class="absolute -top-8 left-10 flex h-16 w-16 items-center justify-center rounded-2xl bg-[#FFC107] shadow-xl transition-transform group-hover:rotate-12"
							>
								<Utensils class="h-8 w-8 text-black" />
							</div>

							<div class="mt-4 flex-1">
								<h3
									class="mb-4 text-[1.8rem] leading-tight font-bold"
									style="font-family:'Playfair Display',serif;color:#fff"
								>
									{prod.title}
								</h3>
								<p
									style="font-family:'Plus Jakarta Sans',sans-serif;font-size:1rem;color:#aaa;line-height:1.7"
								>
									{prod.desc}
								</p>
							</div>

							<div class="mt-10">
								<a
									href="https://wa.me/628123456789?text=Halo%20Admin%20Dapur%20Yonica,%20saya%20tertarik%20dengan%20{prod.title}"
									target="_blank"
									rel="noopener noreferrer"
								>
									<button
										class="w-full rounded-xl bg-linear-to-r from-[#D32F2F] to-[#8c1c1c] py-4 text-sm font-black tracking-widest text-white uppercase transition-all hover:scale-[1.02] hover:shadow-[0_10px_20px_rgba(211,47,47,0.3)]"
										style="font-family:'Plus Jakarta Sans',sans-serif"
									>
										Pesan Sekarang
									</button>
								</a>
							</div>
						</div>
					</div>
				{/each}
			</div>

			<!-- Instagram Link -->
			<div class="mt-20 text-center">
				<a href="https://instagram.com/dapur_yonica" target="_blank" rel="noopener noreferrer">
					<button
						class="group inline-flex h-16 items-center gap-4 rounded-xl border border-[#FFC107]/40 bg-transparent px-12 font-black transition-all hover:bg-[#FFC107] hover:text-black"
						style="font-family:'Plus Jakarta Sans',sans-serif;color:#FFC107"
					>
						<Instagram class="h-6 w-6" />
						<span>LIHAT MENU LENGKAP @DAPUR_YONICA</span>
						<ArrowRight class="h-5 w-5 transition-transform group-hover:translate-x-2" />
					</button>
				</a>
			</div>
		</div>
	</section>

	<!-- ═══════ CARA ORDER & INFO ═══════ -->
	<section id="order" class="py-24" style="background:#F9F5F0">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid items-center gap-16 lg:grid-cols-12">
				<!-- Left: Cara Order Steps -->
				<div class="lg:col-span-7">
					<div class="mb-14">
						<div class="mb-4 flex items-center gap-3">
							<span class="h-1 w-8 bg-[#D32F2F]"></span>
							<span
								style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.8rem;font-weight:900;letter-spacing:0.2em;text-transform:uppercase;color:#D32F2F"
								>Sistem Pemesanan Mudah</span
							>
						</div>
						<h2
							class="mt-2"
							style="font-family:'Playfair Display',serif;font-size:clamp(2.5rem,5vw,3.5rem);color:#121212;line-height:1.1"
						>
							Bawa Kelezatan <span class="text-[#D32F2F] italic">Minang</span><br />ke Meja Makanmu
						</h2>
					</div>

					<div class="space-y-8">
						{#each [{ num: '01', title: 'Pilih Menu & Hubungi Admin', desc: 'Pilih varian Rendang, Pempek, atau Kerupuk favoritmu lalu hubungi kami di WhatsApp atau Instagram.' }, { num: '02', title: 'Konfirmasi & Pembayaran', desc: 'Admin akan mengonfirmasi total pesanan dan ongkir. Lakukan pembayaran via transfer bank.' }, { num: '03', title: 'Pengiriman / Pick-Up', desc: 'Pesananmu akan disiapkan dengan packing khusus agar tetap fresh. Siap dikirim ke seluruh lokasi!' }] as step}
							<div
								class="group flex items-start gap-8 rounded-3xl border border-black/5 bg-white p-8 transition-all hover:-translate-x-2 hover:border-[#FFC107]/30 hover:shadow-2xl"
							>
								<div
									class="flex h-16 w-16 shrink-0 items-center justify-center rounded-2xl text-2xl font-black shadow-xl transition-colors group-hover:bg-[#FFC107] group-hover:text-black"
									style="font-family:'Playfair Display',serif;background:#121212;color:#FFC107"
								>
									{step.num}
								</div>
								<div class="pt-1">
									<h3
										style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:800;color:#121212;margin-bottom:0.5rem"
									>
										{step.title}
									</h3>
									<p
										style="font-family:'Plus Jakarta Sans',sans-serif;font-size:1rem;color:#666;line-height:1.6"
									>
										{step.desc}
									</p>
								</div>
							</div>
						{/each}
					</div>
				</div>

				<!-- Right: Info Lokasi Banner -->
				<div class="lg:col-span-5">
					<div
						class="relative overflow-hidden rounded-[3rem] border border-white/5 bg-[#121212] p-12 text-center shadow-[0_50px_100px_-20px_rgba(0,0,0,0.5)]"
					>
						<!-- Decorative Elements -->
						<div
							class="absolute -top-20 -right-20 h-64 w-64 rounded-full bg-[#D32F2F] opacity-10 blur-[60px]"
						></div>
						<div
							class="absolute -bottom-20 -left-20 h-64 w-64 rounded-full bg-[#FFC107] opacity-10 blur-[60px]"
						></div>

						<div class="relative z-10 flex flex-col items-center gap-10">
							<!-- Header -->
							<div class="flex flex-col items-center">
								<div
									class="mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-linear-to-br from-[#FFC107] to-[#FFB300] text-black shadow-xl"
								>
									<MapPin class="h-10 w-10" />
								</div>
								<h3
									style="font-family:'Playfair Display',serif;font-size:2rem;color:#fff;margin-bottom:0.5rem"
								>
									Lokasi & Operasional
								</h3>
								<div class="h-1 w-12 bg-[#D32F2F]"></div>
							</div>

							<!-- Details -->
							<div
								class="flex w-full flex-col gap-6 rounded-2xl border border-white/10 bg-white/5 p-8 text-left"
							>
								<div class="flex items-start gap-5">
									<Clock class="mt-1 h-6 w-6 shrink-0 text-[#FFC107]" />
									<div>
										<div
											class="mb-1 text-[0.7rem] font-black tracking-[0.2em] text-[#FFC107] uppercase"
										>
											Jam Buka
										</div>
										<div class="text-lg font-bold text-white">08.00 - 20.00 WIB</div>
										<div class="text-sm text-gray-400">Setiap Hari (Termasuk Libur)</div>
									</div>
								</div>

								<div class="h-px w-full bg-white/10"></div>

								<div class="flex items-start gap-5">
									<MapPin class="mt-1 h-6 w-6 shrink-0 text-[#FFC107]" />
									<div>
										<div
											class="mb-1 text-[0.7rem] font-black tracking-[0.2em] text-[#FFC107] uppercase"
										>
											Pusat Produksi
										</div>
										<div class="text-lg font-bold text-white">Kota Padang, Sumbar</div>
										<div class="text-sm text-gray-400">
											Delivery Area Padang & Seluruh Indonesia
										</div>
									</div>
								</div>
							</div>

							<!-- CTA -->
							<a
								href="https://wa.me/628123456789"
								target="_blank"
								rel="noopener noreferrer"
								class="w-full"
							>
								<button
									class="flex h-16 w-full items-center justify-center gap-3 rounded-xl text-lg font-black text-white shadow-xl transition-all hover:scale-[1.03] hover:shadow-[0_20px_40px_rgba(211,47,47,0.3)]"
									style="font-family:'Plus Jakarta Sans',sans-serif;background:#D32F2F"
								>
									<Phone class="h-6 w-6" /> KONSULTASI MENU WA
								</button>
							</a>

							<div
								class="flex items-center gap-2 text-xs font-bold tracking-widest text-gray-500 uppercase"
							>
								<ShieldCheck class="h-4 w-4" /> Trusted & Halal Certified
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ REVIEWS ═══════ -->
	<section id="reviews" class="py-24" style="background:#121212">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mb-16 flex flex-col items-center text-center">
				<div class="mb-4 flex items-center gap-3">
					<span class="h-1 w-8 bg-[#FFC107]"></span>
					<span
						style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.8rem;font-weight:900;letter-spacing:0.2em;text-transform:uppercase;color:#FFC107"
						>Suara Pelanggan</span
					>
					<span class="h-1 w-8 bg-[#FFC107]"></span>
				</div>
				<h2
					style="font-family:'Playfair Display',serif;font-size:clamp(2.5rem,5vw,3.5rem);color:#fff;line-height:1.1"
				>
					Apa Kata Mereka Tentang <br /><span class="text-[#D32F2F] italic">Dapur Yonica</span>
				</h2>
			</div>

			<div class="grid grid-cols-1 gap-8 md:grid-cols-3">
				{#each reviews as rv}
					<div
						class="group flex flex-col rounded-[2.5rem] border border-white/5 bg-[#1e1e1e] p-10 transition-all hover:-translate-y-2 hover:shadow-[0_40px_80px_-20px_rgba(0,0,0,0.4)]"
					>
						<div class="mb-8 flex gap-1">
							{#each Array(rv.stars) as _}
								<Star class="h-5 w-5 fill-[#FFC107] text-[#FFC107]" />
							{/each}
						</div>
						<p
							class="mb-8 flex-1 text-[1.1rem] leading-relaxed italic"
							style="font-family:'Plus Jakarta Sans',sans-serif;color:#aaa"
						>
							"{rv.text}"
						</p>

						<div class="flex items-center gap-5">
							<div
								class="flex h-14 w-14 items-center justify-center rounded-2xl text-[1.2rem] font-bold shadow-xl transition-transform group-hover:rotate-12"
								style="font-family:'Playfair Display',serif;background:linear-gradient(135deg,#D32F2F,#8c1c1c);color:#fff"
							>
								{rv.initial}
							</div>
							<div>
								<div
									class="text-[1.2rem] font-bold"
									style="font-family:'Playfair Display',serif;color:#fff"
								>
									{rv.name}
								</div>
								<div
									style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.8rem;color:#D32F2F;font-weight:700"
								>
									{rv.time}
								</div>
							</div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>
</main>

<!-- ═══════ FOOTER ═══════ -->
<footer style="background:#0a0a0a; border-top:1px solid rgba(255,193,7,0.1)">
	<div class="mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
		<div class="grid grid-cols-1 gap-16 text-center md:grid-cols-3 md:text-left">
			<!-- Brand -->
			<div class="flex flex-col items-center gap-6 md:items-start">
				<a href="#home" class="flex items-center gap-4">
					<div
						class="flex h-12 w-12 items-center justify-center rounded-2xl bg-linear-to-br from-[#D32F2F] to-[#8c1c1c]"
					>
						<Utensils class="h-7 w-7 text-[#FFC107]" />
					</div>
					<div
						class="text-3xl"
						style="font-family:'Playfair Display',serif;font-weight:800;color:#fff"
					>
						Dapur<span style="color:#FFC107">.Yonica</span>
					</div>
				</a>
				<p
					style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.95rem;color:#888;line-height:1.8;max-width:320px"
				>
					Olahan Minang Jadi Selera Dunia ✨. Aneka Rendang, Pempek Cik Unik, & Kerupuk Tulang Tuna.
					Authentic, Premium, & Halal Certified.
				</p>
			</div>

			<!-- Quick Links / Contact -->
			<div class="flex flex-col items-center gap-5 md:items-start">
				<div
					style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.8rem;font-weight:900;letter-spacing:0.2em;text-transform:uppercase;color:#FFC107;margin-bottom:0.5rem"
				>
					Kontak & Lokasi
				</div>
				<div class="flex items-center gap-4 text-white/80">
					<div class="flex h-10 w-10 items-center justify-center rounded-xl bg-white/5">
						<Phone class="h-5 w-5 text-[#D32F2F]" />
					</div>
					<span style="font-family:'Plus Jakarta Sans',sans-serif;font-size:1.1rem;font-weight:600"
						>628123456789</span
					>
				</div>
				<div class="flex items-center gap-4 text-white/80">
					<div class="flex h-10 w-10 items-center justify-center rounded-xl bg-white/5">
						<MapPin class="h-5 w-5 text-[#D32F2F]" />
					</div>
					<span style="font-family:'Plus Jakarta Sans',sans-serif;font-size:1.1rem;font-weight:600"
						>Padang, Sumatera Barat</span
					>
				</div>
			</div>

			<!-- Social Engagement -->
			<div class="flex flex-col items-center gap-6 md:items-start">
				<div
					style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.8rem;font-weight:900;letter-spacing:0.2em;text-transform:uppercase;color:#FFC107;margin-bottom:0.2rem"
				>
					Media Sosial
				</div>
				<a
					href="https://instagram.com/dapur_yonica"
					target="_blank"
					rel="noopener noreferrer"
					class="group flex items-center gap-4 rounded-2xl bg-white/5 p-3 pr-8 transition-all hover:bg-[#FFC107] hover:text-black"
				>
					<div
						class="flex h-12 w-12 items-center justify-center rounded-xl bg-linear-to-tr from-[#f9ce34] via-[#ee2a7b] to-[#6228d7] text-white shadow-lg transition-transform group-hover:rotate-6"
					>
						<Instagram class="h-6 w-6" />
					</div>
					<div class="flex flex-col items-start leading-tight">
						<span
							style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.75rem;font-weight:800;opacity:0.6"
							>Follow Us</span
						>
						<span
							style="font-family:'Plus Jakarta Sans',sans-serif;font-size:1.1rem;font-weight:800"
							>@dapur_yonica</span
						>
					</div>
				</a>
			</div>
		</div>

		<div class="mt-20 border-t pt-10 text-center" style="border-color:rgba(255,193,7,0.05)">
			<p
				style="font-family:'Plus Jakarta Sans',sans-serif;color:rgba(255,255,255,0.3);font-size:0.85rem;letter-spacing:0.05em"
			>
				© 2026 <strong style="color:rgba(255,255,255,0.5)">Dapur Yonica Culinary</strong>. Made with
				❤️ for Minang Heritage.
			</p>
		</div>
	</div>
</footer>
