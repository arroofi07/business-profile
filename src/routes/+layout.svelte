<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/logo.png';
	import ScrollToTop from '$lib/components/ui/ScrollToTop.svelte';

	let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<div class="relative min-h-screen">
	{@render children()}
	<ScrollToTop />
</div>
