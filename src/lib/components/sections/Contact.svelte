<script lang="ts">
	import { waGeneral } from '$lib/data';
	import { Instagram, MessageCircle, MapPin } from 'lucide-svelte';
</script>

<section id="kontak" class="py-24" style="background:var(--sp-gradient-dark);">
	<div class="mx-auto max-w-4xl px-6 text-center">
		<div class="sp-reveal">
			<div
				class="mb-4 inline-block rounded-full px-4 py-1.5 text-xs font-bold tracking-widest uppercase"
				style="background:rgba(255,255,255,0.15); color:#fff; font-family:'Outfit',sans-serif;"
			>
				HUBUNGI KAMI
			</div>
			<h2 class="font-display mb-4 font-bold text-white" style="font-size:clamp(2rem,5vw,3rem);">
				Siap Mencetak <span style="color:#93C5FD;">Bersama Kami?</span>
			</h2>
			<p class="mx-auto mb-10 max-w-xl" style="color:rgba(255,255,255,0.7);">
				Hubungi Smartprint Padang sekarang dan dapatkan konsultasi gratis untuk kebutuhan cetak
				Anda.
			</p>
			<div class="flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
				<a
					href={waGeneral}
					target="_blank"
					class="flex items-center gap-2 rounded-xl px-8 py-4 text-base font-bold transition-all duration-200 hover:opacity-80"
					style="background:linear-gradient(135deg,#25D366,#2DB742); color:white; font-family:'Outfit',sans-serif;"
				>
					<MessageCircle /> Chat WhatsApp Sekarang</a
				>
				<a
					href="https://www.instagram.com/smartprint_padang/"
					target="_blank"
					class="flex items-center gap-2 rounded-xl px-8 py-4 text-base font-bold transition-all duration-200 hover:opacity-80"
					style="background:linear-gradient(135deg,#E1306C,#833AB4); color:white; font-family:'Outfit',sans-serif;"
				>
					<Instagram /> Follow Instagram</a
				>
			</div>
		</div>
		<div class="mt-10 grid grid-cols-1 gap-4 sm:grid-cols-3">
			{#each [{ icon: MessageCircle, label: 'Telepon / WhatsApp', val: '0811 663 528' }, { icon: Instagram, label: 'Instagram', val: '@smartprint_padang' }, { icon: MapPin, label: 'Kota', val: 'Padang, Sumatera Barat' }] as c, i}
				<div
					class="sp-reveal flex flex-col items-center rounded-xl p-5"
					style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); transition-delay:{i *
						100}ms;"
				>
					<div class="mb-3 text-white">
						<svelte:component this={c.icon} size={32} strokeWidth={1.5} />
					</div>
					<div
						class="mb-1 text-xs"
						style="color:rgba(255,255,255,0.55); font-family:'Outfit',sans-serif;"
					>
						{c.label}
					</div>
					<div class="text-sm font-semibold text-white">{c.val}</div>
				</div>
			{/each}
		</div>
	</div>
</section>
