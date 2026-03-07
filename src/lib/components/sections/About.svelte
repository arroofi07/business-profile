<script lang="ts">
	import { Target, Zap, Coins, Handshake, Printer, Clock } from 'lucide-svelte';
	import logo from '$lib/assets/mpm.png';
</script>

<section id="tentang" class="py-24" style="background:var(--sp-bg-off);">
	<div class="mx-auto grid max-w-7xl items-center gap-16 px-6 lg:grid-cols-2">
		<!-- Left copy -->
		<div class="sp-reveal">
			<div class="section-chip mb-6">ABOUT US</div>
			<h2
				class="font-display mb-6 leading-tight font-extrabold text-slate-900"
				style="font-size:clamp(2rem,4vw,3rem);"
			>
				Your Trusted Local <br />
				<span style="color:var(--sp-blue);">Plumbing Experts</span>
			</h2>
			<div class="mb-8 h-1 w-20" style="background:var(--sp-orange);"></div>
			<p class="mb-6 text-lg leading-relaxed font-medium text-slate-700">
				Aldinga Plumbing Services provides fast, reliable, and affordable plumbing solutions across
				Aldinga Beach and surrounding areas in South Australia.
			</p>
			<p class="mb-10 text-base leading-relaxed text-slate-600">
				Our fully licensed and insured team uses the latest technology to ensure every job is done
				right the first time. Whether it's a minor leak, a bathroom renovation, or a major plumbing
				emergency, we are available 24/7 to get your systems back on track.
			</p>

			<div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
				{#each [{ icon: Target, label: 'Quality Workmanship', desc: 'Done right the first time' }, { icon: Zap, label: 'Fast Response', desc: 'Emergency dispatch' }, { icon: Coins, label: 'Upfront Pricing', desc: 'No hidden fees ever' }, { icon: Handshake, label: 'Licensed & Insured', desc: 'Complete peace of mind' }] as v}
					<div
						class="flex items-start gap-4 rounded p-5 shadow-sm transition-all"
						style="background:var(--sp-bg-white); border: 1px solid var(--sp-gray-border);"
					>
						<div
							class="flex h-10 w-10 shrink-0 items-center justify-center rounded text-white"
							style="background:var(--sp-blue);"
						>
							<svelte:component this={v.icon} size={22} strokeWidth={2} />
						</div>
						<div>
							<div class="mb-1 text-sm font-bold text-slate-900">{v.label}</div>
							<div class="text-xs text-slate-500">{v.desc}</div>
						</div>
					</div>
				{/each}
			</div>
		</div>

		<!-- Right visual -->
		<div class="sp-reveal flex flex-col gap-6" style="transition-delay: 200ms;">
			<div
				class="relative w-full overflow-hidden rounded shadow-xl"
				style="border: 4px solid var(--sp-navy); min-height: 400px; background: #0f172a;"
			>
				<img
					src="/plumber-about.png"
					alt="Aldinga Plumbing Team"
					class="absolute inset-0 h-full w-full object-cover opacity-90 transition-opacity hover:opacity-100"
				/>
			</div>

			<div
				class="rounded p-6 shadow-md"
				style="background:var(--sp-bg-white); border: 1px solid var(--sp-gray-border); border-top: 4px solid var(--sp-orange);"
			>
				<div
					class="font-display mb-4 flex items-center gap-3 text-lg font-bold tracking-widest text-slate-900 uppercase"
				>
					<Clock size={24} strokeWidth={2} style="color:var(--sp-orange);" />
					Operating Hours
				</div>
				<div class="flex flex-col gap-3">
					{#each [['Monday – Sunday', '24 Hours Open'], ['Public Holidays', 'Available']] as [hari, jam]}
						<div
							class="flex items-center justify-between border-b pb-3 text-sm last:border-0 last:pb-0"
							style="border-color:var(--sp-gray-border); color:var(--sp-gray);"
						>
							<span class="font-medium text-slate-600">{hari}</span>
							<span
								class="rounded px-3 py-1 text-xs font-bold"
								style="background:rgba(234,88,12,0.1); color:var(--sp-orange);">{jam}</span
							>
						</div>
					{/each}
				</div>
			</div>
		</div>
	</div>
</section>
