export const WA_NUMBER = '61459529693';

export function waLink(msg = '') {
	return `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(msg)}`;
}

export function waProduct(name: string) {
	return waLink(`Hi Aldinga Plumbing Services, I'd like more information regarding *${name}*.`);
}

export const waGeneral = waLink(
	'Hi Aldinga Plumbing Services, I need some plumbing assistance. Can you help?'
);

// ── Categories ──
export const categories = [
	{ key: 'all',          label: 'All Services',       icon: '🔧' },
	{ key: 'blocked',      label: 'Blocked Drains',     icon: '🚽' },
	{ key: 'hotwater',     label: 'Hot Water Systems',  icon: '🔥' },
	{ key: 'gas',          label: 'Gas Fitting',        icon: '💨' },
	{ key: 'emergency',    label: 'Emergency Plumbing', icon: '🚨' },
	{ key: 'maintenance',  label: 'General Maintenance',icon: '🛠️' },
];

// ── All Services (Replaced Products) ──
export const allProducts = [
	// ─── 🚽 BLOCKED DRAINS ───
	{ id: 1,  name: 'Cleared Blocked Toilets', category: 'blocked',   emoji: '🚽', tags: ['Urgent'], desc: 'Fast and hygienic removal of toilet blockages to restore normal function immediately.' },
	{ id: 2,  name: 'Unblock Sinks & Basins',  category: 'blocked',   emoji: '🚰', tags: [],          desc: 'Clearing stubborn clogs from kitchen sinks and bathroom basins.' },
	{ id: 3,  name: 'Drain Camera Inspection', category: 'blocked',   emoji: '📷', tags: ['Popular'], desc: 'Advanced CCTV drain camera inspection to find the exact cause of blockages.' },
	{ id: 4,  name: 'Hydro Jetting Service',   category: 'blocked',   emoji: '💦', tags: ['Popular'], desc: 'High-pressure water jetting to completely clear and clean blocked pipes.' },

	// ─── 🔥 HOT WATER SYSTEMS ───
	{ id: 5,  name: 'Hot Water Repairs',       category: 'hotwater',  emoji: '🔧', tags: ['Urgent'], desc: 'Fast repairs for all major brands of hot water systems.' },
	{ id: 6,  name: 'New System Installation', category: 'hotwater',  emoji: '🔥', tags: ['Popular'], desc: 'Expert installation of electric, gas, and solar hot water units.' },
	{ id: 7,  name: 'Boiler Maintenance',      category: 'hotwater',  emoji: '⚙️', tags: [],          desc: 'Routine maintenance and servicing to keep your boiler running efficiently.' },

	// ─── 💨 GAS FITTING ───
	{ id: 8,  name: 'Gas Leak Detection',      category: 'gas',       emoji: '🔍', tags: ['Urgent'], desc: 'Safe and precise detection and repair of dangerous gas leaks.' },
	{ id: 9,  name: 'Gas Appliance Install',   category: 'gas',       emoji: '🍳', tags: [],          desc: 'Professional installation of gas ovens, cooktops, and heaters.' },
	{ id: 10, name: 'Gas Line Upgrades',       category: 'gas',       emoji: '📏', tags: [],          desc: 'Upgrading and replacing old or unsafe gas lines for residential and commercial spaces.' },

	// ─── 🚨 EMERGENCY PLUMBING ───
	{ id: 11, name: '24/7 Emergency Repairs',  category: 'emergency', emoji: '🚨', tags: ['24/7'],    desc: 'Round-the-clock rapid response for burst pipes, severe leaks, and flooding.' },
	{ id: 12, name: 'Burst Pipe Repair',       category: 'emergency', emoji: '💥', tags: ['Urgent'], desc: 'Immediate repair and replacement of burst or heavily leaking pipes.' },

	// ─── 🛠️ MAINTENANCE & OTHER ───
	{ id: 13, name: 'Tap Repair & Replace',    category: 'maintenance',emoji: '🚰', tags: [],         desc: 'Fixing dripping taps or replacing old tapware with modern fixtures.' },
	{ id: 14, name: 'Toilet Repairs & Install',category: 'maintenance',emoji: '🚽', tags: ['Popular'],desc: 'Repairing running toilets, fixing leaks, or installing brand new toilets.' },
	{ id: 15, name: 'Leak Detection',          category: 'maintenance',emoji: '💧', tags: [],         desc: 'Advanced water leak detection to find hidden leaks behind walls or underground.' },
	{ id: 16, name: 'Roof & Gutter Leaks',     category: 'maintenance',emoji: '🏠', tags: [],         desc: 'Locating and repairing roof leaks and downpipe blockages.' },
];

export const statTargets = { products: 50, clients: 1240, years: 15, followers: 850 };

export const faqs = [
	{
		q: 'Do you offer 24/7 emergency services?',
		a: 'Yes! We are available 24 hours a day, 7 days a week for any plumbing emergencies in Aldinga Beach and surrounding areas.'
	},
	{
		q: 'Are your plumbers licensed and insured?',
		a: 'Absolutely. All our plumbers are fully licensed, highly trained, and fully insured for your peace of mind.'
	},
	{
		q: 'How quickly can you respond to an emergency?',
		a: 'For urgent issues like burst pipes or severe gas leaks, we prioritize your call and aim to be at your property as quickly as possible, usually within the hour.'
	},
	{
		q: 'Do you provide free quotes?',
		a: 'Yes, we provide upfront, transparent pricing and free quotes before we begin any work, so there are no surprises.'
	},
	{
		q: 'Do you handle commercial plumbing?',
		a: 'Yes, we service both residential homes and commercial properties across South Australia.'
	},
	{
		q: 'What payment methods do you accept?',
		a: 'We accept Cash, Credit/Debit cards, and Bank Transfers.'
	}
];

export const testimonials = [
	{
		name: 'John Miller',
		role: 'Homeowner',
		text: 'Aldinga Plumbing Services saved the day when our hot water system burst over the weekend. They arrived fast, quoted fairly, and had a new system installed by the afternoon. Highly recommend!',
		stars: 5
	},
	{
		name: 'Sarah Jenkins',
		role: 'Local Business Owner',
		text: 'Really reliable service. We had blocked drains backing up into our cafe and they cleared it up in no time. Very professional and clean.',
		stars: 5
	},
	{
		name: 'David Thompson',
		role: 'Resident',
		text: 'Called them for a suspected gas leak. They were incredibly thorough and safe. Fixed the issue completely. I feel much safer now.',
		stars: 5
	},
	{
		name: 'Emily Rose',
		role: 'Property Manager',
		text: 'I use Aldinga Plumbing for all our rental properties. They are always on time, communicate well with tenants, and their pricing is very transparent.',
		stars: 5
	},
	{
		name: 'Mark Wilson',
		role: 'Homeowner',
		text: 'Fantastic job upgrading all the tapware in our bathrooms. The team was polite, arrived exactly on time, and left the place spotless.',
		stars: 5
	},
	{
		name: 'Lucy Chen',
		role: 'Resident',
		text: 'We woke up to a flooded kitchen at 3 AM. Called Aldinga Plumbing and they actually answered and showed up! Fixed the burst pipe fast. True lifesavers.',
		stars: 5
	}
];
