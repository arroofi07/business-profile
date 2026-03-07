<script lang="ts">
	import { onMount } from 'svelte';
	import { allProducts, categories, waProduct, waGeneral } from '$lib/data';
	import Navbar from '$lib/components/sections/Navbar.svelte';
	import Footer from '$lib/components/sections/Footer.svelte';

	// ── Reactive state ──
	let searchQuery = $state('');
	let activeCategory = $state('all');
	let currentPage = $state(1);
	const PER_PAGE = 12;

	// ── Correct Svelte 5 $derived: expression, NOT a function wrapper ──
	const filteredProducts = $derived(
		allProducts.filter((p) => {
			const matchCat = activeCategory === 'all' || p.category === activeCategory;
			const q = searchQuery.trim().toLowerCase();
			const matchSearch =
				q === '' || p.name.toLowerCase().includes(q) || p.desc.toLowerCase().includes(q);
			return matchCat && matchSearch;
		})
	);

	// Reset to page 1 whenever filter/search changes
	$effect(() => {
		// Reading these makes the effect re-run when they change
		void searchQuery;
		void activeCategory;
		currentPage = 1;
	});

	// Pagination derived values
	const totalPages = $derived(Math.ceil(filteredProducts.length / PER_PAGE));
	const pagedProducts = $derived(
		filteredProducts.slice((currentPage - 1) * PER_PAGE, currentPage * PER_PAGE)
	);

	// Category counts (static — based on full product list, not filtered)
	const totalByCategory: Record<string, number> = {};
	categories.forEach((c) => {
		totalByCategory[c.key] =
			c.key === 'all' ? allProducts.length : allProducts.filter((p) => p.category === c.key).length;
	});

	function setCategory(key: string) {
		activeCategory = key;
	}

	function goPage(n: number) {
		if (n >= 1 && n <= totalPages) {
			currentPage = n;
			// Scroll to top of content area
			document
				.getElementById('catalog-content')
				?.scrollIntoView({ behavior: 'smooth', block: 'start' });
		}
	}

	onMount(() => {
		requestAnimationFrame(() => {
			document.body.classList.add('js-ready');
			const revealObs = new IntersectionObserver(
				(entries) => {
					entries.forEach((e) => {
						if (e.isIntersecting) {
							e.target.classList.add('sp-visible');
							revealObs.unobserve(e.target);
						}
					});
				},
				{ threshold: 0.05, rootMargin: '0px 0px -20px 0px' }
			);
			document.querySelectorAll('.sp-reveal').forEach((el) => revealObs.observe(el));
			return () => revealObs.disconnect();
		});
	});
</script>

<svelte:head>
	<title>Our Services | Aldinga Plumbing Services</title>
	<meta
		name="description"
		content="Explore the full range of plumbing services offered by Aldinga Plumbing Services. 24/7 emergency response, blocked drains, hot water systems, and more."
	/>
	<link rel="canonical" href="https://aldingaplumbing.com.au/katalog" />
</svelte:head>

<Navbar />

<main class="katalog-page">
	<!-- ── HERO HEADER ── -->

	<div class="relative z-10 mx-auto max-w-7xl px-2 py-7 text-center md:px-6 md:py-12">
		<div class="section-chip mb-0">FULL SERVICE CATALOG</div>
	</div>

	<!-- ── MAIN CONTENT ── -->
	<section class="katalog-body">
		<div class="mx-auto max-w-7xl px-4 py-6 md:px-6 md:py-12">
			<div class="katalog-layout">
				<!-- ── SIDEBAR (Desktop) ── -->
				<aside class="katalog-sidebar">
					<div class="sidebar-card">
						<div class="sidebar-title">Categories</div>
						{#each categories as cat}
							<button
								onclick={() => setCategory(cat.key)}
								class="sidebar-cat-btn"
								class:sidebar-cat-btn--active={activeCategory === cat.key}
							>
								<span class="sidebar-cat-icon">{cat.icon}</span>
								<span class="sidebar-cat-label">{cat.label}</span>
								<span class="sidebar-cat-count">{totalByCategory[cat.key]}</span>
							</button>
						{/each}

						<!-- WA CTA -->
						<div class="sidebar-cta">
							<div class="sidebar-cta-title font-display">Need Advice?</div>
							<p class="sidebar-cta-desc">Our team is ready to help you with any plumbing issue.</p>
							<a href={waGeneral} target="_blank" class="btn-whatsapp sidebar-cta-btn">
								<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"
									><path
										d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"
									/><path
										d="M11.5 2.5C6.262 2.5 2 6.762 2 12c0 1.912.553 3.697 1.508 5.202L2.07 21.5l4.438-1.428A9.45 9.45 0 0 0 11.5 21.5c5.238 0 9.5-4.262 9.5-9.5S16.738 2.5 11.5 2.5z"
										opacity=".3"
									/></svg
								>
								Chat on WhatsApp
							</a>
						</div>
					</div>
				</aside>

				<!-- ── RIGHT PANEL ── -->
				<div class="katalog-content" id="catalog-content">
					<!-- Search + mobile category tabs -->
					<div class="katalog-topbar">
						<div class="search-wrap">
							<span class="search-icon">
								<svg
									width="16"
									height="16"
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2.5"
									stroke-linecap="round"
									stroke-linejoin="round"
									><circle cx="11" cy="11" r="8" /><path d="m21 21-4.35-4.35" /></svg
								>
							</span>
							<input
								type="text"
								bind:value={searchQuery}
								placeholder="Search services... (e.g. drains, hot water)"
								class="search-input"
								id="catalog-search"
							/>
							{#if searchQuery}
								<button class="search-clear" onclick={() => (searchQuery = '')}>✕</button>
							{/if}
						</div>

						<!-- Mobile category tabs -->
						<div class="mobile-cats">
							{#each categories as cat}
								<button
									onclick={() => (activeCategory = cat.key)}
									class="mobile-cat-btn"
									class:mobile-cat-btn--active={activeCategory === cat.key}
								>
									{cat.icon}
									{cat.label}
									<span class="mobile-cat-count">{totalByCategory[cat.key]}</span>
								</button>
							{/each}
						</div>
					</div>

					<!-- Result header -->
					<div class="result-header">
						<div class="result-count">
							<span class="result-count-num font-display">{filteredProducts.length}</span>
							<span class="result-count-text">services found</span>
							{#if activeCategory !== 'all'}
								<span class="result-cat-badge">
									{categories.find((c) => c.key === activeCategory)?.icon}
									{categories.find((c) => c.key === activeCategory)?.label}
								</span>
							{/if}
							{#if searchQuery.trim()}
								<span class="result-query-badge">"{searchQuery}"</span>
							{/if}
						</div>
						{#if totalPages > 1}
							<div class="result-page-info">Page {currentPage} of {totalPages}</div>
						{/if}
					</div>

					<!-- ── PRODUCT GRID ── -->
					{#if filteredProducts.length === 0}
						<div class="empty-state">
							<div class="empty-state-icon">🔍</div>
							<div class="empty-state-title font-display">No services found</div>
							<div class="empty-state-desc">Try a different keyword or category</div>
							<button
								class="btn-primary-sp mt-6"
								onclick={() => {
									searchQuery = '';
									activeCategory = 'all';
								}}>Reset Filters</button
							>
						</div>
					{:else}
						<div class="product-grid">
							{#each pagedProducts as product, i (product.id)}
								<div class="product-card" style="animation-delay: {(i % 6) * 50}ms;">
									<div class="product-card__header">
										<div class="product-card__emoji">{product.emoji}</div>
										<div class="product-card__tags">
											{#each product.tags as tag}
												{#if tag === 'Popular'}<span class="badge-popular">{tag}</span>
												{:else if tag === 'Urgent'}<span
														class="badge-new"
														style="background:rgba(239,68,68,0.1); border-color:#EF4444; color:#EF4444;"
														>{tag}</span
													>
												{:else}<span class="badge-new">{tag}</span>
												{/if}
											{/each}
										</div>
									</div>
									<div class="product-card__body">
										<h3 class="product-card__name font-display">{product.name}</h3>
										<p class="product-card__desc">{product.desc}</p>
									</div>
									<div class="product-card__footer">
										<a
											href={waProduct(product.name)}
											target="_blank"
											class="product-card__order-btn font-display"
										>
											💬 Request Service
										</a>
									</div>
								</div>
							{/each}
						</div>

						<!-- ── PAGINATION ── -->
						{#if totalPages > 1}
							<div class="pagination">
								<button
									class="page-btn page-btn--nav"
									disabled={currentPage === 1}
									onclick={() => goPage(currentPage - 1)}
									aria-label="Previous page"
								>
									← Previous
								</button>

								<div class="page-numbers">
									{#each Array.from({ length: totalPages }, (_, i) => i + 1) as page}
										{#if page === 1 || page === totalPages || Math.abs(page - currentPage) <= 1}
											<button
												class="page-btn"
												class:page-btn--active={page === currentPage}
												onclick={() => goPage(page)}>{page}</button
											>
										{:else if Math.abs(page - currentPage) === 2}
											<span class="page-ellipsis">…</span>
										{/if}
									{/each}
								</div>

								<button
									class="page-btn page-btn--nav"
									disabled={currentPage === totalPages}
									onclick={() => goPage(currentPage + 1)}
									aria-label="Next page"
								>
									Next →
								</button>
							</div>
						{/if}
					{/if}
				</div>
			</div>
		</div>
	</section>

	<!-- ── BOTTOM CTA ── -->
	<section class="katalog-cta">
		<div class="mx-auto max-w-3xl px-4 py-12 text-center md:px-6 md:py-20">
			<div
				class="section-chip mb-5"
				style="background:rgba(255,255,255,0.15); border-color:rgba(255,255,255,0.3); color:#fff;"
			>
				CONTACT US
			</div>
			<h2 class="font-display mb-4 text-3xl font-bold text-white">
				Can't find what you're looking for?
			</h2>
			<p class="mb-8 text-blue-100">
				Our team is ready to consult and help with any plumbing emergency.
			</p>
			<a
				href={waGeneral}
				target="_blank"
				class="btn-whatsapp inline-flex items-center gap-3 px-8 py-4 text-base"
			>
				💬 Chat on WhatsApp
			</a>
		</div>
	</section>
</main>

<Footer />

<style>
	/* ── Page wrapper ── */
	.katalog-page {
		padding-top: var(--nav-height);
		min-height: 100vh;
	}

	/* ── Hero ── */
	.katalog-hero {
		position: relative;
		overflow: hidden;
		background: var(--sp-gradient-hero);
		border-bottom: 1px solid rgba(59, 130, 246, 0.12);
	}

	.katalog-hero__bg-grid {
		position: absolute;
		inset: 0;
		background-image:
			linear-gradient(rgba(59, 130, 246, 0.06) 1px, transparent 1px),
			linear-gradient(90deg, rgba(59, 130, 246, 0.06) 1px, transparent 1px);
		background-size: 40px 40px;
		pointer-events: none;
	}

	.blob {
		position: absolute;
		border-radius: 50%;
		filter: blur(72px);
		opacity: 0.35;
		pointer-events: none;
	}
	.blob-1 {
		width: 480px;
		height: 480px;
		background: radial-gradient(circle, #bfdbfe, #dbeafe);
		top: -120px;
		left: -100px;
	}
	.blob-2 {
		width: 360px;
		height: 360px;
		background: radial-gradient(circle, #bae6fd, #e0f2fe);
		bottom: -80px;
		right: -60px;
	}

	.katalog-hero__title {
		font-size: clamp(2.2rem, 5vw, 3.5rem);
		font-weight: 800;
		color: var(--sp-navy);
		margin-bottom: 1rem;
		line-height: 1.15;
	}

	.katalog-hero__subtitle {
		font-size: 1.1rem;
		color: var(--sp-gray);
		max-width: 560px;
		margin: 0 auto 2.5rem;
		line-height: 1.7;
	}

	.back-link {
		display: inline-flex;
		align-items: center;
		gap: 6px;
		font-size: 0.85rem;
		font-weight: 600;
		color: var(--sp-blue);
		text-decoration: none;
		transition: gap 0.2s;
	}
	.back-link:hover {
		gap: 2px;
	}

	/* ── Stats ── */
	.katalog-stats {
		display: flex;
		justify-content: center;
		gap: 2.5rem;
		flex-wrap: wrap;
		margin-top: 2rem;
	}
	.katalog-stat-item {
		text-align: center;
	}
	.katalog-stat-val {
		font-size: 2rem;
		font-weight: 800;
		color: var(--sp-navy);
		line-height: 1;
	}
	.katalog-stat-label {
		font-size: 0.78rem;
		color: var(--sp-gray);
		margin-top: 4px;
		font-weight: 500;
	}

	/* ── Main layout ── */
	.katalog-body {
		background: var(--sp-bg-section);
	}

	.katalog-layout {
		display: grid;
		grid-template-columns: 260px 1fr;
		gap: 2rem;
		align-items: start;
	}

	/* ── Sidebar ── */
	.katalog-sidebar {
		position: sticky;
		top: calc(var(--nav-height) + 24px);
	}

	.sidebar-card {
		background: #fff;
		border: 1px solid var(--sp-gray-border);
		border-radius: 20px;
		padding: 1.5rem;
		box-shadow: var(--sp-shadow-sm);
		display: flex;
		flex-direction: column;
		gap: 6px;
	}

	.sidebar-title {
		font-family: 'Outfit', sans-serif;
		font-size: 0.72rem;
		font-weight: 700;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--sp-gray);
		margin-bottom: 8px;
		padding-bottom: 10px;
		border-bottom: 1px solid var(--sp-gray-border);
	}

	.sidebar-cat-btn {
		display: flex;
		align-items: center;
		gap: 10px;
		width: 100%;
		text-align: left;
		padding: 10px 12px;
		border-radius: 12px;
		border: none;
		cursor: pointer;
		background: transparent;
		color: var(--sp-gray);
		font-size: 0.88rem;
		font-weight: 500;
		font-family: 'Plus Jakarta Sans', sans-serif;
		transition: all 0.2s ease;
	}
	.sidebar-cat-btn:hover {
		background: var(--sp-bg-off);
		color: var(--sp-navy);
	}
	.sidebar-cat-btn--active {
		background: var(--sp-bg-light) !important;
		color: var(--sp-blue) !important;
		font-weight: 700;
	}
	.sidebar-cat-icon {
		font-size: 1.1rem;
		flex-shrink: 0;
	}
	.sidebar-cat-label {
		flex: 1;
	}
	.sidebar-cat-count {
		background: var(--sp-bg-off);
		color: var(--sp-gray);
		font-size: 0.72rem;
		font-weight: 700;
		font-family: 'Outfit', sans-serif;
		padding: 2px 7px;
		border-radius: 20px;
		min-width: 24px;
		text-align: center;
	}
	.sidebar-cat-btn--active .sidebar-cat-count {
		background: rgba(29, 78, 216, 0.12);
		color: var(--sp-blue);
	}

	/* ── Sidebar CTA ── */
	.sidebar-cta {
		margin-top: 16px;
		padding: 16px;
		border-radius: 14px;
		background: var(--sp-gradient-blue);
		color: #fff;
	}
	.sidebar-cta-title {
		font-size: 0.95rem;
		font-weight: 700;
		margin-bottom: 6px;
	}
	.sidebar-cta-desc {
		font-size: 0.78rem;
		opacity: 0.85;
		margin-bottom: 12px;
		line-height: 1.5;
	}
	.sidebar-cta-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		width: 100%;
		padding: 10px 16px;
		font-size: 0.85rem;
	}

	/* ── Content area ── */
	.katalog-content {
		min-width: 0;
	}

	/* ── Topbar ── */
	.katalog-topbar {
		margin-bottom: 1.5rem;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.search-wrap {
		position: relative;
		display: flex;
		align-items: center;
	}
	.search-icon {
		position: absolute;
		left: 16px;
		color: var(--sp-gray);
		display: flex;
		align-items: center;
		pointer-events: none;
	}
	.search-input {
		width: 100%;
		padding: 13px 44px 13px 46px;
		border-radius: 14px;
		border: 1.5px solid var(--sp-gray-border);
		background: #fff;
		font-size: 0.92rem;
		font-family: 'Plus Jakarta Sans', sans-serif;
		color: var(--sp-text-dark);
		outline: none;
		transition:
			border-color 0.2s,
			box-shadow 0.2s;
		box-shadow: var(--sp-shadow-sm);
	}
	.search-input:focus {
		border-color: var(--sp-blue-mid);
		box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.14);
	}
	.search-input::placeholder {
		color: var(--sp-gray-light);
	}
	.search-clear {
		position: absolute;
		right: 14px;
		background: var(--sp-bg-off);
		border: none;
		cursor: pointer;
		color: var(--sp-gray);
		font-size: 0.75rem;
		width: 22px;
		height: 22px;
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		transition: background 0.2s;
	}
	.search-clear:hover {
		background: var(--sp-bg-light);
		color: var(--sp-blue);
	}

	/* Mobile category tabs — hidden on desktop */
	.mobile-cats {
		display: none;
		gap: 8px;
		overflow-x: auto;
		padding-bottom: 8px;
		scroll-snap-type: x mandatory;
		-webkit-overflow-scrolling: touch;
		scrollbar-width: none;
	}
	.mobile-cats::-webkit-scrollbar {
		display: none;
	}
	.mobile-cat-btn {
		flex-shrink: 0;
		display: inline-flex;
		align-items: center;
		gap: 5px;
		white-space: nowrap;
		padding: 8px 16px;
		border-radius: 100px;
		border: 1.5px solid var(--sp-gray-border);
		background: #fff;
		color: var(--sp-gray);
		font-size: 0.82rem;
		font-weight: 600;
		font-family: 'Plus Jakarta Sans', sans-serif;
		cursor: pointer;
		transition: all 0.2s;
		scroll-snap-align: start;
	}
	.mobile-cat-btn:hover {
		border-color: var(--sp-blue-mid);
		color: var(--sp-blue);
	}
	.mobile-cat-btn--active {
		background: var(--sp-gradient-blue);
		border-color: transparent;
		color: #fff;
	}
	.mobile-cat-count {
		background: rgba(255, 255, 255, 0.25);
		border-radius: 10px;
		padding: 1px 6px;
		font-size: 0.7rem;
		font-weight: 700;
	}
	.mobile-cat-btn:not(.mobile-cat-btn--active) .mobile-cat-count {
		background: var(--sp-bg-off);
		color: var(--sp-gray);
	}

	/* ── Result header ── */
	.result-header {
		margin-bottom: 1.25rem;
	}
	.result-count {
		display: flex;
		align-items: center;
		gap: 8px;
		flex-wrap: wrap;
	}
	.result-count-num {
		font-size: 1.5rem;
		font-weight: 800;
		color: var(--sp-navy);
		line-height: 1;
	}
	.result-count-text {
		font-size: 0.9rem;
		color: var(--sp-gray);
		font-weight: 500;
	}
	.result-cat-badge {
		background: var(--sp-bg-light);
		color: var(--sp-blue);
		font-size: 0.78rem;
		font-weight: 700;
		padding: 3px 10px;
		border-radius: 20px;
		border: 1px solid rgba(59, 130, 246, 0.25);
	}
	.result-query-badge {
		background: rgba(249, 115, 22, 0.08);
		color: var(--sp-orange);
		font-size: 0.78rem;
		font-weight: 700;
		padding: 3px 10px;
		border-radius: 20px;
		border: 1px solid rgba(249, 115, 22, 0.2);
	}

	/* ── Product Grid ── */
	.product-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 1.25rem;
	}

	/* ── Product Card ── */
	.product-card {
		background: #fff;
		border: 1px solid var(--sp-gray-border);
		border-radius: 18px;
		padding: 1.5rem;
		display: flex;
		flex-direction: column;
		gap: 14px;
		box-shadow: var(--sp-shadow-sm);
		transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
	}
	.product-card:hover {
		border-color: rgba(59, 130, 246, 0.35);
		box-shadow: var(--sp-shadow-lg);
		transform: translateY(-4px);
	}

	.product-card__header {
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
	}
	.product-card__emoji {
		width: 56px;
		height: 56px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: var(--sp-bg-off);
		border-radius: 14px;
		font-size: 1.75rem;
		border: 1px solid var(--sp-gray-border);
		flex-shrink: 0;
	}
	.product-card__tags {
		display: flex;
		flex-direction: column;
		align-items: flex-end;
		gap: 4px;
	}

	.product-card__body {
		flex: 1;
	}
	.product-card__name {
		font-size: 1rem;
		font-weight: 700;
		color: var(--sp-navy);
		margin-bottom: 6px;
		line-height: 1.3;
	}
	.product-card__desc {
		font-size: 0.82rem;
		color: var(--sp-gray);
		line-height: 1.65;
	}

	.product-card__footer {
		margin-top: auto;
	}
	.product-card__order-btn {
		display: block;
		width: 100%;
		text-align: center;
		padding: 10px 16px;
		border-radius: 12px;
		border: 1.5px solid rgba(59, 130, 246, 0.3);
		background: var(--sp-bg-light);
		color: var(--sp-blue);
		font-size: 0.85rem;
		font-weight: 600;
		text-decoration: none;
		transition: all 0.22s ease;
	}
	.product-card__order-btn:hover {
		background: var(--sp-gradient-blue);
		border-color: transparent;
		color: #fff;
		transform: translateY(-1px);
		box-shadow: var(--sp-shadow-blue);
	}

	/* ── Empty state ── */
	.empty-state {
		text-align: center;
		padding: 6rem 2rem;
	}
	.empty-state-icon {
		font-size: 4rem;
		margin-bottom: 1rem;
	}
	.empty-state-title {
		font-size: 1.4rem;
		font-weight: 700;
		color: var(--sp-navy);
		margin-bottom: 8px;
	}
	.empty-state-desc {
		color: var(--sp-gray);
		font-size: 0.95rem;
	}

	/* ── Bottom CTA ── */
	.katalog-cta {
		background: var(--sp-gradient-dark);
		position: relative;
		overflow: hidden;
	}
	.katalog-cta::before {
		content: '';
		position: absolute;
		inset: 0;
		background-image: radial-gradient(circle, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
		background-size: 28px 28px;
	}

	/* ── Responsive ── */
	@media (max-width: 1024px) {
		.katalog-layout {
			grid-template-columns: 220px 1fr;
		}
		.product-grid {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 768px) {
		.katalog-layout {
			grid-template-columns: 1fr;
		}
		.katalog-sidebar {
			display: none;
		}
		.katalog-topbar {
			position: sticky;
			top: var(--nav-height, 70px);
			z-index: 40;
			background: var(--sp-bg-section);
			padding: 1rem 0;
			margin-top: -1rem;
		}
		.mobile-cats {
			display: flex;
		}
		.product-grid {
			grid-template-columns: repeat(2, 1fr);
			gap: 1rem;
		}
		.katalog-hero__title {
			font-size: 2rem;
		}
		.katalog-stats {
			gap: 1.5rem;
		}
		.katalog-stat-val {
			font-size: 1.5rem;
		}
	}

	@media (max-width: 480px) {
		.product-grid {
			grid-template-columns: repeat(2, 1fr);
			gap: 0.75rem;
		}
		.product-card {
			padding: 1rem;
			gap: 10px;
		}
		.product-card__header {
			flex-direction: column;
			align-items: flex-start;
			gap: 8px;
		}
		.product-card__tags {
			align-items: flex-start;
		}
		.product-card__emoji {
			width: 42px;
			height: 42px;
			font-size: 1.25rem;
			border-radius: 10px;
		}
		.product-card__name {
			font-size: 0.85rem;
			margin-bottom: 2px;
		}
		.product-card__desc {
			font-size: 0.75rem;
			line-height: 1.4;
			display: -webkit-box;
			-webkit-line-clamp: 2;
			line-clamp: 2;
			-webkit-box-orient: vertical;
			overflow: hidden;
		}
		.product-card__order-btn {
			font-size: 0.75rem;
			padding: 8px 10px;
			border-radius: 10px;
		}
		.katalog-hero__title {
			font-size: 1.75rem;
		}
		.katalog-stat-val {
			font-size: 1.25rem;
		}
		.empty-state-icon {
			font-size: 3rem;
		}
		.empty-state-title {
			font-size: 1.2rem;
		}
	}
	/* ── Result header ── */
	.result-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		flex-wrap: wrap;
		gap: 8px;
		margin-bottom: 1.25rem;
	}
	.result-page-info {
		font-size: 0.82rem;
		font-weight: 600;
		color: var(--sp-gray);
		font-family: 'Outfit', sans-serif;
	}

	/* ── Pagination ── */
	.pagination {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		margin-top: 2.5rem;
		flex-wrap: wrap;
	}
	.page-numbers {
		display: flex;
		align-items: center;
		gap: 4px;
	}
	.page-btn {
		min-width: 38px;
		height: 38px;
		padding: 0 10px;
		border-radius: 10px;
		border: 1.5px solid var(--sp-gray-border);
		background: #fff;
		color: var(--sp-gray);
		font-size: 0.88rem;
		font-weight: 600;
		font-family: 'Outfit', sans-serif;
		cursor: pointer;
		transition: all 0.2s ease;
		display: inline-flex;
		align-items: center;
		justify-content: center;
	}
	.page-btn:hover:not(:disabled) {
		border-color: var(--sp-blue-mid);
		color: var(--sp-blue);
		background: var(--sp-bg-off);
	}
	.page-btn:disabled {
		opacity: 0.38;
		cursor: not-allowed;
	}
	.page-btn--active {
		background: var(--sp-gradient-blue) !important;
		border-color: transparent !important;
		color: #fff !important;
		box-shadow: var(--sp-shadow-blue);
	}
	.page-btn--nav {
		padding: 0 16px;
		font-size: 0.82rem;
		gap: 4px;
	}
	.page-ellipsis {
		color: var(--sp-gray);
		padding: 0 4px;
		font-size: 0.9rem;
		user-select: none;
	}

	/* ── Card entrance animation ── */
	@keyframes card-in {
		from {
			opacity: 0;
			transform: translateY(16px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}
	.product-card {
		animation: card-in 0.4s cubic-bezier(0.16, 1, 0.3, 1) both;
	}
</style>
