<script lang="ts">
	import { waGeneral } from '$lib/data';
</script>

<section
	id="hero"
	class="relative flex min-h-screen items-center overflow-hidden"
	style="background: url('/plumber-hero.png') center/cover no-repeat; padding-top:var(--nav-height);"
>
	<!-- Dark corporate overlay for text legibility -->
	<div
		class="absolute inset-0"
		style="background: linear-gradient(to right, rgba(15, 23, 42, 0.95) 20%, rgba(15, 23, 42, 0.6) 100%); z-index: 1;"
	></div>

	<div
		class="relative z-10 mx-auto grid w-full max-w-7xl items-center gap-12 px-6 py-12 lg:grid-cols-2 lg:gap-16 lg:py-24"
	>
		<!-- Left copy -->
		<div>
			<div class="animate-slide-up mb-6 inline-flex items-center gap-3">
				<span class="inline-block h-3 w-3 rounded-sm" style="background:var(--sp-orange);"></span>
				<span class="text-xs font-bold tracking-widest text-slate-300 uppercase"
					>24/7 Emergency Response</span
				>
			</div>
			<h1
				class="font-display animate-slide-up mb-6 leading-tight font-extrabold delay-100"
				style="font-size:clamp(2.4rem,5.5vw,4.2rem); color:var(--sp-white);"
			>
				Expert Plumbing <br />
				<span style="color:var(--sp-orange);">Services & Repairs</span><br />
				in Aldinga Beach.
			</h1>
			<p
				class="animate-slide-up mb-8 max-w-lg text-lg delay-200"
				style="color:var(--sp-gray-light); line-height:1.7;"
			>
				Fully licensed and insured professionals providing upfront pricing and rapid response times
				for all your residential and commercial plumbing needs.
			</p>

			<div class="animate-slide-up flex flex-col gap-4 delay-300 sm:flex-row">
				<a
					href="tel:+61459529693"
					class="btn-whatsapp w-full text-center shadow-lg sm:w-auto"
					style="padding: 16px 32px; font-size: 15px;"
				>
					CALL +61 459 529 693
				</a>
				<a
					href={waGeneral}
					target="_blank"
					class="btn-primary-sp flex w-full items-center justify-center gap-2 text-center transition-colors sm:w-auto"
					style="padding: 16px 32px; border-color: rgba(255,255,255,0.2); background: rgba(255,255,255,0.05); color: #fff; font-size: 15px;"
					onmouseenter={(e) => (e.currentTarget.style.background = 'rgba(255,255,255,0.1)')}
					onmouseleave={(e) => (e.currentTarget.style.background = 'rgba(255,255,255,0.05)')}
				>
					REQUEST QUOTE
				</a>
			</div>

			<!-- Trust Badges -->
			<div class="animate-slide-up mt-12 flex flex-wrap gap-8 delay-400">
				{#each [{ icon: '🛡️', title: 'Fully Licensed', desc: 'Local Experts' }, { icon: '⚡', title: 'Fast Response', desc: 'Rapid Dispatch' }, { icon: '💰', title: 'Upfront Pricing', desc: 'No hidden fees' }] as badge}
					<div class="flex items-start gap-3">
						<div
							class="flex h-10 w-10 items-center justify-center rounded border border-slate-700 bg-slate-800 text-xl"
						>
							{badge.icon}
						</div>
						<div>
							<div class="text-sm font-bold tracking-wide text-white">{badge.title}</div>
							<div class="mt-0.5 text-xs text-slate-400">{badge.desc}</div>
						</div>
					</div>
				{/each}
			</div>
		</div>

		<!-- Right Side Image/Card -->
		<div class="animate-slide-left hidden justify-end delay-300 lg:flex">
			<div class="relative w-full max-w-md">
				<!-- Solid Corporate Card -->
				<div
					class="relative flex flex-col gap-6 overflow-hidden rounded p-8 shadow-2xl"
					style="background:var(--sp-bg-white); border: 2px solid var(--sp-blue);"
				>
					<!-- Accent strip -->
					<div class="absolute top-0 left-0 h-1 w-full" style="background:var(--sp-orange);"></div>

					<div class="border-b border-slate-200 pb-4">
						<h3 class="font-display text-2xl font-extrabold text-slate-900 uppercase">
							Why Choose Us?
						</h3>
						<p class="mt-2 text-sm font-semibold text-slate-500">Local expertise you can trust.</p>
					</div>

					<ul class="flex flex-col gap-4 text-sm font-bold text-slate-700">
						<li class="flex items-center gap-3">
							<span
								class="flex h-6 w-6 items-center justify-center rounded border border-green-200 bg-green-50 text-xs text-green-600"
								>✓</span
							> Local Aldinga Beach Experts
						</li>
						<li class="flex items-center gap-3">
							<span
								class="flex h-6 w-6 items-center justify-center rounded border border-green-200 bg-green-50 text-xs text-green-600"
								>✓</span
							> Family Owned and Operated
						</li>
						<li class="flex items-center gap-3">
							<span
								class="flex h-6 w-6 items-center justify-center rounded border border-green-200 bg-green-50 text-xs text-green-600"
								>✓</span
							> 100% Satisfaction Guarantee
						</li>
						<li class="flex items-center gap-3">
							<span
								class="flex h-6 w-6 items-center justify-center rounded border border-green-200 bg-green-50 text-xs text-green-600"
								>✓</span
							> Over 15 Years Experience
						</li>
					</ul>

					<div class="mt-4 rounded border border-slate-200 bg-slate-50 p-4 text-center">
						<div class="mb-1 text-sm font-extrabold tracking-wider text-slate-800 uppercase">
							Commercial & Residential
						</div>
						<div class="text-xs font-semibold text-slate-500">No job is too big or too small.</div>
					</div>
				</div>

				<!-- Simple square decoration -->
				<div
					class="absolute -bottom-4 -left-4 h-16 w-16 border-2"
					style="border-color:rgba(255,255,255,0.1); z-index: -1;"
				></div>
			</div>
		</div>
	</div>
</section>
