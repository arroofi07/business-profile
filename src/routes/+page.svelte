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
		'@type': 'LocalBusiness',
		'@id': 'https://mpmdigitalprint.com/#business',
		name: 'MPM Digital Printing',
		alternateName: 'MPM Digital Print',
		description:
			'Pusat percetakan online dan digital printing service. Menerima jasa cetak: Kalender, Undangan, Buku dsb.',
		url: 'https://mpmdigitalprint.com',
		telephone: '+6281166352​8',
		image: 'https://mpmdigitalprint.com/og-image.jpg',
		priceRange: 'Rp',
		currenciesAccepted: 'IDR',
		paymentAccepted: 'Cash, Transfer Bank, QRIS',
		address: {
			'@type': 'PostalAddress',
			addressLocality: 'Padang',
			addressRegion: 'Sumatera Barat',
			addressCountry: 'ID'
		},
		geo: {
			'@type': 'GeoCoordinates',
			latitude: -0.9018741087406714,
			longitude: 100.3502534061413
		},
		openingHoursSpecification: [
			{
				'@type': 'OpeningHoursSpecification',
				dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
				opens: '09:00',
				closes: '17:00'
			}
		],
		sameAs: ['https://www.instagram.com/mpm.digitalprint/'],
		aggregateRating: {
			'@type': 'AggregateRating',
			ratingValue: '5.0',
			reviewCount: '6',
			bestRating: '5',
			worstRating: '1'
		},
		hasOfferCatalog: {
			'@type': 'OfferCatalog',
			name: 'Produk Digital Printing',
			itemListElement: [
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Cetak Kalender',
						description: 'Kalender meja & dinding dengan kualitas premium'
					}
				},
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Undangan',
						description: 'Undangan pernikahan, khitanan, dan acara lainnya dengan desain eksklusif'
					}
				},
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Cetak Buku',
						description: 'Jasa cetak dan jilid buku berkualitas tinggi'
					}
				},
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Spanduk & Banner',
						description: 'Spanduk outdoor kualitas tinggi, banner untuk promosi'
					}
				},
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Kartu Nama',
						description: 'Kartu nama profesional dengan variasi bahan premium'
					}
				},
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Brosur & Flayer',
						description: 'Cetak brosur full color untuk kebutuhan promosi bisnis Anda'
					}
				}
			]
		}
	};

	const faqSchema = {
		'@context': 'https://schema.org',
		'@type': 'FAQPage',
		mainEntity: [
			{
				'@type': 'Question',
				name: 'Berapa lama proses cetak di MPM Digital Printing?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Umumnya 1–3 hari kerja tergantung jenis & ukuran produk.'
				}
			},
			{
				'@type': 'Question',
				name: 'Apakah melayani cetak Kalender dan Buku?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Tentu! Kami melayani jasa cetak kalender, buku, undangan, dan berbagai produk printing lainnya.'
				}
			},
			{
				'@type': 'Question',
				name: 'Bisa order secara online?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Sangat bisa! Anda dapat menghubungi kami via link order atau Instagram untuk proses cetak secara online dengan cepat dan mudah.'
				}
			},
			{
				'@type': 'Question',
				name: 'Format file apa yang diterima?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Kami menerima CDR, AI, PDF, JPG/PNG (min. 150 dpi). Format vektor sangat direkomendasikan.'
				}
			},
			{
				'@type': 'Question',
				name: 'Bagaimana cara pembayaran di MPM Digital Printing?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Pembayaran dapat dilakukan via transfer antar bank. Silakan hubungi admin kami untuk detail lebih lanjut.'
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
	<title>MPM Digital Printing | Printing Service & Percetakan Online</title>
	<meta
		name="description"
		content="MPM Digital Printing — Percetakan online terpercaya. Menerima jasa cetak kalender, undangan, buku, dan berbagai kebutuhan digital printing lainnya dengan proses cepat."
	/>
	<meta
		name="keywords"
		content="mpm digital printing, digital printing online, percetakan online, cetak online, cetak kalender, cetak undangan, cetak buku, printing service, mpm digital print"
	/>
	<meta name="author" content="MPM Digital Printing" />
	<meta
		name="robots"
		content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
	/>
	<meta name="theme-color" content="#F9A8D4" />
	<link rel="canonical" href="https://mpmdigitalprint.com/" />

	<!-- Geo Meta Tags (Local SEO) -->
	<meta name="geo.region" content="ID-SB" />
	<meta name="geo.placename" content="Padang" />
	<meta name="geo.position" content="-0.9471;100.4172" />
	<meta name="ICBM" content="-0.9471, 100.4172" />

	<!-- Open Graph / Facebook -->
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://mpmdigitalprint.com/" />
	<meta property="og:title" content="MPM Digital Printing | Printing Service & Percetakan Online" />
	<meta
		property="og:description"
		content="Percetakan online terpercaya. Menerima jasa cetak kalender, undangan, buku, dan berbagai kebutuhan digital printing lainnya."
	/>
	<meta property="og:image" content="https://mpmdigitalprint.com/og-image.jpg" />
	<meta property="og:image:width" content="1200" />
	<meta property="og:image:height" content="630" />
	<meta property="og:image:alt" content="MPM Digital Printing - Berkualitas dan Cepat" />
	<meta property="og:site_name" content="MPM Digital Printing" />
	<meta property="og:locale" content="id_ID" />

	<!-- Twitter -->
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:url" content="https://mpmdigitalprint.com/" />
	<meta
		name="twitter:title"
		content="MPM Digital Printing | Printing Service & Percetakan Online"
	/>
	<meta
		name="twitter:description"
		content="Percetakan online terpercaya. Menerima jasa cetak kalender, undangan, buku, dan berbagai kebutuhan digital printing lainnya."
	/>
	<meta name="twitter:image" content="https://mpmdigitalprint.com/og-image.jpg" />
	<meta name="twitter:image:alt" content="MPM Digital Printing - Berkualitas dan Cepat" />

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
