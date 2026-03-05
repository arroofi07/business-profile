<script lang="ts">
	import { onMount } from 'svelte';
	import { statTargets } from '$lib/data';

	let statCounter = $state({ products: 0, clients: 0, years: 0, followers: 0 });

	function animateCounters() {
		const duration = 2000,
			step = 16,
			steps = duration / step;
		let frame = 0;
		const timer = setInterval(() => {
			frame++;
			const ease = 1 - Math.pow(1 - Math.min(frame / steps, 1), 3);
			statCounter = {
				products: Math.round(statTargets.products * ease),
				clients: Math.round(statTargets.clients * ease),
				years: Math.round(statTargets.years * ease),
				followers: Math.round(statTargets.followers * ease)
			};
			if (frame >= steps) clearInterval(timer);
		}, step);
	}

	onMount(() => {
		const statsEl = document.getElementById('stats-section');
		if (statsEl) {
			const obs = new IntersectionObserver(
				(entries) => {
					if (entries[0].isIntersecting) {
						animateCounters();
						obs.disconnect();
					}
				},
				{ threshold: 0.4 }
			);
			obs.observe(statsEl);
		}
	});
</script>

<section
	id="stats-section"
	class="py-14"
	style="background:var(--sp-bg-dark); border-top:4px solid var(--sp-blue);"
>
	<div class="mx-auto grid max-w-5xl grid-cols-2 gap-8 px-6 md:grid-cols-4">
		{#each [{ label: 'Jenis Produk', val: statCounter.products, suffix: '+', color: '#93C5FD' }, { label: 'Pelanggan Puas', val: statCounter.clients, suffix: '+', color: '#6EE7B7' }, { label: 'Tahun Pengalaman', val: statCounter.years, suffix: '', color: '#FBD38D' }, { label: 'Instagram Followers', val: statCounter.followers, suffix: '', color: '#C4B5FD' }] as s}
			<div class="text-center">
				<div class="font-display mb-1 font-extrabold" style="font-size:2.5rem; color:{s.color};">
					{s.val}{s.suffix}
				</div>
				<div class="text-sm font-medium" style="color:rgba(255,255,255,0.6);">{s.label}</div>
			</div>
		{/each}
	</div>
</section>
