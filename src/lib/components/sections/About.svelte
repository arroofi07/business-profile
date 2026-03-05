<section id="tentang" class="dot-pattern-light py-24" style="background:var(--sp-bg-white);">
	<div class="mx-auto grid max-w-6xl items-center gap-16 px-6 lg:grid-cols-2">
		<!-- Left copy -->
		<div class="sp-reveal">
			<div class="section-chip mb-4">TENTANG KAMI</div>
			<h2
				class="font-display mb-6 font-bold"
				style="font-size:clamp(1.8rem,4vw,2.8rem); color:var(--sp-navy);"
			>
				Mengapa Pilih <span class="gradient-text-blue">Smartprint?</span>
			</h2>
			<p class="mb-6 text-base leading-relaxed" style="color:var(--sp-gray);">
				Smartprint Padang adalah creative agency yang bergerak di bidang digital printing,
				advertising, dan percetakan. Bagian dari ekosistem <strong style="color:var(--sp-blue);"
					>Redline Communication</strong
				> — kami hadir untuk membantu bisnis Anda tampil profesional.
			</p>
			<p class="mb-8 text-base leading-relaxed" style="color:var(--sp-gray);">
				Dengan pengalaman lebih dari 7 tahun, kami telah melayani ribuan pelanggan di Padang dan
				sekitarnya — dari UMKM, event organizer, sekolah, hingga perusahaan besar.
			</p>
			<div class="grid grid-cols-2 gap-4">
				{#each [{ icon: '🎯', label: 'Kualitas Tinggi', color: 'var(--sp-blue)' }, { icon: '⚡', label: 'Proses Cepat', color: 'var(--sp-cyan)' }, { icon: '💰', label: 'Harga Terjangkau', color: 'var(--sp-orange)' }, { icon: '🤝', label: 'Pelayanan Ramah', color: 'var(--sp-green)' }] as v}
					<div
						class="flex items-center gap-3 rounded-xl p-4"
						style="background:var(--sp-bg-off); border:1px solid var(--sp-gray-border);"
					>
						<span class="text-2xl">{v.icon}</span>
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
				<div class="mb-4 text-7xl">🖨️</div>
				<div class="font-display mb-1 text-xl font-bold text-white">Smartprint Padang</div>
				<div class="mb-3 text-sm" style="color:#93C5FD;">
					Digital Printing · Advertising · Percetakan
				</div>
				<div
					class="rounded-lg p-3 text-xs"
					style="background:rgba(255,255,255,0.1); color:rgba(255,255,255,0.75);"
				>
					Part of <strong style="color:#93C5FD;">@redline_comunication</strong> &
					<strong style="color:#93C5FD;">@redline_production_</strong>
				</div>
			</div>
			<div
				class="rounded-xl p-5 shadow-sm"
				style="background:var(--sp-bg-off); border:1px solid var(--sp-gray-border);"
			>
				<div class="font-display mb-3 text-base font-bold" style="color:var(--sp-navy);">
					📍 Jam Operasional
				</div>
				{#each [['Senin – Jumat', '09:00 – 17:30'], ['Sabtu', '09:00 – 15:00'], ['Minggu', 'Tutup']] as [hari, jam]}
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
