<script lang="ts">
	import { waGeneral } from '$lib/data';
	import { Instagram, MessageCircle, MapPin } from 'lucide-svelte';
</script>

<section
	id="kontak"
	class="py-24"
	style="background:var(--sp-navy); border-top: 4px solid var(--sp-orange);"
>
	<div class="mx-auto max-w-4xl px-6 text-center">
		<div class="sp-reveal">
			<div
				class="mb-6 inline-block rounded-sm px-4 py-1.5 text-xs font-bold tracking-widest uppercase"
				style="background:rgba(234,88,12,0.15); color:var(--sp-orange);"
			>
				CONTACT US
			</div>
			<h2
				class="font-display mb-6 font-extrabold tracking-tight text-white uppercase"
				style="font-size:clamp(2rem,5vw,3rem);"
			>
				Need a <span style="color:var(--sp-orange);">Plumber?</span>
			</h2>
			<div class="mx-auto mb-6 h-1 w-16" style="background:var(--sp-orange);"></div>
			<p class="mx-auto mb-10 max-w-xl text-lg font-medium" style="color:rgba(255,255,255,0.7);">
				Contact Aldinga Plumbing Services now for fast and reliable 24/7 assistance.
			</p>
			<div class="flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
				<a
					href={waGeneral}
					target="_blank"
					class="btn-whatsapp flex items-center gap-2 rounded px-8 py-4 text-sm font-bold shadow-lg"
				>
					<MessageCircle size={20} /> WHATSAPP US NOW</a
				>
				<a
					href="tel:+61459529693"
					class="btn-primary-sp flex items-center gap-2 rounded px-8 py-4 text-sm font-bold shadow-lg"
					style="background:transparent; border-color:var(--sp-orange); color:var(--sp-orange);"
				>
					CALL +61 459 529 693</a
				>
			</div>
		</div>
		<div class="mt-12 grid grid-cols-1 gap-6 sm:grid-cols-3">
			{#each [{ icon: MessageCircle, label: 'Emergency', val: 'Call or WhatsApp' }, { icon: Instagram, label: 'Facebook/Instagram', val: '@aldingaplumbing' }, { icon: MapPin, label: 'Location', val: 'Aldinga Beach SA' }] as c, i}
				<div
					class="sp-reveal flex flex-col items-center border p-6 transition-all hover:bg-slate-800"
					style="background:rgba(255,255,255,0.03); border-color:rgba(255,255,255,0.1); border-radius: 4px; transition-delay:{i *
						100}ms;"
				>
					<div class="mb-4 rounded border border-slate-700 bg-slate-800 p-3 text-white">
						<svelte:component this={c.icon} size={28} strokeWidth={1.5} />
					</div>
					<div
						class="mb-1 text-xs font-bold tracking-widest uppercase"
						style="color:var(--sp-orange);"
					>
						{c.label}
					</div>
					<div class="text-sm font-bold tracking-wider text-white uppercase">{c.val}</div>
				</div>
			{/each}
		</div>
	</div>
</section>
