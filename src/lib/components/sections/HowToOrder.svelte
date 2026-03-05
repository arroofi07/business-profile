<script lang="ts">
	import { waGeneral } from '$lib/data';
	import { MessageCircle, PenTool, CheckCircle, Package } from 'lucide-svelte';
</script>

<section id="cara-pesan" class="py-24" style="background:var(--sp-gradient-dark);">
	<div class="mx-auto max-w-6xl px-6">
		<div class="sp-reveal mb-16 text-center">
			<div
				class="mb-4 inline-block rounded-full px-4 py-1.5 text-xs font-bold tracking-widest uppercase"
				style="background:rgba(255,255,255,0.15); color:#fff; font-family:'Outfit',sans-serif;"
			>
				CARA ORDER
			</div>
			<h2 class="font-display mb-4 font-bold text-white" style="font-size:clamp(2rem,5vw,3rem);">
				4 Langkah <span style="color:#93C5FD;">Mudah</span>
			</h2>
			<p style="color:rgba(255,255,255,0.7);">
				Pesan cetakan Anda dengan proses yang simpel dan transparan.
			</p>
		</div>
		<div class="relative grid grid-cols-1 gap-8 md:grid-cols-4">
			<div
				class="absolute right-[12%] left-[12%] hidden h-px md:block"
				style="background:linear-gradient(90deg,transparent,rgba(255,255,255,0.3),transparent); top:40px;"
			></div>
			{#each [{ step: '01', icon: MessageCircle, title: 'Konsultasi', desc: 'Hubungi kami via WhatsApp, ceritakan kebutuhan cetak Anda.', color: '#93C5FD' }, { step: '02', icon: PenTool, title: 'Desain & File', desc: 'Kirim file desain, atau minta tim kami untuk membantu.', color: '#6EE7B7' }, { step: '03', icon: CheckCircle, title: 'Konfirmasi', desc: 'Setujui harga, spesifikasi, dan estimasi waktu produksi.', color: '#FBD38D' }, { step: '04', icon: Package, title: 'Terima Produk', desc: 'Ambil di toko atau kami antar ke lokasi Anda.', color: '#C4B5FD' }] as step, i}
				<div
					class="sp-reveal relative flex flex-col items-center text-center"
					style="transition-delay:{i * 150}ms;"
				>
					<div
						class="relative z-10 mb-5 flex h-20 w-20 items-center justify-center rounded-2xl shadow-lg"
						style="background:rgba(255,255,255,0.12); border:2px solid {step.color}; backdrop-filter:blur(8px); color: {step.color};"
					>
						<svelte:component this={step.icon} size={32} strokeWidth={1.5} />
					</div>
					<div
						class="mb-2 text-xs font-bold tracking-widest"
						style="color:{step.color}; font-family:'Outfit',sans-serif;"
					>
						LANGKAH {step.step}
					</div>
					<h3 class="font-display mb-2 text-lg font-bold text-white">{step.title}</h3>
					<p class="text-sm leading-relaxed" style="color:rgba(255,255,255,0.65);">{step.desc}</p>
				</div>
			{/each}
		</div>
		<div class="mt-14 text-center">
			<a href={waGeneral} target="_blank" class="btn-whatsapp inline-flex items-center gap-2">
				Mulai Order Sekarang
			</a>
		</div>
	</div>
</section>
