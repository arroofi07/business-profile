<script lang="ts">
	import { onMount } from 'svelte';
	import { waGeneral } from '$lib/data';

	let navScrolled = $state(false);
	let mobileNavOpen = $state(false);
	let isOpen = $state(true);

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
	class="fixed top-0 right-0 left-0 z-50 transition-all duration-300"
	style="background: #fff; box-shadow: {navScrolled
		? 'var(--sp-shadow-md)'
		: 'none'}; border-bottom: 1px solid var(--sp-gray-border);"
>
	<!-- Top Bar (Enterprise) -->
	<div
		class="hidden w-full items-center justify-between py-2 md:flex"
		style="background: var(--sp-navy); color: #fff; font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;"
	>
		<div class="mx-auto flex w-full max-w-7xl justify-between px-6">
			<span class="flex items-center gap-2"><span>🛡️</span> Licensed & Insured Professionals</span>
			<span class="flex items-center gap-6 text-blue-100">
				<span>📍 Serving Aldinga Beach, SA</span>
				<span class="flex items-center gap-2"
					><span
						class="animate-ping-dot inline-block h-2 w-2 rounded-full"
						style="background:var(--sp-orange);"
					></span> 24/7 Emergency Service</span
				>
			</span>
		</div>
	</div>

	<nav
		class="mx-auto flex max-w-7xl items-center justify-between px-6 transition-all duration-300"
		style="height: {navScrolled ? '70px' : 'var(--nav-height)'};"
	>
		<!-- Logo -->
		<a href="/" class="group flex items-center gap-3">
			<div
				class="flex h-11 w-11 items-center justify-center rounded-sm p-1 shadow-sm"
				style="background:transparent;"
			>
				<img src="/logo.svg" alt="Aldinga Plumbing Logo" class="h-full w-full object-contain" />
			</div>
			<div>
				<div
					class="font-display text-xl leading-tight font-extrabold tracking-tight"
					style="color:var(--sp-navy);"
				>
					ALDINGA <span style="color:var(--sp-orange);">PLUMBING</span>
				</div>
				<div
					class="text-xs font-bold tracking-widest text-slate-500"
					style="font-family:'Plus Jakarta Sans',sans-serif;"
				>
					SERVICES & REPAIRS
				</div>
			</div>
		</a>

		<!-- Desktop nav -->
		<div class="hidden items-center gap-8 md:flex">
			{#each [['/#layanan', 'SERVICES'], ['/#produk', 'CATALOG'], ['/#tentang', 'ABOUT US'], ['/#kontak', 'CONTACT']] as [href, label]}
				<a
					{href}
					class="text-sm font-bold transition-colors duration-200"
					style="color:var(--sp-navy); letter-spacing: 0.05em;"
					onmouseenter={(e) => (e.currentTarget.style.color = 'var(--sp-orange)')}
					onmouseleave={(e) => (e.currentTarget.style.color = 'var(--sp-navy)')}>{label}</a
				>
			{/each}
		</div>

		<!-- CTA -->
		<div class="hidden items-center gap-4 md:flex">
			<a href={waGeneral} target="_blank" class="btn-whatsapp text-sm shadow-md"
				>CALL +61 459 529 693</a
			>
		</div>

		<!-- Mobile hamburger -->
		<button
			class="p-2 md:hidden"
			onclick={() => (mobileNavOpen = !mobileNavOpen)}
			aria-label="Toggle nav"
		>
			<div class="space-y-1.5">
				<div class="h-0.5 w-6 rounded-sm bg-slate-900"></div>
				<div class="h-0.5 w-6 rounded-sm bg-slate-900"></div>
				<div class="h-0.5 w-6 rounded-sm bg-slate-900"></div>
			</div>
		</button>
	</nav>

	<!-- Mobile menu -->
	{#if mobileNavOpen}
		<div
			class="animate-slide-down flex flex-col gap-3 px-6 py-5 md:hidden"
			style="background:#fff; border-top:1px solid var(--sp-gray-border); box-shadow: var(--sp-shadow-lg);"
		>
			<div
				class="mb-2 flex items-center justify-between pb-3"
				style="border-bottom:1px solid var(--sp-gray-border);"
			>
				<span class="text-sm font-bold tracking-widest text-slate-800 uppercase"
					>24/7 Emergency Service</span
				>
				<div
					class="animate-ping-dot h-2 w-2 rounded-full"
					style="background:var(--sp-orange);"
				></div>
			</div>

			{#each [['/#layanan', 'SERVICES'], ['/#tentang', 'ABOUT US'], ['/#produk', 'CATALOG'], ['/#kontak', 'CONTACT']] as [href, label]}
				<a
					{href}
					class="border-b py-3 text-sm font-bold text-slate-800"
					style="border-color:var(--sp-gray-border); letter-spacing:0.05em;"
					onclick={() => (mobileNavOpen = false)}>{label}</a
				>
			{/each}
			<a
				href={waGeneral}
				target="_blank"
				class="btn-whatsapp mt-4 w-full text-center text-sm shadow-md">CALL NOW</a
			>
		</div>
	{/if}
</header>
