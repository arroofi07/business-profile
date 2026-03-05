<script lang="ts">
	import { onMount } from 'svelte';
	import { waGeneral } from '$lib/data';
	import logo from '$lib/assets/logo.png';

	let navScrolled = $state(false);
	let mobileNavOpen = $state(false);

	onMount(() => {
		const onScroll = () => {
			navScrolled = window.scrollY > 30;
		};
		window.addEventListener('scroll', onScroll, { passive: true });
		return () => {
			window.removeEventListener('scroll', onScroll);
		};
	});
</script>

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
			<div class="flex h-11 w-11 items-center justify-center rounded-xl text-2xl shadow-md">
				<img src={logo} alt="logo" class="h-full w-full object-cover" />
			</div>
			<div>
				<div class="font-display text-lg leading-tight font-bold" style="color:var(--sp-navy);">
					Smart<span style="color:var(--sp-blue-mid);">print</span> Padang
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
			{#each [['#layanan', 'Layanan'], ['#produk', 'Katalog'], ['#cara-pesan', 'Cara Order'], ['#harga', 'Harga'], ['#tentang', 'Tentang'], ['#kontak', 'Kontak']] as [href, label]}
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
