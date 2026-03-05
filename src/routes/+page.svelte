<script lang="ts">
	import { onMount } from 'svelte';
	import Navbar from '$lib/components/sections/Navbar.svelte';
	import Hero from '$lib/components/sections/Hero.svelte';
	import Stats from '$lib/components/sections/Stats.svelte';
	import Services from '$lib/components/sections/Services.svelte';
	import Catalog from '$lib/components/sections/Catalog.svelte';
	import HowToOrder from '$lib/components/sections/HowToOrder.svelte';
	import Pricing from '$lib/components/sections/Pricing.svelte';
	import About from '$lib/components/sections/About.svelte';
	import Testimonials from '$lib/components/sections/Testimonials.svelte';
	import Faq from '$lib/components/sections/Faq.svelte';
	import Contact from '$lib/components/sections/Contact.svelte';
	import Footer from '$lib/components/sections/Footer.svelte';

	onMount(() => {
		// ── Scroll-reveal: add .sp-visible when element enters viewport ──
		const revealEls = document.querySelectorAll('.sp-reveal');
		const revealObs = new IntersectionObserver(
			(entries) => {
				entries.forEach((e) => {
					if (e.isIntersecting) {
						e.target.classList.add('sp-visible');
						revealObs.unobserve(e.target);
					}
				});
			},
			{ threshold: 0.12 }
		);
		revealEls.forEach((el) => revealObs.observe(el));
	});
</script>

<svelte:head>
	<title>SmartPrint Padang | Digital Printing & Percetakan #1</title>
	<meta
		name="description"
		content="Pusat cetak indoor/outdoor & percetakan berkualitas di Padang."
	/>
</svelte:head>

<Navbar />
<main>
	<Hero />
	<Stats />
	<Services />
	<Catalog />
	<HowToOrder />
	<Pricing />
	<About />
	<Testimonials />
	<Faq />
	<Contact />
</main>
<Footer />
