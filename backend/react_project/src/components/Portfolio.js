import React from 'react';

const Portfolio = () => (
  <section id="portfolio" className="py-20 bg-white">
    <div className="max-w-6xl mx-auto px-4">
      <h2 className="text-3xl italic mb-8 text-center">Portfolio</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {[...Array(6)].map((_, i) => (
          <div key={i} className="overflow-hidden rounded-lg shadow-lg hover:scale-105 transition-transform duration-300">
            <img src="https://images.pexels.com/photos/2442888/pexels-photo-2442888.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop" alt="portfolio" className="w-full h-auto" />
          </div>
        ))}
      </div>
    </div>
  </section>
);

export default Portfolio;