<script lang="ts">
	import { waGeneral } from '$lib/data';
	import { Instagram, MessageCircle, MapPin, Link } from 'lucide-svelte';
	import logo from '$lib/assets/mpm.png';

	let mapLoaded = $state(false);
</script>

<footer style="background:#0F172A; border-top:3px solid var(--sp-blue);">
	<div class="mx-auto max-w-7xl px-6 py-16">
		<div class="grid grid-cols-1 gap-12 md:grid-cols-2 lg:grid-cols-6">
			<!-- Brand -->
			<div class="md:col-span-2">
				<div class="mb-6 flex items-center gap-3">
					<div
						class="flex h-12 w-12 items-center justify-center rounded p-1 shadow-sm"
						style="background:white;"
					>
						<img src="/logo.svg" alt="Aldinga Plumbing Logo" class="h-full w-full object-contain" />
					</div>
					<div>
						<div class="font-display text-lg font-bold text-white">Aldinga Plumbing Services</div>
						<div
							class="text-xs"
							style="color:rgba(255,255,255,0.45); font-family:'Plus Jakarta Sans',sans-serif;"
						>
							24/7 EMERGENCY PLUMBER
						</div>
					</div>
				</div>
				<p class="mb-4 max-w-xs text-sm" style="color:rgba(255,255,255,0.55);">
					Professional 24/7 plumbing services in Aldinga Beach, SA. Call us for commercial and
					residential plumbing.
				</p>
				<div class="flex gap-3">
					<a
						href="https://www.instagram.com/aldingaplumbing/"
						target="_blank"
						class="flex h-10 w-10 items-center justify-center rounded text-lg transition-colors hover:bg-slate-700"
						style="background:rgba(255,255,255,0.1); color: white;"
					>
						<Instagram size={20} />
					</a>
					<a
						href={waGeneral}
						target="_blank"
						class="flex h-10 w-10 items-center justify-center rounded text-lg transition-colors hover:bg-slate-700"
						style="background:rgba(255,255,255,0.1); color: white;"
					>
						<MessageCircle size={20} />
					</a>
				</div>
			</div>

			<!-- Links -->
			<div class="lg:col-span-1">
				<div
					class="font-display mb-4 text-sm font-bold tracking-wider uppercase"
					style="color:rgba(255,255,255,0.4);"
				>
					Services
				</div>
				{#each ['Blocked Drains', 'Hot Water', 'Gas Fitting', 'Emergency', 'Maintenance'] as l}
					<div class="py-1.5 text-sm" style="color:rgba(255,255,255,0.6);">{l}</div>
				{/each}
			</div>

			<!-- Contact -->
			<div class="lg:col-span-1">
				<div
					class="font-display mb-4 text-sm font-bold tracking-wider uppercase"
					style="color:rgba(255,255,255,0.4);"
				>
					Contact
				</div>
				{#each [{ ico: Instagram, val: '@aldingaplumbing' }, { ico: MapPin, val: '292 Aldinga Beach Rd' }] as item}
					{@const Icon = item.ico}
					<div class="flex items-start gap-2 py-1.5 text-sm" style="color:rgba(255,255,255,0.6);">
						<span class="mt-0.5 shrink-0"><Icon size={16} strokeWidth={2} /></span><span
							>{item.val}</span
						>
					</div>
				{/each}
			</div>

			<!-- Map -->
			<div class="md:col-span-2 lg:col-span-2">
				<div
					class="font-display mb-4 text-sm font-bold tracking-wider uppercase"
					style="color:rgba(255,255,255,0.4);"
				>
					Our Location
				</div>
				<div
					class="group relative overflow-hidden rounded border transition-all duration-300 hover:border-orange-500/50 hover:shadow-[0_0_20px_rgba(234,88,12,0.15)]"
					style="border-color: rgba(255,255,255,0.1); background: rgba(255,255,255,0.02); height: 180px;"
				>
					<div
						class="pointer-events-none absolute inset-0 z-10 rounded ring-1 ring-white/10 ring-inset"
					></div>

					{#if mapLoaded}
						<iframe
							src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3257.6534571650893!2d138.4533033!3d-35.2671542!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ab8bbdd812a02dd%3A0x6b40285a86241b21!2s292%20Aldinga%20Beach%20Rd%2C%20Aldinga%20Beach%20SA%205173%2C%20Australia!5e0!3m2!1sen!2sau!4v1709825634567!5m2!1sen!2sau"
							width="100%"
							height="100%"
							class="h-full w-full object-cover"
							style="border:0; filter: invert(90%) hue-rotate(180deg) contrast(1.1) opacity(0.8);"
							allowfullscreen={true}
							loading="lazy"
							referrerpolicy="no-referrer-when-downgrade"
							title="Google Maps Location"
						>
						</iframe>
					{:else}
						<button
							class="relative h-full w-full cursor-pointer"
							aria-label="Load Map"
							onclick={() => (mapLoaded = true)}
							onmouseenter={() => (mapLoaded = true)}
						>
							<div
								class="absolute inset-0 flex flex-col items-center justify-center bg-[#0F172A] text-white/50 transition-colors group-hover:text-white/80"
							>
								<MapPin
									size={32}
									class="mb-2 opacity-50 transition-opacity group-hover:opacity-100"
								/>
								<span class="text-xs font-semibold tracking-wider uppercase">Show Map</span>
							</div>
						</button>
					{/if}

					<div
						class="pointer-events-none absolute inset-0 z-20 bg-orange-500/5 opacity-0 transition-opacity duration-300 group-hover:opacity-100"
					></div>
				</div>
				<a
					href="https://maps.google.com/?q=292+Aldinga+Beach+Rd,+Aldinga+Beach+SA+5173"
					target="_blank"
					class="group/link mt-3 inline-flex items-center gap-2 text-xs font-bold transition-colors hover:text-white"
					style="color: var(--sp-orange);"
				>
					<span>Open in Google Maps</span>
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
			<span>©2026 Aldinga Plumbing Services. All rights reserved. </span>
		</div>
	</div>
</footer>
