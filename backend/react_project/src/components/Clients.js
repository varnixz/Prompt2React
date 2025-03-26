import React from 'react';

const Clients = () => (
  <section id="clients" className="py-20 bg-white">
    <div className="max-w-6xl mx-auto px-4">
      <h2 className="text-3xl italic mb-8 text-center">Clients</h2>
      <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-8">
        {[...Array(6)].map((_, i) => (
          <div key={i} className="flex items-center justify-center">
            <img src="https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=150&h=100&fit=crop" alt="client" className="w-full h-auto grayscale hover:grayscale-0 transition duration-300" />
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Clients;