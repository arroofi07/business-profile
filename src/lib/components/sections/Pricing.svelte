<script lang="ts">
	import { waLink } from '$lib/data';
	import { Tag, Star, Gem } from 'lucide-svelte';
</script>

<section id="harga" class="py-24" style="background:var(--sp-bg-section);">
	<div class="mx-auto max-w-5xl px-6">
		<div class="sp-reveal mb-16 text-center">
			<div class="section-chip mb-4">ESTIMASI HARGA</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Harga <span class="gradient-text-blue">Transparan</span>
			</h2>
			<p style="color:var(--sp-gray);">Kami memberikan harga terbaik tanpa biaya tersembunyi.</p>
		</div>
		<div class="grid gap-8 md:grid-cols-3">
			{#each [{ tier: 'Basic', icon: Tag, color: 'var(--sp-cyan)', desc: 'Cocok untuk kebutuhan cetak kecil & personal', featured: false, items: ['Kartu Nama (100pcs) mulai Rp 30rb', 'Stiker Cutting mulai Rp 15rb', 'Poster A3 mulai Rp 5rb/lembar', 'ID Card mulai Rp 10rb/pcs'] }, { tier: 'Standard', icon: Star, color: 'var(--sp-blue)', desc: 'Pilihan terbaik untuk promosi bisnis Anda', featured: true, items: ['Spanduk PVC mulai Rp 25rb/m²', 'Roll Banner mulai Rp 150rb', 'X-Banner mulai Rp 85rb', 'Backdrop mulai Rp 80rb/m²'] }, { tier: 'Premium', icon: Gem, color: 'var(--sp-orange)', desc: 'Untuk event besar, proyek & order massal', featured: false, items: ['Baliho Outdoor mulai Rp 45rb/m²', 'Custom ukuran besar', 'Nota / Bon custom Rp 45rb/buku', 'Harga grosir (diskusi)'] }] as plan, i}
				<div
					class="sp-reveal relative flex flex-col gap-5 rounded-2xl p-7 transition-all duration-300 hover:-translate-y-2"
					style="{plan.featured
						? 'background:var(--sp-gradient-blue); box-shadow:var(--sp-shadow-xl);'
						: 'background:white; border:1.5px solid var(--sp-gray-border); box-shadow:var(--sp-shadow-sm);'} transition-delay:{i *
						100}ms;"
				>
					{#if plan.featured}
						<div
							class="absolute -top-3 left-1/2 -translate-x-1/2 rounded-full px-4 py-1 text-xs font-bold"
							style="background:var(--sp-orange); color:#fff; font-family:'Outfit',sans-serif; white-space:nowrap;"
						>
							PALING POPULER
						</div>
					{/if}
					<div style="color:{plan.featured ? '#fff' : plan.color};">
						<svelte:component this={plan.icon} size={36} strokeWidth={1.5} />
					</div>
					<div>
						<h3
							class="font-display mb-1 text-2xl font-bold"
							style="color:{plan.featured ? '#fff' : plan.color};"
						>
							{plan.tier}
						</h3>
						<p
							class="text-sm"
							style="color:{plan.featured ? 'rgba(255,255,255,0.75)' : 'var(--sp-gray)'};"
						>
							{plan.desc}
						</p>
					</div>
					<ul class="flex flex-1 flex-col gap-2">
						{#each plan.items as item}
							<li
								class="flex items-start gap-2 text-sm"
								style="color:{plan.featured ? 'rgba(255,255,255,0.88)' : 'var(--sp-text-mid)'};"
							>
								<span
									style="color:{plan.featured
										? '#93C5FD'
										: plan.color}; flex-shrink:0; margin-top:1px;">✓</span
								>{item}
							</li>
						{/each}
					</ul>
					<a
						href={waLink(`Halo MPM Digital Printing, saya mau tanya harga paket *${plan.tier}*`)}
						target="_blank"
						class="font-display block w-full rounded-xl py-3 text-center text-sm font-bold transition-all duration-200"
						style={plan.featured
							? 'background:white; color:var(--sp-blue);'
							: `background:transparent; border:2px solid ${plan.color}; color:${plan.color};`}
					>
						Tanya Harga {plan.tier}
					</a>
				</div>
			{/each}
		</div>
	</div>
</section>
