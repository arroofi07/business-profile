<section id="layanan" class="py-24" style="background:var(--sp-bg-section);">
	<div class="mx-auto max-w-7xl px-6">
		<div class="sp-reveal mb-16 text-center">
			<div class="section-chip mb-4">OUR SERVICES</div>
			<h2
				class="font-display mb-6 font-extrabold tracking-tight uppercase"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Professional <span style="color:var(--sp-orange);">Plumbing</span>
			</h2>
			<div class="mx-auto mb-6 h-1 w-16" style="background:var(--sp-orange);"></div>
			<p class="mx-auto max-w-xl text-lg font-medium" style="color:var(--sp-gray);">
				From minor repairs to major commercial installations, Aldinga Plumbing Services delivers
				top-quality workmanship every time.
			</p>
		</div>
		<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
			{#each [{ icon: '🚽', title: 'Blocked Drains', desc: 'Fast, efficient clearing of blocked toilets, sinks, and drains using high-pressure jetting and CCTV cameras.', color: 'var(--sp-orange)' }, { icon: '🔥', title: 'Hot Water Systems', desc: 'Installation, repair, and maintenance of all major brands of gas, electric, and solar hot water systems.', color: 'var(--sp-blue)' }, { icon: '💨', title: 'Gas Fitting', desc: 'Licensed gas fitting for appliances, leak detection, and safe installation of gas lines.', color: 'var(--sp-cyan)' }, { icon: '🚨', title: 'Emergency Plumbing', desc: '24/7 rapid response for burst pipes, flooding, or any urgent plumbing crisis.', color: 'var(--sp-orange-dim)' }, { icon: '🚰', title: 'Tap & Toilet Repairs', desc: 'Fixing leaks, replacing old tapware, and servicing running or broken toilets.', color: 'var(--sp-blue-mid)' }, { icon: '💧', title: 'Leak Detection', desc: 'Advanced hidden water leak detection to save water and prevent structural property damage.', color: 'var(--sp-green)' }] as s, i}
				<div
					class="sp-reveal group flex flex-col p-8 transition-transform hover:-translate-y-1"
					style="transition-delay: {i *
						50}ms; background:var(--sp-bg-white); border: 1px solid var(--sp-gray-border); border-top: 4px solid var(--sp-navy); border-radius: 4px; box-shadow: var(--sp-shadow-card);"
				>
					<div
						class="mb-6 flex h-16 w-16 items-center justify-center rounded bg-slate-100 text-3xl transition-colors group-hover:bg-slate-200"
					>
						{s.icon}
					</div>
					<h3
						class="font-display mb-3 text-xl font-extrabold text-slate-900 transition-colors group-hover:text-blue-700"
					>
						{s.title}
					</h3>
					<p class="mb-auto text-sm leading-relaxed font-medium text-slate-600">{s.desc}</p>

					<a
						href="/katalog"
						class="mt-6 flex items-center gap-2 text-sm font-bold transition-all group-hover:gap-3"
						style="color:var(--sp-blue);"
					>
						Learn More <span>→</span>
					</a>
				</div>
			{/each}
		</div>
	</div>
</section>
