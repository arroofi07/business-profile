<script lang="ts">
	import { allProducts, categories, waProduct } from '$lib/data';

	// Show 8 popular or varied products as a teaser
	const teaserProducts = allProducts.filter((p) => p.tags.includes('Populer')).slice(0, 8);

	// Category color map for chips
	const catColorMap: Record<string, string> = {
		signage: 'rgba(59,130,246,0.10)',
		promosi: 'rgba(249,115,22,0.10)',
		office: 'rgba(16,185,129,0.10)',
		buku: 'rgba(139,92,246,0.10)',
		souvenir: 'rgba(236,72,153,0.10)',
		textile: 'rgba(234,179,8,0.10)',
		industri: 'rgba(107,114,128,0.10)'
	};
	const catTextMap: Record<string, string> = {
		signage: '#1D4ED8',
		promosi: '#F97316',
		office: '#10B981',
		buku: '#8B5CF6',
		souvenir: '#EC4899',
		textile: '#EAB308',
		industri: '#6B7280'
	};
</script>

<section id="produk" class="py-24" style="background:var(--sp-bg-section);">
	<div class="mx-auto max-w-7xl px-6">
		<!-- Header -->
		<div class="sp-reveal mb-12 text-center">
			<div class="section-chip mb-4">KATALOG PRODUK</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				78+ Pilihan Produk <span class="gradient-text-blue">Cetak Kami</span>
			</h2>
			<p class="mx-auto max-w-xl" style="color:var(--sp-gray);">
				Dari banner hingga souvenir, dari office supplies hingga textile. Semua kebutuhan cetak Anda
				ada di sini dengan kualitas premium.
			</p>
		</div>

		<!-- Category Pills -->
		<div class="sp-reveal mb-10 flex flex-wrap justify-center gap-2">
			{#each categories.slice(1) as cat}
				<a
					href="/katalog"
					class="cat-pill font-display"
					style="background:{catColorMap[cat.key] ?? 'var(--sp-bg-off)'}; color:{catTextMap[
						cat.key
					] ?? 'var(--sp-gray)'}; border:1px solid {catTextMap[cat.key] ?? 'var(--sp-gray)'}33;"
				>
					{cat.icon}
					{cat.label}
				</a>
			{/each}
		</div>

		<!-- Product Teaser Grid -->
		<div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
			{#each teaserProducts as product, i (product.id)}
				<div
					class="card-sp sp-reveal flex flex-col gap-4 p-6"
					style="transition-delay: {(i % 4) * 60}ms;"
				>
					<div class="flex items-start justify-between">
						<div
							class="flex h-14 w-14 items-center justify-center rounded-xl text-3xl"
							style="background:var(--sp-bg-light); border:1px solid var(--sp-gray-border);"
						>
							{product.emoji}
						</div>
						<div class="flex flex-col items-end gap-1">
							{#each product.tags as tag}
								{#if tag === 'Populer'}<span class="badge-popular">{tag}</span>
								{:else if tag === 'Baru'}<span class="badge-new">{tag}</span>
								{/if}
							{/each}
						</div>
					</div>
					<div class="flex-1">
						<h3 class="font-display mb-1 text-base font-bold" style="color:var(--sp-navy);">
							{product.name}
						</h3>
						<p class="text-xs leading-relaxed" style="color:var(--sp-gray);">{product.desc}</p>
					</div>
					<div>
						<a
							href={waProduct(product.name)}
							target="_blank"
							class="font-display block w-full rounded-xl py-2.5 text-center text-sm font-semibold transition-all duration-200 hover:-translate-y-0.5"
							style="background:var(--sp-bg-light); border:1.5px solid rgba(59,130,246,0.3); color:var(--sp-blue);"
							onmouseenter={(e) => {
								e.currentTarget.style.background = 'var(--sp-gradient-blue)';
								e.currentTarget.style.color = '#fff';
								e.currentTarget.style.borderColor = 'transparent';
							}}
							onmouseleave={(e) => {
								e.currentTarget.style.background = 'var(--sp-bg-light)';
								e.currentTarget.style.color = 'var(--sp-blue)';
								e.currentTarget.style.borderColor = 'rgba(59,130,246,0.3)';
							}}
						>
							💬 Pesan Sekarang
						</a>
					</div>
				</div>
			{/each}
		</div>

		<!-- CTA to full catalog -->
		<div class="sp-reveal mt-12 text-center">
			<p class="mb-5 text-base" style="color:var(--sp-gray);">
				Baru menampilkan <strong style="color:var(--sp-blue);">{teaserProducts.length}</strong>
				produk populer dari total
				<strong style="color:var(--sp-navy);">{allProducts.length}+ produk</strong> kami.
			</p>
			<a href="/katalog" class="btn-primary-sp inline-flex items-center gap-2 text-sm">
				Lihat Semua Katalog
			</a>
		</div>
	</div>
</section>

<style>
	.cat-pill {
		display: inline-flex;
		align-items: center;
		gap: 5px;
		padding: 6px 14px;
		border-radius: 100px;
		font-size: 0.8rem;
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
