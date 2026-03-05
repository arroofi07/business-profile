<script lang="ts">
	import { onMount } from 'svelte';
	import { waGeneral } from '$lib/data';
	import logo from '$lib/assets/logo.png';

	// Typewriter
	const typeWords = ['cetakmu', 'desainmu', 'promosimu', 'bannermu', 'stikermu', 'brosurmu'];
	let typeText = $state(typeWords[0]);
	let typeFading = $state(false);

	// Particles
	let canvasEl = $state<HTMLCanvasElement | null>(null);

	onMount(() => {
		// ── Typewriter loop ──
		let wordIdx = 0;
		const typeTimer = setInterval(() => {
			typeFading = true;
			setTimeout(() => {
				wordIdx = (wordIdx + 1) % typeWords.length;
				typeText = typeWords[wordIdx];
				typeFading = false;
			}, 400);
		}, 2800);

		// ── Canvas floating particles ──
		const canvas = canvasEl;
		let raf: number;
		let cleanupCanvas = () => {};

		if (canvas) {
			const ctx = canvas.getContext('2d')!;
			const resize = () => {
				canvas.width = canvas.offsetWidth;
				canvas.height = canvas.offsetHeight;
			};
			resize();
			window.addEventListener('resize', resize);
			const NUM = 38;
			let pts = Array.from({ length: NUM }, () => ({
				x: Math.random() * canvas.width,
				y: Math.random() * canvas.height,
				r: 1.5 + Math.random() * 3,
				dx: (Math.random() - 0.5) * 0.35,
				dy: (Math.random() - 0.5) * 0.35,
				o: 0.2 + Math.random() * 0.55
			}));
			const draw = () => {
				ctx.clearRect(0, 0, canvas.width, canvas.height);
				for (const p of pts) {
					p.x += p.dx;
					p.y += p.dy;
					if (p.x < 0) p.x = canvas.width;
					if (p.x > canvas.width) p.x = 0;
					if (p.y < 0) p.y = canvas.height;
					if (p.y > canvas.height) p.y = 0;
					ctx.beginPath();
					ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
					ctx.fillStyle = `rgba(59,130,246,${p.o})`;
					ctx.fill();
				}
				// draw connections
				for (let i = 0; i < pts.length; i++) {
					for (let j = i + 1; j < pts.length; j++) {
						const dist = Math.hypot(pts[i].x - pts[j].x, pts[i].y - pts[j].y);
						if (dist < 120) {
							ctx.beginPath();
							ctx.strokeStyle = `rgba(59,130,246,${0.12 * (1 - dist / 120)})`;
							ctx.lineWidth = 0.7;
							ctx.moveTo(pts[i].x, pts[i].y);
							ctx.lineTo(pts[j].x, pts[j].y);
							ctx.stroke();
						}
					}
				}
				raf = requestAnimationFrame(draw);
			};
			draw();

			cleanupCanvas = () => {
				cancelAnimationFrame(raf);
				window.removeEventListener('resize', resize);
			};
		}

		return () => {
			clearInterval(typeTimer);
			cleanupCanvas();
		};
	});
</script>

<section
	id="hero"
	class="dot-pattern-light relative flex min-h-screen items-center overflow-hidden"
	style="background:var(--sp-gradient-hero); padding-top:var(--nav-height);"
>
	<!-- Canvas Particles -->
	<canvas bind:this={canvasEl} class="absolute inset-0 z-0 h-full w-full"></canvas>

	<!-- Decorative blobs -->
	<div
		class="pointer-events-none absolute top-20 -left-20 h-96 w-96 rounded-full opacity-40"
		style="background:radial-gradient(circle, rgba(59,130,246,0.25) 0%, transparent 70%); filter:blur(60px);"
	></div>
	<div
		class="pointer-events-none absolute -right-20 bottom-20 h-80 w-80 rounded-full opacity-30"
		style="background:radial-gradient(circle, rgba(14,165,233,0.2) 0%, transparent 70%); filter:blur(60px);"
	></div>

	<div
		class="relative z-10 mx-auto grid w-full max-w-7xl items-center gap-10 px-6 py-12 lg:grid-cols-2 lg:gap-16 lg:py-20"
	>
		<!-- Left copy -->
		<div>
			<div class="animate-slide-up section-chip mb-6 inline-flex items-center gap-2">
				<span>✦</span> DIGITAL PRINTING · PADANG
			</div>
			<h1
				class="font-display animate-slide-up mb-6 leading-tight font-extrabold delay-100"
				style="font-size:clamp(2.4rem,5.5vw,3.8rem); color:var(--sp-navy);"
			>
				Apapun Kebutuhan<br />
				<span
					class="gradient-text-shimmer inline-block min-w-[300px] transition-opacity duration-300"
					style="opacity: {typeFading ? 0 : 1};">{typeText}</span
				><br />
				<span style="color:var(--sp-orange);">Ingat Smartprint aja!</span>
			</h1>
			<p
				class="animate-slide-up mb-8 max-w-lg text-lg delay-200"
				style="color:var(--sp-gray); line-height:1.8;"
			>
				Digital Printing · Advertising · Percetakan. Lebih dari 100 produk cetak berkualitas tinggi
				— harga terjangkau, hasil profesional, pengerjaan cepat.
			</p>
			<div class="animate-slide-up flex flex-col gap-3 delay-300 sm:flex-row sm:gap-4">
				<a href="#produk" class="btn-primary-sp w-full text-center sm:w-auto">Lihat Katalog ↓</a>
				<a
					href={waGeneral}
					target="_blank"
					class="btn-whatsapp flex w-full items-center justify-center gap-2 text-center sm:w-auto"
					>💬 Chat WhatsApp</a
				>
			</div>

			<!-- Mini stats -->
			<div class="animate-slide-up mt-10 flex gap-8 delay-500">
				{#each [['1.149+', 'Followers IG', 'var(--sp-blue)'], ['100+', 'Jenis Produk', 'var(--sp-orange)'], ['⭐ 5.0', 'Rating', 'var(--sp-cyan)']] as [val, lbl, col]}
					<div>
						<div class="font-display text-2xl font-bold" style="color:{col};">{val}</div>
						<div class="text-xs font-medium" style="color:var(--sp-gray);">{lbl}</div>
					</div>
				{/each}
			</div>
		</div>

		<!-- Right floating card -->
		<div class="animate-scale-reveal flex justify-center delay-300">
			<div class="relative w-full max-w-sm lg:max-w-md">
				<div
					class="animate-float-soft rounded-2xl p-5 shadow-2xl lg:p-8"
					style="background:white; border:1.5px solid rgba(59,130,246,0.25);"
				>
					<div class="mb-4 flex items-center gap-3">
						<div
							class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl text-3xl lg:h-14 lg:w-14"
							style="background:var(--sp-gradient-blue);"
						>
							<img src={logo} class="h-full w-full object-contain" alt="" />
						</div>
						<div>
							<div
								class="font-display text-base leading-tight font-bold lg:text-lg"
								style="color:var(--sp-navy);"
							>
								Smartprint Padang
							</div>
							<div class="text-[11px] font-semibold lg:text-xs" style="color:var(--sp-blue-mid);">
								@smartprint_padang
							</div>
						</div>
					</div>
					<div
						class="mb-5 grid grid-cols-3 gap-2 text-center text-xs font-bold"
						style="color:var(--sp-gray);"
					>
						{#each [['417', 'Posts'], ['1.149', 'Followers'], ['770', 'Following']] as [n, l]}
							<div class="rounded-lg py-2" style="background:var(--sp-bg-off);">
								<div class="font-display text-base font-extrabold" style="color:var(--sp-navy);">
									{n}
								</div>
								<div>{l}</div>
							</div>
						{/each}
					</div>
					<div class="grid grid-cols-2 gap-2">
						{#each ['Spanduk', 'Baliho', 'Stiker Label', 'Kartu Nama', 'Roll Banner', 'ID Card'] as p}
							<div
								class="rounded-lg px-3 py-2 text-center text-xs font-semibold"
								style="background:var(--sp-bg-light); color:var(--sp-blue);"
							>
								{p}
							</div>
						{/each}
					</div>
					<div
						class="mt-5 flex items-center justify-center gap-2 text-sm font-semibold"
						style="color:var(--sp-green);"
					>
						<span class="h-2 w-2 rounded-full" style="background:var(--sp-green);"></span>Senin –
						Sabtu · 09:00 – 17:00
					</div>
					<div
						class="mt-3 rounded-lg p-3 text-center text-xs"
						style="background:var(--sp-bg-off); color:var(--sp-gray);"
					>
						Part of
						<a
							href="https://www.instagram.com/redline_comunication/"
							class="hover:text-white"
							target="_blank"
						>
							<strong style="color:var(--sp-blue);">@redline_comunication</strong>
						</a>
						&
						<a
							href="https://www.instagram.com/redline_production_/"
							class="hover:text-white"
							target="_blank"
						>
							<strong style="color:var(--sp-blue);">@redline_production_</strong>
						</a>
					</div>
				</div>
				<!-- Decorative ring -->
				<div
					class="animate-spin-slow absolute -top-5 -right-5 h-16 w-16 rounded-full border-2 opacity-25"
					style="border-color:var(--sp-blue-mid);"
				></div>
				<div
					class="animate-spin-slow absolute -bottom-4 -left-4 h-10 w-10 rounded-full border-2 opacity-20"
					style="border-color:var(--sp-orange); animation-direction:reverse;"
				></div>
			</div>
		</div>
	</div>
</section>
