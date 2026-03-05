<script lang="ts">
	import { waGeneral } from '$lib/data';
	import { Instagram, MessageCircle, MapPin, Link } from 'lucide-svelte';
	import logo from '$lib/assets/logo.png';
</script>

<footer style="background:#0F172A; border-top:3px solid var(--sp-blue);">
	<div class="mx-auto max-w-7xl px-6 py-16">
		<div class="grid grid-cols-1 gap-10 md:grid-cols-2 lg:grid-cols-6">
			<!-- Brand -->
			<div class="md:col-span-2">
				<div class="mb-4 flex items-center gap-3">
					<div
						class="flex h-11 w-11 items-center justify-center rounded-xl text-2xl"
						style="background:white"
					>
						<img src={logo} alt="" class="h-full w-full object-cover" />
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
						style="background:linear-gradient(135deg,#E1306C,#833AB4);"
					>
						<Instagram />
					</a>
					<a
						href={waGeneral}
						target="_blank"
						class="flex h-9 w-9 items-center justify-center rounded-lg text-lg transition-opacity hover:opacity-75"
						style="background:linear-gradient(135deg,#25D366,#128C7E);"
					>
						<MessageCircle />
					</a>
				</div>
			</div>

			<!-- Links -->
			<div class="lg:col-span-1">
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
			<div class="lg:col-span-1">
				<div
					class="font-display mb-4 text-sm font-bold tracking-wider uppercase"
					style="color:rgba(255,255,255,0.4);"
				>
					Kontak
				</div>
				{#each [{ ico: MessageCircle, val: '0811 663 528' }, { ico: Instagram, val: '@smartprint_padang' }, { ico: MapPin, val: 'Padang, Sumatera Barat' }, { ico: Link, val: 'Part of @redline_comunication' }] as item}
					<div class="flex items-start gap-2 py-1.5 text-sm" style="color:rgba(255,255,255,0.6);">
						<span class="mt-0.5 shrink-0"
							><svelte:component this={item.ico} size={16} strokeWidth={2} /></span
						><span>{item.val}</span>
					</div>
				{/each}
			</div>

			<!-- Map -->
			<div class="md:col-span-2 lg:col-span-2">
				<div
					class="font-display mb-4 text-sm font-bold tracking-wider uppercase"
					style="color:rgba(255,255,255,0.4);"
				>
					Lokasi Kami
				</div>
				<div
					class="group relative overflow-hidden rounded-xl border transition-all duration-300 hover:border-[#1E90FF]/50 hover:shadow-[0_0_20px_rgba(30,144,255,0.2)]"
					style="border-color: rgba(255,255,255,0.1); background: rgba(255,255,255,0.02); height: 180px;"
				>
					<div
						class="pointer-events-none absolute inset-0 z-10 rounded-xl ring-1 ring-white/10 ring-inset"
					></div>
					<iframe
						src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2328.8685642568494!2d100.35031756277502!3d-0.9018060688247466!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2fd4b8b2cf5e6e9f%3A0xfe9dacac7f8093d0!2sPlaza%20Computer!5e0!3m2!1sen!2sid!4v1772718244706!5m2!1sen!2sid"
						width="100%"
						height="100%"
						class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
						style="border:0; filter: invert(90%) hue-rotate(180deg) contrast(1.1) opacity(0.8);"
						allowfullscreen={true}
						loading="lazy"
						referrerpolicy="no-referrer-when-downgrade"
						title="Lokasi Google Maps"
					>
					</iframe>
					<div
						class="pointer-events-none absolute inset-0 z-20 bg-[#1E90FF]/10 opacity-0 transition-opacity duration-300 group-hover:opacity-100"
					></div>
				</div>
				<a
					href="https://maps.app.goo.gl/7dJk77JraC61ZCfq5"
					target="_blank"
					class="group/link mt-3 inline-flex items-center gap-2 text-xs transition-colors hover:text-white"
					style="color: var(--sp-blue-light);"
				>
					<span>Buka di Google Maps</span>
					<span
						class="text-[10px] transition-transform duration-300 group-hover/link:translate-x-0.5 group-hover/link:-translate-y-0.5"
						>↗</span
					>
				</a>
			</div>
		</div>

		<div class="section-divider my-8"></div>
		<div
			class="flex flex-col items-center justify-between gap-3 text-xs sm:flex-row"
			style="color:rgba(255,255,255,0.35);"
		>
			<span
				>©2026 Smartprint Padang. Powered by
				<a
					href="https://solaria.icu"
					target="_blank"
					class="transition-colors hover:text-white"
					style="color:var(--sp-blue-light);">solaria.icu</a
				>.</span
			>
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
