import React from 'react';
import { Link } from 'react-router-dom';
import { useCart } from './CartContext';

function Header() {
  const { cartItems } = useCart();
  
  return (
    <header className="header">
      <nav>
        <Link to="/" className="logo">E-Shop</Link>
        <div className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/cart">
            Cart ({cartItems.reduce((total, item) => total + item.quantity, 0)})
          </Link>
        </div>
      </nav>
    </header>
  );
}

export default Header;