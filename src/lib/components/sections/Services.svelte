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
			{#each [{ icon: '🖨️', title: 'Digital Printing', desc: 'Layanan digital printing Padang berkualitas tinggi dengan teknologi digital terkini. Warna akurat, detail tajam, hasil memuaskan.', color: 'var(--sp-blue)' }, { icon: '📢', title: 'Advertising', desc: 'Solusi advertising Padang kreatif untuk promosi brand dan produk Anda — spanduk, baliho, banner outdoor.', color: 'var(--sp-orange)' }, { icon: '📄', title: 'Percetakan', desc: 'Pusat percetakan Padang untuk kartu nama, nota, brosur, poster hingga undangan. Semua dikerjakan dengan presisi tinggi.', color: 'var(--sp-cyan)' }, { icon: '🎨', title: 'Desain Grafis', desc: 'Tim desainer siap membantu membuat desain menarik sesuai identitas brand Anda.', color: 'var(--sp-blue-mid)' }, { icon: '🚚', title: 'Pengiriman', desc: 'Layanan antar ke seluruh wilayah Kota Padang dan sekitarnya dengan aman dan tepat waktu.', color: 'var(--sp-green)' }, { icon: '💼', title: 'Corporate Branding', desc: 'Paket branding lengkap untuk perusahaan — seragam, ID card, media promosi, & lebih banyak lagi.', color: 'var(--sp-orange)' }] as s, i}
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
