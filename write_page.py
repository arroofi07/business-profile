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
		Clock,
		Heart,
		Gift,
		Sparkles
	} from 'lucide-svelte';

	let menuOpen = $state(false);

	const navLinks = [
		{ href: '#home', label: 'Beranda' },
		{ href: '#about', label: 'Tentang' },
		{ href: '#menu', label: 'Varian Menu' },
		{ href: '#order', label: 'Cara Pesan' },
		{ href: '#reviews', label: 'Review' }
	];

	const stats = [
		{ value: '6.8K+', label: 'Pengikut Instagram' },
		{ value: '223+', label: 'Varian & Postingan' },
		{ value: '100%', label: 'Bahan Premium' },
		{ value: 'Fresh', label: 'Dibuat Setiap Hari' }
	];

	const features = [
		{ icon: Sparkles, title: 'Bahan Premium', desc: 'Hanya menggunakan bahan berkualitas tinggi untuk rasa terbaik.' },
		{ icon: Heart, title: 'Tanpa Pengawet', desc: 'Aman dikonsumsi anak-anak hingga dewasa, selalu fresh.' },
		{ icon: Award, title: 'Rasa Juara', desc: 'Kombinasi tekstur lembut dan manis yang pas di lidah.' },
		{ icon: Gift, title: 'Cocok untuk Hampers', desc: 'Packaging cantik & aman untuk hantaran kerabat.' }
	];

	const products = [
		{
			category: 'Best Seller',
			title: 'Triple Chocolate Pudding',
			desc: 'Lapis coklat pekat, susu coklat, dan dark chocolate yang lumer di mulut.',
			image: 'https://images.unsplash.com/photo-1551024601-bec78aea704b?q=80&w=600&fit=crop'
		},
		{
			category: 'Segar & Sehat',
			title: 'Puding Buah Kaca Segar',
			desc: 'Puding bening berpadu dengan buah-buahan segar pilihan (Strawberry, Kiwi, Jeruk, Anggur).',
			image: 'https://images.unsplash.com/photo-1543880406-03f3ea4d8c8c?q=80&w=600&fit=crop'
		},
		{
			category: 'Gurih Manis',
			title: 'Puding Susu Keju Lumer',
			desc: 'Paduan keju premium dan susu segar murni yang memberikan sensasi creamy.',
			image: 'https://images.unsplash.com/photo-1563805042-7684c8e9e533?q=80&w=600&fit=crop'
		},
		{
			category: 'Pesta & Acara',
			title: 'Puding Tumpeng Mini',
			desc: 'Kreasi puding unik berbentuk tumpeng, sangat cocok untuk acara perayaan dan syukuran.',
			image: 'https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?q=80&w=600&fit=crop'
		},
		{
			category: 'Cemilan Praktis',
			title: 'Dessert Cup Varian',
			desc: 'Puding cup mini aneka rasa yang sangat simpel dibawa dan dinikmati kapan saja.',
			image: 'https://images.unsplash.com/photo-1587314168485-3236d6710814?q=80&w=600&fit=crop'
		},
		{
			category: 'Hampers Spesial',
			title: 'Premium Gift Box',
			desc: 'Pilihan puding eksklusif dalam boks cantik yang dilengkapi dengan pita dan kartu ucapan.',
			image: 'https://images.unsplash.com/photo-1577907575239-166e4a2e584a?q=80&w=600&fit=crop'
		}
	];

	const reviews = [
		{
			name: 'Rina S.',
			initial: 'RS',
			time: '1 minggu lalu',
			stars: 5,
			text: 'Selalu pesan di Azzalea Pudding buat acara arisan. Semua tamu bilang enak, teksturnya lembut dan fla-nya juara banget!'
		},
		{
			name: 'Aulia Rahman',
			initial: 'AR',
			time: '3 minggu lalu',
			stars: 5,
			text: 'Puding buahnya seger banget, buahnya melimpah gak pelit. Packing aman sampai tujuan nggak hancur.'
		},
		{
			name: 'Mutiara',
			initial: 'M',
			time: '1 bulan lalu',
			stars: 5,
			text: 'Pelopor puding nomor 1 di Padang emang the best. Nggak pernah kecewa, langganan tetap!'
		}
	];
</script>

<svelte:head>
	<title>Azzalea Pudding | Pelopor Puding No. 1 di Padang</title>
	<meta
		name="description"
		content="Azzalea Pudding – Pelopor puding eksklusif di Padang. Menjaga kualitas rasa hingga ke tangan kamu. Pesan dan rasakan kelembutannya!"
	/>
	<link
		href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Nunito:wght@400;500;600;700;800&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<!-- ═══════ NAVBAR ═══════ -->
<header class="fixed inset-x-0 top-0 z-50">
	<nav
		class="border-b backdrop-blur-md transition-all"
		style="background:rgba(255,253,245,0.92);border-color:rgba(224,122,95,0.15);box-shadow:0 4px 20px rgba(90,62,42,0.06)"
	>
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="flex h-20 items-center justify-between">

				<!-- Logo -->
				<a href="#home" class="group flex items-center gap-3">
					<div
						class="flex h-11 w-11 items-center justify-center rounded-2xl transition-transform duration-300 group-hover:rotate-12 group-hover:scale-110"
						style="background:linear-gradient(135deg,#F4A261,#E76F51);box-shadow:0 6px 15px rgba(231,111,81,0.3)"
					>
						<span style="font-family:'Fredoka',sans-serif;font-size:1.6rem;font-weight:700;color:#FFFBF0">A</span>
					</div>
					<div class="leading-tight">
						<div style="font-family:'Fredoka',sans-serif;font-size:1.3rem;font-weight:700;color:#3D261A">
							Azzalea<span style="color:#E76F51">.Pudding</span>
						</div>
						<div style="font-family:'Nunito',sans-serif;font-size:0.65rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;color:#D4A373">
							Padang, Indonesia
						</div>
					</div>
				</a>

				<!-- Desktop Nav -->
				<div class="hidden items-center gap-2 md:flex">
					{#each navLinks as link}
						<a
							href={link.href}
							class="group relative rounded-full px-5 py-2 text-[0.9rem] font-bold transition-all duration-200"
							style="font-family:'Nunito',sans-serif;color:#5A3E2A"
						>
							{link.label}
							<span
								class="absolute bottom-1.5 left-1/2 h-1 w-0 -translate-x-1/2 rounded-full opacity-80 transition-all duration-300 group-hover:w-5"
								style="background:#E76F51"
							></span>
						</a>
					{/each}
				</div>

				<!-- CTA -->
				<div class="hidden items-center gap-4 md:flex">
					<div
						class="flex items-center gap-2 rounded-full border px-3 py-1.5"
						style="border-color:rgba(231,111,81,0.3);color:#E76F51;font-size:0.7rem;font-weight:800;font-family:'Nunito',sans-serif"
					>
						<Heart class="h-3.5 w-3.5" /> 100% Homemade
					</div>
					<a href="https://wa.me/6281378454700" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-11 items-center gap-2 rounded-full px-6 text-[0.95rem] font-bold text-white transition-all hover:-translate-y-1 hover:shadow-xl"
							style="font-family:'Nunito',sans-serif;background:linear-gradient(135deg,#F4A261,#E76F51);box-shadow:0 6px 20px rgba(231,111,81,0.35);color:#FFFDF2"
						>
							<MessageCircle class="h-4.5 w-4.5" /> Pesan Sekarang
						</button>
					</a>
				</div>

				<!-- Mobile Toggle -->
				<button
					onclick={() => (menuOpen = !menuOpen)}
					class="rounded-xl p-2 transition hover:bg-orange-50 md:hidden"
					style="color:#3D261A"
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
				style="background:#FFFDF5;border-color:rgba(231,111,81,0.15)"
			>
				{#each navLinks as link}
					<a
						href={link.href}
						onclick={() => (menuOpen = false)}
						class="flex items-center gap-3 rounded-2xl px-5 py-3.5 text-base font-bold transition hover:bg-orange-50"
						style="font-family:'Nunito',sans-serif;color:#5A3E2A"
					>
						{link.label}
					</a>
				{/each}
				<div class="mt-4 border-t pt-5" style="border-color:rgba(231,111,81,0.15)">
					<a href="https://wa.me/6281378454700" target="_blank" rel="noopener noreferrer">
						<button
							class="flex h-12 w-full items-center justify-center gap-2 rounded-2xl text-base font-bold shadow-lg"
							style="font-family:'Nunito',sans-serif;background:linear-gradient(135deg,#F4A261,#E76F51);color:#FFFDF2"
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
		class="relative min-h-[90vh] overflow-hidden flex items-center"
		style="background:linear-gradient(180deg,#FFFDF5 0%,#FFF0E5 100%)"
	>
		<!-- Decorative blobs (soft pastel food themes) -->
		<div
			class="pointer-events-none absolute -top-20 -left-20 h-[600px] w-[600px] opacity-40 mix-blend-multiply"
			style="background:radial-gradient(ellipse,#FFE5D9 0%,transparent 70%);filter:blur(50px)"
		></div>
		<div
			class="pointer-events-none absolute bottom-0 right-0 h-[500px] w-[500px] opacity-50 mix-blend-multiply"
			style="background:radial-gradient(circle,#F4A261 0%,transparent 65%);filter:blur(60px)"
		></div>
		
		<!-- Floating elements (optional CSS decor) -->
		<div class="absolute inset-0 pointer-events-none overflow-hidden">
			<div class="absolute top-[20%] left-[10%] opacity-20" style="color:#E76F51">
				<svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor" class="animate-bounce-slow"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
			</div>
			<div class="absolute bottom-[30%] right-[15%] opacity-30" style="color:#F4A261">
				<svg width="50" height="50" viewBox="0 0 24 24" fill="currentColor" class="animate-float"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/></svg>
			</div>
		</div>

		<div
			class="relative mx-auto w-full max-w-7xl px-4 pb-20 pt-16 sm:px-6 lg:grid lg:grid-cols-12 lg:gap-10 lg:px-8 lg:pt-20 lg:pb-28"
		>
			<!-- Left text -->
			<div class="animate-slide-up z-10 lg:col-span-6 flex flex-col justify-center space-y-7">

				<!-- Tag pill -->
				<div
					class="inline-flex items-center gap-2.5 self-start rounded-full px-4 py-2 border-2"
					style="border-color:rgba(231,111,81,0.3);background:rgba(255,255,255,0.7);backdrop-filter:blur(4px)"
				>
					<span class="flex h-3 w-3 items-center justify-center">
						<span class="absolute inline-flex h-2.5 w-2.5 animate-ping rounded-full" style="background:#E76F51;opacity:0.6"></span>
						<span class="relative inline-flex h-2 w-2 rounded-full" style="background:#E76F51"></span>
					</span>
					<span style="font-family:'Nunito',sans-serif;font-size:0.75rem;font-weight:800;letter-spacing:0.08em;text-transform:uppercase;color:#D4A373">
						Ratulangi, Padang
					</span>
				</div>

				<!-- Heading -->
				<div class="animate-slide-up delay-100">
					<h1
						style="font-family:'Fredoka',sans-serif;font-size:clamp(3.5rem,6.5vw,5.5rem);line-height:1.1;color:#3D261A"
					>
						Pelopor<br />
						<span class="relative inline-block">
							<span class="relative z-10" style="color:#E76F51">Puding No. 1</span>
							<span class="absolute -bottom-2 left-0 -z-10 h-6 w-full rounded-full opacity-30" style="background:#F4A261"></span>
						</span><br />
						<span style="font-size:0.65em;color:#5A3E2A">di Padang 🌟</span>
					</h1>
				</div>

				<p class="animate-slide-up max-w-lg text-[1.1rem] leading-relaxed delay-200" style="font-family:'Nunito',sans-serif;color:#5A3E2A">
					Menjaga Kualitas Pudding hingga ke tangan kamu. Manis yang pas, tekstur selembut sutra, dan dibuat <strong style="color:#E76F51">fresh setiap hari</strong> menggunakan bahan premium pilihan.
				</p>

				<!-- CTA -->
				<div class="animate-slide-up flex flex-wrap gap-4 pt-2 delay-300">
					<a href="https://wa.me/6281378454700" target="_blank" rel="noopener noreferrer">
						<button
							class="group flex h-14 items-center gap-2.5 rounded-full px-8 text-base font-bold transition-all hover:scale-105"
							style="font-family:'Nunito',sans-serif;background:linear-gradient(135deg,#E76F51,#D48128);color:white;box-shadow:0 10px 25px rgba(231,111,81,0.4)"
						>
							<ShoppingBag class="h-5 w-5 transition-transform group-hover:-translate-y-1 group-hover:rotate-6" /> Pesan Pudingmu
						</button>
					</a>
					<a href="#menu">
						<button
							class="flex h-14 items-center gap-2.5 rounded-full border-2 px-8 text-base font-bold transition-all hover:bg-white"
							style="font-family:'Nunito',sans-serif;border-color:rgba(231,111,81,0.4);color:#3D261A"
						>
							Lihat Menu Puding
						</button>
					</a>
				</div>
				
				<div class="animate-slide-up flex gap-5 pt-4 delay-400">
					<div class="flex -space-x-3">
						<img src="https://i.pravatar.cc/100?img=1" alt="User 1" class="h-10 w-10 rounded-full border-2 border-white object-cover" />
						<img src="https://i.pravatar.cc/100?img=5" alt="User 2" class="h-10 w-10 rounded-full border-2 border-white object-cover" />
						<img src="https://i.pravatar.cc/100?img=9" alt="User 3" class="h-10 w-10 rounded-full border-2 border-white object-cover" />
						<div class="flex h-10 w-10 items-center justify-center rounded-full border-2 border-white bg-orange-100 text-xs font-bold text-orange-600">
							+1K
						</div>
					</div>
					<div class="flex flex-col justify-center">
						<div class="flex items-center gap-1 text-sm text-yellow-500">
							<Star class="h-4 w-4 fill-current" />
							<Star class="h-4 w-4 fill-current" />
							<Star class="h-4 w-4 fill-current" />
							<Star class="h-4 w-4 fill-current" />
							<Star class="h-4 w-4 fill-current" />
						</div>
						<div class="text-xs font-bold" style="font-family:'Nunito',sans-serif;color:#5A3E2A">
							Azzalea lovers
						</div>
					</div>
				</div>

			</div>

			<!-- Right image -->
			<div class="animate-slide-left relative mt-16 lg:col-span-6 lg:mt-0 delay-200">
				<div class="relative pl-8 pr-4 lg:pl-12">
					<!-- Blob bg -->
					<div
						class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 rounded-full opacity-20"
						style="width: 120%; height: 120%; background:radial-gradient(circle,#F4A261,transparent 65%); z-index: 0;"
					></div>

					<!-- Main Image Layout with organic shape -->
					<div class="relative z-10 mx-auto w-full max-w-[500px]">
						<div
							class="relative overflow-hidden"
							style="border-radius:45% 55% 40% 60% / 55% 45% 60% 40%; border:12px solid #FFFDF5; box-shadow:0 30px 60px -15px rgba(231,111,81,0.3)"
						>
							<img
								src="https://images.unsplash.com/photo-1543880406-03f3ea4d8c8c?q=80&w=800&auto=format&fit=crop"
								alt="Puding Buah Segar Azzalea"
								class="w-full object-cover transition-transform duration-700 hover:scale-110 hover:rotate-2"
								style="aspect-ratio:3/4"
							/>
						</div>
					</div>

					<!-- Float card: Instagram -->
					<a href="https://instagram.com/azzalea.pudding" target="_blank" rel="noopener noreferrer">
						<div
							class="absolute -left-2 top-24 z-20 rounded-2xl p-3 shadow-xl backdrop-blur-md transition-transform hover:scale-105 lg:-left-6"
							style="background:rgba(255,255,255,0.9); animation: float 6s ease-in-out infinite;"
						>
							<div class="flex items-center gap-3 pr-3">
								<div
									class="flex h-12 w-12 items-center justify-center rounded-xl text-white shadow-md"
									style="background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888)"
								>
									<Instagram class="h-6 w-6" />
								</div>
								<div>
									<div style="font-family:'Fredoka',sans-serif;font-size:1.1rem;color:#3D261A;line-height:1">6,848</div>
									<div style="font-family:'Nunito',sans-serif;font-size:0.75rem;font-weight:700;color:#E76F51">Followers Ig</div>
								</div>
							</div>
						</div>
					</a>

					<!-- Float card: Jam buka -->
					<div
						class="absolute -bottom-6 right-0 z-20 rounded-2xl p-4 shadow-xl backdrop-blur-md text-center lg:right-4"
						style="background:rgba(255,255,255,0.9); animation: float 7s ease-in-out infinite reverse;"
					>
						<div class="flex items-center gap-2 justify-center mb-1">
							<Clock class="h-4 w-4" style="color:#F4A261" />
							<span style="font-family:'Nunito',sans-serif;font-size:0.7rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;color:#F4A261">Jam Buka</span>
						</div>
						<div style="font-family:'Fredoka',sans-serif;font-size:1.2rem;color:#3D261A">09.00 - 18.00</div>
						<div style="font-family:'Nunito',sans-serif;font-size:0.75rem;font-weight:700;color:#5A3E2A">Setiap Hari</div>
					</div>
				</div>
			</div>
		</div>

		<!-- Cute wavy divider -->
		<div class="absolute bottom-0 w-full overflow-hidden leading-none z-10" style="transform: translateY(1px);">
			<svg viewBox="0 0 1200 120" preserveAspectRatio="none" style="display:block; width:100%; height:60px;">
				<path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V95.8C59.71,118.08,130.83,120.22,192.39,106.67,246.42,94.66,303.45,71.29,321.39,56.44Z" fill="#FFFDF5"></path>
			</svg>
		</div>
	</section>

	<style>
		@keyframes float {
			0% { transform: translateY(0px); }
			50% { transform: translateY(-15px); }
			100% { transform: translateY(0px); }
		}
		.animate-float {
			animation: float 5s ease-in-out infinite;
		}
		.animate-bounce-slow {
			animation: bounce 3s infinite;
		}
		/* Blob shapes */
		.blob-shape {
			border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
		}
	</style>

	<!-- ═══════ STATS ═══════ -->
	<section class="py-12 relative z-20" style="background:#FFFDF5">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-2 gap-4 md:grid-cols-4 lg:gap-8">
				{#each stats as s}
					<div class="flex flex-col items-center justify-center p-6 text-center rounded-3xl" style="background:rgba(244,162,97,0.08)">
						<div
							style="font-family:'Fredoka',sans-serif;font-size:2.2rem;font-weight:600;color:#E76F51"
						>
							{s.value}
						</div>
						<div class="mt-1" style="font-family:'Nunito',sans-serif;font-size:0.8rem;font-weight:800;letter-spacing:0.05em;color:#D48128">
							{s.label}
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

	<!-- ═══════ ABOUT / TENTANG ═══════ -->
	<section id="about" class="relative overflow-hidden py-24" style="background:#FFFDF5">
		<!-- Decorative elements -->
		<div class="absolute right-0 top-1/4 h-64 w-64 -translate-y-1/2 translate-x-1/2 rounded-full opacity-20" style="background:#F4A261; filter:blur(40px)"></div>
		<div class="absolute left-0 bottom-1/4 h-80 w-80 translate-y-1/2 -translate-x-1/2 rounded-full opacity-10" style="background:#E76F51; filter:blur(50px)"></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="grid grid-cols-1 items-center gap-16 lg:grid-cols-2">

				<!-- Image side -->
				<div class="relative order-2 lg:order-1">
					<div class="relative z-10 mx-auto w-full max-w-md">
						<div class="relative overflow-hidden shadow-2xl blob-shape" style="border:10px solid white">
							<img
								src="https://images.unsplash.com/photo-1551024601-bec78aea704b?q=80&w=600&auto=format&fit=crop"
								alt="Kenikmatan Puding"
								class="w-full object-cover transition-transform duration-700 hover:scale-105"
								style="aspect-ratio:4/5"
							/>
						</div>
						<!-- Small overlay image -->
						<div class="absolute -bottom-8 -right-8 z-20 overflow-hidden shadow-xl rounded-[2.5rem] border-8 border-white hidden md:block" style="width:200px; height:200px; background:#FFF0E5">
							<img
								src="https://images.unsplash.com/photo-1587314168485-3236d6710814?q=80&w=300&auto=format&fit=crop"
								alt="Dessert Cup"
								class="h-full w-full object-cover"
							/>
						</div>
						<!-- Trust Badge -->
						<div class="absolute -top-6 -left-6 z-20 flex h-28 w-28 flex-col items-center justify-center rounded-full shadow-lg" style="background:linear-gradient(135deg,#F4A261,#E76F51); color:white; border:4px solid white; transform: rotate(-10deg)">
							<Award class="h-8 w-8 mb-1" />
							<span style="font-family:'Fredoka',sans-serif;font-size:0.9rem;font-weight:600;line-height:1">100%</span>
							<span style="font-family:'Nunito',sans-serif;font-size:0.6rem;font-weight:800;letter-spacing:0.05em">PREMIUM</span>
						</div>
					</div>
				</div>

				<!-- Text side -->
				<div class="order-1 flex flex-col justify-center lg:order-2">
					<div class="mb-4 inline-flex items-center gap-3">
						<span class="h-2 w-8 rounded-full" style="background:#F4A261"></span>
						<span style="font-family:'Nunito',sans-serif;font-size:0.85rem;font-weight:800;letter-spacing:0.15em;text-transform:uppercase;color:#E76F51">Kenalan dengan Azzalea</span>
					</div>

					<h2
						class="mb-6"
						style="font-family:'Fredoka',sans-serif;font-size:clamp(2.5rem,4vw,3.5rem);line-height:1.15;color:#3D261A"
					>
						Manis yang Pas,<br />
						<span style="color:#E76F51">Lembut di Setiap Gigitan</span>
					</h2>

					<p class="mb-8 text-lg" style="font-family:'Nunito',sans-serif;color:#5A3E2A;line-height:1.7">
						Kami mengerti bahwa hidangan penutup bukan sekadar makanan, melainkan momen bahagia. 
						<strong style="color:#E76F51">Azzalea.Pudding</strong> hadir untuk menemani hari-hari spesial, acara keluarga, hingga cemilan soremu dengan rasa juara yang tak terlupakan.
					</p>

					<div class="grid grid-cols-1 sm:grid-cols-2 gap-5 mb-10">
						{#each features as f}
							<div class="flex items-start gap-4 p-4 rounded-3xl transition-transform hover:-translate-y-1" style="background:rgba(255,240,229,0.5)">
								<div class="mt-1 flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl text-white shadow-sm" style="background:#F4A261">
									<svelte:component this={f.icon} class="h-6 w-6" />
								</div>
								<div>
									<h4 class="mb-1 text-[1.05rem]" style="font-family:'Fredoka',sans-serif;color:#3D261A">{f.title}</h4>
									<p class="text-[0.85rem] leading-snug" style="font-family:'Nunito',sans-serif;color:#5A3E2A">{f.desc}</p>
								</div>
							</div>
						{/each}
					</div>

				</div>
			</div>
		</div>
	</section>

	<!-- ═══════ MENU PUDING ═══════ -->
	<section id="menu" class="relative py-28" style="background:linear-gradient(180deg,#FFF0E5 0%,#FFFDF5 100%)">
		<!-- Section background texture -->
		<div class="absolute inset-0 opacity-[0.03]" style="background-image: radial-gradient(#E76F51 2px, transparent 2px); background-size: 30px 30px;"></div>

		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<!-- Header -->
			<div class="mb-16 flex flex-col items-center text-center">
				<div class="mb-4 inline-flex items-center gap-3">
					<span class="h-2 w-8 rounded-full" style="background:#F4A261"></span>
					<span style="font-family:'Nunito',sans-serif;font-size:0.85rem;font-weight:800;letter-spacing:0.15em;text-transform:uppercase;color:#E76F51">Pilihan Menu Terbaik</span>
					<span class="h-2 w-8 rounded-full" style="background:#F4A261"></span>
				</div>
				<h2
					class="mx-auto max-w-2xl"
					style="font-family:'Fredoka',sans-serif;font-size:clamp(2.5rem,4vw,3.5rem);line-height:1.2;color:#3D261A"
				>
					Varian Puding Favorit <em class="not-italic" style="color:#E76F51">Pelanggan Kami</em>
				</h2>
			</div>

			<!-- Product Grid -->
			<div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
				{#each products as prod}
					<div
						class="group flex flex-col overflow-hidden rounded-[2rem] bg-white transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl"
						style="box-shadow: 0 10px 30px rgba(90,62,42,0.06); border: 1px solid rgba(244,162,97,0.1)"
					>
						<div class="relative overflow-hidden aspect-[4/3]">
							<img
								src={prod.image}
								alt={prod.title}
								class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-110"
							/>
							<div class="absolute top-4 right-4 z-10 rounded-full px-4 py-1.5 shadow-md backdrop-blur-md" style="background:rgba(255,255,255,0.95)">
								<span style="font-family:'Nunito',sans-serif;font-size:0.75rem;font-weight:800;letter-spacing:0.05em;color:#E76F51;text-transform:uppercase">{prod.category}</span>
							</div>
						</div>
						<div class="flex flex-1 flex-col p-8 text-center bg-white relative">
							<!-- Decorative separator -->
							<div class="absolute -top-4 left-1/2 flex h-8 w-16 -translate-x-1/2 items-center justify-center rounded-full bg-white shadow-sm z-20">
								<Heart class="h-4 w-4" style="color:#F4A261" />
							</div>
							
							<div class="mt-2 flex-1">
								<h3
									class="mb-3 text-[1.4rem]"
									style="font-family:'Fredoka',sans-serif;color:#3D261A"
								>
									{prod.title}
								</h3>
								<p style="font-family:'Nunito',sans-serif;font-size:0.95rem;color:#5A3E2A;line-height:1.6">
									{prod.desc}
								</p>
							</div>
							
							<div class="mt-6">
								<a href="https://wa.me/6281378454700?text=Halo%20Admin,%20saya%20tertarik%20dengan%20{prod.title}" target="_blank" rel="noopener noreferrer">
									<button
										class="w-full rounded-2xl py-3 text-[0.95rem] font-bold transition-colors hover:text-white bg-[#E76F51]/10 text-[#E76F51] hover:bg-[#E76F51]"
										style="font-family:'Nunito',sans-serif"
									>
										Tanya Harga / Pesan WA
									</button>
								</a>
							</div>
						</div>
					</div>
				{/each}
			</div>
			
			<div class="mt-16 text-center">
				<a href="https://instagram.com/azzalea.pudding" target="_blank" rel="noopener noreferrer">
					<button
						class="inline-flex h-14 items-center gap-3 rounded-full border-2 bg-transparent px-10 font-bold transition-all hover:scale-105"
						style="font-family:'Nunito',sans-serif;border-color:#F4A261;color:#D48128"
					>
						<Instagram class="h-5 w-5" /> Lihat Menu Lengkap di IG
					</button>
				</a>
			</div>
		</div>
	</section>

	<!-- ═══════ CARA ORDER & INFO ═══════ -->
	<section id="order" class="py-24" style="background:#FFFDF5">
		<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			
			<div class="grid lg:grid-cols-12 gap-12 items-center">
				
				<!-- Left: Cara Order Steps -->
				<div class="lg:col-span-7">
					<div class="mb-10">
						<span style="font-family:'Nunito',sans-serif;font-size:0.85rem;font-weight:800;letter-spacing:0.15em;text-transform:uppercase;color:#E76F51">Mudahkan Belanjamu</span>
						<h2
							class="mt-2"
							style="font-family:'Fredoka',sans-serif;font-size:clamp(2rem,4vw,3rem);color:#3D261A;line-height:1.2"
						>
							Cara Beli & Pesan<br>Azzalea Pudding
						</h2>
					</div>
					
					<div class="space-y-6">
						{#each [
							{ num: '1', title: 'Hubungi WhatsApp / DM IG', desc: 'Sampaikan varian puding dan ukuran yang ingin kamu pesan.' },
							{ num: '2', title: 'Konfirmasi Pesanan', desc: 'Admin akan mengecek ketersediaan / jadwal pembuatan, lalu memberikan total harga & ongkir.' },
							{ num: '3', title: 'Transfer & Tunggu', desc: 'Lakukan pembayaran. Puding siap dikurir ke alamatmu atau bisa dipick-up langsung!' }
						] as step}
							<div class="flex items-start gap-6 p-6 rounded-[2rem] bg-white transition hover:shadow-lg hover:-translate-y-1" style="box-shadow:0 10px 25px rgba(90,62,42,0.04); border:1px solid rgba(244,162,97,0.1)">
								<div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-full text-xl shadow-md" style="font-family:'Fredoka',sans-serif;background:linear-gradient(135deg,#F4A261,#E76F51);color:white">
									{step.num}
								</div>
								<div class="pt-1">
									<h3 style="font-family:'Fredoka',sans-serif;font-size:1.3rem;color:#3D261A;margin-bottom:0.2rem">{step.title}</h3>
									<p style="font-family:'Nunito',sans-serif;color:#5A3E2A">{step.desc}</p>
								</div>
							</div>
						{/each}
					</div>
				</div>
				
				<!-- Right: Info Lokasi & Jam Buka Banner -->
				<div class="lg:col-span-5">
					<div class="relative overflow-hidden rounded-[2.5rem] bg-white p-10 text-center shadow-2xl" style="border:1px solid rgba(224,122,95,0.2)">
						<!-- Bg decorator -->
						<div class="absolute -top-20 -right-20 h-48 w-48 rounded-full opacity-10" style="background:#E76F51"></div>
						<div class="absolute -bottom-20 -left-20 h-48 w-48 rounded-full opacity-10" style="background:#F4A261"></div>
						
						<div class="relative z-10 flex flex-col items-center gap-8">
							<!-- Jam Operasional -->
							<div class="flex flex-col items-center">
								<div class="flex h-16 w-16 items-center justify-center rounded-2xl mb-4" style="background:rgba(244,162,97,0.1);color:#D48128">
									<Clock class="h-8 w-8" />
								</div>
								<div style="font-family:'Nunito',sans-serif;font-size:0.8rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;color:#D4A373;margin-bottom:0.5rem">Jam Buka</div>
								<div style="font-family:'Fredoka',sans-serif;font-size:1.8rem;color:#3D261A">09.00 - 18.00</div>
								<div style="font-family:'Nunito',sans-serif;font-size:1rem;color:#5A3E2A;font-weight:600">Buka Setiap Hari</div>
							</div>
							
							<div class="h-px w-full" style="background:linear-gradient(90deg,transparent,rgba(224,122,95,0.3),transparent)"></div>
							
							<!-- Lokasi -->
							<div class="flex flex-col items-center">
								<div class="flex h-16 w-16 items-center justify-center rounded-2xl mb-4" style="background:rgba(231,111,81,0.1);color:#E76F51">
									<svg xmlns="http://www.ourage.com/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-map-pin"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 15 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/></svg>
								</div>
								<div style="font-family:'Nunito',sans-serif;font-size:0.8rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;color:#D4A373;margin-bottom:0.5rem">Lokasi Kami</div>
								<div style="font-family:'Fredoka',sans-serif;font-size:1.4rem;color:#3D261A">Ratulangi, Padang</div>
								<div style="font-family:'Nunito',sans-serif;font-size:0.95rem;color:#5A3E2A" class="mt-2 text-center max-w-[200px]">
									Tersedia layanan Pick-Up atau Delivery area Padang.
								</div>
							</div>
							
							<a href="https://wa.me/6281378454700" target="_blank" rel="noopener noreferrer" class="w-full mt-4">
								<button class="w-full flex justify-center items-center gap-2 h-14 rounded-full text-white text-lg font-bold shadow-lg transition hover:-translate-y-1 hover:shadow-xl" style="font-family:'Nunito',sans-serif;background:linear-gradient(135deg,#F4A261,#E76F51)">
									<Phone class="h-5 w-5" /> Hubungi Kami
								</button>
							</a>
						</div>
					</div>
				</div>
			</div>
			
		</div>
	</section>

	<!-- ═══════ REVIEWS ═══════ -->
	<section id="reviews" class="relative py-24" style="background:#FFF0E5">
		<!-- Decorative blobs for warm feeling -->
		<div class="absolute inset-0 z-0 opacity-[0.2]" style="background:radial-gradient(circle at 50% 100%, #F4A261 0%, transparent 70%);"></div>
		
		<div class="relative z-10 mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">

			<div class="mb-14 text-center">
				<h2
					style="font-family:'Fredoka',sans-serif;font-size:clamp(2rem,4vw,3.2rem);color:#3D261A;line-height:1.2"
				>
					Apa Kata <span style="color:#E76F51">Penikmat Azzalea?</span>
				</h2>
				<p class="mt-4" style="font-family:'Nunito',sans-serif;font-size:1.1rem;color:#5A3E2A">Ribuan cuapan bahagia dari pelanggan setia kami.</p>
			</div>

			<div class="grid grid-cols-1 gap-6 md:grid-cols-3">
				{#each reviews as rv}
					<div
						class="flex flex-col rounded-[2rem] bg-white p-8 transition-transform hover:-translate-y-2 hover:shadow-2xl"
						style="box-shadow:0 15px 35px rgba(231,111,81,0.06)"
					>
						<div class="mb-4 flex gap-1">
							{#each Array(rv.stars) as _}
								<Star class="h-5 w-5 fill-current" style="color:#F4A261" />
							{/each}
						</div>
						<p class="mb-8 flex-1 text-[1.05rem] italic leading-relaxed" style="font-family:'Nunito',sans-serif;color:#5A3E2A">"{rv.text}"</p>
						
						<div class="flex items-center gap-4">
							<div
								class="flex h-12 w-12 items-center justify-center rounded-full text-[1.1rem] font-bold"
								style="font-family:'Fredoka',sans-serif;background:linear-gradient(135deg,#F4A261,#E76F51);color:white"
							>
								{rv.initial}
							</div>
							<div>
								<div class="text-[1.1rem]" style="font-family:'Fredoka',sans-serif;color:#3D261A">{rv.name}</div>
								<div style="font-family:'Nunito',sans-serif;font-size:0.8rem;color:#D4A373">{rv.time}</div>
							</div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</section>

</main>

<!-- ═══════ FOOTER ═══════ -->
<footer style="background:#3D261A; border-top:5px solid #E76F51">
	<div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8">
		<div class="grid grid-cols-1 md:grid-cols-3 gap-12 text-center md:text-left">
			
			<!-- Brand -->
			<div class="flex flex-col items-center md:items-start gap-4">
				<a href="#home" class="flex items-center gap-3">
					<div
						class="flex h-10 w-10 items-center justify-center rounded-xl"
						style="background:linear-gradient(135deg,#F4A261,#E76F51)"
					>
						<span style="font-family:'Fredoka',sans-serif;font-size:1.4rem;color:white">A</span>
					</div>
					<div class="text-2xl" style="font-family:'Fredoka',sans-serif;color:white">Azzalea<span style="color:#F4A261">.Pudding</span></div>
				</a>
				<p style="font-family:'Nunito',sans-serif;font-size:0.95rem;color:#D4A373;line-height:1.6;max-width:300px">
					Pelopor Puding no. 1 di Padang 🌟. Menghadirkan porsi kenikmatan manis, lembut, dan selalu fresh untuk memeriahkan harimu.
				</p>
			</div>

			<!-- Links -->
			<div class="flex flex-col items-center md:items-start gap-3">
				<div style="font-family:'Nunito',sans-serif;font-size:0.9rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;color:#F4A261;margin-bottom:0.5rem">Hubungi Biz</div>
				<div class="flex items-center gap-3 text-white">
					<Phone class="h-4 w-4" style="color:#D48128" />
					<span style="font-family:'Nunito',sans-serif;font-size:1rem">0813-7845-4700</span>
				</div>
				<div class="flex items-center gap-3 text-white">
					<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-map-pin" style="color:#D48128"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 15 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/></svg>
					<span style="font-family:'Nunito',sans-serif;font-size:1rem">Ratulangi, Padang</span>
				</div>
			</div>

			<!-- Social -->
			<div class="flex flex-col items-center md:items-start gap-4">
				<div style="font-family:'Nunito',sans-serif;font-size:0.9rem;font-weight:800;letter-spacing:0.1em;text-transform:uppercase;color:#F4A261;margin-bottom:0.1rem">Ikuti Kami</div>
				<a
					href="https://instagram.com/azzalea.pudding"
					target="_blank"
					rel="noopener noreferrer"
					class="flex items-center gap-3 rounded-full bg-white/5 pr-6 p-2 transition-colors hover:bg-white/10"
				>
					<div class="flex h-10 w-10 items-center justify-center rounded-full bg-gradient-to-tr from-yellow-400 via-orange-500 to-pink-500 text-white">
						<Instagram class="h-5 w-5" />
					</div>
					<span style="font-family:'Nunito',sans-serif;color:white;font-weight:600">@azzalea.pudding</span>
				</a>
			</div>
		</div>

		<div
			class="mt-14 border-t pt-8 text-center"
			style="border-color:rgba(255,255,255,0.1)"
		>
			<p style="font-family:'Nunito',sans-serif;color:rgba(255,255,255,0.4);font-size:0.85rem">
				© 2025 Azzalea Pudding. All rights reserved.
			</p>
		</div>
	</div>
</footer>
"""

with open(r'r:/demo-client/clinic/src/routes/+page.svelte', 'w', encoding='utf-8') as f:
    f.write(content)

print("DONE: +page.svelte written successfully for Azzalea Pudding")
