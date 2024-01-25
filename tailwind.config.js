
import withMT from "@material-tailwind/html/utils/withMT";
 
// /** @type {import('tailwindcss').Config} */
// module.exports = withMT({
//   content: ["**/*.html"],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// });


// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = withMT({
  content: ["**/*.html"],
  // darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          "50": "#eff6ff",
          "100": "#dbeafe",
          "200": "#bfdbfe",
          "300": "#93c5fd",
          "400": "#60a5fa",
          "500": "#3b82f6",
          "600": "#2563eb",
          "700": "#1d4ed8",
          "800": "#1e40af",
          "900": "#1e3a8a",
          "950": "#172554",
        },
      },
    },
    fontFamily: {
      'body': [
        'Inter',
        'ui-sans-serif',
        'system-ui',
        '-apple-system',
        'BlinkMacSystemFont',
        'Segoe UI',
        'Roboto',
        'Helvetica Neue',
        'Arial',
        'Noto Sans',
        'sans-serif',
        'Apple Color Emoji',
        'Segoe UI Emoji',
        'Segoe UI Symbol',
        'Noto Color Emoji',
      ],
    },
  },
  plugins: [],
});
