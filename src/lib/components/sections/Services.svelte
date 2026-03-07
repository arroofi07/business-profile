<section id="layanan" class="py-24" style="background:var(--sp-bg-section);">
	<div class="mx-auto max-w-7xl px-6">
		<div class="sp-reveal mb-16 text-center">
			<div class="section-chip mb-4">LAYANAN KAMI</div>
			<h2
				class="font-display mb-4 font-bold"
				style="font-size:clamp(2rem,5vw,3rem); color:var(--sp-navy);"
			>
				Apa yang Bisa Kami <span class="gradient-text-blue">Lakukan</span>
			</h2>
			<p class="mx-auto max-w-xl" style="color:var(--sp-gray);">
				Kami hadir sebagai mitra kreatif untuk kebutuhan cetak dan advertising bisnis Anda.
			</p>
		</div>
		<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
			{#each [{ icon: '📅', title: 'Cetak Kalender', desc: 'Kalender meja dan dinding eksklusif untuk kebutuhan promosi atau personalisasi Anda.', color: 'var(--sp-blue)' }, { icon: '💌', title: 'Cetak Undangan', desc: 'Desain elegan dan bahan premium untuk momen spesial Anda. Bebas kustomisasi sesuai tema acara.', color: 'var(--sp-orange)' }, { icon: '📖', title: 'Cetak Buku', desc: 'Layanan cetak dan jilid buku berkualitas tinggi, cocok untuk keperluan akademik maupun komersial.', color: 'var(--sp-cyan)' }, { icon: '🖨️', title: 'Digital Printing', desc: 'Cetak berkualitas tinggi dengan teknologi digital terkini. Warna akurat, detail tajam, hasil memuaskan.', color: 'var(--sp-blue-mid)' }, { icon: '📦', title: 'Merchandise', desc: 'Pembuatan berbagai merchandise promosi seperti mug, tumbler, dan souvenir lainnya.', color: 'var(--sp-green)' }, { icon: '📄', title: 'Percetakan Umum', desc: 'Dari kartu nama, nota, brosur, hingga brosur. Semua dikerjakan dengan presisi tinggi.', color: 'var(--sp-orange-dim)' }] as s, i}
				<div class="card-sp sp-reveal p-7" style="transition-delay: {i * 50}ms;">
					<div
						class="mb-4 flex h-14 w-14 items-center justify-center rounded-xl text-3xl"
						style="background:color-mix(in srgb, {s.color} 12%, transparent);"
					>
						{s.icon}
					</div>
					<h3 class="font-display mb-2 text-lg font-bold" style="color:var(--sp-navy);">
						{s.title}
					</h3>
					<p class="text-sm leading-relaxed" style="color:var(--sp-gray);">{s.desc}</p>
				</div>
			{/each}
		</div>
	</div>
</section>
