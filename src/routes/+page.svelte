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
		'@id': 'https://smartprintpadang.com/#business',
		name: 'SmartPrint Padang',
		alternateName: 'Smartprint Padang Digital Printing',
		description:
			'Pusat cetak indoor/outdoor & percetakan berkualitas di Padang. Melayani cetak banner, spanduk, stiker, kartu nama, brosur, dan lainnya.',
		url: 'https://smartprintpadang.com',
		telephone: '+6281166352​8',
		image: 'https://smartprintpadang.com/og-image.jpg',
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
		sameAs: [
			'https://www.instagram.com/smartprint_padang/',
			'https://www.instagram.com/redline_production_/'
		],
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
						name: 'Spanduk PVC',
						description: 'Spanduk outdoor berkualitas tinggi, tahan cuaca & sinar UV'
					}
				},
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Baliho Outdoor',
						description: 'Baliho ukuran besar untuk promosi jalan & event outdoor'
					}
				},
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Stiker Cutting',
						description: 'Stiker cutting presisi tinggi untuk kaca, motor, & properti'
					}
				},
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Kartu Nama Premium',
						description: 'Kartu nama profesional, art carton 260gsm, full color'
					}
				},
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Roll Banner',
						description: 'Banner roll-up portabel untuk pameran & promosi indoor'
					}
				},
				{
					'@type': 'Offer',
					itemOffered: {
						'@type': 'Service',
						name: 'Backdrop Photobooth',
						description: 'Backdrop custom untuk acara pernikahan, wisuda, & event'
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
				name: 'Berapa lama proses cetak di SmartPrint Padang?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Umumnya 1–3 hari kerja tergantung jenis & ukuran produk. Untuk order urgent bisa lebih cepat — hubungi kami langsung.'
				}
			},
			{
				'@type': 'Question',
				name: 'Apakah bisa custom ukuran cetak?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Tentu! Kami melayani cetak dengan ukuran custom sesuai kebutuhan Anda.'
				}
			},
			{
				'@type': 'Question',
				name: 'Format file apa yang diterima SmartPrint Padang?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Kami menerima CDR, AI, PDF, JPG/PNG (min. 150 dpi). Format vektor sangat direkomendasikan.'
				}
			},
			{
				'@type': 'Question',
				name: 'Apakah ada layanan antar di SmartPrint Padang?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Ada! Kami melayani pengiriman ke seluruh wilayah Kota Padang & sekitarnya.'
				}
			},
			{
				'@type': 'Question',
				name: 'Bagaimana cara pembayaran di SmartPrint Padang?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Transfer bank (BCA, BRI, Mandiri), QRIS, dan cash. DP 50% untuk order custom.'
				}
			},
			{
				'@type': 'Question',
				name: 'Apakah ada harga grosir untuk cetak dalam jumlah besar?',
				acceptedAnswer: {
					'@type': 'Answer',
					text: 'Ya, tersedia harga spesial untuk order dalam jumlah besar. Hubungi kami via WhatsApp.'
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
	<title>Percetakan Padang & Digital Printing Padang | SmartPrint</title>
	<meta
		name="description"
		content="Mencari percetakan Padang atau digital printing Padang? SmartPrint adalah pusat advertising Padang terlengkap. Melayani cetak spanduk, banner, brosur, dll."
	/>
	<meta
		name="keywords"
		content="digital printing padang, percetakan padang, cetak spanduk padang, cetak banner padang, cetak stiker padang, smartprint padang, smart print padang, cetak murah padang, percetakan terdekat, cetak baliho padang, cetak kartu nama padang, cetak brosur padang, advertising padang, jasa cetak padang, cetak undangan padang, cetak stiker label padang, cetak backdrop padang, percetakan sumatera barat, digital printing sumatera barat"
	/>
	<meta name="author" content="SmartPrint Padang" />
	<meta
		name="robots"
		content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
	/>
	<meta name="theme-color" content="#1E40AF" />
	<link rel="canonical" href="https://smartprintpadang.com/" />

	<!-- Geo Meta Tags (Local SEO) -->
	<meta name="geo.region" content="ID-SB" />
	<meta name="geo.placename" content="Padang" />
	<meta name="geo.position" content="-0.9471;100.4172" />
	<meta name="ICBM" content="-0.9471, 100.4172" />

	<!-- Open Graph / Facebook -->
	<meta property="og:type" content="website" />
	<meta property="og:url" content="https://smartprintpadang.com/" />
	<meta
		property="og:title"
		content="Percetakan Padang & Digital Printing Padang | SmartPrint"
	/>
	<meta
		property="og:description"
		content="Mencari percetakan Padang atau digital printing Padang? SmartPrint adalah pusat advertising Padang terlengkap. Melayani cetak spanduk, banner, brosur, dll."
	/>
	<meta property="og:image" content="https://smartprintpadang.com/og-image.jpg" />
	<meta property="og:image:width" content="1200" />
	<meta property="og:image:height" content="630" />
	<meta
		property="og:image:alt"
		content="SmartPrint Padang - Digital Printing & Percetakan Berkualitas"
	/>
	<meta property="og:site_name" content="SmartPrint Padang" />
	<meta property="og:locale" content="id_ID" />

	<!-- Twitter -->
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:url" content="https://smartprintpadang.com/" />
	<meta
		name="twitter:title"
		content="Percetakan Padang & Digital Printing Padang | SmartPrint"
	/>
	<meta
		name="twitter:description"
		content="Mencari percetakan Padang atau digital printing Padang? SmartPrint adalah pusat advertising Padang terlengkap. Melayani cetak spanduk, banner, brosur, dll."
	/>
	<meta name="twitter:image" content="https://smartprintpadang.com/og-image.jpg" />
	<meta
		name="twitter:image:alt"
		content="SmartPrint Padang - Digital Printing & Percetakan Berkualitas"
	/>

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
