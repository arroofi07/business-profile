<script lang="ts">
	import { allProducts, categories, waProduct } from '$lib/data';

	let searchQuery = $state('');
	let activeCategory = $state('semua');
	let sortOrder = $state('populer');

	const filteredProducts = $derived(() => {
		let list = allProducts.filter((p) => {
			const matchCat = activeCategory === 'semua' || p.category === activeCategory;
			const matchSearch =
				p.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
				p.desc.toLowerCase().includes(searchQuery.toLowerCase());
			return matchCat && matchSearch;
		});
		if (sortOrder === 'populer')
			list = [...list].sort(
				(a, b) => (b.tags.includes('Populer') ? 1 : 0) - (a.tags.includes('Populer') ? 1 : 0)
			);
		else if (sortOrder === 'baru')
			list = [...list].sort(
				(a, b) => (b.tags.includes('Baru') ? 1 : 0) - (a.tags.includes('Baru') ? 1 : 0)
			);
		return list;
	});
</script>

<section id="produk" class="py-24" style="background:var(--sp-bg-white);">
	<div class="mx-auto max-w-7xl px-6">
		<div class="sp-reveal mb-12 text-center">
			<div class="section-chip mb-4">KATALOG PRODUK</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Semua Solusi Cetak <span class="gradient-text-blue">Anda</span>
			</h2>
			<p class="mx-auto max-w-xl" style="color:var(--sp-gray);">
				Temukan produk yang Anda butuhkan. Kualitas premium, harga bersaing.
			</p>
		</div>

		<!-- Search + Sort -->
		<div class="mb-6 flex flex-col gap-4 md:flex-row">
			<div class="relative flex-1">
				<span class="absolute top-1/2 left-4 -translate-y-1/2 text-lg">🔍</span>
				<input
					type="text"
					bind:value={searchQuery}
					placeholder="Cari produk cetak..."
					class="w-full rounded-xl py-3.5 pr-4 pl-12 text-sm font-medium transition-all duration-300 outline-none"
					style="background:var(--sp-bg-off); border:1.5px solid var(--sp-gray-border); color:var(--sp-text-dark); font-family:'Plus Jakarta Sans',sans-serif;"
					onfocus={(e) => {
						e.currentTarget.style.borderColor = 'var(--sp-blue-mid)';
						e.currentTarget.style.boxShadow = '0 0 0 3px rgba(59,130,246,0.12)';
					}}
					onblur={(e) => {
						e.currentTarget.style.borderColor = 'var(--sp-gray-border)';
						e.currentTarget.style.boxShadow = 'none';
					}}
				/>
			</div>
			<select
				bind:value={sortOrder}
				class="cursor-pointer rounded-xl px-4 py-3.5 text-sm font-medium outline-none"
				style="background:var(--sp-bg-off); border:1.5px solid var(--sp-gray-border); color:var(--sp-text-dark); min-width:160px; font-family:'Plus Jakarta Sans',sans-serif;"
			>
				<option value="populer">⭐ Terpopuler</option>
				<option value="baru">🆕 Terbaru</option>
				<option value="default">🔤 Default</option>
			</select>
		</div>

		<!-- Category filter -->
		<div class="-mx-6 mb-10 overflow-x-auto px-6 sm:mx-0 sm:px-0">
			<div class="flex gap-2 pb-2 sm:flex-wrap sm:pb-0" style="min-width:max-content;">
				{#each categories as cat}
					<button
						onclick={() => (activeCategory = cat.key)}
						class="font-display shrink-0 cursor-pointer rounded-full px-5 py-2 text-sm font-semibold transition-all duration-200"
						style={activeCategory === cat.key
							? 'background:var(--sp-gradient-blue); color:#fff; box-shadow:var(--sp-shadow-blue);'
							: 'background:var(--sp-bg-off); color:var(--sp-gray); border:1.5px solid var(--sp-gray-border);'}
					>
						{cat.label}
					</button>
				{/each}
			</div>
		</div>

		<!-- Grid -->
		{#if filteredProducts().length === 0}
			<div class="py-20 text-center">
				<div class="mb-4 text-5xl">🔍</div>
				<div class="font-display mb-2 text-xl font-bold" style="color:var(--sp-navy);">
					Produk tidak ditemukan
				</div>
				<div style="color:var(--sp-gray);">Coba kata kunci atau kategori lain</div>
			</div>
		{:else}
			<div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
				{#each filteredProducts() as product, i (product.id)}
					<div
						class="card-sp sp-reveal flex flex-col gap-4 p-6"
						style="transition-delay: {(i % 4) * 50}ms;"
					>
						<div class="flex items-start justify-between">
							<div
								class="flex h-14 w-14 items-center justify-center rounded-xl text-3xl"
								style="background:var(--sp-bg-light);"
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
							<div
								class="mb-3 text-sm font-bold"
								style="color:var(--sp-blue); font-family:'Outfit',sans-serif;"
							>
								{product.price}
							</div>
							<a
								href={waProduct(product.name)}
								target="_blank"
								class="font-display block w-full rounded-xl py-2.5 text-center text-sm font-semibold transition-all duration-200 hover:-translate-y-0.5"
								style="background:var(--sp-bg-light); border:1.5px solid rgba(59,130,246,0.3); color:var(--sp-blue);"
								onmouseenter={(e) => {
									e.currentTarget.style.background = 'var(--sp-gradient-blue)';
									e.currentTarget.style.color = '#fff';
								}}
								onmouseleave={(e) => {
									e.currentTarget.style.background = 'var(--sp-bg-light)';
									e.currentTarget.style.color = 'var(--sp-blue)';
								}}
							>
								💬 Pesan Sekarang
							</a>
						</div>
					</div>
				{/each}
			</div>
			<p class="mt-8 text-center text-sm" style="color:var(--sp-gray);">
				Menampilkan <span style="color:var(--sp-blue); font-weight:700;"
					>{filteredProducts().length}</span
				>
				dari {allProducts.length} produk
			</p>
		{/if}
	</div>
</section>
