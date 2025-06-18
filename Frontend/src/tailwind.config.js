/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html"],
  theme: {
    extend: {
      animation: {
        "spin-slow": "spin 1.5s linear infinite",
      },
    },
  },
  plugins: [],
};
