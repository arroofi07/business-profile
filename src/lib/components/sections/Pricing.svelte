<script lang="ts">
	import { waLink } from '$lib/data';
	import { Tag, Star, Gem } from 'lucide-svelte';
</script>

<section id="harga" class="py-24" style="background:var(--sp-bg-section);">
	<div class="mx-auto max-w-6xl px-6">
		<div class="sp-reveal mb-16 text-center">
			<div class="section-chip mb-4">PRICING ESTIMATES</div>
			<h2
				class="font-display mb-6 font-extrabold tracking-tight uppercase"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Transparent <span style="color:var(--sp-orange);">Pricing</span>
			</h2>
			<div class="mx-auto mb-6 h-1 w-16" style="background:var(--sp-orange);"></div>
			<p class="text-lg font-semibold" style="color:var(--sp-gray);">
				We provide upfront pricing with absolutely no hidden fees.
			</p>
		</div>
		<div class="grid items-center gap-6 md:grid-cols-3">
			{#each [{ tier: 'Fix Leaks', icon: Tag, color: 'var(--sp-navy)', desc: 'Perfect for minor plumbing issues', featured: false, items: ['Tap Replacements from $99', 'Toilet Repairs from $120', 'Leak Inspections from $80', 'General Maintenance from $90'] }, { tier: 'Blocked Drains', icon: Star, color: 'var(--sp-orange)', desc: 'Advanced clearing for stubborn blocks', featured: true, items: ['CCTV Drain Inspection from $150', 'High Pressure Jetting from $250', 'Sewer Cleaning from $200', 'Pipe Relining quotes available'] }, { tier: 'Installations', icon: Gem, color: 'var(--sp-navy)', desc: 'For major appliances & new builds', featured: false, items: ['Hot Water System Install from $800', 'Gas Line Fitting from $350', 'Full Bathroom Plumbing from $1500', 'Commercial fit-outs custom quote'] }] as plan, i}
				<div
					class="sp-reveal relative flex flex-col gap-6 p-8 transition-all"
					style="{plan.featured
						? 'background:var(--sp-navy); border-top: 6px solid var(--sp-orange); box-shadow:var(--sp-shadow-xl); transform: scale(1.05); z-index: 10;'
						: 'background:white; border:1px solid var(--sp-gray-border); box-shadow:var(--sp-shadow-sm);'} border-radius: 4px; transition-delay:{i *
						100}ms;"
				>
					{#if plan.featured}
						<div
							class="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 text-xs font-bold tracking-widest shadow-md"
							style="background:var(--sp-orange); color:#fff; white-space:nowrap; border-radius: 2px;"
						>
							MOST POPULAR
						</div>
					{/if}
					<div style="color:{plan.featured ? 'var(--sp-orange)' : plan.color};">
						<svelte:component this={plan.icon} size={40} strokeWidth={2} />
					</div>
					<div
						class="border-b pb-6"
						style="border-color:{plan.featured
							? 'rgba(255,255,255,0.1)'
							: 'var(--sp-gray-border)'};"
					>
						<h3
							class="font-display mb-2 text-2xl font-extrabold tracking-tight uppercase"
							style="color:{plan.featured ? '#fff' : 'var(--sp-navy)'};"
						>
							{plan.tier}
						</h3>
						<p
							class="text-sm font-semibold"
							style="color:{plan.featured ? 'var(--sp-gray-light)' : 'var(--sp-gray)'};"
						>
							{plan.desc}
						</p>
					</div>
					<ul class="flex flex-1 flex-col gap-4 py-4">
						{#each plan.items as item}
							<li
								class="flex items-start gap-3 text-sm font-semibold"
								style="color:{plan.featured ? '#fff' : 'var(--sp-navy)'};"
							>
								<span
									style="color:{plan.featured
										? 'var(--sp-orange)'
										: 'var(--sp-blue)'}; flex-shrink:0;">✓</span
								>{item}
							</li>
						{/each}
					</ul>
					<a
						href={waLink(`Hello Aldinga Plumbing Services, I'd like a quote for *${plan.tier}*`)}
						target="_blank"
						class="font-display mt-4 block w-full py-4 text-center text-sm font-bold tracking-widest uppercase transition-colors"
						style={plan.featured
							? 'background:var(--sp-orange); color:#fff; border-radius: 4px;'
							: 'background:transparent; border:2px solid var(--sp-navy); color:var(--sp-navy); border-radius: 4px;'}
						onmouseenter={(e) => {
							if (!plan.featured) {
								e.currentTarget.style.background = 'var(--sp-navy)';
								e.currentTarget.style.color = '#fff';
							} else {
								e.currentTarget.style.background = '#C2410C';
							}
						}}
						onmouseleave={(e) => {
							if (!plan.featured) {
								e.currentTarget.style.background = 'transparent';
								e.currentTarget.style.color = 'var(--sp-navy)';
							} else {
								e.currentTarget.style.background = 'var(--sp-orange)';
							}
						}}
					>
						Get Quote
					</a>
				</div>
			{/each}
		</div>
	</div>
</section>
