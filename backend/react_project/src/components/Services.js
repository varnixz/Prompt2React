import React from 'react';

const Services = () => {
  return (
    <section className="h-[500px] bg-white p-8">
      <h2 className="text-3xl font-bold text-center mb-8">Our Services</h2>
      <div className="grid grid-cols-3 gap-8">
        {[1, 2, 3, 4, 5, 6].map((index) => (
          <div key={index} className="bg-gray-200 p-6 rounded-lg">
            <h3 className="text-xl font-bold mb-2">Service {index}</h3>
            <p className="text-sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Services;