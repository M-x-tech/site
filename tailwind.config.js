/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        pale: '#bdc6de',
        'soft-black': '#2F4F4F', // A dark, rich greenish-black
        'creamy-white': '#F5F5DC', // A creamy, off-white
        navy: '#0000c0', // A deep, rich navy blue
      },
      fontFamily: {
        cursive: ['cursive'],
        mono: [
          'Courier New',
          'Courier',
          'Lucida Sans Typewriter',
          'Lucida Typewriter',
          'monospace',
        ],
        sans: ["'Rubik', sans-serif"],
        serif: ["'Times New Roman'", 'Times', 'serif'],
      },

      // navy text shadow
      textShadow: {
        navy: '0 2px 0 #0000c0',
      },
    },
  },
  plugins: [],
}
