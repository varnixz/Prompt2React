import React from 'react';

const Features = () => (
  <section className="py-20 bg-black text-white">
    <div className="max-w-6xl mx-auto px-4">
      <h2 className="text-3xl italic mb-8 text-center">Features</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="text-center">
          <h3 className="text-xl font-bold mb-4">Free Shipping</h3>
          <p>Fast and reliable delivery for all your needs.</p>
        </div>
        <div className="text-center">
          <h3 className="text-xl font-bold mb-4">24/7 Availability</h3>
          <p>We are always here to support you.</p>
        </div>
        <div className="text-center">
          <h3 className="text-xl font-bold mb-4">Best Prices</h3>
          <p>Affordable solutions for every budget.</p>
        </div>
      </div>
    </div>
  </section>
);

export default Features;