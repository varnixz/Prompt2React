import React from 'react';
import { useParams } from 'react-router-dom';
import { useCart } from './CartContext';
import products from './products';

function ProductDetail() {
  const { productId } = useParams();
  const { addToCart } = useCart();
  const product = products.find(p => p.id === parseInt(productId));

  return (
    <div className="product-detail">
      <img src={product.image} alt={product.title} />
      <div className="product-info">
        <h1>{product.title}</h1>
        <p className="price">${product.price}</p>
        <p className="description">{product.description}</p>
        <button onClick={() => addToCart(product)}>Add to Cart</button>
      </div>
    </div>
  );
}

export default ProductDetail;