<script lang="ts">
	import { Separator } from '$lib/components/ui/separator';

	// Assets from static/assets
	const heroImg = '/assets/hero.png';
	const keripikImg = '/assets/kerupuk.png';
	const rendangImg = '/assets/hero.png';
	const sambalImg = '/assets/pempek.png';

	import {
		Instagram,
		MapPin,
		Truck,
		ShieldCheck,
		UtensilsCrossed,
		ArrowRight,
		Star,
		MessageCircle,
		Menu,
		X,
		ShoppingBag,
		Heart,
		Camera,
		CheckCircle2,
		Award
	} from 'lucide-svelte';

	let menuOpen = $state(false);

	const stats = [
		{ value: '2.3K+', label: 'Followers' },
		{ value: '247', label: 'Postingan' },
		{ value: '100%', label: 'Homemade' },
		{ value: 'MUI', label: 'Halal Certified' }
	];

	const locations = [
		{ city: 'Padang', desc: 'Pusat Produksi' },
		{ city: 'Jakarta', desc: 'Distribusi Utama' },
		{ city: 'Bali', desc: 'Reseller Point' }
	];

	const features = [
		{
			icon: Camera,
			title: 'Real Pict',
			desc: 'Semua foto produk diambil langsung (Amora Food Original).'
		},
		{
			icon: Heart,
			title: 'Homemade',
			desc: 'Dibuat dengan kasih sayang menggunakan resep keluarga.'
		},
		{
			icon: Truck,
			title: 'Kirim Se-Indonesia',
			desc: 'Packaging double safety untuk kiriman antar pulau.'
		},
		{
			icon: ShieldCheck,
			title: 'Halal Certified',
			desc: 'Terjamin kebersihan dan kehalalan bahan baku.'
		}
	];

	const categories = [
		{ title: 'Rendang Daging', price: 'Premium', img: rendangImg },
		{ title: 'Keripik Sanjai', price: 'Best Seller', img: keripikImg },
		{ title: 'Aneka Sambal', price: 'Authentic', img: sambalImg }
	];
</script>

<svelte:head>
	<title>Amora Food PDG | Oleh-Oleh Khas Padang ✨</title>
	<meta name="description" content="Oleh-oleh khas Padang Homemade & Halal. Pengiriman seluruh Indonesia dari Padang, Jakarta, dan Bali." />
	<link
		href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<!-- ═══════ NAVBAR ═══════ -->
<header class="fixed inset-x-0 top-0 z-50 px-4 pt-4 md:px-8">
	<nav
		class="mx-auto max-w-7xl rounded-3xl border border-[#D97706]/10 backdrop-blur-xl transition-all"
		style="background:rgba(255,251,235,0.85); box-shadow: 0 10px 30px rgba(180,83,9,0.08)"
	>
		<div class="px-6 py-4">
			<div class="flex items-center justify-between">
				<!-- Logo -->
				<a href="/" class="flex items-center gap-3">
					<div class="flex h-11 w-11 items-center justify-center rounded-2xl bg-linear-to-br from-[#F59E0B] to-[#B45309] shadow-lg">
						<UtensilsCrossed class="h-6 w-6 text-white" />
					</div>
					<div>
						<div style="font-family:'Outfit',sans-serif;font-size:1.3rem;font-weight:800;color:#451A03;letter-spacing:-0.02em">
							Amora<span class="text-[#D97706]">Food</span>
						</div>
						<div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:0.6rem;font-weight:800;letter-spacing:0.15em;text-transform:uppercase;color:#92400E">
							Oleh-Oleh Khas Padang
						</div>
					</div>
				</a>

				<!-- Desktop Menu -->
				<div class="hidden items-center gap-8 md:flex">
					{#each ['Beranda', 'Produk', 'Lokasi', 'Order'] as link}
						<a href="#{link.toLowerCase()}" class="text-sm font-bold transition-colors hover:text-[#D97706]" style="color:#451A03">
							{link}
						</a>
					{/each}
				</div>

				<!-- CTA -->
				<div class="flex items-center gap-3">
					<a href="https://www.instagram.com/amorafoodpdg/" target="_blank" class="hidden sm:block">
						<button class="flex items-center gap-2 rounded-2xl bg-[#451A03] px-5 py-2.5 text-sm font-bold text-white transition-all hover:scale-105">
							<Instagram class="h-4 w-4" /> @amorafoodpdg
						</button>
					</a>
					<button 
						onclick={() => menuOpen = !menuOpen}
						class="rounded-xl bg-[#F59E0B]/10 p-2 text-[#B45309] md:hidden"
					>
						{#if menuOpen}<X class="h-6 w-6" />{:else}<Menu class="h-6 w-6" />{/if}
					</button>
				</div>
			</div>
		</div>

		<!-- Mobile Menu -->
		{#if menuOpen}
			<div class="border-t border-[#D97706]/10 p-6 md:hidden">
				<div class="flex flex-col gap-4">
					{#each ['Beranda', 'Produk', 'Lokasi', 'Order'] as link}
						<a href="#{link.toLowerCase()}" class="text-lg font-bold" style="color:#451A03">{link}</a>
					{/each}
					<a href="https://www.instagram.com/amorafoodpdg/" target="_blank" class="mt-4 flex w-full items-center justify-center gap-2 rounded-2xl bg-[#F59E0B] py-4 font-bold text-white">
						<Instagram class="h-5 w-5" /> Follow Our Instagram
					</a>
				</div>
			</div>
		{/if}
	</nav>
</header>

<main>
	<!-- ═══════ HERO SECTION ═══════ -->
	<section id="beranda" class="relative overflow-hidden pt-32 pb-20 md:pt-48 md:pb-32" style="background:#FFFBEB">
		<!-- Decorative Background -->
		<div class="absolute top-0 right-0 -mr-20 h-[600px] w-[600px] rounded-full opacity-30 blur-[120px]" style="background:#F59E0B"></div>
		<div class="absolute bottom-0 left-0 -ml-20 h-[500px] w-[500px] rounded-full opacity-20 blur-[100px]" style="background:#B45309"></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-1 items-center gap-16 lg:grid-cols-2">
				<!-- Text -->
				<div class="order-2 lg:order-1">
					<div class="mb-6 inline-flex items-center gap-2 rounded-full border border-[#D97706]/20 bg-[#F59E0B]/10 px-4 py-2">
						<CheckCircle2 class="h-4 w-4 text-[#D97706]" />
						<span class="text-xs font-black tracking-widest text-[#B45309] uppercase">Authentic & Homemade</span>
					</div>
					
					<h1 class="mb-8 leading-[1.1]" style="font-family:'Outfit',sans-serif; font-size:clamp(3rem, 8vw, 5.5rem); font-weight:800; color:#451A03">
						Bawa Pulang <br />
						<span class="relative">
							Cita Rasa
							<svg class="absolute -bottom-4 left-0 w-full" height="15" viewBox="0 0 300 15" fill="none" xmlns="http://www.w3.org/2000/svg">
								<path d="M2 13C50 3 150 3 298 13" stroke="#F59E0B" stroke-width="4" stroke-linecap="round"/>
							</svg>
						</span><br />
						<span class="text-[#D97706]">Padang Asli.</span>
					</h1>

					<p class="mb-10 max-w-lg text-lg leading-relaxed md:text-xl" style="font-family:'Plus Jakarta Sans',sans-serif; color:#78350F">
						Oleh-oleh premium khas Padang dengan resep turun-temurun. Kami hadir di <span class="font-bold underline decoration-[#F59E0B]">Padang, Jakarta, & Bali</span> untuk menemani kerinduan Anda.
					</p>

					<div class="flex flex-wrap gap-4">
						<a href="https://www.instagram.com/amorafoodpdg/" target="_blank" class="group flex items-center gap-3 rounded-2xl bg-[#451A03] px-8 py-5 text-lg font-bold text-white transition-all hover:scale-105 hover:shadow-2xl">
							Pesan Sekarang <ArrowRight class="transition-transform group-hover:translate-x-2" />
						</a>
						<div class="flex items-center gap-4 px-4">
							<div class="flex -space-x-3">
								{#each [1,2,3] as _}
									<div class="h-10 w-10 rounded-full border-2 border-white bg-[#F59E0B]"></div>
								{/each}
							</div>
							<div class="text-sm font-bold text-[#451A03]">
								2.3K+ Customers <br />
								<span class="text-[#B45309] opacity-70">Joined us</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Hero Image -->
				<div class="relative order-1 lg:order-2">
					<div class="relative z-10 mx-auto aspect-square w-full max-w-lg overflow-hidden rounded-[3rem] shadow-2xl border-8 border-white">
						<img src={heroImg} alt="Amora Food PDG" class="h-full w-full object-cover" />
						<!-- Floating Info -->
						<div class="absolute right-6 bottom-6 rounded-3xl bg-white/90 p-6 backdrop-blur-md shadow-xl border border-[#F59E0B]/20">
							<div class="flex items-center gap-4">
								<div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-[#F59E0B]">
									<Camera class="h-6 w-6 text-white" />
								</div>
								<div>
									<div class="text-xs font-black text-[#B45309] uppercase tracking-tighter">Photography</div>
									<div class="text-lg font-bold text-[#451A03]">100% Real Pict</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Background Shapes -->
					<div class="absolute -top-10 -left-10 h-40 w-40 rounded-full bg-[#F59E0B] opacity-20 blur-2xl"></div>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ STATS ═══════ -->
	<section class="relative z-20 -mt-10 px-4">
		<div class="mx-auto max-w-6xl rounded-[2.5rem] bg-[#451A03] p-8 shadow-2xl md:p-12">
			<div class="grid grid-cols-2 gap-8 md:grid-cols-4">
				{#each stats as s}
					<div class="text-center">
						<div class="text-3xl font-black text-[#F59E0B] md:text-5xl" style="font-family:'Outfit',sans-serif">
							{s.value}
						</div>
						<div class="mt-1 text-[0.65rem] font-black tracking-[0.2em] text-white/60 uppercase">
							{s.label}
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ LOKASI KAMI ═══════ -->
	<section id="lokasi" class="py-24" style="background:#FFFBEB">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mb-16 text-center">
				<h2 style="font-family:'Outfit',sans-serif; font-size:3rem; font-weight:800; color:#451A03">
					Tersedia di <span class="text-[#D97706]">3 Kota Utama</span>
				</h2>
				<p class="mx-auto mt-4 max-w-2xl text-[#78350F]">Kami mempermudah Anda mendapatkan stok oleh-oleh favorit dengan ketersediaan stok di Padang, Jakarta, dan Bali.</p>
			</div>

			<div class="grid grid-cols-1 gap-6 md:grid-cols-3">
				{#each locations as loc}
					<div class="group relative overflow-hidden rounded-3xl bg-white p-8 transition-all hover:-translate-y-2 hover:shadow-xl border border-[#D97706]/10">
						<div class="mb-6 flex h-14 w-14 items-center justify-center rounded-2xl bg-[#FFFBEB] text-[#D97706] group-hover:bg-[#F59E0B] group-hover:text-white transition-colors">
							<MapPin class="h-8 w-8" />
						</div>
						<h3 class="text-2xl font-bold text-[#451A03]">{loc.city}</h3>
						<p class="mt-2 text-[#78350F]">{loc.desc}</p>
						<div class="mt-6 flex items-center gap-2 text-sm font-bold text-[#D97706]">
							Lihat Detail <ArrowRight class="h-4 w-4" />
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ FEATURES ═══════ -->
	<section class="py-24" style="background:#FDF5E6">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-1 gap-12 lg:grid-cols-2 lg:items-center">
				<div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
					{#each features as feat}
						<div class="rounded-3xl bg-white p-8 shadow-sm border border-[#D97706]/5">
							<feat.icon class="mb-4 h-10 w-10 text-[#F59E0B]" />
							<h4 class="mb-2 text-lg font-bold text-[#451A03]">{feat.title}</h4>
							<p class="text-sm leading-relaxed text-[#78350F]">{feat.desc}</p>
						</div>
					{/each}
				</div>
				<div class="lg:pl-12">
					<h2 class="mb-6 leading-tight" style="font-family:'Outfit',sans-serif; font-size:3.5rem; font-weight:800; color:#451A03">
						Kenapa Harus <br /><span class="text-[#D97706]">Amora Food?</span>
					</h2>
					<p class="mb-8 text-lg text-[#78350F]">
						Kami menjaga kualitas setiap kemasan. Dari pemilihan bahan rempah segar hingga proses pengemasan yang aman untuk dikirim ke seluruh pelosok Indonesia.
					</p>
					<ul class="space-y-4">
						{#each ['Tanpa Bahan Pengawet', 'Bumbu Rempah Berlimpah', 'Packaging Double Sealed', 'Freshly Made Every Week'] as item}
							<li class="flex items-center gap-3 font-bold text-[#451A03]">
								<div class="flex h-6 w-6 items-center justify-center rounded-full bg-[#F59E0B] text-white">
									<CheckCircle2 class="h-4 w-4" />
								</div>
								{item}
							</li>
						{/each}
					</ul>
				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ PRODUCTS ═══════ -->
	<section id="produk" class="py-24" style="background:#FFFBEB">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mb-16 flex flex-col items-center text-center">
				<span class="text-xs font-black tracking-widest text-[#D97706] uppercase">Katalog Terfavorit</span>
				<h2 class="mt-4" style="font-family:'Outfit',sans-serif; font-size:3.5rem; font-weight:800; color:#451A03">
					Menu Unggulan <span class="italic text-[#B45309]">Amora</span>
				</h2>
			</div>

			<div class="grid grid-cols-1 gap-8 md:grid-cols-3">
				{#each categories as cat}
					<div class="group overflow-hidden rounded-[3rem] bg-white border border-[#D97706]/10 transition-all hover:shadow-2xl">
						<div class="relative aspect-[4/5] overflow-hidden">
							<img src={cat.img} alt={cat.title} class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-110" />
							<div class="absolute top-6 left-6 rounded-2xl bg-white/90 px-4 py-2 text-xs font-black text-[#B45309] shadow-sm">
								{cat.price}
							</div>
						</div>
						<div class="p-8 text-center">
							<h3 class="text-2xl font-bold text-[#451A03]">{cat.title}</h3>
							<p class="mt-2 text-sm text-[#78350F]">Authentic Minang Taste</p>
							<button class="mt-6 w-full rounded-2xl bg-[#FFFBEB] py-4 font-bold text-[#B45309] transition-all hover:bg-[#F59E0B] hover:text-white">
								Detail Produk
							</button>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ ORDER SECTION ═══════ -->
	<section id="order" class="py-24 px-4">
		<div class="mx-auto max-w-5xl rounded-[4rem] bg-linear-to-br from-[#F59E0B] to-[#B45309] p-12 text-center text-white shadow-2xl md:p-24">
			<h2 class="mb-8" style="font-family:'Outfit',sans-serif; font-size:clamp(2.5rem, 6vw, 4.5rem); font-weight:800">
				Siap Menikmati <br /> Kelezatan Padang?
			</h2>
			<p class="mx-auto mb-12 max-w-xl text-lg text-white/90 font-medium">
				Klik tombol di bawah untuk langsung terhubung dengan admin kami via WhatsApp atau katalog lengkap di Instagram.
			</p>
			<div class="flex flex-wrap justify-center gap-6">
				<a href="https://wa.me/628123456789" class="flex items-center gap-3 rounded-2xl bg-white px-10 py-5 text-lg font-bold text-[#B45309] transition-all hover:scale-105 shadow-xl">
					<MessageCircle class="h-6 w-6" /> Chat via WhatsApp
				</a>
				<a href="https://www.instagram.com/amorafoodpdg/" class="flex items-center gap-3 rounded-2xl border-2 border-white px-10 py-5 text-lg font-bold text-white transition-all hover:bg-white/10">
					<Instagram class="h-6 w-6" /> Instagram Feed
				</a>
			</div>
		</div>
	</section>
</main>

<!-- ═══════ FOOTER ═══════ -->
<footer class="py-20" style="background:#451A03">
	<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
		<div class="grid grid-cols-1 gap-16 md:grid-cols-3">
			<div>
				<div class="flex items-center gap-3 mb-6">
					<div class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#F59E0B]">
						<UtensilsCrossed class="h-5 w-5 text-white" />
					</div>
					<div class="text-2xl font-black text-white" style="font-family:'Outfit',sans-serif">
						Amora<span class="text-[#F59E0B]">Food</span>
					</div>
				</div>
				<p class="text-white/60 leading-relaxed">
					Oleh-oleh khas Padang Homemade & Halal Certified. Menghadirkan rasa otentik Minang ke seluruh Indonesia.
				</p>
			</div>
			
			<div class="text-white">
				<h4 class="mb-6 text-lg font-bold">Lokasi Kami</h4>
				<ul class="space-y-4 text-white/60">
					<li class="flex gap-3"><MapPin class="h-5 w-5 text-[#F59E0B] shrink-0" /> Padang (Produksi)</li>
					<li class="flex gap-3"><MapPin class="h-5 w-5 text-[#F59E0B] shrink-0" /> Jakarta (Distribusi)</li>
					<li class="flex gap-3"><MapPin class="h-5 w-5 text-[#F59E0B] shrink-0" /> Bali (Reseller)</li>
				</ul>
			</div>

			<div>
				<h4 class="mb-6 text-lg font-bold text-white">Hubungi Kami</h4>
				<div class="flex gap-4">
					{#each [Instagram, MessageCircle, Heart] as Icon}
						<a href="https://www.instagram.com/amorafoodpdg/" class="flex h-12 w-12 items-center justify-center rounded-2xl bg-white/5 text-white transition-all hover:bg-[#F59E0B] hover:scale-110">
							<Icon class="h-5 w-5" />
						</a>
					{/each}
				</div>
				<p class="mt-8 text-xs font-bold tracking-widest text-white/40 uppercase">
					© 2026 Amora Food PDG. All rights reserved.
				</p>
			</div>
		</div>
	</div>
</footer>

<style>
	:global(html) {
		scroll-behavior: smooth;
	}
	
	@keyframes float {
		0%, 100% { transform: translateY(0px); }
		50% { transform: translateY(-10px); }
	}
</style>
