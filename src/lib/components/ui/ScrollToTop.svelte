<script lang="ts">
	import { onMount } from 'svelte';
	import { fly } from 'svelte/transition';

	let showButton = $state(false);

	function handleScroll() {
		showButton = window.scrollY > 300;
	}

	function scrollToTop() {
		window.scrollTo({ top: 0, behavior: 'smooth' });
	}

	onMount(() => {
		window.addEventListener('scroll', handleScroll);
		return () => window.removeEventListener('scroll', handleScroll);
	});
</script>

{#if showButton}
	<button
		onclick={scrollToTop}
		transition:fly={{ y: 20, duration: 300 }}
		class="fixed right-6 bottom-6 z-50 flex h-12 w-12 items-center justify-center rounded-full text-white shadow-[0_0_15px_rgba(30,144,255,0.4)] transition-all hover:scale-110 hover:shadow-[0_0_25px_rgba(30,144,255,0.6)]"
		style="background: var(--sp-gradient-blue); border: 1px solid rgba(255,255,255,0.2);"
		aria-label="Scroll to top"
	>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			class="h-6 w-6"
			fill="none"
			viewBox="0 0 24 24"
			stroke="currentColor"
			stroke-width="2.5"
		>
			<path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7m0 0l7 7m-7-7v18" />
		</svg>
	</button>
{/if}
