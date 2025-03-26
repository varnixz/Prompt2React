import React from 'react';
import { Link } from 'react-router-dom';
import { useCart } from './CartContext';
import products from './products';

function ProductListing() {
  const { addToCart } = useCart();

  return (
    <div className="product-listing">
      <h1>Products</h1>
      <div className="product-grid">
        {products.map(product => (
          <div key={product.id} className="product-card">
            <Link to={`/product/${product.id}`}>
              <img src={product.image} alt={product.title} />
              <h3>{product.title}</h3>
              <p>${product.price}</p>
            </Link>
            <button onClick={() => addToCart(product)}>Add to Cart</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductListing;