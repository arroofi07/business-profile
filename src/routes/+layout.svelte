<script lang="ts">
	import './layout.css';
	import ScrollToTop from '$lib/components/ui/ScrollToTop.svelte';

	let { children } = $props();
</script>

<div class="relative min-h-screen">
	{@render children()}
	<ScrollToTop />
</div>
