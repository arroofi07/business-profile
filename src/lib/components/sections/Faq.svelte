<script lang="ts">
	import { faqs } from '$lib/data';

	let openFaq = $state<number | null>(null);
</script>

<section class="py-24" style="background:var(--sp-bg-white);">
	<div class="mx-auto max-w-3xl px-6">
		<div class="sp-reveal mb-14 text-center">
			<div class="section-chip mb-4">FAQ</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(1.8rem,4vw,2.5rem); color:var(--sp-navy);"
			>
				Pertanyaan <span class="gradient-text-blue">Umum</span>
			</h2>
		</div>
		<div class="flex flex-col gap-3">
			{#each faqs as faq, i}
				<div
					class="sp-reveal overflow-hidden rounded-xl transition-all duration-200"
					style="{openFaq === i
						? 'border:2px solid var(--sp-blue); box-shadow:var(--sp-shadow-md);'
						: 'border:1.5px solid var(--sp-gray-border);'} transition-delay:{i * 50}ms;"
				>
					<button
						class="flex w-full items-center justify-between p-5 text-left"
						onclick={() => (openFaq = openFaq === i ? null : i)}
					>
						<span class="font-display text-base font-semibold" style="color:var(--sp-navy);"
							>{faq.q}</span
						>
						<span
							class="text-xl font-bold transition-transform duration-200"
							style="color:var(--sp-blue); transform:{openFaq === i
								? 'rotate(45deg)'
								: 'rotate(0deg)'};">+</span
						>
					</button>
					{#if openFaq === i}
						<div
							class="animate-slide-down px-5 pb-5 text-sm leading-relaxed"
							style="color:var(--sp-gray);"
						>
							{faq.a}
						</div>
					{/if}
				</div>
			{/each}
		</div>
	</div>
</section>
