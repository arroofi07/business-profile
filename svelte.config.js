import adapter from '@sveltejs/adapter-vercel';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter({
			// Use Edge runtime for faster cold-start on Vercel
			runtime: 'nodejs22.x'
		})
	}
};

export default config;
