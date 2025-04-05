import React from 'react';
import { FaShippingFast, FaClock, FaStar } from 'react-icons/fa';

const Features = () => {
  const features = [
    { icon: <FaShippingFast className="text-4xl" />, title: 'Free Shipping', description: 'Get your game delivered for free.' },
    { icon: <FaClock className="text-4xl" />, title: '24/7 Availability', description: 'Play anytime, anywhere.' },
    { icon: <FaStar className="text-4xl" />, title: 'Best Prices', description: 'Affordable and competitive pricing.' },
  ];

  return (
    <section className="w-full py-16 bg-gray-900 text-white">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto px-8">
        {features.map((feature, index) => (
          <div key={index} className="text-center p-6 bg-gray-800 rounded-lg shadow-lg">
            {feature.icon}
            <h3 className="text-xl font-serif mt-4">{feature.title}</h3>
            <p className="mt-2">{feature.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Features;