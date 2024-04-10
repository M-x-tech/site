import { defineConfig } from 'astro/config';
import path from 'path';

import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  site: 'https://M-x.tech',
  // base: '/M-x.tech',
  vite: {
    resolve: {
      alias: {
        // Set up '@' to point to the 'src' directory
        '@': path.resolve('./src'),
      },
    },
  },
});