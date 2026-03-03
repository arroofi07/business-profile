content = r"""<script lang="ts">
	import { Separator } from '$lib/components/ui/separator';
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
		Clock
	} from 'lucide-svelte';

	let menuOpen = $state(false);

	const navLinks = [
		{ href: '#home', label: 'Beranda' },
		{ href: '#about', label: 'Tentang' },
		{ href: '#products', label: 'Produk' },
		{ href: '#order', label: 'Cara Order' },
		{ href: '#reviews', label: 'Ulasan' }
	];

	const stats = [
		{ value: '22.6K', label: 'Followers Instagram' },
		{ value: '1.4K+', label: 'Total Postingan' },
		{ value: '100%', label: 'Produk Original' },
		{ value: 'BNI & BRI', label: 'Metode Pembayaran' }
	];

	const features = [
		{ icon: ShieldCheck, title: 'Produk Original', desc: 'Garansi keaslian produk 100% dari agen resmi.' },
		{ icon: Award, title: 'Bersertifikat BPOM', desc: 'Aman digunakan, sudah terdaftar dan diuji BPOM.' },
		{ icon: CheckCircle2, title: 'Halal & MUI', desc: 'Tersertifikasi halal resmi oleh Majelis Ulama Indonesia.' },
		{ icon: ShoppingBag, title: 'Open Reseller', desc: 'Daftar sebagai reseller dan raih penghasilan tambahan.' }
	];

	const products = [
		{
			category: 'Serum Perawatan',
			title: 'Brightening & Anti-Aging Serum',
			desc: 'Serum dengan bahan aktif premium untuk wajah bercahaya dan melawan tanda penuaan.',
			image: 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?q=80&w=600&fit=crop'
		},
		{
			category: 'Pelembap Wajah',
			title: 'Deep Hydration Cream',
			desc: 'Krim ringan yang melembapkan pori-pori sejak pagi hingga malam hari.',
			image: 'https://images.unsplash.com/photo-1629198688000-71f23e745b6e?q=80&w=600&fit=crop'
		},
		{
			category: 'Pembersih Wajah',
			title: 'Gentle Facial Wash',
			desc: 'Membersihkan kotoran dan sisa makeup dengan lembut tanpa menghilangkan kelembapan.',
			image: 'https://images.unsplash.com/photo-1556228578-0d85b1a4d571?q=80&w=600&fit=crop'
		},
		{
			category: 'Pelindung UV',
			title: 'Daily Sunscreen SPF 50',
			desc: 'Perlindungan terbaik dari sinar UV A &amp; B setiap hari, ringan di kulit.',
			image: 'https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?q=80&w=600&fit=crop'
		},
		{
			category: 'Paket Bundling',
			title: 'Glow Starter Bundle',
			desc: 'Paket hemat untuk memulai rutinitas skincare sehari-hari dengan hasil maksimal.',
			image: 'https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?q=80&w=600&fit=crop'
		},
		{
			category: 'Perawatan Khusus',
			title: 'Acne & Blemish Control',
			desc: 'Formula khusus untuk mengatasi jerawat membandel dan memudarkan bekas noda.',
			image: 'https://images.unsplash.com/photo-1611077544795-c23f26038d1d?q=80&w=600&fit=crop'
		}
	];

	const reviews = [
		{
			name: 'Amanda Lestari',
			initial: 'AL',
			time: '2 minggu lalu',
			stars: 5,
			text: 'Produknya benar-benar bagus! Serum brightening-nya cepat meresap dan kulit jadi lebih glowing dalam seminggu. Sangat puas!'
		},
		{
			name: 'Siti Maysaroh',
			initial: 'SM',
			time: '1 bulan lalu',
			stars: 5,
			text: 'Alhamdulillah, sudah BPOM dan Halal MUI jadi aman. Admin-nya responsif dan ramah. Proses order via WA sangat mudah!'
		},
		{
			name: 'Dina Prita Wulandari',
			initial: 'DW',
			time: '2 bulan lalu',
			stars: 5,
			text: 'Kualitas premium dengan harga yang bersahabat. Sudah repeat order 3x dan selalu puas. Recommended banget!'
		}
	];
</script>

<svelte:head>
	<title>Marwah Skincare – Agen Resmi | BPOM · Halal · MUI</title>
	<meta
		name="description"
		content="Marwah Skincare – agen resmi produk skincare original bersertifikat BPOM, Halal, dan MUI. Open reseller. Buka 08.00–18.00. Order via WhatsApp."
	/>
	<link
		href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=DM+Sans:wght@300;400;500;600;700&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<!-- ═══════ NAVBAR ═══════ -->
<header class="fixed inset-x-0 top-0 z-50">
	<nav
		class="border-b backdrop-blur-2xl transition-all"
		style="background:rgba(253,248,240,0.96);border-color:rgba(201,168,76,0.2);box-shadow:0 2px 32px rgba(61,26,74,0.08)"
	>
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-20 items-center justify-between">

				<!-- Logo -->
				<a href="#home" class="group flex items-center gap-3">
					<div
						class="flex h-11 w-11 items-center justify-center rounded-full transition-transform duration-300 group-hover:scale-110"
						style="background:linear-gradient(135deg,#c9a84c,#e8ca7a);box-shadow:0 4px 20px rgba(201,168,76,0.4)"
					>
						<span style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;font-weight:700;color:#3d1a4a">M</span>
					</div>
					<div class="leading-tight">
						<div style="font-family:'Cormorant Garamond',serif;font-size:1.15rem;font-weight:700;color:#3d1a4a">
							Marwah<span style="color:#c9a84c"> Skincare</span>
						</div>
						<div style="font-size:0.6rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#805690">
							Official Agent
						</div>
					</div>
				</a>

				<!-- Desktop Nav -->
				<div class="hidden items-center gap-1 md:flex">
					{#each navLinks as link}
						<a
							href={link.href}
							class="group relative rounded-xl px-4 py-2 text-sm font-semibold transition-all duration-200"
							style="color:#5c2d6e"
						>
							{link.label}
							<span
								class="absolute bottom-1 left-1/2 h-0.5 w-0 -translate-x-1/2 rounded-full transition-all duration-300 group-hover:w-4"
								style="background:#c9a84c"
							></span>
						</a>
					{/each}
				</div>

				<!-- CTA -->
				<div class="hidden items-center gap-3 md:flex">
					<div
						class="flex items-center gap-2 rounded-full border px-3 py-1.5"
						style="border-color:#c9a84c;color:#c9a84c;font-size:0.65rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase"
					>
						<ShieldCheck class="h-3.5 w-3.5" /> BPOM & Halal MUI
					</div>
					<a href="https://wa.me/1234567890" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-10 items-center gap-2 rounded-xl px-5 text-sm font-bold text-white transition-all hover:-translate-y-0.5 hover:shadow-lg"
							style="background:linear-gradient(135deg,#c9a84c,#e8ca7a);box-shadow:0 4px 16px rgba(201,168,76,0.4);color:#3d1a4a"
						>
							<MessageCircle class="h-4 w-4" /> Order Sekarang
						</button>
					</a>
				</div>

				<!-- Mobile Toggle -->
				<button
					onclick={() => (menuOpen = !menuOpen)}
					class="rounded-xl p-2 transition hover:bg-amber-50 md:hidden"
					style="color:#3d1a4a"
					aria-label="Toggle menu"
				>
					{#if menuOpen}<X class="h-6 w-6" />{:else}<Menu class="h-6 w-6" />{/if}
				</button>
			</div>
		</div>

		<!-- Mobile Menu -->
		{#if menuOpen}
			<div
				class="border-t px-4 pt-3 pb-6 md:hidden"
				style="background:#fdf8f0;border-color:rgba(201,168,76,0.15)"
			>
				{#each navLinks as link}
					<a
						href={link.href}
						onclick={() => (menuOpen = false)}
						class="flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-semibold transition"
						style="color:#5c2d6e"
					>
						{link.label}
					</a>
				{/each}
				<div class="mt-4 border-t pt-4" style="border-color:rgba(201,168,76,0.15)">
					<a href="https://wa.me/1234567890" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-11 w-full items-center justify-center gap-2 rounded-xl text-sm font-bold"
							style="background:linear-gradient(135deg,#c9a84c,#e8ca7a);color:#3d1a4a"
						>
							<MessageCircle class="h-4 w-4" /> Order via WhatsApp
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
		style="background:linear-gradient(135deg,#fdf8f0 0%,#f5ede0 100%)"
	>
		<!-- Decorative blobs -->
		<div
			class="pointer-events-none absolute -top-32 -left-20 h-[550px] w-[550px] opacity-50"
			style="background:radial-gradient(ellipse,#f2eff9 0%,transparent 70%);filter:blur(60px)"
		></div>
		<div
			class="pointer-events-none absolute bottom-0 right-0 h-[450px] w-[450px] opacity-40"
			style="background:radial-gradient(circle,#e8ca7a 0%,transparent 65%);filter:blur(70px)"
		></div>
		<!-- Subtle dot pattern -->
		<div class="dot-pattern pointer-events-none absolute inset-0 opacity-30"></div>

		<div
			class="relative mx-auto max-w-7xl px-4 pb-24 pt-20 sm:px-6 lg:grid lg:grid-cols-12 lg:gap-0 lg:px-8 lg:pt-28"
		>
			<!-- Left text — 6 cols -->
			<div class="animate-slide-up lg:col-span-6 flex flex-col justify-center space-y-8">

				<!-- Tag pill -->
				<div
					class="inline-flex items-center gap-2.5 self-start rounded-full border px-4 py-2"
					style="border-color:rgba(201,168,76,0.4);background:rgba(201,168,76,0.07)"
				>
					<span class="h-2 w-2 animate-pulse rounded-full" style="background:#c9a84c"></span>
					<span style="font-size:0.72rem;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;color:#5c2d6e">
						Agen Resmi Marwah Skincare
					</span>
				</div>

				<!-- Heading -->
				<div class="animate-slide-up delay-100">
					<h1
						style="font-family:'Cormorant Garamond',serif;font-size:clamp(3rem,6vw,5rem);line-height:1.08;color:#3d1a4a;font-weight:500"
					>
						Cantik Natural,<br />
						<em style="color:#c9a84c;font-weight:700">Kulit Bersinar</em><br />
						<span style="font-size:0.55em;font-weight:400;color:#805690">untuk Setiap Wanita Indonesia</span>
					</h1>
				</div>

				<p class="animate-slide-up max-w-md text-base leading-relaxed delay-200" style="color:#5c2d6e">
					Produk skincare original, diformulasikan untuk kecantikan alami yang eksklusif. Sepenuhnya terjamin oleh
					<strong style="color:#3d1a4a">BPOM, Halal MUI</strong> — aman &amp; nyaman untuk kulitmu.
				</p>

				<!-- CTA -->
				<div class="animate-slide-up flex flex-wrap gap-4 delay-300">
					<a href="https://wa.me/1234567890" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-14 items-center gap-2.5 rounded-2xl px-8 text-sm font-bold transition-all hover:scale-105 hover:shadow-2xl"
							style="background:linear-gradient(135deg,#3d1a4a,#5c2d6e);color:white;box-shadow:0 8px 30px rgba(61,26,74,0.35)"
						>
							<MessageCircle class="h-5 w-5" /> Pesan via WhatsApp
						</button>
					</a>
					<a href="#products">
						<button
							class="flex h-14 items-center gap-2.5 rounded-2xl border px-8 text-sm font-semibold transition-all hover:bg-amber-50"
							style="border-color:rgba(201,168,76,0.4);color:#3d1a4a"
						>
							Lihat Produk <ArrowRight class="h-4 w-4" />
						</button>
					</a>
				</div>

				<!-- Trust pills -->
				<div
					class="animate-slide-up flex flex-wrap items-center gap-3 border-t pt-6 delay-400"
					style="border-color:rgba(201,168,76,0.2)"
				>
					{#each ['Aman Digunakan', 'BPOM Approved', 'Halal & MUI', 'Open Reseller'] as tag}
						<div
							class="flex items-center gap-1.5 rounded-full border bg-white px-3 py-1"
							style="border-color:rgba(201,168,76,0.3)"
						>
							<Check class="h-3 w-3" style="color:#c9a84c" />
							<span style="font-size:0.7rem;font-weight:700;color:#3d1a4a">{tag}</span>
						</div>
					{/each}
				</div>
			</div>

			<!-- Right image — 6 cols -->
			<div class="animate-slide-left relative mt-16 lg:col-span-6 lg:mt-0 delay-200">
				<div class="relative pl-8 lg:pl-12">
					<!-- Organic blob bg -->
					<div
						class="absolute inset-0 rounded-full opacity-20"
						style="background:radial-gradient(circle,#c9a84c,transparent 70%);transform:scale(1.3)"
					></div>

					<!-- Main image with organic border-radius -->
					<div
						class="relative overflow-hidden shadow-2xl"
						style="border-radius:60% 40% 50% 50% / 50% 60% 40% 50%;border:8px solid white;box-shadow:0 40px 80px -20px rgba(61,26,74,0.3)"
					>
						<img
							src="https://images.unsplash.com/photo-1620916566398-39f1143ab7be?q=80&w=700&auto=format&fit=crop"
							alt="Marwah Skincare produk unggulan"
							class="w-full object-cover transition-transform duration-700 hover:scale-105"
							style="aspect-ratio:3/4"
						/>
						<div
							class="absolute inset-0"
							style="background:linear-gradient(to top,rgba(61,26,74,0.25) 0%,transparent 60%)"
						></div>
					</div>

					<!-- Float card: Instagram -->
					<div
						class="glass-light animate-float-gentle absolute -left-4 top-16 rounded-2xl px-4 py-3 shadow-xl lg:-left-8"
					>
						<div class="flex items-center gap-3">
							<div
								class="flex h-10 w-10 items-center justify-center rounded-full text-white"
								style="background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888)"
							>
								<Instagram class="h-5 w-5" />
							</div>
							<div>
								<div class="text-sm font-bold" style="color:#3d1a4a">22.6K Followers</div>
								<div style="font-size:0.65rem;color:#805690">@marwah_skincare_id</div>
							</div>
						</div>
					</div>

					<!-- Float card: Jam buka -->
					<div
						class="glass-light animate-float-gentle absolute -bottom-4 right-4 rounded-2xl px-5 py-3 shadow-xl text-center"
						style="animation-delay:1.5s"
					>
						<div style="font-size:0.65rem;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;color:#c9a84c">Jam Buka</div>
						<div class="mt-1 text-sm font-bold" style="color:#3d1a4a">08.00 – 18.00</div>
						<div style="font-size:0.65rem;color:#805690">Setiap Hari</div>
					</div>

					<!-- Decorative ring -->
					<div
						class="animate-spin-slow pointer-events-none absolute -right-4 top-1/3 h-24 w-24 rounded-full border-2 border-dashed opacity-30"
						style="border-color:#c9a84c"
					></div>
				</div>
			</div>
		</div>

		<!-- Wave divider -->
		<div class="pointer-events-none absolute inset-x-0 bottom-0">
			<svg viewBox="0 0 1440 80" fill="none" preserveAspectRatio="none" class="w-full" style="height:60px">
				<path d="M0,40 C360,80 720,0 1080,40 C1260,60 1380,30 1440,40 L1440,80 L0,80 Z" fill="#3d1a4a" />
			</svg>
		</div>
	</section>

	<!-- ═══════ STATS ═══════ -->
	<section class="py-16" style="background:#3d1a4a">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-2 gap-px md:grid-cols-4" style="background:rgba(201,168,76,0.15)">
				{#each stats as s}
					<div class="flex flex-col items-center py-10 text-center" style="background:#3d1a4a">
						<div
							style="font-family:'Cormorant Garamond',serif;font-size:2.4rem;font-weight:700;background:linear-gradient(135deg,#c9a84c,#e8ca7a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text"
						>
							{s.value}
						</div>
						<div class="mt-1.5 text-xs font-bold uppercase tracking-widest" style="color:rgba(232,202,122,0.7)">
							{s.label}
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ ABOUT ═══════ -->
	<section id="about" class="relative overflow-hidden py-28" style="background:#f5ede0">
		<div class="dot-pattern pointer-events-none absolute inset-0 opacity-30"></div>
		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-1 items-center gap-16 lg:grid-cols-2">

				<!-- Image side -->
				<div class="relative">
					<div
						class="overflow-hidden shadow-2xl"
						style="border-radius:50% 30% 50% 30% / 30% 50% 30% 50%;border:10px solid white"
					>
						<img
							src="https://images.unsplash.com/photo-1556228720-1c2a468e1824?q=80&w=600&auto=format&fit=crop"
							alt="Skincare natural ingredients"
							class="w-full object-cover transition-transform duration-500 hover:scale-105"
							style="aspect-ratio:4/5"
						/>
					</div>
					<div
						class="absolute -bottom-4 -right-4 hidden overflow-hidden rounded-full border-8 border-white shadow-xl md:block"
						style="width:160px;height:160px"
					>
						<img
							src="https://images.unsplash.com/photo-1615397323136-2244c079860b?q=80&w=300&auto=format&fit=crop"
							alt="Cream texture"
							class="h-full w-full object-cover"
						/>
					</div>
					<!-- Gold accent card -->
					<div
						class="absolute -top-4 -left-4 rounded-2xl px-5 py-4 shadow-xl text-center"
						style="background:linear-gradient(135deg,#c9a84c,#e8ca7a);min-width:120px"
					>
						<div style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;font-weight:700;color:#3d1a4a">
							1K+
						</div>
						<div style="font-size:0.6rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(61,26,74,0.7)">
							Happy Customer
						</div>
					</div>
				</div>

				<!-- Text side -->
				<div class="space-y-8">
					<div class="flex items-center gap-3">
						<div class="h-px w-10 rounded" style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"></div>
						<span style="font-size:0.72rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#c9a84c">Tentang Kami</span>
					</div>

					<div>
						<h2
							style="font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,4vw,2.8rem);line-height:1.2;color:#3d1a4a;font-weight:500"
						>
							Agen Skincare<br />
							<em style="color:#c9a84c;font-weight:700">Terpercaya</em> untuk Kulitmu
						</h2>
					</div>

					<p class="text-base leading-relaxed" style="color:#5c2d6e">
						<strong style="color:#3d1a4a">Marwah Skincare</strong> adalah agen resmi produk perawatan kulit yang menyediakan rangkaian skincare original berkualitas tinggi. Seluruh produk telah tersertifikasi
						<strong style="color:#3d1a4a">BPOM, Halal MUI</strong> sehingga aman dan nyaman untuk semua jenis kulit.
					</p>
					<p class="text-sm leading-relaxed" style="color:#805690">
						Kami melayani pembelian individual maupun reseller dengan penuh keramahan dan kejujuran. Kepuasan dan kepercayaan Anda adalah prioritas utama kami.
					</p>

					<div class="grid grid-cols-1 gap-3 sm:grid-cols-2">
						{#each [
							'Produk 100% Original',
							'Legalitas BPOM & Halal MUI',
							'Konsultasi Gratis via WA',
							'Harga Terjangkau & Transparan',
							'Pembayaran BNI & BRI',
							'Open Reseller Aktif'
						] as item}
							<div
								class="flex items-center gap-3 rounded-2xl border bg-white px-4 py-3 transition-all card-hover"
								style="border-color:rgba(201,168,76,0.2);box-shadow:var(--brand-shadow-card)"
							>
								<div
									class="flex h-5 w-5 shrink-0 items-center justify-center rounded-full"
									style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"
								>
									<Check class="h-3 w-3" style="color:#3d1a4a" />
								</div>
								<span class="text-sm font-medium" style="color:#3d1a4a">{item}</span>
							</div>
						{/each}
					</div>

					<a href="#order">
						<button
							class="flex h-12 items-center gap-2.5 rounded-2xl px-8 text-sm font-bold text-white transition-all hover:scale-105 hover:shadow-lg"
							style="background:linear-gradient(135deg,#3d1a4a,#5c2d6e);box-shadow:0 8px 24px rgba(61,26,74,0.3)"
						>
							Cara Order <ArrowRight class="h-4 w-4" />
						</button>
					</a>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ KEUNGGULAN ═══════ -->
	<section class="py-20" style="background:#f2eff9">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mb-14 text-center">
				<div class="mb-3 inline-flex items-center gap-3">
					<div class="h-px w-8 rounded" style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"></div>
					<span style="font-size:0.72rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#c9a84c">Keunggulan Kami</span>
					<div class="h-px w-8 rounded" style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"></div>
				</div>
				<h2
					style="font-family:'Cormorant Garamond',serif;font-size:clamp(1.8rem,4vw,2.6rem);color:#3d1a4a;font-weight:500"
				>
					Kenapa Pilih <em style="color:#c9a84c;font-weight:700">Marwah Skincare?</em>
				</h2>
			</div>

			<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
				{#each features as f}
					<div
						class="card-hover group flex flex-col items-center rounded-3xl bg-white p-8 text-center"
						style="border:1px solid rgba(201,168,76,0.15);box-shadow:var(--brand-shadow-card)"
					>
						<div
							class="mb-5 flex h-16 w-16 items-center justify-center rounded-full transition-transform duration-300 group-hover:scale-110"
							style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"
						>
							<svelte:component this={f.icon} class="h-8 w-8" style="color:#3d1a4a" />
						</div>
						<h3 class="mb-2 text-base font-bold" style="color:#3d1a4a">{f.title}</h3>
						<p class="text-sm leading-relaxed" style="color:#805690">{f.desc}</p>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ PRODUK ═══════ -->
	<section id="products" class="relative overflow-hidden py-28" style="background:#3d1a4a">
		<div class="dot-pattern-plum pointer-events-none absolute inset-0"></div>
		<div
			class="pointer-events-none absolute -top-20 right-1/4 h-96 w-96 rounded-full opacity-[0.08]"
			style="background:radial-gradient(circle,#c9a84c 0%,transparent 65%);filter:blur(40px)"
		></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<!-- Header -->
			<div class="mb-16 max-w-2xl">
				<div class="mb-3 flex items-center gap-3">
					<div class="h-px w-10 rounded" style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"></div>
					<span style="font-size:0.72rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#e8ca7a">Produk Unggulan</span>
				</div>
				<h2
					class="text-white"
					style="font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,4vw,3rem);font-weight:400"
				>
					Rangkaian Perawatan<br />
					<em style="color:#e8ca7a;font-weight:700">Terbaik untuk Kulit Anda</em>
				</h2>
				<p class="mt-4 text-sm leading-relaxed" style="color:rgba(255,255,255,0.45)">
					Semua produk Marwah Skincare hadir dengan formulasi premium, aman, dan terbukti efektif untuk berbagai jenis kulit.
				</p>
			</div>

			<!-- Product Grid -->
			<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
				{#each products as prod}
					<div
						class="group relative overflow-hidden rounded-3xl border transition-all duration-350 hover:-translate-y-2 hover:border-amber-400/40"
						style="border-color:rgba(201,168,76,0.12);background:rgba(255,255,255,0.04)"
					>
						<div class="aspect-[4/3] overflow-hidden">
							<img
								src={prod.image}
								alt={prod.title}
								class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110"
							/>
						</div>
						<div class="p-6">
							<div
								class="mb-3 inline-flex items-center rounded-full px-3 py-1"
								style="background:rgba(201,168,76,0.12);color:#e8ca7a;font-size:0.65rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase"
							>
								{prod.category}
							</div>
							<h3
								class="mb-2 text-xl font-semibold text-white"
								style="font-family:'Cormorant Garamond',serif"
							>
								{prod.title}
							</h3>
							<p class="text-sm leading-relaxed" style="color:rgba(255,255,255,0.5)">{@html prod.desc}</p>
						</div>
						<!-- Bottom gold line on hover -->
						<div
							class="absolute bottom-0 left-0 h-0.5 w-0 rounded-full transition-all duration-500 group-hover:w-full"
							style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"
						></div>
					</div>
				{/each}
			</div>

			<div class="mt-14 text-center">
				<a href="https://wa.me/1234567890" target="_blank" rel="noopener noreferrer">
					<button
						class="inline-flex h-14 items-center gap-3 rounded-2xl px-10 text-sm font-bold transition-all hover:scale-105 hover:shadow-2xl"
						style="background:linear-gradient(135deg,#c9a84c,#e8ca7a);color:#3d1a4a;box-shadow:0 8px 30px rgba(201,168,76,0.4)"
					>
						<MessageCircle class="h-5 w-5" /> Tanyakan Produk & Harga
					</button>
				</a>
			</div>
		</div>
	</section>

	<!-- ═══════ CARA ORDER ═══════ -->
	<section id="order" class="py-24" style="background:#fdf8f0">
		<div class="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
			<div class="mb-14 text-center">
				<div class="mb-3 inline-flex items-center gap-3">
					<div class="h-px w-8 rounded" style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"></div>
					<span style="font-size:0.72rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#c9a84c">Pemesanan</span>
					<div class="h-px w-8 rounded" style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"></div>
				</div>
				<h2
					style="font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,4vw,2.8rem);color:#3d1a4a;font-weight:500"
				>
					3 Langkah Mudah <em style="color:#c9a84c;font-weight:700">Belanja Online</em>
				</h2>
			</div>

			<div class="grid grid-cols-1 gap-8 md:grid-cols-3">
				{#each [
					{ step: '01', title: 'Hubungi Kami', desc: 'Chat via WhatsApp atau DM Instagram @marwah_skincare_id untuk konsultasi produk gratis.' },
					{ step: '02', title: 'Pilih Produk', desc: 'Pilih produk sesuai kebutuhan kulitmu. Kami siap membantu merekomendasikan yang terbaik.' },
					{ step: '03', title: 'Transfer & Kirim', desc: 'Lakukan pembayaran via BNI atau BRI, lalu produk langsung dikemas rapi dan dikirim ke kamu.' }
				] as o}
					<div
						class="relative flex flex-col items-center rounded-3xl bg-white p-8 text-center"
						style="border:1px solid rgba(201,168,76,0.2);box-shadow:var(--brand-shadow-card)"
					>
						<div
							class="absolute -top-6 flex h-12 w-12 items-center justify-center rounded-full shadow-lg"
							style="background:linear-gradient(135deg,#3d1a4a,#5c2d6e);font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:700;color:white"
						>
							{o.step}
						</div>
						<h3 class="mt-4 mb-3 text-lg font-bold" style="color:#3d1a4a">{o.title}</h3>
						<p class="text-sm leading-relaxed" style="color:#805690">{o.desc}</p>
					</div>
				{/each}
			</div>

			<!-- CTA Banner -->
			<div
				class="mt-12 flex flex-col items-center justify-between gap-6 overflow-hidden rounded-3xl p-8 sm:flex-row"
				style="background:linear-gradient(135deg,#3d1a4a,#5c2d6e);box-shadow:0 20px 60px rgba(61,26,74,0.3)"
			>
				<div>
					<div
						class="text-xl font-bold text-white"
						style="font-family:'Cormorant Garamond',serif"
					>
						Siap Mulai Perawatan Kulitmu?
					</div>
					<p class="mt-1 text-sm" style="color:rgba(255,255,255,0.65)">
						Jam operasional 08.00 – 18.00 · Pembayaran BNI & BRI · Open Reseller
					</p>
				</div>
				<div class="flex shrink-0 flex-col gap-3 sm:flex-row">
					<a href="https://wa.me/1234567890" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-12 items-center gap-2 rounded-2xl bg-white px-7 text-sm font-bold transition-all hover:scale-105"
							style="color:#3d1a4a"
						>
							<MessageCircle class="h-4 w-4" /> WhatsApp Sekarang
						</button>
					</a>
					<a href="https://instagram.com/marwah_skincare_id" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-12 items-center gap-2 rounded-2xl border-2 border-white/30 px-7 text-sm font-semibold text-white transition-all hover:bg-white/10"
						>
							<Instagram class="h-4 w-4" /> Instagram
						</button>
					</a>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ JAM OPERASIONAL ═══════ -->
	<section class="py-20" style="background:#f5ede0">
		<div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
			<div class="overflow-hidden rounded-3xl shadow-2xl" style="border:1px solid rgba(201,168,76,0.2)">
				<!-- Header -->
				<div class="px-8 py-6" style="background:linear-gradient(135deg,#3d1a4a,#5c2d6e)">
					<div class="flex items-center gap-3">
						<Clock class="h-5 w-5" style="color:#e8ca7a" />
						<div>
							<div class="text-sm font-bold text-white">Jam Operasional</div>
							<div style="font-size:0.65rem;color:rgba(232,202,122,0.6)">Marwah Skincare Official Agent</div>
						</div>
					</div>
				</div>
				<!-- Rows -->
				<div class="divide-y bg-white" style="divide-color:rgba(201,168,76,0.1)">
					{#each [
						{ day: 'Senin', time: '08.00 – 18.00', open: true },
						{ day: 'Selasa', time: '08.00 – 18.00', open: true },
						{ day: 'Rabu', time: '08.00 – 18.00', open: true },
						{ day: 'Kamis', time: '08.00 – 18.00', open: true },
						{ day: 'Jumat', time: '08.00 – 18.00', open: true },
						{ day: 'Sabtu', time: '08.00 – 18.00', open: true },
						{ day: 'Minggu', time: 'Tutup', open: false }
					] as h, i}
						<div
							class="flex items-center justify-between px-8 py-4 transition-colors hover:bg-amber-50"
						>
							<div class="flex items-center gap-3">
								<div
									class="h-2 w-2 rounded-full"
									style="background:{h.open ? 'linear-gradient(135deg,#c9a84c,#e8ca7a)' : '#d1d5db'}"
								></div>
								<span class="text-sm font-semibold" style="color:#3d1a4a">{h.day}</span>
							</div>
							<span
								class="rounded-full px-3 py-1 text-xs font-bold"
								style="background:{h.open ? 'rgba(201,168,76,0.1)' : 'rgba(209,213,219,0.3)'};color:{h.open ? '#c9a84c' : '#9ca3af'}"
							>
								{h.time}
							</span>
						</div>
					{/each}
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ REVIEWS ═══════ -->
	<section id="reviews" class="relative py-24" style="background:#fdf8f0">
		<div class="dot-pattern pointer-events-none absolute inset-0 opacity-30"></div>
		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">

			<div class="mb-16 text-center">
				<div class="mb-3 inline-flex items-center gap-3">
					<div class="h-px w-8 rounded" style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"></div>
					<span style="font-size:0.72rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#c9a84c">Ulasan Pelanggan</span>
					<div class="h-px w-8 rounded" style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"></div>
				</div>
				<h2
					style="font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,4vw,2.8rem);color:#3d1a4a;font-weight:500"
				>
					Mereka yang Sudah <em style="color:#c9a84c;font-weight:700">Percaya</em>
				</h2>
				<!-- Rating pill -->
				<div
					class="mt-6 inline-flex items-center gap-4 rounded-2xl border bg-white px-7 py-4 shadow-sm"
					style="border-color:rgba(201,168,76,0.2)"
				>
					<div class="text-3xl font-bold" style="color:#c9a84c">★★★★★</div>
					<Separator orientation="vertical" class="h-8" />
					<div class="text-left">
						<div class="text-sm font-bold" style="color:#3d1a4a">Rating Bintang 5</div>
						<div style="font-size:0.7rem;color:#805690">Testimoni Pelanggan Setia</div>
					</div>
				</div>
			</div>

			<div class="grid grid-cols-1 gap-6 md:grid-cols-3">
				{#each reviews as rv}
					<div
						class="group relative flex flex-col rounded-3xl bg-white p-8 transition-all card-hover"
						style="border:1px solid rgba(201,168,76,0.12);box-shadow:var(--brand-shadow-card)"
					>
						<div
							class="mb-3 text-6xl font-bold leading-none select-none"
							style="color:rgba(201,168,76,0.15);font-family:'Cormorant Garamond',serif"
						>
							"
						</div>
						<p class="mb-6 flex-1 text-sm leading-relaxed" style="color:#5c2d6e">{rv.text}</p>
						<div class="mb-4 flex gap-1">
							{#each Array(rv.stars) as _}
								<Star class="h-4 w-4 fill-current" style="color:#c9a84c" />
							{/each}
						</div>
						<Separator style="background:rgba(201,168,76,0.12)" />
						<div class="mt-4 flex items-center gap-3">
							<div
								class="flex h-11 w-11 items-center justify-center rounded-full text-sm font-bold"
								style="background:linear-gradient(135deg,#3d1a4a,#5c2d6e);color:white"
							>
								{rv.initial}
							</div>
							<div>
								<div class="text-sm font-bold" style="color:#3d1a4a">{rv.name}</div>
								<div style="font-size:0.65rem;color:#805690">{rv.time}</div>
							</div>
						</div>
						<div
							class="absolute bottom-0 left-0 right-0 h-1 rounded-b-3xl opacity-0 transition-opacity duration-300 group-hover:opacity-100"
							style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"
						></div>
					</div>
				{/each}
			</div>
		</div>
	</section>

</main>

<!-- ═══════ FOOTER ═══════ -->
<footer style="background:#2a0f35;border-top:1px solid rgba(201,168,76,0.1)">
	<div class="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
		<div class="flex flex-col items-center justify-between gap-8 md:flex-row">
			<!-- Brand -->
			<div class="flex items-center gap-3">
				<div
					class="flex h-10 w-10 items-center justify-center rounded-full"
					style="background:linear-gradient(135deg,#c9a84c,#e8ca7a)"
				>
					<span style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:700;color:#3d1a4a">M</span>
				</div>
				<div>
					<div
						class="text-base font-bold text-white"
						style="font-family:'Cormorant Garamond',serif"
					>
						Marwah Skincare
					</div>
					<div style="font-size:0.6rem;color:rgba(201,168,76,0.5);letter-spacing:0.1em;text-transform:uppercase">
						Official Agent · Health & Beauty
					</div>
				</div>
			</div>

			<!-- Links -->
			<div class="flex flex-col items-center gap-3 text-sm md:items-start">
				<div style="font-size:0.65rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#c9a84c">Informasi</div>
				<div class="flex items-center gap-2 text-white/60">
					<Clock class="h-4 w-4" style="color:#c9a84c" /> Jam 08.00 – 18.00
				</div>
				<div class="flex items-center gap-2 text-white/60">
					<ShieldCheck class="h-4 w-4" style="color:#c9a84c" /> BPOM · Halal · MUI
				</div>
			</div>

			<!-- Social -->
			<div class="flex flex-col items-center gap-3 md:items-end">
				<div style="font-size:0.65rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:#c9a84c">Hubungi Kami</div>
				<a
					href="https://instagram.com/marwah_skincare_id"
					target="_blank"
					rel="noopener noreferrer"
					class="flex items-center gap-2 text-sm text-white/70 transition-colors hover:text-amber-300"
				>
					<Instagram class="h-4 w-4" /> @marwah_skincare_id
				</a>
				<a
					href="https://wa.me/1234567890"
					target="_blank"
					rel="noopener noreferrer"
					class="flex items-center gap-2 text-sm text-white/70 transition-colors hover:text-amber-300"
				>
					<MessageCircle class="h-4 w-4" /> Chat WhatsApp
				</a>
			</div>
		</div>

		<div
			class="mt-10 border-t pt-6 text-center"
			style="border-color:rgba(255,255,255,0.06);color:rgba(255,255,255,0.2);font-size:0.7rem"
		>
			© 2025 Marwah Skincare Official Agent · AMAN · BPOM · HALAL · MUI
		</div>
	</div>
</footer>
"""

with open(r'r:/demo-client/clinic/src/routes/+page.svelte', 'w', encoding='utf-8') as f:
    f.write(content)

print("DONE: +page.svelte written successfully")
