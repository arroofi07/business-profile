<script lang="ts">
	import { waGeneral } from '$lib/data';
	import { MessageCircle, PenTool, CheckCircle, Package } from 'lucide-svelte';
</script>

<section id="cara-pesan" class="py-24" style="background:var(--sp-navy);">
	<div class="mx-auto max-w-6xl px-6">
		<div class="sp-reveal mb-16 text-center">
			<div
				class="mb-6 inline-block rounded-sm px-4 py-1.5 text-xs font-bold tracking-widest uppercase"
				style="background:rgba(234,88,12,0.15); color:var(--sp-orange);"
			>
				HOW WE WORK
			</div>
			<h2
				class="font-display mb-6 font-extrabold tracking-tight text-white uppercase"
				style="font-size:clamp(2rem,5vw,3rem);"
			>
				4 Easy <span style="color:var(--sp-orange);">Steps</span>
			</h2>
			<div class="mx-auto mb-6 h-1 w-16" style="background:var(--sp-orange);"></div>
			<p class="font-semibold" style="color:rgba(255,255,255,0.7);">
				Experience hassle-free plumbing services from start to finish.
			</p>
		</div>
		<div class="relative grid grid-cols-1 gap-8 md:grid-cols-4">
			<div
				class="absolute right-[12%] left-[12%] hidden h-px md:block"
				style="background:rgba(255,255,255,0.1); top:40px;"
			></div>
			{#each [{ step: '01', icon: MessageCircle, title: 'Contact Us', desc: 'Call or message us 24/7 to explain your plumbing issue.' }, { step: '02', icon: PenTool, title: 'Diagnosis', desc: 'We inspect and accurately diagnose the problem on-site.' }, { step: '03', icon: CheckCircle, title: 'Upfront Quote', desc: 'Approve our transparent fixed-price quote with no surprises.' }, { step: '04', icon: Package, title: 'Job Done', desc: 'We fix the issue efficiently and clean up the work area.' }] as step, i}
				<div
					class="sp-reveal group relative flex flex-col items-center text-center"
					style="transition-delay:{i * 150}ms;"
				>
					<div
						class="relative z-10 mb-6 flex h-20 w-20 items-center justify-center bg-slate-800 transition-colors group-hover:bg-slate-700"
						style="border:2px solid var(--sp-orange); color: var(--sp-white); border-radius: 4px;"
					>
						<svelte:component this={step.icon} size={32} strokeWidth={1.5} />
					</div>
					<div class="mb-2 text-xs font-bold tracking-widest" style="color:var(--sp-orange);">
						STEP {step.step}
					</div>
					<h3 class="font-display mb-3 text-lg font-bold tracking-wider text-white uppercase">
						{step.title}
					</h3>
					<p class="text-sm leading-relaxed" style="color:max(rgba(255,255,255,0.7));">
						{step.desc}
					</p>
				</div>
			{/each}
		</div>
		<div class="mt-14 text-center">
			<a href={waGeneral} target="_blank" class="btn-whatsapp inline-flex items-center gap-2">
				Book a Plumber Now
			</a>
		</div>
	</div>
</section>
