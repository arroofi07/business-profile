<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/logo.png';

	let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<div class="min-h-screen">
	{@render children()}
</div>
