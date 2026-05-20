# 🛍️ ShopNest — React Ecommerce Frontend

A fully functional, production-ready ecommerce frontend built with React.js.

## Features

- **Product Catalog** — 12 demo products across 6 categories
- **Search & Filter** — Live search, category filters, sort by price/rating
- **Product Cards** — Hover animations, badges, wishlist toggle, add to cart
- **Product Detail Modal** — Color picker, quantity selector, trust badges
- **Cart Drawer** — Slide-in cart with qty controls, free shipping progress
- **2-Step Checkout** — Shipping info → Payment → Order confirmation
- **Wishlist Page** — Save and manage favourite products
- **Toast Notifications** — Feedback for cart/wishlist actions
- **Responsive Layout** — Works on desktop and mobile

## Getting Started

### Prerequisites
- Node.js 14+ and npm

### Install & Run

```bash
npm install
npm start
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build for Production

```bash
npm run build
```

## Project Structure

```
src/
├── App.js                  # Main app + routing logic
├── index.js                # Entry point
├── index.css               # Global styles
├── context/
│   └── CartContext.js      # Cart state management (useReducer)
├── components/
│   ├── Navbar.jsx          # Sticky navigation bar
│   ├── Hero.jsx            # Landing hero section
│   ├── ProductCard.jsx     # Product grid card
│   ├── ProductModal.jsx    # Product detail popup
│   ├── CartDrawer.jsx      # Slide-in cart panel
│   ├── CheckoutModal.jsx   # 2-step checkout flow
│   ├── Toast.jsx           # Notification toast
│   └── Footer.jsx          # Site footer
└── data/
    └── products.js         # Product & category data
```

## Connecting Your Backend

Replace the static data in `src/data/products.js` with API calls:

```js
// Example: fetch products from your API
useEffect(() => {
  fetch('/api/products')
    .then(res => res.json())
    .then(data => setProducts(data));
}, []);
```

Hook up checkout in `CheckoutModal.jsx`:

```js
// Replace step 3 navigation with:
const response = await fetch('/api/orders', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ cart, form, total }),
});
```

## Tech Stack

- React 18
- React Context API + useReducer (cart state)
- Inline styles (no CSS framework dependency)
- Create React App

---

Built with ❤️ using ShopNest
