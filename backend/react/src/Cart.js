import React from 'react';
import { useCart } from './CartContext';

function Cart() {
  const { cartItems, removeFromCart, total } = useCart();

  return (
    <div className="cart">
      <h1>Shopping Cart</h1>
      {cartItems.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        <>
          {cartItems.map(item => (
            <div key={item.id} className="cart-item">
              <img src={item.image} alt={item.title} />
              <div>
                <h3>{item.title}</h3>
                <p>${item.price} x {item.quantity}</p>
                <button onClick={() => removeFromCart(item.id)}>Remove</button>
              </div>
            </div>
          ))}
          <div className="total">
            <h3>Total: ${total}</h3>
            <button>Checkout</button>
          </div>
        </>
      )}
    </div>
  );
}

export default Cart;