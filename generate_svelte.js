const fs = require('fs');

const content = `<script lang="ts">
import { Separator } from '$lib/components/ui/separator';
import { Phone, MessageCircle, Menu, X, ArrowRight, ShieldCheck, CheckCircle, ShoppingBag, Award, Star, Instagram, Check } from 'lucide-svelte';

let menuOpen = $state(false);

const navLinks = [
'#home', label: 'Beranda' },
'#about', label: 'Tentang' },
'#products', label: 'Produk' },
'#order', label: 'Cara Order' },
'#reviews', label: 'Ulasan' }
];

const stats = [
'22.6K', label: 'Followers' },
'1.4K+', label: 'Posts' },
'100%', label: 'Original' },
'2', label: 'Metode Bayar (BNI & BRI)' }
];

const features = [
: ShieldCheck, title: 'Produk Original', desc: 'Garansi produk asli 100%' },
: Award, title: 'Bersertifikat BPOM', desc: 'Aman untuk penggunaan kulit Anda' },
: CheckCircle, title: 'Halal & MUI', desc: 'Tersertifikasi halal oleh MUI' },
: ShoppingBag, title: 'Open Reseller', desc: 'Bergabung dan jadilah bagian dari kami' }
];

const products = [
: 'Serum Perawatan',
ing & Anti-Aging',
dengan bahan aktif untuk membuat wajah bercahaya dan melawan tanda penuaan.',
splash.com/photo-1620916566398-39f1143ab7be?q=80&w=400&fit=crop'
: 'Pelembap Wajah',
Hydration Cream',
wajah yang melembapkan hingga ke dalam pori-pori sepanjang hari.',
splash.com/photo-1629198688000-71f23e745b6e?q=80&w=400&fit=crop'
: 'Pembersih',
Wash Extra Gentle',
 wajah dari kotoran dengan tekstur lembut yang tidak membuat kulit kering.',
splash.com/photo-1556228578-0d85b1a4d571?q=80&w=400&fit=crop'
: 'Pelindung',
 Sunscreen UV',
cegah kerusakan kulit akibat paparan sinar UV setiap harinya.',
splash.com/photo-1608248543803-ba4f8c70ae0b?q=80&w=400&fit=crop'
: 'Paket Spesial',
Routine Bundle',
bundling untuk rutinitas perawatan sehari-hari Anda dengan harga terbaik.',
splash.com/photo-1556228453-efd6c1ff04f6?q=80&w=400&fit=crop'
: 'Khusus',
e Solution Care',
 khusus untuk mengurangi kemerahan dan mengobati jerawat secara efektif.',
splash.com/photo-1611077544795-c23f26038d1d?q=80&w=400&fit=crop'
st reviews = [
ame: 'Amanda L.',
itial: 'AL',
minggu lalu',
ya benar-benar bagus! Tekstur serumnya cepat meresap dan muka jadi lebih glowing. Senang banget bisa ketemu Marwah Skincare!'
ame: 'Siti Maysaroh',
itial: 'SM',
bulan lalu',
ya ragu, tapi liat aman sudah BPOM & Halal MUI jadi beli. Admin sangat ramah dan proses pembelian via WhatsApp juga cepat.'
ame: 'Dina Prita',
itial: 'DP',
bulan lalu',
bersahabat untuk kualitas premium. Pengiriman aman pakai bubble wrap. Repeat order terus buat skincare rutin.'
Skincare | Official Agent</title>
<meta name="description" content="Marwah Skincare official product agent. Skincare aman, bersertifikat BPOM, Halal, dan MUI. Open reseller! Buka jam 08.00 - 18.00." />
</svelte:head>

<header class="fixed inset-x-0 top-0 z-50">
<nav class="border-b backdrop-blur-2xl transition-all" style="background:rgba(253,248,240,0.96);border-color:rgba(201,168,76,0.15);box-shadow:0 1px 30px rgba(61,26,74,0.08)">
max-w-7xl px-4 sm:px-6 lg:px-8">
h-20 items-center justify-between">
class="group flex items-center gap-3">
h-11 w-11 items-center justify-center rounded-3xl transition-transform group-hover:scale-105" style="background:var(--brand-gradient-gold);box-shadow:var(--brand-shadow-gold)">
 class="text-white font-display text-xl font-bold">M</span>
class="leading-tight">
font-bold text-ms-plum font-display">Marwah<span style="color:var(--ms-gold)"> Skincare</span></div>
font-bold tracking-[0.15em] uppercase" style="color:var(--ms-text-soft)">Official Agent</div>
class="hidden md:flex items-center gap-2">
avLinks as link}
k.href} class="relative rounded-xl px-4 py-2 text-sm font-semibold transition-all duration-200 text-ms-text-mid hover:text-ms-plum group">
k.label}
 class="absolute bottom-1 left-1/2 h-0.5 w-0 -translate-x-1/2 rounded-full transition-all duration-300 group-hover:w-4" style="background:var(--ms-gold)"></span>
class="hidden items-center gap-4 md:flex">
items-center gap-2 rounded-full border px-3 py-1.5 text-[10px] font-bold uppercase tracking-wider" style="border-color:var(--ms-gold);color:var(--ms-gold)">
w-3.5" /> BPOM & Halal
href="#order">
 class="flex h-10 items-center gap-2 rounded-xl px-5 text-sm font-bold text-white shadow-md transition-all hover:-translate-y-0.5" style="background:var(--brand-gradient-gold);box-shadow:var(--brand-shadow-gold)">Order Sekarang</button>
 onclick={() => (menuOpen = !menuOpen)} class="rounded-xl p-2 text-ms-plum transition hover:bg-ms-gold/10 md:hidden">
uOpen}<X class="h-6 w-6" />{:else}<Menu class="h-6 w-6" />{/if}
>
menuOpen}
px-4 pt-3 pb-6 md:hidden" style="background:var(--ms-ivory);border-color:rgba(201,168,76,0.15)">
flex-col gap-1">
avLinks as link}
k.href} onclick={() => (menuOpen = false)} class="rounded-xl px-4 py-3 text-sm font-semibold text-ms-text-mid hover:bg-ms-gold-light/10 hover:text-ms-plum">{link.label}</a>
class="mt-4 pt-4 border-t flex flex-col gap-3" style="border-color:rgba(201,168,76,0.15)">
class="block w-full">
 class="flex h-11 w-full items-center justify-center rounded-xl text-sm font-bold text-white shadow-md" style="background:var(--brand-gradient-gold)">Order Sekarang</button>
av>
</header>

<main class="pt-20">
<section id="home" class="relative min-h-screen overflow-hidden flex items-center pt-10" style="background:var(--brand-gradient-hero)">
-top-40 -left-20 h-[600px] w-[600px] rounded-[100px] opacity-[0.4]" style="background:radial-gradient(ellipse at center, var(--ms-lavender) 0%, transparent 70%); transform:rotate(15deg); filter:blur(40px);"></div>
bottom-10 right-0 h-[500px] w-[500px] rounded-full opacity-[0.3]" style="background:radial-gradient(circle, var(--ms-gold-light) 0%, transparent 60%); filter:blur(50px);"></div>

mx-auto max-w-7xl px-4 pb-20 pt-16 sm:px-6 lg:grid lg:grid-cols-12 lg:gap-8 lg:px-8">
imate-slide-up lg:col-span-6 flex flex-col justify-center space-y-8 relative z-10">
line-flex items-center gap-2 self-start rounded-full border px-4 py-2" style="border-color:rgba(201,168,76,0.4);background:rgba(201,168,76,0.05)">
 class="h-2 w-2 rounded-full animate-pulse-gold bg-ms-gold"></span>
 class="text-xs font-bold uppercase tracking-widest text-ms-plum-mid">Agen Resmi Marwah Skincare</span>
class="font-display text-5xl leading-[1.1] text-ms-plum lg:text-[76px] font-medium">Cantik Natural,<br/><span class="font-bold italic gradient-text-gold">Kulit Bersinar</span></h1>
max-w-md text-base leading-relaxed text-ms-text-mid md:text-lg">Produk skincare original, diformulasikan untuk kecantikan eksklusifmu. Menjamin keamanan dengan sertifikasi <strong>BPOM, Halal, & MUI</strong>.</p>
class="flex flex-wrap items-center gap-4">
 class="flex h-14 items-center gap-2.5 rounded-2xl px-8 text-sm font-bold text-white transition-all hover:scale-105 hover:shadow-xl" style="background:var(--brand-gradient-gold);box-shadow:var(--brand-shadow-gold)">Pesan Sekarang <ArrowRight class="h-4 w-4" /></button></a>
 class="flex h-14 items-center gap-2.5 rounded-2xl border px-8 text-sm font-semibold text-ms-plum-mid transition-all hover:bg-ms-plum/5" style="border-color:rgba(61,26,74,0.15)">Lihat Produk</button></a>
class="flex flex-wrap gap-3 pt-4">
 Digunakan', 'BPOM Approved', 'Halal MUI', 'Open Reseller'] as tag}
items-center gap-1.5 rounded-full px-3 py-1 text-[11px] font-bold text-ms-plum border" style="border-color:rgba(201,168,76,0.3); background:white"><Check class="h-3 w-3 text-ms-gold" /> {tag}</div>
class="animate-slide-left relative mt-16 lg:col-span-6 lg:mt-0 delay-200">
mx-auto max-w-md lg:max-w-none">
overflow-hidden shadow-2xl" style="border-radius:40px 140px 40px 140px; border:8px solid white;">
splash.com/photo-1620916566398-39f1143ab7be?q=80&w=700&auto=format&fit=crop" alt="Marwah Skincare Products" class="w-full object-cover transition-transform duration-700 hover:scale-105" style="aspect-ratio:4/5" />
class="glass-light animate-float-gentle absolute -left-4 top-20 rounded-2xl p-4 shadow-xl">
items-center gap-3">
h-10 w-10 items-center justify-center rounded-full text-white" style="background:linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%)"><Instagram class="h-5 w-5" /></div>
font-bold text-ms-plum">22.6K Followers</div><div class="text-[11px] text-ms-text-soft">@marwah_skincare_id</div></div>
class="glass-light animate-float-gentle absolute -bottom-6 right-2 rounded-2xl p-4 shadow-xl text-center" style="animation-delay: 1.5s;">
font-bold text-ms-gold tracking-widest uppercase">Jam Buka</div><div class="mt-1 text-sm font-bold text-ms-plum">08.00 - 18.00</div>
class="pointer-events-none absolute inset-x-0 bottom-0 overflow-hidden">
0 1440 100" fill="none" preserveAspectRatio="none" class="w-full h-12 md:h-20"><path d="M0,50 C320,100 420,0 740,50 C1060,100 1120,0 1440,50 L1440,100 L0,100 Z" fill="#3d1a4a" /></svg>
>

<section class="py-16 md:py-20 relative z-10" style="background:var(--ms-plum)">
max-w-7xl px-4 sm:px-6 lg:px-8">
grid-cols-2 gap-8 md:grid-cols-4 divide-x divide-ms-plum-mid">
as s}
flex-col items-center text-center px-4">
t-display text-4xl font-bold gradient-text-gold">{s.value}</div>
text-xs font-bold tracking-widest uppercase text-ms-ivory/80">{s.label}</div>
>

<section id="about" class="py-24" style="background:var(--ms-ivory-warm)">
max-w-7xl px-4 sm:px-6 lg:px-8">
grid-cols-1 items-center gap-16 lg:grid-cols-2">
order-2 lg:order-1">
 rounded-full shadow-2xl border-[10px] border-white" style="aspect-ratio:3/4">
splash.com/photo-1556228720-1c2a468e1824?q=80&w=600&fit=crop" class="w-full h-full object-cover" alt="Skincare Details" />
class="absolute bottom-10 -right-4 h-40 w-40 overflow-hidden rounded-full border-8 border-white shadow-lg hidden md:block">
splash.com/photo-1615397323136-2244c079860b?q=80&w=300&fit=crop" class="w-full h-full object-cover" alt="Cream Texture" />
class="order-1 lg:order-2 space-y-8">
line-flex items-center gap-3"><div class="h-px w-8 bg-ms-gold"></div><span class="text-xs font-bold uppercase tracking-widest text-ms-gold">Tentang Kami</span></div>
t-display text-4xl leading-tight text-ms-plum md:text-5xl font-medium">Agen Resmi Marwah Skincare <br/><em class="font-bold text-ms-plum-mid">Terpercaya</em></h2>
leading-relaxed">Kami adalah agen resmi <strong>Marwah Skincare</strong> yang menyediakan produk perawatan kulit lengkap. Semua produk dijamin aman, memiliki legalitas lengkap, dan telah disesuaikan dengan kebutuhan kulit para wanita Indonesia.</p>
grid-cols-1 gap-4 sm:grid-cols-2 mt-6">
100% Original', 'Sertifikasi Teruji', 'Terjamin Halal MUI', 'Pelayanan Ramah', 'Pilihan Bank (BNI/BRI)', 'Siap Melayani Reseller'] as item}
items-center gap-3 rounded-2xl bg-white px-4 py-3 shadow-sm border border-ms-gold/10"><CheckCircle class="h-4 w-4 text-ms-gold" /><span class="text-sm font-semibold text-ms-plum">{item}</span></div>
>

<section class="py-24" style="background:var(--ms-lavender)">
max-w-7xl px-4 sm:px-6 lg:px-8">
text-center">
t-display text-3xl md:text-4xl text-ms-plum font-semibold">Keunggulan Berbelanja di Sini</h2>
text-ms-text-soft text-sm max-w-lg mx-auto">Kami memastikan setiap produk yang kamu terima memiliki standar tinggi, aman, dan memuaskan.</p>
class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
as f}
group flex flex-col items-center rounded-3xl bg-white p-8 text-center shadow-sm" style="border: 1px solid rgba(201,168,76,0.15)">
flex h-16 w-16 items-center justify-center rounded-full bg-ms-ivory transition-transform group-hover:scale-110"><svelte:component this={f.icon} class="h-8 w-8 text-ms-gold" /></div>
text-lg font-bold text-ms-plum">{f.title}</h3>
text-ms-text-soft">{f.desc}</p>
>

<section id="products" class="py-28 relative overflow-hidden" style="background:var(--ms-plum)">
-plum absolute inset-0 opacity-40"></div>
mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
flex flex-col items-center text-center">
inline-flex items-center gap-3"><div class="h-px w-8 bg-ms-gold-light"></div><span class="text-xs font-bold uppercase tracking-widest text-ms-gold-light">Katalog Pilihan</span><div class="h-px w-8 bg-ms-gold-light"></div></div>
t-display text-4xl font-semibold text-ms-ivory md:text-5xl">Produk Unggulan</h2>
class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
as prod}
relative overflow-hidden rounded-3xl bg-white/5 border border-white/10 transition-all hover:bg-white/10 hover:border-ms-gold/40">
w-full overflow-hidden"><img src={prod.image} alt={prod.title} class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" /></div>
inline-block rounded-full border border-ms-gold/30 bg-ms-gold/10 px-3 py-1 text-[10px] font-bold uppercase tracking-widest text-ms-gold-light">{prod.category}</div>
font-display text-xl font-bold text-ms-ivory">{prod.title}</h3>
text-ms-ivory/60 leading-relaxed">{prod.desc}</p>
class="mt-16 text-center">
 class="inline-flex h-12 items-center gap-2 rounded-xl bg-ms-gold px-8 text-sm font-bold text-ms-plum transition-all hover:bg-ms-gold-light hover:scale-105">Tanyakan Harga <ArrowRight class="h-4 w-4" /></button></a>
>

<section id="order" class="py-24" style="background:var(--ms-ivory)">
max-w-5xl px-4 sm:px-6 lg:px-8">
text-center">
t-display text-4xl font-semibold text-ms-plum">Cara Gampang Belanja</h2>
text-ms-text-mid text-sm">Ikuti 3 langkah mudah ini untuk mulai merawat kulitmu dengan produk dari Marwah Skincare.</p>
class="grid grid-cols-1 md:grid-cols-3 gap-8">
step: 1, title: 'Hubungi Kami', desc: 'Klik tombol WhatsApp atau DM Instagram kami untuk konsultasi, pesan produk.' }, { step: 2, title: 'Pilih & Konsultasi', desc: 'Tentukan produk/paket yang cocok atau tanyakan pada kami.' }, { step: 3, title: 'Transfer & Kirim', desc: 'Selesaikan pembayaran via BNI atau BRI. Pesanan segera dikirim.' }] as o}
flex flex-col items-center bg-white p-8 rounded-3xl text-center shadow-sm border border-ms-gold/20">
-top-6 flex h-12 w-12 items-center justify-center rounded-full font-display text-xl font-bold text-white shadow-lg" style="background:var(--brand-gradient-gold)">{o.step}</div>
mb-3 text-lg font-bold text-ms-plum">{o.title}</h3>
text-ms-text-soft">{o.desc}</p>
class="mt-16 pt-10 border-t border-ms-gold/20 flex flex-col md:flex-row items-center justify-between gap-6" style="background:var(--ms-lavender); border-radius: 2rem; padding: 2rem;">
class="font-display text-2xl font-bold text-ms-plum">Siap Untuk Order?</h3>
text-ms-text-mid mt-1">Layanan buka: 08.00 - 18.00 setiap hari.</p>
href="https://wa.me/1234567890" target="_blank" rel="noopener noreferrer"><button class="flex h-12 items-center gap-2 rounded-full bg-ms-plum px-8 text-sm font-bold text-white transition-all shadow-lg hover:bg-ms-plum-mid hover:scale-105"><MessageCircle class="h-4 w-4" /> Order by WhatsApp</button></a>
>

<section id="reviews" class="py-24" style="background:var(--ms-ivory-warm)">
max-w-7xl px-4 sm:px-6 lg:px-8">
text-center"><h2 class="font-display text-4xl font-semibold text-ms-plum">Kata Mereka</h2></div>
grid-cols-1 gap-6 md:grid-cols-3">
as rv}
flex flex-col rounded-3xl bg-white p-8 shadow-sm border border-ms-gold/10">
flex gap-1">{#each Array(5) as _}<Star class="h-4 w-4 fill-current text-ms-gold" />{/each}</div>
flex-1 text-sm italic text-ms-text-mid leading-relaxed">"{rv.text}"</p>
items-center gap-3 border-t border-ms-gold/10 pt-4">
h-10 w-10 items-center justify-center rounded-full bg-ms-plum text-xs font-bold text-white">{rv.initial}</div>
font-bold text-ms-plum">{rv.name}</div><div class="text-[10px] text-ms-text-soft">{rv.time}</div></div>
>
</main>

<footer class="pt-16 pb-8 text-ms-ivory" style="background:var(--ms-plum)">
<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
flex-col items-center justify-between gap-8 md:flex-row border-b border-ms-ivory/10 pb-10 text-center md:text-left">
flex-col items-center md:items-start">
items-center gap-3 mb-4">
h-10 w-10 items-center justify-center rounded-full bg-ms-gold"><span class="font-display text-xl font-bold text-ms-plum">M</span></div>
t-display text-2xl font-bold">Marwah Skincare</div>
class="text-sm text-ms-ivory/60 max-w-xs">Health & Beauty. Penuhi kebutuhan kulit cantikmu bersama Agen Resmi Marwah Skincare.</p>
class="flex flex-col gap-3 text-sm">
t-bold text-ms-gold uppercase tracking-widest text-xs mb-1">Informasi</div>
items-center justify-center md:justify-start gap-2"><ShieldCheck class="h-4 w-4 text-ms-gold" /> BPOM & Halal MUI</div>
al: 08.00 - 18.00</div>
ar: BNI & BRI</div>
class="flex flex-col items-center md:items-end gap-4">
t-bold text-ms-gold uppercase tracking-widest text-xs">Hubungi Kami</div>
stagram.com/marwah_skincare_id" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2 hover:text-ms-gold transition-colors"><Instagram class="h-4 w-4" /> @marwah_skincare_id</a>
class="flex items-center gap-2 hover:text-ms-gold transition-colors"><MessageCircle class="h-4 w-4" /> Open Reseller</a>
class="mt-8 text-center text-xs text-ms-ivory/40">&copy; 2025 Marwah Skincare Official Agent. All rights reserved.</div>
</div>
</footer>
`;
fs.writeFileSync('r:/demo-client/clinic/src/routes/+page.svelte', content);
