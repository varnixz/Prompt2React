import React from 'react';

const Hero = () => (
  <section className="relative h-screen flex items-center justify-center">
    <img src="https://images.pexels.com/photos/164005/pexels-photo-164005.jpeg?auto=compress&cs=tinysrgb&w=1920&h=800&fit=crop" alt="banner" className="w-full h-full object-cover" />
    <div className="absolute inset-0 bg-black bg-opacity-50 flex flex-col items-center justify-center">
      <h1 className="text-white text-5xl uppercase font-bold mb-4">Empowering Founders</h1>
      <p className="text-white text-xl">Building the future of startups</p>
    </div>
  </section>
);

export default Hero;