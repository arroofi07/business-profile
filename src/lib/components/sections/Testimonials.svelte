<script lang="ts">
	import { testimonials } from '$lib/data';
</script>

<section class="py-24" style="background:var(--sp-bg-light);">
	<div class="mx-auto max-w-6xl px-6">
		<div class="sp-reveal mb-14 text-center">
			<div class="section-chip mb-4">TESTIMONI</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Kata Pelanggan <span class="gradient-text-blue">Kami</span>
			</h2>
		</div>
		<div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
			{#each testimonials as t, i}
				<div class="card-sp sp-reveal p-6" style="transition-delay: {(i % 3) * 100}ms;">
					<div class="mb-3 flex gap-0.5">
						{#each Array(t.stars) as _}<span style="color:#FBBF24;">★</span>{/each}
					</div>
					<p class="mb-4 text-sm leading-relaxed" style="color:var(--sp-text-mid);">"{t.text}"</p>
					<div class="flex items-center gap-3">
						<div
							class="flex h-10 w-10 items-center justify-center rounded-full text-sm font-bold text-white"
							style="background:var(--sp-gradient-blue);"
						>
							{t.name[0]}
						</div>
						<div>
							<div class="text-sm font-semibold" style="color:var(--sp-navy);">{t.name}</div>
							<div class="text-xs" style="color:var(--sp-gray);">{t.role}</div>
						</div>
					</div>
				</div>
			{/each}
		</div>
	</div>
</section>
