<script lang="ts">
	import { allProducts, categories, waProduct } from '$lib/data';

	// Show 8 popular or varied products as a teaser
	const teaserProducts = allProducts.slice(0, 8);

	// Category color map for chips
	const catColorMap: Record<string, string> = {
		blocked: 'rgba(59,130,246,0.10)',
		hotwater: 'rgba(249,115,22,0.10)',
		gas: 'rgba(16,185,129,0.10)',
		emergency: 'rgba(239,68,68,0.10)',
		maintenance: 'rgba(139,92,246,0.10)'
	};
	const catTextMap: Record<string, string> = {
		blocked: 'var(--sp-navy)',
		hotwater: 'var(--sp-navy)',
		gas: 'var(--sp-navy)',
		emergency: 'var(--sp-orange)',
		maintenance: 'var(--sp-navy)'
	};
</script>

<section id="produk" class="py-16 md:py-24" style="background:var(--sp-bg-section);">
	<div class="mx-auto max-w-7xl px-4 md:px-6">
		<!-- Header -->
		<div class="sp-reveal mb-12 text-center">
			<div class="section-chip mb-4">OUR SERVICES</div>
			<h2
				class="font-display mb-6 font-extrabold tracking-tight uppercase"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Comprehensive <span style="color:var(--sp-blue);">Solutions</span>
			</h2>
			<div class="mx-auto mb-6 h-1 w-16" style="background:var(--sp-orange);"></div>
			<p class="mx-auto max-w-xl" style="color:var(--sp-gray);">
				From blocked drains and hot water systems to gas fitting and general maintenance, we handle
				it all with expertise and speed.
			</p>
		</div>

		<!-- Category Pills -->
		<div class="sp-reveal mb-10 flex flex-wrap justify-center gap-2">
			{#each categories.slice(1) as cat}
				<a
					href="/katalog"
					class="cat-pill font-display"
					style="background:var(--sp-bg-white); color:{catTextMap[cat.key] ??
						'var(--sp-navy)'}; border:1px solid var(--sp-gray-border);"
				>
					{cat.icon}
					{cat.label}
				</a>
			{/each}
		</div>

		<!-- Product Teaser Grid -->
		<div class="grid grid-cols-2 gap-3 sm:gap-5 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
			{#each teaserProducts as product, i (product.id)}
				<div
					class="card-sp sp-reveal flex flex-col gap-3 p-4 md:gap-4 md:p-6"
					style="transition-delay: {(i % 4) * 60}ms;"
				>
					<div class="flex flex-col items-start gap-2 md:flex-row md:justify-between md:gap-0">
						<div
							class="flex h-12 w-12 shrink-0 items-center justify-center text-2xl md:h-14 md:w-14 md:text-3xl"
							style="background:var(--sp-bg-off); border:1px solid var(--sp-gray-border); border-radius:4px;"
						>
							{product.emoji}
						</div>
						<div class="flex flex-col items-start gap-1 md:items-end">
							{#each product.tags as tag}
								{#if tag === 'Popular'}<span
										class="badge-popular px-2 py-0.5 text-[0.65rem] md:px-2.5 md:py-1 md:text-xs"
										>{tag}</span
									>
								{:else if tag === 'Urgent'}<span
										class="badge-new px-2 py-0.5 text-[0.65rem] md:px-2.5 md:py-1 md:text-xs"
										style="background:rgba(239,68,68,0.1); color:#EF4444; border-color:#EF4444;"
										>{tag}</span
									>
								{:else}<span
										class="badge-new px-2 py-0.5 text-[0.65rem] md:px-2.5 md:py-1 md:text-xs"
										>{tag}</span
									>
								{/if}
							{/each}
						</div>
					</div>
					<div class="flex-1">
						<h3
							class="font-display mb-1 text-sm font-bold md:text-base"
							style="color:var(--sp-navy);"
						>
							{product.name}
						</h3>
						<p
							class="text-[0.7rem] leading-relaxed md:text-xs"
							style="color:var(--sp-gray); display: -webkit-box; -webkit-line-clamp: 2; line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;"
						>
							{product.desc}
						</p>
					</div>
					<div>
						<a
							href={waProduct(product.name)}
							target="_blank"
							class="font-display block w-full py-2 text-center text-xs font-bold tracking-widest uppercase transition-all duration-200"
							style="background:var(--sp-white); border:2px solid var(--sp-navy); color:var(--sp-navy); border-radius: 4px;"
							onmouseenter={(e) => {
								e.currentTarget.style.background = 'var(--sp-navy)';
								e.currentTarget.style.color = '#fff';
							}}
							onmouseleave={(e) => {
								e.currentTarget.style.background = 'var(--sp-white)';
								e.currentTarget.style.color = 'var(--sp-navy)';
							}}
						>
							💬 Request Service
						</a>
					</div>
				</div>
			{/each}
		</div>

		<!-- CTA to full catalog -->
		<div class="sp-reveal mt-12 text-center">
			<p class="mb-5 text-base" style="color:var(--sp-gray);">
				Showing <strong style="color:var(--sp-blue);">{teaserProducts.length}</strong>
				popular services out of
				<strong style="color:var(--sp-navy);">{allProducts.length}+ services</strong> we offer.
			</p>
			<a href="/katalog" class="btn-primary-sp inline-flex items-center gap-2 text-sm">
				View All Services
			</a>
		</div>
	</div>
</section>

<style>
	.cat-pill {
		display: inline-flex;
		align-items: center;
		gap: 5px;
		padding: 6px 16px;
		border-radius: 4px;
		font-size: 0.85rem;
		font-weight: 700;
		text-decoration: none;
		transition:
			transform 0.2s,
			box-shadow 0.2s;
	}
	.cat-pill:hover {
		transform: translateY(-2px);
		box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
	}
</style>
