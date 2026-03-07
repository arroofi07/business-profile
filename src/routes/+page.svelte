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

	// JSON-LD Structured Data
	const localBusinessSchema = {
		'@context': 'https://schema.org',
		'@type': 'Plumber',
		'@id': 'https://aldingaplumbing.com.au/#business',
		name: 'Aldinga Plumbing Services',
		description:
			'Professional 24/7 plumbing services in Aldinga Beach, SA. Blocked drains, hot water systems, gas fitting, and emergency repairs.',
		url: 'https://aldingaplumbing.com.au',
		telephone: '+61459529693',
		image: 'https://aldingaplumbing.com.au/og-image.jpg',
		priceRange: '$$',
		address: {
			'@type': 'PostalAddress',
			streetAddress: '292 Aldinga Beach Rd',
			addressLocality: 'Aldinga Beach',
			addressRegion: 'SA',
			postalCode: '5173',
			addressCountry: 'AU'
		},
		geo: {
			'@type': 'GeoCoordinates',
			latitude: -35.2673,
			longitude: 138.4556
		},
		openingHoursSpecification: [
			{
				'@type': 'OpeningHoursSpecification',
				dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
				opens: '00:00',
				closes: '23:59'
			}
		],
		aggregateRating: {
			'@type': 'AggregateRating',
			ratingValue: '5.0',
			reviewCount: '124',
			bestRating: '5',
			worstRating: '1'
		}
	};

	const faqSchema = {
		'@context': 'https://schema.org',
		'@type': 'FAQPage',
		mainEntity: [
			{
				'@type': 'Question',
				name: 'Do you offer 24/7 emergency services?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Yes! We are available 24 hours a day, 7 days a week for any plumbing emergencies in Aldinga Beach.'
				}
			},
			{
				'@type': 'Question',
				name: 'Are your plumbers licensed?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Absolutely. All our plumbers are fully licensed, highly trained, and fully insured for your peace of mind.'
				}
			}
		]
	};

	onMount(() => {
		// ── Scroll-reveal: add .sp-visible when element enters viewport ──
		// Gunakan requestAnimationFrame agar semua komponen selesai render dulu
		// sebelum IntersectionObserver mulai observe, mencegah elemen "terkunci" invisible.
		requestAnimationFrame(() => {
			// Aktifkan CSS guard — elemen baru disembunyikan setelah observer siap
			document.body.classList.add('js-ready');

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
				// rootMargin positif: elemen yang sudah ada dalam/dekat viewport
				// langsung ditandai visible tanpa menunggu scroll
				{ threshold: 0.08, rootMargin: '0px 0px -30px 0px' }
			);
			revealEls.forEach((el) => revealObs.observe(el));

			return () => revealObs.disconnect();
		});
	});
</script>

<svelte:head>
	<title>Aldinga Plumbing Services | 24/7 Plumber in Aldinga Beach SA</title>
	<meta
		name="description"
		content="Professional 24/7 plumbing services in Aldinga Beach, SA. Blocked drains, hot water systems, gas fitting, and emergency repairs."
	/>
	<meta
		name="keywords"
		content="aldinga plumbing, plumber aldinga beach, 24/7 plumber sa, blocked drains aldinga, hot water system repair sa"
	/>
	<meta name="author" content="Aldinga Plumbing Services" />
	<meta name="robots" content="index, follow, max-image-preview:large" />
	<meta name="theme-color" content="#2563EB" />
	<link rel="canonical" href="https://aldingaplumbing.com.au/" />

	<!-- Geo Meta Tags (Local SEO) -->
	<meta name="geo.region" content="AU-SA" />
	<meta name="geo.placename" content="Aldinga Beach" />
	<meta name="geo.position" content="-35.2673;138.4556" />
	<meta name="ICBM" content="-35.2673, 138.4556" />

	<!-- Open Graph / Facebook -->
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://aldingaplumbing.com.au/" />
	<meta property="og:title" content="Aldinga Plumbing Services | 24/7 Plumber" />
	<meta
		property="og:description"
		content="Professional 24/7 plumbing services in Aldinga Beach, SA. Call us for commercial and residential plumbing."
	/>
	<meta property="og:image" content="https://aldingaplumbing.com.au/og-image.jpg" />
	<meta property="og:locale" content="en_AU" />

	<!-- JSON-LD Structured Data -->
	{@html `<script type="application/ld+json">${JSON.stringify(localBusinessSchema)}</script>`}
	{@html `<script type="application/ld+json">${JSON.stringify(faqSchema)}</script>`}
</svelte:head>

<Navbar />
<main>
	<Hero />
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
