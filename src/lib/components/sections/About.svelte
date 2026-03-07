<script lang="ts">
	import { Target, Zap, Coins, Handshake, Printer, Clock } from 'lucide-svelte';
	import logo from '$lib/assets/mpm.png';
</script>

<section id="tentang" class="dot-pattern-light py-24" style="background:var(--sp-bg-white);">
	<div class="mx-auto grid max-w-6xl items-center gap-16 px-6 lg:grid-cols-2">
		<!-- Left copy -->
		<div class="sp-reveal">
			<div class="section-chip mb-4">TENTANG KAMI</div>
			<h2
				class="font-display mb-6 font-bold"
				style="font-size:clamp(1.8rem,4vw,2.8rem); color:var(--sp-navy);"
			>
				Mengapa Pilih <span class="gradient-text-blue">MPM Digital Printing?</span>
			</h2>
			<p class="mb-6 text-base leading-relaxed" style="color:var(--sp-gray);">
				MPM Digital Printing hadir sebagai solusi percetakan online yang praktis dan efisien. Kami
				berdedikasi tinggi memberikan kemudahan bagi Anda untuk mencetak berbagai keperluan seperti
				kalender, undangan, dan buku langsung secara online.
			</p>
			<p class="mb-8 text-base leading-relaxed" style="color:var(--sp-gray);">
				Bekerja dengan tenaga ahli dan menggunakan teknologi terdepan, kami menjamin kualitas setiap
				cetakan tetap maksimal, disertai pelayanan yang cepat tanggap, membantu setiap kebutuhan
				cetak Anda tercapai dengan mudah dan memuaskan.
			</p>
			<div class="grid grid-cols-2 gap-4">
				{#each [{ icon: Target, label: 'Kualitas Tinggi', color: 'var(--sp-blue)' }, { icon: Zap, label: 'Proses Cepat', color: 'var(--sp-cyan)' }, { icon: Coins, label: 'Harga Terjangkau', color: 'var(--sp-orange)' }, { icon: Handshake, label: 'Pelayanan Ramah', color: 'var(--sp-green)' }] as v}
					<div
						class="flex items-center gap-3 rounded-xl p-4"
						style="background:var(--sp-bg-off); border:1px solid var(--sp-gray-border);"
					>
						<div style="color:{v.color};">
							<svelte:component this={v.icon} size={28} strokeWidth={1.5} />
						</div>
						<span class="text-sm font-semibold" style="color:var(--sp-navy);">{v.label}</span>
					</div>
				{/each}
			</div>
		</div>

		<!-- Right visual -->
		<div class="sp-reveal flex flex-col gap-4" style="transition-delay: 200ms;">
			<div
				class="animate-float-soft rounded-2xl p-8 text-center shadow-xl"
				style="background:var(--sp-gradient-dark);"
			>
				<div class="mx-auto mb-5 flex w-fit justify-center rounded-4xl bg-accent p-2 text-white">
					<img src={logo} class="h-20 w-20 object-cover" alt="" />
				</div>
				<div class="font-display mb-1 text-xl font-bold text-white">MPM Digital Printing</div>
				<div class="mb-3 text-sm" style="color:#F9A8D4;">Percetakan Online · Printing Service</div>
				<div
					class="rounded-lg p-3 text-xs"
					style="background:rgba(255,255,255,0.1); color:rgba(255,255,255,0.75);"
				>
					Menerima jasa cetak: Kalender, Undangan, Buku dsb.
				</div>
			</div>
			<div
				class="rounded-xl p-5 shadow-sm"
				style="background:var(--sp-bg-off); border:1px solid var(--sp-gray-border);"
			>
				<div
					class="font-display mb-3 flex items-center gap-2 text-base font-bold"
					style="color:var(--sp-navy);"
				>
					<Clock size={20} strokeWidth={2} /> Jam Operasional
				</div>
				{#each [['Senin – Sabtu', '09:00 – 17:00'], ['Minggu', 'Tutup']] as [hari, jam]}
					<div
						class="flex justify-between border-b py-1.5 text-sm last:border-0"
						style="border-color:var(--sp-gray-border); color:var(--sp-text-mid);"
					>
						<span>{hari}</span><span class="font-semibold" style="color:var(--sp-blue);">{jam}</span
						>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>
