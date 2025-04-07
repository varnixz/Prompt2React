import React from 'react';

const Features = () => {
  const features = [
    { title: 'Free Shipping', description: 'Get your orders delivered for free.', icon: '🚚' },
    { title: '24/7 Availability', description: 'We’re always here for you.', icon: '⏰' },
    { title: 'Best Prices', description: 'Affordable and reliable.', icon: '💲' },
  ];

  return (
    <section className="w-full py-16 bg-gray-900 text-white">
      <div className="grid grid-cols-3 gap-8 px-8">
        {features.map((feature, index) => (
          <div key={index} className="text-center">
            <div className="text-4xl mb-4">{feature.icon}</div>
            <h3 className="text-xl font-bold mb-2">{feature.title}</h3>
            <p>{feature.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Features;