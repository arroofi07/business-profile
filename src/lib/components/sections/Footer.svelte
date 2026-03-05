<script lang="ts">
	import { waGeneral } from '$lib/data';
</script>

<footer style="background:#0F172A; border-top:3px solid var(--sp-blue);">
	<div class="mx-auto max-w-7xl px-6 py-16">
		<div class="grid grid-cols-1 gap-10 md:grid-cols-4">
			<!-- Brand -->
			<div class="md:col-span-2">
				<div class="mb-4 flex items-center gap-3">
					<div
						class="flex h-11 w-11 items-center justify-center rounded-xl text-2xl"
						style="background:var(--sp-gradient-blue);"
					>
						🖨️
					</div>
					<div>
						<div class="font-display text-lg font-bold text-white">Smartprint Padang</div>
						<div
							class="text-xs"
							style="color:rgba(255,255,255,0.45); font-family:'Plus Jakarta Sans',sans-serif;"
						>
							DIGITAL PRINTING PADANG
						</div>
					</div>
				</div>
				<p class="mb-4 max-w-xs text-sm" style="color:rgba(255,255,255,0.55);">
					Creative Agency · Digital Printing · Advertising · Percetakan. Bagian dari ekosistem
					Redline Communication.
				</p>
				<div class="flex gap-3">
					<a
						href="https://www.instagram.com/smartprint_padang/"
						target="_blank"
						class="flex h-9 w-9 items-center justify-center rounded-lg text-lg transition-opacity hover:opacity-75"
						style="background:linear-gradient(135deg,#E1306C,#833AB4);">📷</a
					>
					<a
						href={waGeneral}
						target="_blank"
						class="flex h-9 w-9 items-center justify-center rounded-lg text-lg transition-opacity hover:opacity-75"
						style="background:linear-gradient(135deg,#25D366,#128C7E);">💬</a
					>
				</div>
			</div>

			<!-- Links -->
			<div>
				<div
					class="font-display mb-4 text-sm font-bold tracking-wider uppercase"
					style="color:rgba(255,255,255,0.4);"
				>
					Layanan
				</div>
				{#each ['Digital Printing', 'Advertising', 'Percetakan', 'Desain Grafis', 'Corporate Branding'] as l}
					<div class="py-1.5 text-sm" style="color:rgba(255,255,255,0.6);">{l}</div>
				{/each}
			</div>

			<!-- Contact -->
			<div>
				<div
					class="font-display mb-4 text-sm font-bold tracking-wider uppercase"
					style="color:rgba(255,255,255,0.4);"
				>
					Kontak
				</div>
				{#each [['📞', '0811 663 528'], ['📸', '@smartprint_padang'], ['🏙️', 'Padang, Sumatera Barat'], ['🔗', 'Part of @redline_comunication']] as [ico, val]}
					<div class="flex items-start gap-2 py-1.5 text-sm" style="color:rgba(255,255,255,0.6);">
						<span>{ico}</span><span>{val}</span>
					</div>
				{/each}
			</div>
		</div>

		<div class="section-divider my-8"></div>
		<div
			class="flex flex-col items-center justify-between gap-3 text-xs sm:flex-row"
			style="color:rgba(255,255,255,0.35);"
		>
			<span>© 2025 Smartprint Padang. All rights reserved.</span>
			<span
				>Part of <a
					href="https://www.instagram.com/redline_comunication/"
					target="_blank"
					style="color:var(--sp-blue-light);">Redline Communication</a
				></span
			>
		</div>
	</div>
</footer>
